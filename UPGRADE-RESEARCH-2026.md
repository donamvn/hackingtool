# HackingTool Upgrade Research (2026-07-15)

## Methodology

1. Cloned repo, audited all 148 HackingTool classes across 24 Python files
2. Checked GitHub API status for 40 potentially dead/outdated repos
3. Researched new tools for 2025-2026 via GitHub topics, security blogs, community lists
4. Categorized actions: REMOVE (dead), FIX (URL moved), KEEP, ADD (new)

---

## Phase 1: Dead/Removed Tools (REMOVE or mark deprecated)

### Confirmed 404 (repo deleted, no successor)

| Tool | Old URL | Action |
|------|---------|--------|
| aSYNcrone | fatihsnsy/aSYNcrone | REMOVE |
| Infoga | m4ll0k/Infoga | REMOVE |
| XSS-Freak | PR0PH3CY33/XSS-Freak | REMOVE |
| wifijammer-ng | MisterBianco/wifijammer-ng | REMOVE |
| finduser | xHak9x/finduser | REMOVE |

### Archived by owner (read-only)

| Tool | URL | Last Activity | Action |
|------|-----|---------------|--------|
| GoldenEye | jseidl/GoldenEye | 2023 | REMOVE (author says "NO LONGER MAINTAINED") |
| HeraKeylogger | UndeadSec/HeraKeylogger | 2022 | REMOVE (archived 2026-05) |
| Enigma | UndeadSec/Enigma | 2021 | REMOVE (archived 2026-05) |
| pyshell | knassar702/pyshell | 2022 | REMOVE (archived 2022-07) |

### Dead (no activity 5+ years, no archive flag)

| Tool | URL | Last Activity | Action |
|------|-----|---------------|--------|
| spycam | indexnotfound404/spycam | 2018 | REMOVE |
| Brutal | Screetsec/Brutal | 2020 | REMOVE |
| Vegile | Screetsec/Vegile | 2022 | REMOVE |
| fakeap (EvilTwin) | Z4nzu/fakeap | 2018 | REMOVE |
| fastssh | Z4nzu/fastssh | 2018 | REMOVE |
| websploit | The404Hacking/websploit | 2017 | REMOVE |
| XSSCon | menkrep1337/XSSCon | 2019 | REMOVE |
| XanXSS | Ekultek/XanXSS | 2018 | REMOVE |
| instaBrute | chinoogawa/instaBrute | 2019 | REMOVE (Python 2 only) |
| Brute_Force | Matrix07ksa/Brute_Force | 2019 | REMOVE |
| social_mapper | Greenwolf/social_mapper | 2021 | REMOVE (README: "no longer maintained") |

### Stale but functional (keep with warning)

| Tool | URL | Last Activity | Action |
|------|-----|---------------|--------|
| Stitch | nathanlopez/Stitch | 2024 | KEEP (mark stale) |
| venom | r00t-3xp10it/venom | 2023 | KEEP (mark stale) |
| TheFatRat | Screetsec/TheFatRat | 2024 | KEEP (mark stale) |
| Mob-Droid | kinghacker0/Mob-Droid | 2025 | KEEP |
| reconspider | bhavsec/reconspider | 2023 | KEEP (mark stale) |
| ReconDog | s0md3v/ReconDog | 2021 | REMOVE (superseded by httpx+katana) |
| Striker | s0md3v/Striker | 2023 | KEEP (mark stale, "2.0 prototype") |
| RVuln | iinc0gnit0/RVuln -> yangr0/RVuln | 2020 | REMOVE (dead at new URL too) |

**Total REMOVE: ~24 tools**

---

## Phase 2: URL Fixes (repo moved/renamed)

| Tool | Old URL | New URL | Action |
|------|---------|---------|--------|
| Blazy | UltimateHackers/Blazy | s0md3v/Blazy | FIX URL |
| XSStrike | UltimateHackers/XSStrike | s0md3v/XSStrike | FIX URL (active, v3.1.6) |
| RVuln | iinc0gnit0/RVuln | yangr0/RVuln | REMOVE (dead at both) |

---

## Phase 3: New Tools to Add (2025-2026)

### Information Gathering / OSINT

| Tool | GitHub | Description | Priority |
|------|--------|-------------|----------|
| Uncover | projectdiscovery/uncover | Query multiple search engines (Shodan, Censys, FOFA, Hunter) from CLI | HIGH |
| Alterx | projectdiscovery/alterx | DSL-based subdomain wordlist permutation generator | MEDIUM |
| GitDorker | obheda12/GitDorker | GitHub dorking for sensitive info/secrets | MEDIUM |
| Recon-ng | lanmaster53/recon-ng | Full-featured OSINT web reconnaissance framework | HIGH |

### Web Attack

| Tool | GitHub | Description | Priority |
|------|--------|-------------|----------|
| Param Miner | (BurpSuite extension) | Identify hidden params — skip (Burp-only) | - |
| Ghauri | r0oth3x49/ghauri | Advanced SQL injection detection (sqlmap alternative) | HIGH |
| CRLFuzz | dwisiswant0/crlfuzz | Fast CRLF vulnerability scanner | MEDIUM |
| Corsy | s0md3v/Corsy | CORS misconfiguration scanner | MEDIUM |

### Post Exploitation / C2

| Tool | GitHub | Description | Priority |
|------|--------|-------------|----------|
| Villain | t3l3machus/Villain | C2 managing multiple reverse TCP/HoaxShell shells | HIGH |
| Starkiller | BC-SECURITY/Starkiller | Frontend for Empire C2 framework | MEDIUM |
| Covenant | cobbr/Covenant | .NET C2 framework | MEDIUM (archived?) |

### Active Directory

| Tool | GitHub | Description | Priority |
|------|--------|-------------|----------|
| Coercer | p0dalirius/Coercer | Windows coerce authentication attacks (PetitPotam etc) | HIGH |
| ADReaper | AidenPearce369/ADReaper | Fast Go-based AD enumeration | MEDIUM |
| Ldapdomaindump | dirkjanm/ldapdomaindump | LDAP info dumper | MEDIUM |

### Container / Cloud

| Tool | GitHub | Description | Priority |
|------|--------|-------------|----------|
| CDK | cdk-team/CDK | Container/K8s penetration toolkit | HIGH |
| Kubescape | kubescape/kubescape | K8s security scanning | HIGH |

### AI/LLM Security

| Tool | GitHub | Description | Priority |
|------|--------|-------------|----------|
| PyRIT | Azure/PyRIT | Microsoft red-teaming toolkit for AI/LLM | HIGH |
| Garak | NVIDIA/garak | LLM vulnerability scanner | HIGH |

### Wireless

| Tool | GitHub | Description | Priority |
|------|--------|-------------|----------|
| ESP8266 Deauther | SpacehuhnTech/esp8266_deauther | Hardware WiFi deauth tool | MEDIUM |

---

## Phase 4: Code Quality Improvements

### Current issues in codebase

1. **Inconsistent install patterns**: mix of `sudo pip3`, `pip install --user`, `pip install`
2. **No Windows support**: all INSTALL_COMMANDS assume Linux/bash
3. **Python 2 remnants**: some tools still reference Python 2
4. **Missing error handling**: git clone failures not caught
5. **No version pinning**: tools installed from latest (may break)
6. **Duplicate tools**: some tools appear in multiple categories
7. **Missing SUPPORTED_OS**: most tools don't declare OS support

### Recommended code changes

1. Standardize install to `pip install --user` (no sudo)
2. Add `SUPPORTED_OS` to all tools
3. Add `LAST_VERIFIED` date field to HackingTool base class
4. Add `ALTERNATIVES` field for deprecated tools pointing to replacements
5. Add `TAGS` field for better search/filtering
6. Update `requirements.txt` with current dependencies
7. Add Windows install commands where applicable (winget, scoop, choco)

---

## Phase 5: Implementation Priority

### Batch 1 (Critical) — DONE 2026-07-15
- [x] Remove 24 dead/404/archived tools
- [x] Fix 2 moved URLs (Blazy, XSStrike)
- [x] Add HIGH priority new tools (12 tools)

### Batch 2 (Important) — DONE 2026-07-15
- [x] Add MEDIUM priority new tools (6 tools: LinkFinder, WhatWaf, GitDorker, Ldapdomaindump, ESP8266 Deauther, Starkiller)
- [x] Add SUPPORTED_OS to all existing tools
- [x] Standardize install commands (all sudo pip → pip install --user)

### Batch 3 (Polish) — DONE 2026-07-15
- [x] Update constants.py: repo owner → donamvn, version → 2.1.0
- [x] Rewrite README: badges, What's New v2.1.0, correct tool count

### Batch 4 (Future — next session)
- [ ] Add TAGS field to HackingTool base class
- [ ] Add LAST_VERIFIED date field
- [ ] Add Windows install alternatives (winget/scoop/choco)
- [ ] Add Docker support for more tools
- [ ] CI: auto-check repo URLs monthly
- [ ] Integrate tool catalog into reverse-skill as reference

---

## Summary

| Category | Count |
|----------|-------|
| Original tools | 148 |
| To REMOVE | ~24 |
| To FIX URL | 2 |
| To ADD (Batch 1) | ~12 |
| To ADD (Batch 2) | ~8 |
| **Final count (after Batch 1)** | **~136** |
| **Final count (after all)** | **~144** |

---

*Research conducted 2026-07-15 by Claude. Sources: GitHub API, agent web research, community tool lists.*
*Next update: verify all remaining tool URLs, add Batch 2 tools.*
