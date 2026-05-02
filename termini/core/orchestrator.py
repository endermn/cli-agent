from termini.services.system_info import SystemInfo
from termini.tools.common_tools.interfaces import SystemInfoInterface
from termini.settings.config import Config
from termini.tools.common_tools.history_parser import TerminalHistoryParser

from termini.agents.interfaces import Agent
from termini.agents.base_agent import BaseAgent
from termini.agents.google_search_agent import GoogleSearchAgent
from termini.prompts.fitness_agent_prompt import system_instructions as fitness_prompt

from termini.tools.agent_tools.interfaces import Tool

from termini.tools.agent_tools.todo import ToDoTool
from termini.tools.agent_tools.read_files import CatFile
from termini.tools.agent_tools.weather_tool import WeatherTool
from termini.tools.agent_tools.system_health import SystemHealthTool

from google.genai import types, errors

from typing import Optional
import logging

from termini.services.logger import FileLogger

logger: logging.Logger = FileLogger(name=__name__, file="termini.log").get_logger()


class Orchestrator:
    """Orchestrates the workflow of the termini"""

    config: Config

    system_specs: Optional[str]
    files_in_pwd: Optional[str]
    terminal_history: str

    base_agent: Optional[Agent]
    search_agent: Optional[Agent]

    def __init__(self, config: Config) -> None:
        """Initializes the orchestrator and its main components"""
        self.config = config

        system_info: SystemInfoInterface = SystemInfo()
        self.files_in_pwd = system_info.get_pwd_files()
        self.system_specs = system_info.get_system_specs()

        history_parser: TerminalHistoryParser = TerminalHistoryParser()
        self.terminal_history = history_parser.get_terminal_history(self.config)

        weather_tool: Tool = WeatherTool()
        health_tool: Tool = SystemHealthTool()
        cat_tool: Tool = CatFile()
        todo_tool: Tool = ToDoTool()

        main_tools = [
            weather_tool.get_weather_location,
            health_tool.get_system_health,
            cat_tool.cat_file,
            todo_tool.add_task,
            todo_tool.view_tasks,
            todo_tool.remove_task,
            todo_tool.clear_tasks,
        ]

        self.base_agent = BaseAgent(tools=main_tools)

        self.search_agent = GoogleSearchAgent(model="gemini-2.5-flash-lite")

        self.fitness_agent = BaseAgent(
            model="gemini-2.5-flash-lite", system_prompt=fitness_prompt
        )

    def start_workflow(self, user_prompt: str, agent_mode: str = "") -> None:
        logger.info("Starting workflow")
        logger.info(f"User prompt: {user_prompt}")

        if agent_mode == "google":
            response = self.call_agent(agent=self.search_agent, prompt=user_prompt)
        elif agent_mode == "monk":
            response = self.call_agent(agent=self.fitness_agent, prompt=user_prompt)
        else:
            response = self.call_agent(agent=self.base_agent, prompt=user_prompt)

        if response is None:
            return

        # Extract text from response, handling both direct text and function call results
        response_text = self._extract_response_text(response)

        if response_text and "google_search_agent" in response_text:
            search_results: Optional[types.GenerateContentResponse] = self.call_agent(
                agent=self.search_agent, prompt=user_prompt
            )
            if search_results is not None:
                search_text = self._extract_response_text(search_results)
                print(search_text)
                logger.info(search_results)
                logger.info(search_text)

        else:
            print(response_text)
            logger.info(response)
            logger.info(response_text)

    def define_prompt(self, prompt: str) -> str:
        logger.info("Defining prompt")

        full_prompt: str = f"""
        ** System specs **
        {self.system_specs}

        ** Files in pwd **
        {self.files_in_pwd}

        ** Terminal history **
        {self.terminal_history}

        ** Question **
        {prompt}
        """

        return full_prompt

    def call_agent(
        self, agent: Optional[Agent], prompt: str
    ) -> Optional[types.GenerateContentResponse]:
        try:
            if agent is not None:
                return agent.call_agent(self.define_prompt(prompt))
        except errors.ServerError as e:
            print(f"A server error occurred: {e.message}")
            logger.error(f"Server error: {e.message}")
        except errors.APIError as e:
            print(f"An API error occurred: {e.message}")
            logger.error(f"API error: {e.message}")
        except Exception as e:
            print(f"An unexpected error occurred: {str(e)}")
            logger.error(f"Unexpected error: {str(e)}")
            return None

    def _extract_response_text(self, response: types.GenerateContentResponse) -> str:
        """Extract text from response, handling both direct text and function call results"""
        if response.text:
            return response.text

        # If automatic function calling was used, extract result from function response
        if (
            not hasattr(response, "automatic_function_calling_history")
            or not response.automatic_function_calling_history
        ):
            return ""

        for content in reversed(response.automatic_function_calling_history):
            if not content.parts:
                continue

            for part in content.parts:
                func_response = part.function_response
                if not func_response or not func_response.response:
                    continue

                # Check for function response with result
                if hasattr(part, "function_response"):
                    result = func_response.response.get("result", "")
                    if result:
                        return result

        return ""
