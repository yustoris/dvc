from dvc.remote.local import RemoteLOCAL
from dvc.remote.s3 import RemoteS3
from dvc.remote.gs import RemoteGS
from dvc.remote.hdfs import RemoteHDFS
from dvc.remote.ssh import RemoteSSH

from dvc.config import Config
from dvc.exceptions import DvcException


REMOTES = [RemoteHDFS, RemoteSSH, RemoteS3, RemoteGS, RemoteLOCAL]


def supported_url(url):
    config = {Config.SECTION_REMOTE_URL: url}
    for r in REMOTES:
        if r.supported(config):
            return True
    return False


def Remote(project, config):
    for r in REMOTES:
        if r.supported(config):
            return r(project, config)
    raise DvcException('Remote \'{}\' is not supported.'.format(config))
