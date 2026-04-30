from abc import ABC, abstractmethod

from typing import Optional


class SystemInfoInterface(ABC):
    @abstractmethod
    def get_fastfetch_specs(self) -> Optional[str]:
        pass

    @abstractmethod
    def get_neofetch_specs(self) -> Optional[str]:
        pass
