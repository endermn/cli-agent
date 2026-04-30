from typing import Callable, Optional

from agents.interfaces import Agent
from prompts.main_agent_prompt import system_prompt

from google.genai import types
from google import genai


class BaseAgent(Agent):
    client: genai.Client
    tools: list[Callable]

    def __init__(self, model: str, api_key: str, tools: list[Callable]) -> None:
        super().__init__(model=model)
        self.client = genai.Client(api_key=api_key)
        self.tools = tools

    def call_agent(self, content: str) -> Optional[types.GenerateContentResponse]:
        response = self.client.models.generate_content(
            model=self.model,
            contents=content,
            config=types.GenerateContentConfig(
                system_instruction=system_prompt, 
                tools=self.tools,
            ),
        )

        return response
