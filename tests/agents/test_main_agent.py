from google.genai.types import GenerateContentResponse
from termini.agents.base_agent import BaseAgent
from termini.agents.interfaces import Agent
from typing import Optional


def test_base_agent():
    agent: Agent = BaseAgent()
    response: Optional[GenerateContentResponse] = agent.call_agent(
        "Hello, what is your name?"
    )
    assert response is not None
    assert response.text is not None
    assert "termini" in response.text
