import os
import subprocess

from core import HackingTool, HackingToolsCollection, console

from rich.panel import Panel
from rich.prompt import Prompt
from rich import box


class Sherlock(HackingTool):
    TITLE = "Sherlock"
    SUPPORTED_OS = ["linux"]
    TAGS = ["osint", "social", "recon"]
    LAST_VERIFIED = "2026-07-15"
    DESCRIPTION = "Hunt down social media accounts by username across social networks \n " \
                  "For More Usage \n" \
                  "\t >>python3 sherlock --help"
    INSTALL_COMMANDS = [
        "git clone https://github.com/sherlock-project/sherlock.git",
        "cd sherlock;pip install --user -r requirements.txt"
    ]
    PROJECT_URL = "https://github.com/sherlock-project/sherlock"

    def run(self):
        from config import get_tools_dir
        from rich.prompt import Prompt
        name = Prompt.ask("Enter Username")
        # Bug 3 fix: os.chdir() replaced with cwd= parameter
        subprocess.run(
            ["python3", "sherlock", name],
            cwd=str(get_tools_dir() / "sherlock"),
        )


class SocialScan(HackingTool):
    TITLE = "SocialScan | Username or Email"
    SUPPORTED_OS = ["linux", "macos", "windows"]
    TAGS = ["osint", "social"]
    LAST_VERIFIED = "2026-07-15"
    DESCRIPTION = "Check email address and username availability on online " \
                  "platforms with 100% accuracy"
    INSTALL_COMMANDS = ["pip install --user socialscan"]
    PROJECT_URL = "https://github.com/iojw/socialscan"

    def run(self):
        name = input(
            "Enter Username or Emailid (if both then please space between email & username) >> ")
        subprocess.run(["sudo", "socialscan", f"{name}"])


class SocialMediaFinderTools(HackingToolsCollection):
    TITLE = "SocialMedia Finder"
    TOOLS = [
        Sherlock(),
        SocialScan()
    ]

if __name__ == "__main__":
    tools = SocialMediaFinderTools()
    tools.show_options()
