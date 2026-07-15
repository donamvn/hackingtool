from core import HackingTool
from core import HackingToolsCollection


class Prowler(HackingTool):
    TITLE = "Prowler (Cloud Security Scanner)"
    DESCRIPTION = "Open-source security tool for AWS, Azure, GCP, and Kubernetes assessments."
    INSTALL_COMMANDS = ["pip install --user prowler"]
    RUN_COMMANDS = ["prowler --help"]
    PROJECT_URL = "https://github.com/prowler-cloud/prowler"
    SUPPORTED_OS = ["linux", "macos"]
    TAGS = ["cloud", "scanner", "recon"]
    LAST_VERIFIED = "2026-07-15"


class ScoutSuite(HackingTool):
    TITLE = "ScoutSuite (Multi-Cloud Auditing)"
    DESCRIPTION = "Multi-cloud security auditing tool for AWS, Azure, GCP, Alibaba, and Oracle."
    INSTALL_COMMANDS = ["pip install --user scoutsuite"]
    RUN_COMMANDS = ["scout --help"]
    PROJECT_URL = "https://github.com/nccgroup/ScoutSuite"
    SUPPORTED_OS = ["linux", "macos"]
    TAGS = ["cloud", "scanner", "recon"]
    LAST_VERIFIED = "2026-07-15"


class Pacu(HackingTool):
    TITLE = "Pacu (AWS Exploitation Framework)"
    DESCRIPTION = "AWS exploitation framework for offensive security testing of AWS environments."
    INSTALL_COMMANDS = ["pip install --user pacu"]
    RUN_COMMANDS = ["pacu --help"]
    PROJECT_URL = "https://github.com/RhinoSecurityLabs/pacu"
    SUPPORTED_OS = ["linux", "macos"]
    TAGS = ["cloud", "exploit", "post-exploit"]
    LAST_VERIFIED = "2026-07-15"


class Trivy(HackingTool):
    TITLE = "Trivy (Container/K8s Scanner)"
    DESCRIPTION = "Comprehensive vulnerability scanner for containers, Kubernetes, IaC, and code."
    INSTALL_COMMANDS = [
        "curl -sfL https://raw.githubusercontent.com/aquasecurity/trivy/main/contrib/install.sh | sudo sh -s -- -b /usr/local/bin",
    ]
    RUN_COMMANDS = ["trivy --help"]
    PROJECT_URL = "https://github.com/aquasecurity/trivy"
    SUPPORTED_OS = ["linux", "macos"]
    TAGS = ["container", "k8s", "scanner", "cloud"]
    LAST_VERIFIED = "2026-07-15"
    WIN_INSTALL_HINT = "choco install trivy"


class CDK(HackingTool):
    TITLE = "CDK (Container/K8s Pentesting)"
    SUPPORTED_OS = ["linux"]
    DESCRIPTION = "Zero-dependency container/K8s penetration toolkit for escaping and lateral movement."
    TAGS = ["container", "k8s", "exploit", "post-exploit"]
    LAST_VERIFIED = "2026-07-15"
    INSTALL_COMMANDS = [
        "curl -sSL https://github.com/cdk-team/CDK/releases/latest/download/cdk_linux_amd64 -o cdk",
        "chmod +x cdk",
    ]
    PROJECT_URL = "https://github.com/cdk-team/CDK"


class Kubescape(HackingTool):
    TITLE = "Kubescape (K8s Security Scanner)"
    SUPPORTED_OS = ["linux"]
    DESCRIPTION = "Kubernetes security platform — risk analysis, compliance, misconfiguration scanning."
    TAGS = ["k8s", "scanner", "cloud"]
    LAST_VERIFIED = "2026-07-15"
    INSTALL_COMMANDS = ["curl -s https://raw.githubusercontent.com/kubescape/kubescape/master/install.sh | /bin/bash"]
    PROJECT_URL = "https://github.com/kubescape/kubescape"


class CloudSecurityTools(HackingToolsCollection):
    TITLE = "Cloud Security Tools"
    DESCRIPTION = "Tools for cloud infrastructure security assessment and exploitation."
    TOOLS = [
        Prowler(),
        ScoutSuite(),
        Pacu(),
        Trivy(),
        CDK(),
        Kubescape(),
    ]
