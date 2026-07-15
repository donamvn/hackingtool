import subprocess

from core import HackingTool, HackingToolsCollection, console

from rich.prompt import Prompt


class PyRIT(HackingTool):
    TITLE = "PyRIT (AI Red Teaming)"
    DESCRIPTION = "Microsoft Python Risk Identification Toolkit for red-teaming generative AI and LLM systems."
    INSTALL_COMMANDS = ["pip install --user pyrit"]
    PROJECT_URL = "https://github.com/Azure/PyRIT"

    def __init__(self):
        super().__init__(runnable=False)


class Garak(HackingTool):
    TITLE = "Garak (LLM Vulnerability Scanner)"
    DESCRIPTION = "NVIDIA's LLM vulnerability scanner — probes for hallucination, data leakage, prompt injection, toxicity."
    INSTALL_COMMANDS = ["pip install --user garak"]
    PROJECT_URL = "https://github.com/NVIDIA/garak"

    def run(self):
        model = Prompt.ask("Enter model name (e.g. gpt-3.5-turbo)")
        subprocess.run(["garak", "--model_type", "openai", "--model_name", model, "--probes", "all"])


class AISecurityTools(HackingToolsCollection):
    TITLE = "AI / LLM Security Tools"
    TOOLS = [PyRIT(), Garak()]


if __name__ == "__main__":
    tools = AISecurityTools()
    tools.show_options()
