import sys

from settings.config import Config
from tools.common_tools.history_parser import TerminalHistoryParser
from core.orchestrator import Orchestrator

config: Config = Config()
history_parser: TerminalHistoryParser = TerminalHistoryParser()



def main(args: list[str]) -> None:
    if len(args) < 2:
        print("Please provide a query. Use 'termini help' for more information.")
        sys.exit(1)
    if args[1] == "config" and len(args) >= 3 and "history" in args[2]:
        config.change_config(setting=args[2:][0], history_parser=history_parser)
        return
    elif args[1] == "config" and len(args) == 2:
        print(
            "To set path to terminal history use termini config history='path_to_history_file'"
        )
        return
    elif args[1] == "help":
        print("Usage: termini <your query>")
        print(
            "To set path to terminal history use termini config history='path_to_history_file' (set history='default' to reset to default path)"
        )
        print(
            "If it's your first time using termini, please run the installation script first."
        )
        return

    orchestrator: Orchestrator = Orchestrator(config=config)
    user_prompt: str = ""

    if args[1] == "google" or args[1] == "monk":
        user_prompt = " ".join(args[2:])
        agent_mode: str = args[1]
        orchestrator.start_workflow(user_prompt=user_prompt, agent_mode=agent_mode)
    else:
        user_prompt = " ".join(args[1:])
        orchestrator.start_workflow(user_prompt=user_prompt)


if __name__ == "__main__":
    main(sys.argv)
