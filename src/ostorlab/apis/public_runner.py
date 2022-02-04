"""Handles the public API calls.

    Typical usage example:
    public_runner = PublicAPIRunner()
    public_runner.execute()
"""

import requests
from typing import Dict

from ostorlab.apis import runner
from ostorlab.apis import request as api_request



class PublicAPIRunner(runner.APIRunner):
    """Responsible for the public API calls, and preparing the responses."""
    def __init__(self,
                proxy: str = None,
                verify: bool = True):
        """
        Args:
            proxy: The proxy through which a request is made. Defaults to None.
            verify: Whether or not to verify the TLS certificate. Defaults to True.
        """
        super().__init__(proxy, verify)

    def execute(self, request: api_request.APIRequest) -> Dict:
        """Executes a request using the Public GraphQL API.

        Args:
            request: The request to be executed

        Raises:
            ResponseError: When the API returns an error

        Returns:
            The API response
        """
        response = self._sent_request(request)
        if response.status_code != 200:
            raise runner.ResponseError(
                f'Response status code is {response.status_code}: {response.content}')
        else:
            return response.json()

    def _sent_request(self, request: api_request.APIRequest) -> requests.Response:
        """Sends an API request."""
        if self._proxy is not None:
            proxy = {
                'https': self._proxy
            }
        else:
            proxy = None
        return requests.post(request.endpoint, data=request.data,
                             proxies=proxy, verify=self._verify)
