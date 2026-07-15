from core import HackingTool, HackingToolsCollection, console

from rich.panel import Panel
from rich.prompt import Prompt


class PwndropServer(HackingTool):
    TITLE = "pwndrop (File Hosting for Red Team)"
    DESCRIPTION = "Self-deployable file hosting service with anti-crawl protection for red team payloads."
    INSTALL_COMMANDS = [
        "go install github.com/kgretzky/pwndrop@latest",
    ]
    PROJECT_URL = "https://github.com/kgretzky/pwndrop"


class RemoteAdministrationTools(HackingToolsCollection):
    TITLE = "Remote Administrator Tools (RAT)"
    TOOLS = [
        PwndropServer()
    ]

if __name__ == "__main__":
    tools = RemoteAdministrationTools()
    tools.show_options()
