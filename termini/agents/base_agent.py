import sys
from typing import Callable, Optional

from termini.agents.interfaces import Agent
from termini.prompts.base_agent_prompt import system_prompt as base_prompt
from termini.settings.settings import settings

from google.genai import types
from google import genai


class BaseAgent(Agent):
    client: genai.Client
    tools: list[Callable]

    def __init__(
        self,
        tools: list[Callable] = [],
        model: str = "gemini-2.5-flash",
        system_prompt: str = base_prompt,
    ) -> None:

        super().__init__(model=model)
        if not settings.google_api_key:
            print("Error: GENAI_API_KEY environment variable not set.")
            sys.exit(1)
        self.client = genai.Client(api_key=settings.google_api_key)
        self.tools = tools
        self.system_prompt: str = system_prompt

    def call_agent(self, content: str) -> Optional[types.GenerateContentResponse]:
        response = self.client.models.generate_content(
            model=self.model,
            contents=content,
            config=types.GenerateContentConfig(
                system_instruction=self.system_prompt,
                tools=self.tools,
            ),
        )
        return response
