import logging

from ostorlab.cli.rootcli import scan

logger = logging.getLogger(__name__)


@scan.command()
def ios_store():
    """Command on cli1"""