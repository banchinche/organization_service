import os
import toml

from dataclass_factory import Factory

from typing import Type, TypeVar

T = TypeVar("T")
DEFAULT_CONFIG_PATH: str = "./config/local.config.toml"


def read_toml(path: str) -> dict:
    return toml.load(path)


def load_config(config_class: Type[T], config_scope: str | None = None, path: str | None = None) -> T:
    if path is None:
        path = os.getenv("CONFIG_PATH", DEFAULT_CONFIG_PATH)

    data = read_toml(path)

    if config_scope is not None:
        data = data[config_scope]

    dcf = Factory()
    config = dcf.load(data, config_class)

    return config
