from abc import ABC, abstractmethod
from google.genai import types
from typing import Optional


class Agent(ABC):
	model: str

	def __init__(self, model: str) -> None:
		self.model = model

	@abstractmethod
	def call_agent(self, content: str) -> Optional[types.GenerateContentResponse]:
		pass
