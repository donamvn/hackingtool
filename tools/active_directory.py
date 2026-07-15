import subprocess

from core import HackingTool
from core import HackingToolsCollection

from rich.prompt import Prompt


class BloodHound(HackingTool):
    TITLE = "BloodHound (AD Attack Paths)"
    DESCRIPTION = "Uses graph theory to reveal hidden attack paths in Active Directory/Azure environments."
    INSTALL_COMMANDS = [
        "pip install --user bloodhound",
        "sudo apt-get install -y neo4j",
    ]
    RUN_COMMANDS = ["bloodhound-python --help"]
    PROJECT_URL = "https://github.com/BloodHoundAD/BloodHound"
    SUPPORTED_OS = ["linux", "macos"]
    TAGS = ["ad", "recon", "windows", "network"]
    LAST_VERIFIED = "2026-07-15"


class NetExec(HackingTool):
    TITLE = "NetExec — nxc (Network Pentesting)"
    DESCRIPTION = "Swiss army knife for pentesting Windows/AD networks. Successor to CrackMapExec."
    INSTALL_COMMANDS = ["pip install --user netexec"]
    RUN_COMMANDS = ["nxc --help"]
    PROJECT_URL = "https://github.com/Pennyw0rth/NetExec"
    SUPPORTED_OS = ["linux", "macos"]
    TAGS = ["ad", "windows", "network", "post-exploit"]
    LAST_VERIFIED = "2026-07-15"


class Impacket(HackingTool):
    TITLE = "Impacket (Network Protocol Tools)"
    DESCRIPTION = "Python classes for working with SMB, MSRPC, Kerberos, LDAP, and more."
    INSTALL_COMMANDS = ["pip install --user impacket"]
    RUN_COMMANDS = ["impacket-smbclient --help"]
    PROJECT_URL = "https://github.com/fortra/impacket"
    SUPPORTED_OS = ["linux", "macos"]
    TAGS = ["ad", "network", "windows", "kerberos"]
    LAST_VERIFIED = "2026-07-15"


class Responder(HackingTool):
    TITLE = "Responder (LLMNR/NBT-NS Poisoner)"
    DESCRIPTION = "LLMNR/NBT-NS/MDNS poisoner with rogue authentication servers for credential capture."
    INSTALL_COMMANDS = ["git clone https://github.com/lgandx/Responder.git"]
    RUN_COMMANDS = ["cd Responder && sudo python3 Responder.py --help"]
    PROJECT_URL = "https://github.com/lgandx/Responder"
    SUPPORTED_OS = ["linux"]
    TAGS = ["ad", "network", "password", "windows"]
    LAST_VERIFIED = "2026-07-15"


class Certipy(HackingTool):
    TITLE = "Certipy (AD Certificate Abuse)"
    DESCRIPTION = "Active Directory Certificate Services enumeration and abuse tool."
    INSTALL_COMMANDS = ["pip install --user certipy-ad"]
    RUN_COMMANDS = ["certipy --help"]
    PROJECT_URL = "https://github.com/ly4k/Certipy"
    SUPPORTED_OS = ["linux", "macos"]
    TAGS = ["ad", "windows", "exploit"]
    LAST_VERIFIED = "2026-07-15"


class Kerbrute(HackingTool):
    TITLE = "Kerbrute (Kerberos Brute Force)"
    DESCRIPTION = "Kerberos pre-auth brute-forcer for username enumeration and password spraying."
    REQUIRES_GO = True
    INSTALL_COMMANDS = [
        "go install github.com/ropnop/kerbrute@latest",
    ]
    RUN_COMMANDS = ["kerbrute --help"]
    PROJECT_URL = "https://github.com/ropnop/kerbrute"
    SUPPORTED_OS = ["linux", "macos"]
    TAGS = ["ad", "kerberos", "password", "cracking"]
    LAST_VERIFIED = "2026-07-15"


class Coercer(HackingTool):
    TITLE = "Coercer (Windows Coerce Attacks)"
    SUPPORTED_OS = ["linux", "macos", "windows"]
    DESCRIPTION = "Automatically find and exploit Windows coerce authentication vulnerabilities (PetitPotam, PrinterBug, etc)."
    TAGS = ["ad", "windows", "exploit", "network"]
    LAST_VERIFIED = "2026-07-15"
    INSTALL_COMMANDS = ["pip install --user coercer"]
    PROJECT_URL = "https://github.com/p0dalirius/Coercer"

    def run(self):
        target = Prompt.ask("Enter target IP/hostname")
        subprocess.run(["coercer", "scan", "-t", target])


class Ldapdomaindump(HackingTool):
    TITLE = "ldapdomaindump (LDAP Info Dumper)"
    SUPPORTED_OS = ["linux", "macos", "windows"]
    DESCRIPTION = "Dump LDAP information from Active Directory into human-readable HTML/JSON/grep format."
    TAGS = ["ad", "recon", "windows", "network"]
    LAST_VERIFIED = "2026-07-15"
    INSTALL_COMMANDS = ["pip install --user ldapdomaindump"]
    PROJECT_URL = "https://github.com/dirkjanm/ldapdomaindump"

    def run(self):
        target = Prompt.ask("Enter DC IP")
        domain = Prompt.ask("Enter domain (e.g. CORP)")
        user = Prompt.ask("Enter username")
        subprocess.run(["ldapdomaindump", target, "-u", f"{domain}\\{user}", "-p", ""])


class ActiveDirectoryTools(HackingToolsCollection):
    TITLE = "Active Directory Tools"
    DESCRIPTION = "Tools for AD enumeration, attack path discovery, and credential attacks."
    TOOLS = [
        BloodHound(),
        NetExec(),
        Impacket(),
        Responder(),
        Certipy(),
        Kerbrute(),
        Coercer(),
        Ldapdomaindump(),
    ]