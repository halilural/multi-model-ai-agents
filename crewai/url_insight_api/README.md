# UrlInsightBot Crew

Welcome to the UrlInsightBot Crew project, powered by [crewAI](https://crewai.com). This template is designed to help you set up a multi-agent AI system with ease, leveraging the powerful and flexible framework provided by crewAI. Our goal is to enable your agents to collaborate effectively on complex tasks, maximizing their collective intelligence and capabilities.

## Installation

Ensure you have Python >=3.10 <3.13 installed on your system. This project uses [UV](https://docs.astral.sh/uv/) for dependency management and package handling, offering a seamless setup and execution experience.

First, if you haven't already, install uv:

```bash
pip install uv
```

Next, navigate to your project directory and install the dependencies:

(Optional) Lock the dependencies and install them by using the CLI command:

```bash
crewai install
```

### Customizing

**Add your `OPENAI_API_KEY` into the `.env` file**

- Modify `src/url_insight_api/config/agents.yaml` to define your agents
- Modify `src/url_insight_api/config/tasks.yaml` to define your tasks
- Modify `src/url_insight_api/crew.py` to add your own logic, tools and specific args
- Modify `src/url_insight_api/main.py` to add custom inputs for your agents and tasks

## Running the Project

To kickstart your crew of AI agents and begin task execution, run this from the root folder of your project:

```bash
$ crewai run
```

This command initializes the url-insight-bot Crew, assembling the agents and assigning them tasks as defined in your configuration.

This example, unmodified, will run the create a `report.md` file with the output of a research on LLMs in the root folder.

## Understanding Your Crew

The url-insight-bot Crew is composed of multiple AI agents, each with unique roles, goals, and tools. These agents collaborate on a series of tasks, defined in `config/tasks.yaml`, leveraging their collective skills to achieve complex objectives. The `config/agents.yaml` file outlines the capabilities and configurations of each agent in your crew.

## Support

For support, questions, or feedback regarding the UrlInsightBot Crew or crewAI.

- Visit our [documentation](https://docs.crewai.com)
- Reach out to us through our [GitHub repository](https://github.com/joaomdmoura/crewai)
- [Join our Discord](https://discord.com/invite/X4JWnZnxPb)
- [Chat with our docs](https://chatg.pt/DWjSBZn)

Let's create wonders together with the power and simplicity of crewAI.


## Development

### Setting Up Python (On Windows)

To create a virtual environment and install the dependencies listed in a requirements.txt file, you can follow these steps:

1. Create the virtual environment:
   
  ```bash
  python -m venv venv
  ```

2. Activate the virtual environment:

    ```bash
  .\venv\Scripts\activate
  ```

3. Install the dependencies:

  ```bash
  python -m pip install -r requirements.txt
  ```

### Setting Up Python (On macOS/Linux)

To create a virtual environment and install the dependencies listed in a requirements.txt file, you can follow these steps:

1. Create the virtual environment:

  ```bash
  python3 -m venv venv
  ```

2. Activate the virtual environment:

  ```bash
  source venv/bin/activate
  ```

3. Install the dependencies:

  ```bash
  pip install -r requirements.txt
  ```

### Starting the Server

To start the server, navigate to your project directory and run the following command:

```bash
cd ./crewai/url_insight_api
uvicorn src.url_insight_api.url_analyzer:app --reload --reload-include *.py --port 8000 --log-config config/log_config.yaml
```

This will start the server with live reloading enabled on port 8000.

### Test the server

Using curl 

```bash
# Start analysis
curl -X POST http://localhost:8000/api/analyze \
  -H "Content-Type: application/json" \
  -d '{"topic": "AI LLMs"}'

# Check task status (replace <task_id> with actual ID from previous response)
curl http://localhost:8000/api/task/<task_id>
```