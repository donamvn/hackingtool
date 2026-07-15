import os
import subprocess
from rich.panel import Panel
from rich.prompt import Prompt

from core import HackingTool, HackingToolsCollection, console


class Dalfox(HackingTool):
    TITLE = "DalFox (Finder of XSS)"
    SUPPORTED_OS = ["linux"]
    DESCRIPTION = "XSS Scanning and Parameter Analysis tool."
    INSTALL_COMMANDS = [
        "sudo apt-get install -y golang",
        "go install github.com/hahwul/dalfox/v2@latest",
    ]
    RUN_COMMANDS = [
        "~/go/bin/dalfox --help",
    ]
    PROJECT_URL = "https://github.com/hahwul/dalfox"


class XSSPayloadGenerator(HackingTool):
    TITLE = "XSS Payload Generator"
    SUPPORTED_OS = ["linux"]
    DESCRIPTION = "XSS PAYLOAD GENERATOR - XSS SCANNER - XSS DORK FINDER"
    INSTALL_COMMANDS = [
        "git clone https://github.com/capture0x/XSS-LOADER.git",
        "cd XSS-LOADER;pip install --user -r requirements.txt"
    ]
    RUN_COMMANDS = ["cd XSS-LOADER;sudo python3 payloader.py"]
    PROJECT_URL = "https://github.com/capture0x/XSS-LOADER.git"


class XSSFinder(HackingTool):
    TITLE = "Extended XSS Searcher and Finder"
    SUPPORTED_OS = ["linux"]
    DESCRIPTION = "Extended XSS Searcher and Finder"
    INSTALL_COMMANDS = [
        "git clone https://github.com/Damian89/extended-xss-search.git"]
    PROJECT_URL = "https://github.com/Damian89/extended-xss-search"

    def after_install(self):
        console.print(Panel.fit(
            "[bold cyan]Follow These Steps After Installation:[/bold cyan]\n"
            "[red]*[/red] Go to [yellow]extended-xss-search[/yellow] directory\n"
            "[green]*[/green] Rename [bold]example.app-settings.conf[/bold] → [bold]app-settings.conf[/bold]",
            title="[ Install Notes ]",
            border_style="magenta"
        ))
        input("Press ENTER to continue")

    def run(self):
        console.print(Panel.fit(
            "[bold cyan]You need to add links to scan[/bold cyan]\n"
            "[red]*[/red] Go to [yellow]extended-xss-search/config/urls-to-test.txt[/yellow]\n"
            "[green]*[/green] Run: [bold]python3 extended-xss-search.py[/bold]",
            title="[ Run Instructions ]",
            border_style="blue"
        ))


class XSpear(HackingTool):
    TITLE = "XSpear"
    SUPPORTED_OS = ["linux", "macos"]
    DESCRIPTION = "XSpear is an XSS Scanner built on Ruby Gems."
    INSTALL_COMMANDS = ["gem install XSpear"]
    RUN_COMMANDS = ["XSpear -h"]
    PROJECT_URL = "https://github.com/hahwul/XSpear"


class XSSStrike(HackingTool):
    TITLE = "Advanced XSS Detection Suite"
    SUPPORTED_OS = ["linux"]
    DESCRIPTION = "XSStrike is a Python-based tool designed to detect and exploit XSS vulnerabilities."
    INSTALL_COMMANDS = [
        "sudo rm -rf XSStrike",
        "git clone https://github.com/s0md3v/XSStrike.git "
        "&& cd XSStrike && pip install -r requirements.txt"
    ]
    PROJECT_URL = "https://github.com/s0md3v/XSStrike"

    def __init__(self):
        super().__init__(runnable=False)


class XSSAttackTools(HackingToolsCollection):
    TITLE = "XSS Attack Tools"
    TOOLS = [
        Dalfox(),
        XSSPayloadGenerator(),
        XSSFinder(),
        XSpear(),
        XSSStrike(),
    ]

    def show_info(self):
        console.print(Panel.fit(
            "[bold magenta]XSS Attack Tools Collection[/bold magenta]\n"
            "A curated set of tools for XSS vulnerability analysis and exploitation.",
            border_style="bright_magenta"
        ))
