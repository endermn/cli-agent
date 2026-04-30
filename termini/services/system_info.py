import logging
import subprocess
import re
import shutil
from typing import Optional

from tools.common_tools.interfaces import SystemInfoInterface
from services.logger import terminiLogger

logger: logging.Logger = terminiLogger(name=__name__, file="termini.log").get_logger()

class SystemInfo(SystemInfoInterface):
    def get_fastfetch_specs(self) -> Optional[str]:
        try:
            output = subprocess.check_output(["fastfetch"], text=True)
            clean_output = re.sub(r"\x1B\[[0-?]*[ -/]*[@-~]", "", output)
        except Exception as e:
            print("Error: Failed to run fastfetch")
            logger.error(f"Error running fastfetch: {e}")
            clean_output = None
        return clean_output

    def get_neofetch_specs(self) -> Optional[str]:
        try:
            output = subprocess.check_output(["neofetch", "--stdout"], text=True)
            clean_output = re.sub(r"\x1B\[[0-?]*[ -/]*[@-~]", "", output)
        except Exception as e:
            print("Error: Failed to run neofetch")
            logger.error(f"Error: Failed to run neofetch: {e}")
            clean_output = None
        return clean_output

    def get_pwd_files(self) -> Optional[str]:
        try:
            output = subprocess.check_output(["ls", "-R"], text=True)
        except Exception as e:
            print("Error running ls -R")
            logger.error(f"Error running ls -R: {e}")
            output = None
        return output

    def get_system_specs(self) -> Optional[str]:
        if shutil.which("fastfetch"):
            return self.get_fastfetch_specs()
        elif shutil.which("neofetch"):
            return self.get_neofetch_specs()
        else:
            return None
