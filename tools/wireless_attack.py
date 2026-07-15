from rich.prompt import Prompt

from core import HackingTool, HackingToolsCollection, console


class WIFIPumpkin(HackingTool):
    TITLE = "WiFi-Pumpkin"
    DESCRIPTION = (
        "The WiFi-Pumpkin is a rogue AP framework to easily create fake networks\n"
        "while forwarding legitimate traffic to and from the unsuspecting target."
    )
    INSTALL_COMMANDS = [
        "sudo apt install -y libssl-dev libffi-dev build-essential python3-pyqt5",
        "git clone https://github.com/P0cL4bs/wifipumpkin3.git",
        "chmod -R 755 wifipumpkin3",
        "cd wifipumpkin3 && pip install --user .",
    ]
    RUN_COMMANDS = ["sudo wifipumpkin3"]
    PROJECT_URL = "https://github.com/P0cL4bs/wifipumpkin3"
    SUPPORTED_OS = ["linux"]
    TAGS = ["wireless", "wifi", "phishing"]
    LAST_VERIFIED = "2026-07-15"
    REQUIRES_WIFI = True


class pixiewps(HackingTool):
    TITLE = "pixiewps"
    DESCRIPTION = (
        "Pixiewps is a tool written in C used to bruteforce offline the WPS pin\n"
        "exploiting the low or non-existing entropy of some Access Points "
        "(pixie dust attack)."
    )
    INSTALL_COMMANDS = [
        # Bug 29 fix: removed wget https://pastebin.com/... (insecure download from pastebin)
        "git clone https://github.com/wiire/pixiewps.git && apt-get -y install build-essential",
        "cd pixiewps && make",
        "cd pixiewps && sudo make install",
    ]
    PROJECT_URL = "https://github.com/wiire/pixiewps"
    SUPPORTED_OS = ["linux"]
    TAGS = ["wireless", "wifi", "cracking"]
    LAST_VERIFIED = "2026-07-15"
    REQUIRES_WIFI = True

    def run(self):
        console.print(
            "[bold cyan]Usage:[/bold cyan]\n"
            " 1. Put interface into monitor mode: [yellow]airmon-ng start <iface>[/yellow]\n"
            " 2. Scan: [yellow]wash -i <mon-iface>[/yellow]\n"
            " 3. Attack: [yellow]reaver -i <mon-iface> -b <BSSID> -c <ch> -vvv -K 1 -f[/yellow]\n"
            " 4. Run: [yellow]pixiewps -h[/yellow]"
        )


class BluePot(HackingTool):
    TITLE = "Bluetooth Honeypot GUI Framework"
    DESCRIPTION = (
        "You need at least 1 bluetooth receiver.\n"
        "Install libbluetooth-dev (Ubuntu) / bluez-libs-devel (Fedora) / bluez-devel (openSUSE)."
    )
    INSTALL_COMMANDS = [
        # Bug 15 fix: missing comma caused implicit string concatenation — two strings joined
        "sudo wget https://raw.githubusercontent.com/andrewmichaelsmith/bluepot/master/bin/bluepot-0.2.tar.gz",
        "sudo tar xfz bluepot-0.2.tar.gz && sudo rm bluepot-0.2.tar.gz",
    ]
    RUN_COMMANDS = ["cd bluepot && sudo java -jar bluepot.jar"]
    PROJECT_URL = "https://github.com/andrewmichaelsmith/bluepot"
    SUPPORTED_OS = ["linux"]
    TAGS = ["wireless", "recon"]
    LAST_VERIFIED = "2026-07-15"
    REQUIRES_JAVA = True


class Fluxion(HackingTool):
    TITLE = "Fluxion"
    DESCRIPTION = "Fluxion is a remake of linset by vk496 with enhanced functionality."
    INSTALL_COMMANDS = [
        "git clone https://github.com/FluxionNetwork/fluxion.git",
        "cd fluxion && chmod +x fluxion.sh",
    ]
    RUN_COMMANDS = ["cd fluxion && sudo bash fluxion.sh -i"]
    PROJECT_URL = "https://github.com/FluxionNetwork/fluxion"
    SUPPORTED_OS = ["linux"]
    TAGS = ["wireless", "wifi", "phishing"]
    LAST_VERIFIED = "2026-07-15"
    REQUIRES_WIFI = True


class Wifiphisher(HackingTool):
    TITLE = "Wifiphisher"
    DESCRIPTION = (
        "Wifiphisher is a rogue Access Point framework for conducting red team engagements\n"
        "or Wi-Fi security testing. Easily achieve man-in-the-middle position against\n"
        "wireless clients by performing targeted Wi-Fi association attacks."
    )
    INSTALL_COMMANDS = [
        "git clone https://github.com/wifiphisher/wifiphisher.git",
        "cd wifiphisher && pip install --user .",
    ]
    RUN_COMMANDS = ["cd wifiphisher && sudo wifiphisher"]
    PROJECT_URL = "https://github.com/wifiphisher/wifiphisher"
    SUPPORTED_OS = ["linux"]
    TAGS = ["wireless", "wifi", "phishing"]
    LAST_VERIFIED = "2026-07-15"
    REQUIRES_WIFI = True


class Wifite(HackingTool):
    TITLE = "Wifite"
    DESCRIPTION = "Wifite is an automated wireless attack tool."
    INSTALL_COMMANDS = [
        "git clone https://github.com/derv82/wifite2.git",
        "cd wifite2 && pip install --user .",
    ]
    RUN_COMMANDS = ["sudo wifite"]
    PROJECT_URL = "https://github.com/derv82/wifite2"
    SUPPORTED_OS = ["linux"]
    TAGS = ["wireless", "wifi", "cracking"]
    LAST_VERIFIED = "2026-07-15"
    REQUIRES_WIFI = True


class Howmanypeople(HackingTool):
    TITLE = "Howmanypeople"
    DESCRIPTION = (
        "Count the number of people around you by monitoring wifi signals.\n"
        "[@] WIFI ADAPTER REQUIRED\n"
        "[*] It may be illegal to monitor networks for MAC addresses on networks you do not own."
    )
    INSTALL_COMMANDS = [
        # Bug 14 fix: missing comma caused "sudo apt-get install tshark;sudo python3..."
        # to be one implicitly concatenated string — only first command ran
        "sudo apt-get install -y tshark",
        "pip install --user howmanypeoplearearound",
    ]
    RUN_COMMANDS = ["howmanypeoplearearound"]
    SUPPORTED_OS = ["linux"]
    TAGS = ["wireless", "wifi", "recon"]
    LAST_VERIFIED = "2026-07-15"
    REQUIRES_WIFI = True


class Airgeddon(HackingTool):
    TITLE = "Airgeddon (Wireless Attack Suite)"
    DESCRIPTION = (
        "Multi-use bash script for auditing wireless networks.\n"
        "Covers WPA/WPA2, WEP, WPS, PMKID, evil twin, handshake capture and more."
    )
    SUPPORTED_OS = ["linux"]
    TAGS = ["wireless", "wifi", "cracking"]
    LAST_VERIFIED = "2026-07-15"
    REQUIRES_WIFI = True
    INSTALL_COMMANDS = [
        "git clone https://github.com/v1s1t0r1sh3r3/airgeddon.git",
    ]
    RUN_COMMANDS = ["cd airgeddon && sudo bash airgeddon.sh"]
    PROJECT_URL = "https://github.com/v1s1t0r1sh3r3/airgeddon"


class Hcxdumptool(HackingTool):
    TITLE = "hcxdumptool (PMKID Capture)"
    DESCRIPTION = (
        "Capture packets and PMKID hashes from WLAN devices.\n"
        "Usage: hcxdumptool -i <iface> -o capture.pcapng --enable_status=1"
    )
    SUPPORTED_OS = ["linux"]
    TAGS = ["wireless", "wifi", "cracking"]
    LAST_VERIFIED = "2026-07-15"
    REQUIRES_WIFI = True
    INSTALL_COMMANDS = [
        "git clone https://github.com/ZerBea/hcxdumptool.git",
        "cd hcxdumptool && make && sudo make install",
    ]
    RUN_COMMANDS = ["hcxdumptool --help"]
    PROJECT_URL = "https://github.com/ZerBea/hcxdumptool"


class Hcxtools(HackingTool):
    TITLE = "hcxtools (PMKID/Hash Conversion)"
    DESCRIPTION = (
        "Convert captured WLAN packets to hashcat/JtR-compatible format.\n"
        "Usage: hcxpcapngtool -o hashes.txt capture.pcapng"
    )
    SUPPORTED_OS = ["linux"]
    TAGS = ["wireless", "wifi", "cracking"]
    LAST_VERIFIED = "2026-07-15"
    INSTALL_COMMANDS = [
        "git clone https://github.com/ZerBea/hcxtools.git",
        "cd hcxtools && make && sudo make install",
    ]
    RUN_COMMANDS = ["hcxpcapngtool --help"]
    PROJECT_URL = "https://github.com/ZerBea/hcxtools"


class Bettercap(HackingTool):
    TITLE = "Bettercap (Network/WiFi/BLE MITM)"
    DESCRIPTION = "Swiss army knife for WiFi, BLE, HID, and Ethernet network recon and MITM attacks."
    TAGS = ["wireless", "wifi", "network"]
    LAST_VERIFIED = "2026-07-15"
    SUPPORTED_OS = ["linux"]
    INSTALL_COMMANDS = ["sudo apt-get install -y bettercap"]
    RUN_COMMANDS = ["sudo bettercap --help"]
    PROJECT_URL = "https://github.com/bettercap/bettercap"


class Esp8266Deauther(HackingTool):
    TITLE = "ESP8266 Deauther (Hardware WiFi Deauth)"
    SUPPORTED_OS = ["linux", "macos", "windows"]
    DESCRIPTION = "Scan for WiFi devices, perform deauth attacks, create beacons — runs on ESP8266 hardware."
    TAGS = ["wireless", "wifi", "dos"]
    LAST_VERIFIED = "2026-07-15"
    INSTALL_COMMANDS = [
        "git clone https://github.com/SpacehuhnTech/esp8266_deauther.git",
    ]
    PROJECT_URL = "https://github.com/SpacehuhnTech/esp8266_deauther"

    def __init__(self):
        super().__init__(runnable=False)


class WirelessAttackTools(HackingToolsCollection):
    TITLE = "Wireless attack tools"
    TOOLS = [
        WIFIPumpkin(),
        pixiewps(),
        BluePot(),
        Fluxion(),
        Wifiphisher(),
        Wifite(),
        Howmanypeople(),
        Airgeddon(),
        Hcxdumptool(),
        Hcxtools(),
        Bettercap(),
        Esp8266Deauther(),
    ]


if __name__ == "__main__":
    tools = WirelessAttackTools()
    tools.show_options()
