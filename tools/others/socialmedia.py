import contextlib
import os
import subprocess

from core import HackingTool, HackingToolsCollection, console

from rich.panel import Panel
from rich.prompt import Prompt
from rich import box


class AppCheck(HackingTool):
    TITLE = "Application Checker"
    DESCRIPTION = "Tool to check if an app is installed on the target device through a link."
    INSTALL_COMMANDS = [
        "git clone https://github.com/jakuta-tech/underhanded.git",
        "cd underhanded && sudo chmod +x underhanded.sh"
    ]
    RUN_COMMANDS = ["cd underhanded;sudo bash underhanded.sh"]
    PROJECT_URL = "https://github.com/jakuta-tech/underhanded"


class SocialMediaBruteforceTools(HackingToolsCollection):
    TITLE = "SocialMedia Bruteforce"
    TOOLS = [
        AppCheck()
    ]

if __name__ == "__main__":
    tools = SocialMediaBruteforceTools()
    tools.show_options()
