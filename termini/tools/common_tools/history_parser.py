import os
from tools.tool_utils import logger
from settings.settings import settings


class TerminalHistoryParser:
    @property
    def name(self) -> str:
        return "terminal_history_parser"

    @property
    def description(self) -> str:
        return "parses the terminal history and returns the last 10 commands starting with a hyphen"

    def _get_default_history_path(self) -> str:
        shell = settings.shell.lower()

        if "zsh" in shell:
            return "~/.zsh_history"
        elif "fish" in shell:
            return "~/.local/share/fish/fish_history"
        # Defaulting to bash for other Unix-like shells
        elif os.name == "posix":
            return "~/.bash_history"
        elif os.name == "nt":
            return os.path.join(
                settings.app_data,
                "Microsoft\\Windows\\PowerShell\\PSReadLine\\ConsoleHost_history.txt",
            )
    def get_terminal_history(self, config) -> str:
        logger.info("Tool 'get_terminal_history' called")
        config_parser = config.read_config()

        path = config_parser.get(
            "settings", "history", fallback=self._get_default_history_path()
        )

        history_file = os.path.expanduser(str(path))
        try:
            with open(history_file, "r", errors="ignore") as f:
                lines: list[str] = f.readlines()
            hyphen_lines = [line for line in lines if line.strip().startswith("-")]
            return "".join(hyphen_lines[-10:])
        except FileNotFoundError:
            return f"Error: History file not found at '{history_file}'. Please check the path or configure it with 'termini config history=<path>'."
        except Exception as e:
            return f"An unexpected error occurred: {e}"
