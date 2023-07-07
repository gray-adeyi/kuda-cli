import functools
import json
import os.path
from pathlib import Path
from typing import Optional, cast

import typer
from pykuda2 import Kuda, APIResponse, Mode
from typer import get_app_dir
from rich import print as rprint

APP_NAME = "kuda-cli"

CACHED_SETTINGS: Optional[dict] = None


def get_settings_path() -> Path:
    app_dir = get_app_dir(APP_NAME)
    if not os.path.isdir(app_dir):
        os.mkdir(app_dir)
    return Path(app_dir) / ".settings.json"


def get_all_settings() -> dict:
    global CACHED_SETTINGS
    if CACHED_SETTINGS:
        return CACHED_SETTINGS
    settings_path = get_settings_path()
    if not settings_path.is_file():
        with settings_path.open("w+") as f:
            f.write(json.dumps({}))
    with settings_path.open("r") as f:
        CACHED_SETTINGS = json.loads(f.read())
        return CACHED_SETTINGS


def get_settings(option: str) -> Optional[str]:
    all_settings = get_all_settings()
    return all_settings.get(option)


def update_settings(option: str, value: str):
    all_settings = get_all_settings()
    all_settings[option] = value
    settings_path = get_settings_path()
    with settings_path.open("w") as f:
        f.write(json.dumps(all_settings))


def reset_settings():
    global CACHED_SETTINGS
    CACHED_SETTINGS = None
    settings_path = get_settings_path()
    with settings_path.open("w+") as f:
        f.write(json.dumps({}))


def get_kuda_wrapper() -> "KudaSingleton":
    email = get_settings("email")
    api_key = get_settings("api_key")
    mode = get_settings("mode")
    mode = cast(Mode, mode)
    if not email:
        rprint(
            "[bold red]Error![/bold red] your email has not been configured. please run `kuda config <email> <api_key>`"
        )
        raise typer.Abort()
    if not api_key:
        rprint(
            "[bold red]Error![/bold red] your api_key as not been configured. please run `kuda config <email> <api_key>`"
        )
        raise typer.Abort()
    if not mode:
        rprint(
            "[bold red]Error![/bold red] your mode as not been configured. please run `kuda config <email> <api_key> --<mode>`"
        )
        raise typer.Abort()
    return KudaSingleton(email=email, api_key=api_key, mode=mode)


def strip_raw(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        response = func(*args, **kwargs)
        response.raw = None
        return response

    return wrapper


def override_output(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        response = func(*args, **kwargs)
        if kwargs["data_only"]:
            return response.data
        return response

    return wrapper


def colorized_print(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        response = func(*args, **kwargs)
        rprint(response)

    return wrapper


class KudaSingleton:
    instance: Optional[Kuda] = None

    def __init__(self, email: str, api_key: str, mode: Mode = Mode.DEVELOPMENT):
        ...

    def __new__(cls, *args, **kwargs):
        if not KudaSingleton.instance:
            KudaSingleton.instance = Kuda(*args, **kwargs)
        return KudaSingleton.instance

    def __getattr__(self, item):
        return getattr(self.instance, item)

    def __setattr__(self, key, value):
        return setattr(self.instance, key, value)
