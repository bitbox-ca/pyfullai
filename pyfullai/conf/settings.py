from quasiqueue import Settings as QuasiQueueSettings
from .db import DatabaseSettings
from .cache import CacheSettings


class Settings(QuasiQueueSettings, DatabaseSettings, CacheSettings):
    project_name: str = "pyfullai"
    debug: bool = False
