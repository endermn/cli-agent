from .interfaces import Tool
from tools.tool_utils import logger


class CatFile(Tool):
    @property
    def name(self) -> str:
        return "cat_file"

    @property
    def description(self) -> str:
        return "returns the contents of the given file"

    def cat_file(self, file: str) -> str:
        logger.info(f"Tool 'cat_file' called with file: {file}")
        with open(file, "r") as f:
            return f.read()
