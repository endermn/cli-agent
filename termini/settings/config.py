import os
import configparser
from tools.common_tools.history_parser import TerminalHistoryParser
from settings.settings import settings
import logging

from services.logger import terminiLogger

logger: logging.Logger = terminiLogger(name=__name__, file="termini.log").get_logger()


class Config:
    config_file: str
    config_dir: str

    def __init__(self) -> None:
        if os.name == "nt":
            self.config_dir = os.path.join(settings.app_data, "termini")
        else:
            self.config_dir = os.path.join(os.path.expanduser("~"), ".config", "termini")
        self.config_file = os.path.join(self.config_dir, "config.ini")

    def read_config(self) -> configparser.ConfigParser:
        config = configparser.ConfigParser()
        config.read(self.config_file)
        return config

    def write_config(self, config) -> None:
        os.makedirs(self.config_dir, exist_ok=True)
        with open(self.config_file, "w") as file:
            config.write(file)

    def change_config(
        self, history_parser: TerminalHistoryParser, setting: str
    ) -> None:
        default_value = history_parser._get_default_history_path()

        if "=" in setting:
            key, value = setting.split("=", 1)

            config_obj = self.read_config()
            if "settings" not in config_obj:
                config_obj["settings"] = {}
            if value == "default":
                config_obj["settings"][key] = default_value
            else:
                config_obj["settings"][key] = value
            self.write_config(config_obj)
            print(f"Configuration updated: {key} = {value}")
            logger.debug(f"Configuration updated: {key} = {value}")
        else:
            key = setting
            config_obj = self.read_config()
            value = config_obj.get("settings", key, fallback=None)

            if value is not None:
                print(f"{key} = {value} (set explicitly)")
            else:
                if key == "history":
                    print(f"{key} = {default_value} (default)")
                else:
                    print(f"{key} = Not set (no default)")
