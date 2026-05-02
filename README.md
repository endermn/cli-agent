# Termini

Termini, is a terminal assistant designed to help users interact with their systems and access information efficiently, explaining complex code and handling different agent modes.

(The name gevai was used in the video as the name was different in the past)


![t-rec](https://github.com/user-attachments/assets/d22bec44-a3bf-41dd-8825-7d6b72afa3f3)

## Get started

1. Install Dependencies:
	1.1 Install poetry with pip
	```bash
	pip install poetry
	```

	1.2 Let poetry do the rest
	```bash
	poetry install
	```

2. Run installation script:
	**MacOS/Linux (Recommended):**
	```bash
	./scripts/install.sh
	```
	**Windows:**
	```bash
	./scripts/install.sh
	```
3. Configure:
 	Set up your environment variables or modify the configuration files as needed. Specifically, you might need to set your API keys for the generative AI model in a .env file following the example. You can also configure the path to your terminal history using:
	```bash
	termini config history='path/to/your/terminal/history'
	```
4.  **Run:** Execute the assistant from your terminal:
	```bash
	termini <your query>
	```

## Reporting bugs:

Feel free to report any current bugs on our (issues page)[https://github.com/endermn/cli-agent/issues]
Here's a breakdown of its key features and structure:

## Connect on discord:

If there are any other issues feel free to connect with me on (discord)[https://discord.gg/tWhh3CbPm]

## Features:

*   **AI-Powered Assistance:** Utilizes generative AI models to understand and respond to user queries.
*   **System Information:** Can fetch system specifications and details about the current environment using tools like `fastfetch` and `neofetch`.
*   **Weather Forecasts:** Integrates with external services (via `curl`) to provide weather information for specified locations.
*   **Configuration Management:** Allows users to configure the tool, including specifying the path to their terminal history for context.
*   **Extensible Tooling:** Designed with a clear structure for adding new tools and functionalities.
*	**Custom Agents:** Specific agents available for specific questions.

## Contributing:

Contributions are very welcome!
Please fork the repository and submit a pull request with your changes in a new branch.
Ensure that your code adheres to the existing style and includes tests for new features.