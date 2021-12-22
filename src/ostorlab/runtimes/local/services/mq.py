import binascii
import logging
import os

import docker
import tenacity
from docker import errors
from docker import types
from docker.models import services

logger = logging.getLogger(__name__)

MQ_IMAGE = 'rabbitmq:3.9-management'


class LocalRabbitMQ:
    def __init__(self,
                 name: str,
                 network: str,
                 image: str = MQ_IMAGE) -> None:

        self._name = name
        self._docker_client = docker.from_env()
        # images
        self._mq_image = image
        self._network = network
        self._mq_host = f'mq_{self._name}'
        # service
        self._mq_service = None

    @property
    def url(self):
        return f'amqp://guest:guest@{self._mq_host}:5672/'

    @property
    def vhost(self):
        return '/'

    def start(self) -> None:
        """Start local rabbit mq instance."""
        self._create_network()
        self._mq_service = self._start_mq()

        if not self._is_service_healthy():
            logger.error('MQ container for service %s is not ready', self._mq_service.id)
            return

    def stop(self):
        for service in self._docker_client.services.list():
            universe = service.attrs['Spec']['Labels']['ostorlab.universe']
            if service.name.startswith('mq_') and self._name in universe:
                service.remove()

    def _create_network(self):
        if any(network.name == self._network for network in self._docker_client.networks.list()):
            logger.warning('network already exists.')
        else:
            logger.info('creating private network %s', self._network)
            return self._docker_client.networks.create(
                name=self._network,
                driver='overlay',
                attachable=True,
                labels={'ostorlab.universe': self._name, },
                check_duplicate=True
            )

    def _start_mq(self) -> services.Service:
        logger.info('starting MQ')
        endpoint_spec = types.services.EndpointSpec(mode='vip')
        service_mode = types.services.ServiceMode('replicated', replicas=1)
        return self._docker_client.services.create(
            image=self._mq_image,
            networks=[self._network],
            name=self._mq_host,
            env=[
                'TASK_ID={{.Task.Slot}}',
                f'MQ_SERVICE_NAME={self._mq_host}',
                f'RABBITMQ_ERLANG_COOKIE={binascii.hexlify(os.urandom(10)).decode()}',
            ],
            restart_policy=types.RestartPolicy(condition='any'),
            mode=service_mode,
            labels={'ostorlab.universe': self._name, 'ostorlab.mq': ''},
            endpoint_spec=endpoint_spec)

    @tenacity.retry(stop=tenacity.stop_after_attempt(20),
                    wait=tenacity.wait_exponential(multiplier=1, max=12),
                    # return last value and don't raise RetryError exception.
                    retry_error_callback=lambda lv: lv.result(),
                    retry=tenacity.retry_if_result(lambda v: v is False))
    def _is_service_healthy(self) -> bool:
        logger.info('checking service %s', self._mq_service.name)
        return self.is_healthy

    @property
    def is_healthy(self) -> bool:
        try:
            return len([task for task in self._mq_service.tasks() if task['Status']['State'] == 'running']) == 1
        except errors.DockerException:
            return False