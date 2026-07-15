from core import HackingTool, HackingToolsCollection, console

from rich.panel import Panel
from rich.prompt import Prompt
from rich import box


class WifiJammingTools(HackingToolsCollection):
    TITLE = "Wifi Deauthenticate"
    TOOLS = []

if __name__ == "__main__":
    tools = WifiJammingTools()
    tools.show_options()
