# Termini
---

Termini, is a terminal assistant designed to help users interact with their systems and access information efficiently, explaining complex code and handling different agent modes.

![t-rec](https://github.com/user-attachments/assets/d22bec44-a3bf-41dd-8825-7d6b72afa3f3)

## Get started
---

1.  **Install Dependencies:**
	1.1 Install poetry with pip
	```bash
	pip install poetry
	```

	1.2 Let poetry do the rest
	```bash
	poetry install
	```

2.  **Run installation script:**
	```bash
	./scripts/install.sh
	```
3.  **Configure:** Set up your environment variables or modify the configuration files as needed. Specifically, you might need to set your API keys for the generative AI model. You can also configure the path to your terminal history using:
	```bash
	termini config history='path/to/your/terminal/history'
	```
4.  **Run:** Execute the assistant from your terminal:
	```bash
	termini <your query>
	```

Here's a breakdown of its key features and structure:

### Features:

*   **AI-Powered Assistance:** Utilizes generative AI models to understand and respond to user queries.
*   **System Information:** Can fetch system specifications and details about the current environment using tools like `fastfetch` and `neofetch`.
*   **Weather Forecasts:** Integrates with external services (via `curl`) to provide weather information for specified locations.
*   **Configuration Management:** Allows users to configure the tool, including specifying the path to their terminal history for context.
*   **Extensible Tooling:** Designed with a clear structure for adding new tools and functionalities.

## Contributing:

Contributions are very welcome!
Please fork the repository and submit a pull request with your changes in a new branch.
Ensure that your code adheres to the existing style and includes tests for new features.


### Project Structure:

The project is organized into several key directories:

*   **`termini/`**: The main package containing the core logic.
	*   **`core/`**: Houses the central orchestration and interface logic.
		*   `orchestrator.py`: Manages the AI agent's interaction and workflow.
		*   `interfaces.py`: Defines data structures and contracts for core components.
	*   **`prompts/`**: Contains the AI prompts, including system prompts for the Gemini model.
	*   **`services/`**: Includes modules for specific functionalities.
		*   `system_info.py`: Fetches system-related information.
		*   `genai_service.py`: Interacts with the generative AI service.
	*   **`settings/`**: Manages project configuration.
		*   `config.py`: Handles configuration loading and changes.
	*   **`tools/`**: Contains various utility tools that the AI can leverage.
		*   **`agent_tools**
			*   `weather_tool.py`: A tool for fetching weather information.
			*   `system_health.py`: A tool for checking system health.
			*   `read_files.py`: A tool for reading file contents.

		*   **`common_tools**

			*   `history_parser.py`: a tool to parse terminal's history
*   **`tests/`**: Contains unit and integration tests for the project.
*   **`example.env`**: An example environment file for configuration.
*   **`poetry.lock`**: Lock file for Poetry dependency management.
*   **`pyproject.toml`**: Project metadata, dependencies, and build configuration.


### Dependencies:

All project dependencies are in the pyproject.toml file, poetry will install them for you.


## Roadmap:

*   **Enhanced Tooling:** Adding more tools for various functionalities.
*   **Local DB Integration:** Implementing a local database for storing issues you face and solve so you never have to face the same issue twice
