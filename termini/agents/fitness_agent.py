from agents.interfaces import Agent
from prompts.fitness_agent_prompt import system_instructions

from google.genai import types
from google import genai

from tools.tool_utils import logger
from typing import Optional


class FitnessAgent(Agent):
    client: genai.Client
    tools: list[types.Tool]

    def __init__(self, model: str, api_key: str) -> None:
        super().__init__(model=model)
        self.client = genai.Client(api_key=api_key)
        grounding_tool = types.Tool(google_search=types.GoogleSearch())
        self.tools = [grounding_tool]

    def call_agent(self, content: str) -> Optional[types.GenerateContentResponse]:
        logger.info(f"GoogleSearchAgent called with content: {content}")
        response = self.client.models.generate_content(
            model=self.model,
            contents=content,
            config=types.GenerateContentConfig(
                system_instruction=system_instructions, tools=self.tools
            ),
        )

        return response
