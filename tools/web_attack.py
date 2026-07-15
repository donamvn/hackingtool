import subprocess
from core import HackingTool, HackingToolsCollection, console

from rich.panel import Panel
from rich.prompt import Prompt


class Web2Attack(HackingTool):
    TITLE = "Web2Attack"
    SUPPORTED_OS = ["linux"]
    TAGS = ["web", "webapp", "exploit"]
    LAST_VERIFIED = "2026-07-15"
    DESCRIPTION = "Web hacking framework with tools, exploits by python"
    TAGS = ["web", "webapp", "exploit"]
    LAST_VERIFIED = "2026-07-15"
    INSTALL_COMMANDS = [
        "git clone https://github.com/santatic/web2attack.git"
    ]
    RUN_COMMANDS = ["cd web2attack && sudo python3 w2aconsole"]
    PROJECT_URL = "https://github.com/santatic/web2attack"


class Skipfish(HackingTool):
    TITLE = "Skipfish"
    TAGS = ["web", "webapp", "scanner"]
    LAST_VERIFIED = "2026-07-15"
    DESCRIPTION = (
        "Skipfish – Fully automated, active web application "
        "security reconnaissance tool \n "
        "Usage: skipfish -o [FolderName] targetip/site"
    )
    TAGS = ["web", "scanner", "recon"]
    LAST_VERIFIED = "2026-07-15"
    RUN_COMMANDS = [
        "sudo skipfish -h",
        'echo "skipfish -o [FolderName] targetip/site"|boxes -d headline | lolcat'
    ]

    def __init__(self):
        super().__init__(installable=False)


class SubDomainFinder(HackingTool):
    TITLE = "SubDomain Finder"
    SUPPORTED_OS = ["linux"]
    TAGS = ["web", "recon", "scanner"]
    LAST_VERIFIED = "2026-07-15"
    DESCRIPTION = (
        "Sublist3r is a python tool designed to enumerate "
        "subdomains of websites using OSINT \n "
        "Usage:\n\t[1] python3 sublist3r.py -d example.com \n"
        "[2] python3 sublist3r.py -d example.com -p 80,443"
    )
    TAGS = ["recon", "osint", "web"]
    LAST_VERIFIED = "2026-07-15"
    INSTALL_COMMANDS = [
        "pip install --user requests argparse dnspython",
        "git clone https://github.com/aboul3la/Sublist3r.git",
        "cd Sublist3r && pip install --user -r requirements.txt"
    ]
    RUN_COMMANDS = ["cd Sublist3r && python3 sublist3r.py -h"]
    PROJECT_URL = "https://github.com/aboul3la/Sublist3r"


class CheckURL(HackingTool):
    TITLE = "CheckURL"
    SUPPORTED_OS = ["linux"]
    TAGS = ["web", "scanner"]
    LAST_VERIFIED = "2026-07-15"
    DESCRIPTION = (
        "Detect evil urls that uses IDN Homograph Attack.\n\t"
        "[!] python3 checkURL.py --url google.com"
    )
    TAGS = ["web", "phishing", "recon"]
    LAST_VERIFIED = "2026-07-15"
    INSTALL_COMMANDS = ["git clone https://github.com/UndeadSec/checkURL.git"]
    RUN_COMMANDS = ["cd checkURL && python3 checkURL.py --help"]
    PROJECT_URL = "https://github.com/UndeadSec/checkURL"


class SubDomainTakeOver(HackingTool):
    TITLE = "Sub-Domain TakeOver"
    SUPPORTED_OS = ["linux", "macos"]
    TAGS = ["web", "webapp", "exploit"]
    LAST_VERIFIED = "2026-07-15"
    DESCRIPTION = (
        "Sub-domain takeover vulnerability occur when a sub-domain "
        "\n (subdomain.example.com) is pointing to a service "
        "(e.g: GitHub, AWS/S3,..)\nthat has been removed or deleted.\n"
        "Usage:python3 takeover.py -d www.domain.com -v"
    )
    TAGS = ["web", "recon", "cloud"]
    LAST_VERIFIED = "2026-07-15"
    INSTALL_COMMANDS = [
        "git clone https://github.com/edoardottt/takeover.git",
        "cd takeover && pip install --user ."
    ]
    PROJECT_URL = "https://github.com/edoardottt/takeover"

    def __init__(self):
        super().__init__(runnable=False)


class Dirb(HackingTool):
    TITLE = "Dirb"
    SUPPORTED_OS = ["linux"]
    TAGS = ["web", "webapp", "scanner"]
    LAST_VERIFIED = "2026-07-15"
    DESCRIPTION = (
        "DIRB is a Web Content Scanner. It looks for existing "
        "(and/or hidden) Web Objects.\n"
        "It basically works by launching a dictionary based "
        "attack against \n a web server and analyzing the response."
    )
    TAGS = ["web", "scanner", "recon"]
    LAST_VERIFIED = "2026-07-15"
    INSTALL_COMMANDS = [
        "git clone https://gitlab.com/kalilinux/packages/dirb.git",
        "cd dirb;sudo bash configure;make"
    ]
    PROJECT_URL = "https://gitlab.com/kalilinux/packages/dirb"

    def run(self):
        uinput = input("Enter Url >> ")
        subprocess.run(["sudo", "dirb", uinput])


class Nuclei(HackingTool):
    TITLE = "Nuclei (Vulnerability Scanner)"
    SUPPORTED_OS = ["linux", "macos", "windows"]
    TAGS = ["web", "scanner", "exploit"]
    LAST_VERIFIED = "2026-07-15"
    DESCRIPTION = (
        "Fast, template-based vulnerability scanner used by 50k+ security teams.\n"
        "Usage: nuclei -u https://example.com"
    )
    TAGS = ["web", "scanner", "exploit"]
    LAST_VERIFIED = "2026-07-15"
    REQUIRES_GO = True
    INSTALL_COMMANDS = [
        "go install -v github.com/projectdiscovery/nuclei/v3/cmd/nuclei@latest",
        "nuclei -update-templates",
    ]
    RUN_COMMANDS = ["nuclei -h"]
    PROJECT_URL = "https://github.com/projectdiscovery/nuclei"


class Ffuf(HackingTool):
    TITLE = "ffuf (Web Fuzzer)"
    SUPPORTED_OS = ["linux", "macos", "windows"]
    TAGS = ["web", "webapp", "scanner"]
    LAST_VERIFIED = "2026-07-15"
    DESCRIPTION = (
        "Fast web fuzzer — content discovery, parameter fuzzing, vhost discovery.\n"
        "Usage: ffuf -w wordlist.txt -u https://example.com/FUZZ"
    )
    TAGS = ["web", "scanner", "recon"]
    LAST_VERIFIED = "2026-07-15"
    REQUIRES_GO = True
    INSTALL_COMMANDS = [
        "go install -v github.com/ffuf/ffuf/v2@latest",
    ]
    RUN_COMMANDS = ["ffuf -h"]
    PROJECT_URL = "https://github.com/ffuf/ffuf"


class Feroxbuster(HackingTool):
    TITLE = "Feroxbuster (Directory Brute Force)"
    TAGS = ["web", "webapp", "scanner"]
    LAST_VERIFIED = "2026-07-15"
    DESCRIPTION = (
        "Fast, recursive content discovery tool written in Rust.\n"
        "Usage: feroxbuster -u https://example.com -w wordlist.txt"
    )
    TAGS = ["web", "scanner", "recon"]
    LAST_VERIFIED = "2026-07-15"
    SUPPORTED_OS = ["linux"]
    INSTALL_COMMANDS = [
        "curl -sL https://raw.githubusercontent.com/epi052/feroxbuster/main/install-nix.sh "
        "| sudo bash -s /usr/local/bin",
    ]
    RUN_COMMANDS = ["feroxbuster -h"]
    PROJECT_URL = "https://github.com/epi052/feroxbuster"


class Nikto(HackingTool):
    TITLE = "Nikto (Web Server Scanner)"
    TAGS = ["web", "scanner", "webapp"]
    LAST_VERIFIED = "2026-07-15"
    WIN_INSTALL_HINT = "Works via WSL or Docker"
    DESCRIPTION = (
        "Scan web servers for dangerous files, outdated software, misconfigurations.\n"
        "Usage: nikto -h https://example.com"
    )
    TAGS = ["web", "scanner", "webapp"]
    LAST_VERIFIED = "2026-07-15"
    SUPPORTED_OS = ["linux"]
    INSTALL_COMMANDS = ["sudo apt-get install -y nikto"]
    RUN_COMMANDS = ["nikto -Help"]
    PROJECT_URL = "https://github.com/sullo/nikto"


class Wafw00f(HackingTool):
    TITLE = "wafw00f (WAF Detector)"
    SUPPORTED_OS = ["linux", "macos"]
    TAGS = ["web", "scanner", "recon"]
    LAST_VERIFIED = "2026-07-15"
    DESCRIPTION = (
        "Fingerprint and identify Web Application Firewalls (WAF).\n"
        "Usage: wafw00f https://example.com"
    )
    TAGS = ["web", "recon", "scanner"]
    LAST_VERIFIED = "2026-07-15"
    INSTALL_COMMANDS = [
        "git clone https://github.com/EnableSecurity/wafw00f.git",
        "cd wafw00f && pip install --user .",
    ]
    RUN_COMMANDS = ["wafw00f --help"]
    PROJECT_URL = "https://github.com/EnableSecurity/wafw00f"


class Katana(HackingTool):
    TITLE = "Katana (Web Crawler)"
    SUPPORTED_OS = ["linux", "macos", "windows"]
    TAGS = ["web", "recon", "scanner"]
    LAST_VERIFIED = "2026-07-15"
    DESCRIPTION = (
        "Next-generation crawling and spidering framework from ProjectDiscovery.\n"
        "Usage: katana -u https://example.com"
    )
    TAGS = ["web", "recon", "scanner"]
    LAST_VERIFIED = "2026-07-15"
    REQUIRES_GO = True
    INSTALL_COMMANDS = [
        "go install -v github.com/projectdiscovery/katana/cmd/katana@latest",
    ]
    RUN_COMMANDS = ["katana -h"]
    PROJECT_URL = "https://github.com/projectdiscovery/katana"


class Gobuster(HackingTool):
    TITLE = "Gobuster (Dir/DNS/Vhost Brute Force)"
    SUPPORTED_OS = ["linux", "macos", "windows"]
    TAGS = ["web", "webapp", "scanner"]
    LAST_VERIFIED = "2026-07-15"
    DESCRIPTION = "Directory/file, DNS, and vhost brute-forcing tool written in Go."
    TAGS = ["web", "scanner", "recon"]
    LAST_VERIFIED = "2026-07-15"
    REQUIRES_GO = True
    INSTALL_COMMANDS = ["go install github.com/OJ/gobuster/v3@latest"]
    RUN_COMMANDS = ["gobuster --help"]
    PROJECT_URL = "https://github.com/OJ/gobuster"


class Dirsearch(HackingTool):
    TITLE = "Dirsearch (Web Path Discovery)"
    SUPPORTED_OS = ["linux", "macos", "windows"]
    TAGS = ["web", "webapp", "scanner"]
    LAST_VERIFIED = "2026-07-15"
    DESCRIPTION = "Web path brute-forcing tool for discovering directories and files on web servers."
    TAGS = ["web", "scanner", "recon"]
    LAST_VERIFIED = "2026-07-15"
    INSTALL_COMMANDS = ["pip install --user dirsearch"]
    RUN_COMMANDS = ["dirsearch --help"]
    PROJECT_URL = "https://github.com/maurosoria/dirsearch"


class OwaspZap(HackingTool):
    TITLE = "OWASP ZAP (Web App Scanner)"
    TAGS = ["web", "webapp", "scanner"]
    LAST_VERIFIED = "2026-07-15"
    WIN_INSTALL_HINT = "winget install ZAP.ZAP"
    DESCRIPTION = "Full-featured web application security scanner — proxy, spider, fuzzer, scanner."
    TAGS = ["web", "webapp", "scanner"]
    LAST_VERIFIED = "2026-07-15"
    WIN_INSTALL_HINT = "winget install ZAP.ZAP"
    SUPPORTED_OS = ["linux"]
    INSTALL_COMMANDS = ["sudo apt-get install -y zaproxy"]
    RUN_COMMANDS = ["zaproxy --help"]
    PROJECT_URL = "https://github.com/zaproxy/zaproxy"


class TestSSL(HackingTool):
    TITLE = "testssl.sh (TLS/SSL Checker)"
    SUPPORTED_OS = ["linux"]
    TAGS = ["web", "scanner"]
    LAST_VERIFIED = "2026-07-15"
    DESCRIPTION = "Check TLS/SSL ciphers, protocols, and cryptographic flaws on any port."
    TAGS = ["web", "scanner", "network"]
    LAST_VERIFIED = "2026-07-15"
    INSTALL_COMMANDS = ["git clone https://github.com/drwetter/testssl.sh.git"]
    RUN_COMMANDS = ["cd testssl.sh && ./testssl.sh --help"]
    PROJECT_URL = "https://github.com/drwetter/testssl.sh"


class Arjun(HackingTool):
    TITLE = "Arjun (HTTP Parameter Discovery)"
    SUPPORTED_OS = ["linux", "macos", "windows"]
    TAGS = ["web", "webapp", "recon"]
    LAST_VERIFIED = "2026-07-15"
    DESCRIPTION = "HTTP parameter discovery suite that finds hidden GET/POST parameters."
    TAGS = ["web", "recon", "scanner"]
    LAST_VERIFIED = "2026-07-15"
    INSTALL_COMMANDS = ["pip install --user arjun"]
    RUN_COMMANDS = ["arjun --help"]
    PROJECT_URL = "https://github.com/s0md3v/Arjun"


class Caido(HackingTool):
    TITLE = "Caido (Web Security Auditing)"
    TAGS = ["web", "webapp", "scanner"]
    LAST_VERIFIED = "2026-07-15"
    DESCRIPTION = "Lightweight, modern web security auditing toolkit — Burp Suite alternative written in Rust."
    TAGS = ["web", "webapp", "scanner"]
    LAST_VERIFIED = "2026-07-15"
    INSTALL_COMMANDS = [
        "curl -sSL https://caido.download/releases/latest/caido-cli-linux-x86_64.tar.gz | sudo tar xz -C /usr/local/bin",
    ]
    RUN_COMMANDS = ["caido --help"]
    PROJECT_URL = "https://github.com/caido/caido"
    SUPPORTED_OS = ["linux", "macos"]


class Mitmproxy(HackingTool):
    TITLE = "mitmproxy (Intercepting Proxy)"
    SUPPORTED_OS = ["linux", "macos", "windows"]
    TAGS = ["web", "webapp", "network"]
    LAST_VERIFIED = "2026-07-15"
    WIN_INSTALL_HINT = "pip install mitmproxy"
    DESCRIPTION = "Interactive TLS-capable intercepting HTTP proxy for pentesters and developers."
    TAGS = ["web", "network", "scanner"]
    LAST_VERIFIED = "2026-07-15"
    WIN_INSTALL_HINT = "pip install mitmproxy"
    INSTALL_COMMANDS = ["pip install --user mitmproxy"]
    RUN_COMMANDS = ["mitmproxy --version"]
    PROJECT_URL = "https://github.com/mitmproxy/mitmproxy"


class Corsy(HackingTool):
    TITLE = "Corsy (CORS Misconfiguration Scanner)"
    SUPPORTED_OS = ["linux", "macos"]
    TAGS = ["web", "webapp", "scanner"]
    LAST_VERIFIED = "2026-07-15"
    DESCRIPTION = "Scan for CORS misconfigurations that allow cross-origin data theft."
    TAGS = ["web", "webapp", "scanner"]
    LAST_VERIFIED = "2026-07-15"
    INSTALL_COMMANDS = [
        "git clone https://github.com/s0md3v/Corsy.git",
        "cd Corsy && pip install --user -r requirements.txt",
    ]
    PROJECT_URL = "https://github.com/s0md3v/Corsy"


class CRLFuzz(HackingTool):
    TITLE = "CRLFuzz (CRLF Injection Scanner)"
    SUPPORTED_OS = ["linux", "macos", "windows"]
    TAGS = ["web", "webapp", "scanner"]
    LAST_VERIFIED = "2026-07-15"
    DESCRIPTION = "Fast tool to scan CRLF vulnerability in web applications."
    TAGS = ["web", "webapp", "scanner"]
    LAST_VERIFIED = "2026-07-15"
    INSTALL_COMMANDS = ["go install github.com/dwisiswant0/crlfuzz/cmd/crlfuzz@latest"]
    PROJECT_URL = "https://github.com/dwisiswant0/crlfuzz"


class LinkFinder(HackingTool):
    TITLE = "LinkFinder (JS Endpoint Discovery)"
    SUPPORTED_OS = ["linux", "macos"]
    TAGS = ["web", "recon", "scanner"]
    LAST_VERIFIED = "2026-07-15"
    DESCRIPTION = "Discover endpoints and API paths hidden inside JavaScript files."
    TAGS = ["web", "recon", "osint"]
    LAST_VERIFIED = "2026-07-15"
    INSTALL_COMMANDS = [
        "git clone https://github.com/GerbenJavado/LinkFinder.git",
        "cd LinkFinder && pip install --user -r requirements.txt",
    ]
    PROJECT_URL = "https://github.com/GerbenJavado/LinkFinder"

    def run(self):
        url = Prompt.ask("Enter JS file URL")
        subprocess.run(["python3", "linkfinder.py", "-i", url, "-o", "cli"])


class WhatWaf(HackingTool):
    TITLE = "WhatWaf (WAF Detection & Bypass)"
    SUPPORTED_OS = ["linux", "macos"]
    TAGS = ["web", "webapp", "scanner"]
    LAST_VERIFIED = "2026-07-15"
    DESCRIPTION = "Detect and attempt to bypass web application firewalls and protection systems."
    TAGS = ["web", "webapp", "recon"]
    LAST_VERIFIED = "2026-07-15"
    INSTALL_COMMANDS = [
        "git clone https://github.com/Ekultek/WhatWaf.git",
        "cd WhatWaf && pip install --user -r requirements.txt",
    ]
    PROJECT_URL = "https://github.com/Ekultek/WhatWaf"

    def run(self):
        url = Prompt.ask("Enter target URL")
        subprocess.run(["python3", "whatwaf", "-u", url])


class WebAttackTools(HackingToolsCollection):
    TITLE = "Web Attack tools"
    DESCRIPTION = ""
    TOOLS = [
        Web2Attack(),
        Skipfish(),
        SubDomainFinder(),
        CheckURL(),
        SubDomainTakeOver(),
        Dirb(),
        Nuclei(),
        Ffuf(),
        Feroxbuster(),
        Nikto(),
        Wafw00f(),
        Katana(),
        Gobuster(),
        Dirsearch(),
        OwaspZap(),
        TestSSL(),
        Arjun(),
        Caido(),
        Mitmproxy(),
        Corsy(),
        CRLFuzz(),
        LinkFinder(),
        WhatWaf(),
    ]

if __name__ == "__main__":
    tools = WebAttackTools()
    tools.show_options()
