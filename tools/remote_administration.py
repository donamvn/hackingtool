from core import HackingTool, HackingToolsCollection, console

from rich.panel import Panel
from rich.prompt import Prompt


class PwndropServer(HackingTool):
    TITLE = "pwndrop (File Hosting for Red Team)"
    SUPPORTED_OS = ["linux", "macos", "windows"]
    DESCRIPTION = "Self-deployable file hosting service with anti-crawl protection for red team payloads."
    TAGS = ["rat", "remote", "payload"]
    LAST_VERIFIED = "2026-07-15"
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
