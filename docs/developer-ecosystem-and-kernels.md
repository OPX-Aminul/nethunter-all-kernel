# Developer Platforms and Kernel Ecosystem - Master Index

Compiled from official documentation, public APIs, and project registries (October 2026).

Scope: a curated, linkable index. There is no complete public registry of every developer
or every open-source project in the world, so this document covers the platforms,
registries, communities, and kernel families that define the ecosystem. It does not
contain scraped personal data.

Companion file: `docs/nethunter-kernels.md` (full Kali NetHunter device and kernel table,
generated from the official `devices.yml`).

---

## 1. Code Hosting and Version Control

| Platform | URL | Type / Notes |
|---|---|---|
| GitHub | https://github.com | Largest public code host; GitHub API, Actions, Packages |
| GitLab | https://gitlab.com | DevOps platform; self-managed option; GitLab API |
| Codeberg | https://codeberg.org | Non-profit Forgejo instance (EU) |
| Bitbucket | https://bitbucket.org | Atlassian; Git + Mercurial legacy |
| SourceForge | https://sourceforge.net | Long-running OSS host and mirror |
| GNU Savannah | https://savannah.gnu.org | GNU/FSF project hosting |
| GNU Savannah (non-GNU) | https://savannah.nongnu.org | Non-GNU free software |
| SourceHut | https://sr.ht | Minimalist forge; git, mailing lists, CI |
| Launchpad | https://launchpad.net | Ubuntu/Bazaar hosting and build farm |
| Gitee | https://gitee.com | Major Chinese code host |
| Azure Repos | https://azure.microsoft.com/products/devops/repos | Microsoft DevOps |
| AWS CodeCommit | https://aws.amazon.com/codecommit/ | Managed Git (closed to new customers) |
| Google Cloud Source Repositories | https://cloud.google.com/source-repositories | Managed Git (migration to Cloud Build) |
| NotABug | https://notabug.org | Free-software-focused forge |
| GitGud | https://gitgud.io | GitLab-based host |
| Fossil SCM | https://fossil-scm.org | Distributed SCM with built-in wiki/tickets |
| Radicle | https://radicle.xyz | Peer-to-peer code collaboration |
| Gitea | https://gitea.com | Self-hostable forge |
| Forgejo | https://forgejo.org | Community fork of Gitea |
| Gogs | https://gogs.io | Lightweight self-hosted Git |
| Gerrit | https://www.gerritcodereview.com | Code review for large projects |
| Phabricator (archived) | https://phacility.com/phabricator/ | Legacy review/workflow suite |
| Kallithea | https://kallithea-scm.org | Self-hosted SCM |
| RhodeCode | https://rhodecode.com | Self-hosted enterprise SCM |

## 2. Package Registries and Artifact Hubs

| Registry | URL | Ecosystem |
|---|---|---|
| npm | https://www.npmjs.com | JavaScript / Node.js |
| PyPI | https://pypi.org | Python |
| Maven Central | https://central.sonatype.com | Java / JVM |
| NuGet | https://www.nuget.org | .NET |
| crates.io | https://crates.io | Rust |
| RubyGems | https://rubygems.org | Ruby |
| Packagist | https://packagist.org | PHP / Composer |
| Hex | https://hex.pm | Elixir / Erlang |
| pub.dev | https://pub.dev | Dart / Flutter |
| CPAN | https://www.cpan.org | Perl |
| CTAN | https://www.ctan.org | TeX |
| Anaconda | https://anaconda.org | Python / data science |
| conda-forge | https://conda-forge.org | Community conda channel |
| Homebrew | https://brew.sh | macOS / Linux packages |
| Chocolatey | https://chocolatey.org | Windows packages |
| vcpkg | https://vcpkg.io | C/C++ (Microsoft) |
| Conan | https://conan.io | C/C++ |
| Docker Hub | https://hub.docker.com | Container images |
| Quay | https://quay.io | Container images (Red Hat) |
| GitHub Container Registry | https://ghcr.io | Container images |
| Artifact Hub | https://artifacthub.io | Helm charts, CNCF artifacts |
| JSR | https://jsr.io | JavaScript/TypeScript registry |
| Open VSX | https://open-vsx.org | VS Code extensions |
| F-Droid | https://f-droid.org | Android FOSS apps |
| Flathub | https://flathub.org | Linux desktop apps |
| Snap Store | https://snapcraft.io/store | Linux apps |
| AppImageHub | https://www.appimagehub.com | Linux AppImages |

## 3. CI/CD, Build and DevOps

| Service | URL | Notes |
|---|---|---|
| GitHub Actions | https://github.com/features/actions | CI/CD integrated with GitHub |
| GitLab CI/CD | https://docs.gitlab.com/ee/ci/ | Integrated pipelines |
| Jenkins | https://www.jenkins.io | Self-hosted automation server |
| CircleCI | https://circleci.com | Hosted CI |
| Travis CI | https://www.travis-ci.com | Hosted CI |
| Azure Pipelines | https://azure.microsoft.com/products/devops/pipelines | Microsoft CI/CD |
| AWS CodePipeline / CodeBuild | https://aws.amazon.com/codepipeline/ | AWS CI/CD |
| Google Cloud Build | https://cloud.google.com/build | GCP CI/CD |
| Buildkite | https://buildkite.com | Hybrid CI |
| Drone | https://www.drone.io | Container-native CI |
| Woodpecker CI | https://woodpecker-ci.org | Community fork of Drone |
| Tekton | https://tekton.dev | Kubernetes-native CI/CD |
| Argo CD | https://argoproj.github.io/cd/ | GitOps continuous delivery |
| Flux | https://fluxcd.io | GitOps |
| TeamCity | https://www.jetbrains.com/teamcity/ | JetBrains CI |
| AppVeyor | https://www.appveyor.com | Windows CI |
| Cirrus CI | https://cirrus-ci.org | Free CI for OSS |
| Codecov | https://about.codecov.io | Coverage reporting |
| SonarQube | https://www.sonarsource.com/products/sonarqube/ | Static analysis |
| Dependabot | https://github.com/dependabot | Dependency updates |
| Renovate | https://docs.renovatebot.com | Dependency updates |

## 4. Cloud IDEs, Notebooks and Sandboxes

| Platform | URL | Notes |
|---|---|---|
| GitHub Codespaces | https://github.com/features/codespaces | Cloud dev environments |
| Gitpod | https://www.gitpod.io | Ephemeral dev environments |
| Replit | https://replit.com | Browser IDE and hosting |
| CodeSandbox | https://codesandbox.io | Web app sandboxes |
| StackBlitz | https://stackblitz.com | Browser dev environment (WebContainers) |
| Glitch | https://glitch.com | Collaborative app hosting |
| Google Colab | https://colab.research.google.com | Hosted Jupyter notebooks |
| Kaggle Notebooks | https://www.kaggle.com/code | Data science notebooks |
| Jupyter | https://jupyter.org | Notebook ecosystem |
| Binder | https://mybinder.org | Reproducible notebooks from repos |
| AWS Cloud9 | https://aws.amazon.com/cloud9/ | Cloud IDE |
| Eclipse Che | https://eclipse.dev/che/ | Kubernetes-native IDE |
| Coder | https://coder.com | Self-hosted cloud dev environments |
| Daytona | https://www.daytona.io | Dev environment manager |
| Devcontainers | https://containers.dev | Dev container specification |

## 5. Developer Communities, Q&A and Publishing

| Platform | URL | Notes |
|---|---|---|
| Stack Overflow | https://stackoverflow.com | Q&A |
| Stack Exchange | https://stackexchange.com | Network of Q&A sites |
| Dev.to | https://dev.to | Developer blogging |
| Hashnode | https://hashnode.com | Developer blogging |
| Medium | https://medium.com | General publishing |
| Substack | https://substack.com | Newsletters |
| Reddit | https://www.reddit.com | Topic communities (r/programming, r/linux, r/opensource) |
| Hacker News | https://news.ycombinator.com | Tech discussion |
| Lobsters | https://lobste.rs | Computing link aggregator |
| Discord | https://discord.com | Community chat |
| Discourse | https://www.discourse.org | Forum software |
| GitHub Discussions | https://docs.github.com/discussions | Repo discussions |
| Gitter (Matrix) | https://matrix.org | Chat, migrated to Matrix |
| Libera.Chat | https://libera.chat | IRC network for OSS |
| OFTC | https://www.oftc.net | IRC network |
| Matrix | https://matrix.org | Federated chat protocol |
| X / Twitter | https://x.com | Developer announcements |
| Mastodon | https://joinmastodon.org | Federated social |
| Bluesky | https://bsky.app | Social |
| LinkedIn | https://www.linkedin.com | Professional network |
| Product Hunt | https://www.producthunt.com | Product launches |

## 6. Learning, Video and Reference

| Platform | URL | Notes |
|---|---|---|
| YouTube | https://www.youtube.com | Video tutorials and conference talks |
| PeerTube | https://joinpeertube.org | Federated video |
| freeCodeCamp | https://www.freecodecamp.org | Free curriculum |
| MDN Web Docs | https://developer.mozilla.org | Web platform reference |
| web.dev | https://web.dev | Google web guidance |
| W3C | https://www.w3.org | Web standards |
| WHATWG | https://whatwg.org | Living web standards |
| IETF | https://www.ietf.org | Internet standards (RFCs) |
| TC39 | https://tc39.es | ECMAScript standardization |
| ECMA International | https://ecma-international.org | Standards |
| ISO | https://www.iso.org | International standards |
| IEEE | https://www.ieee.org | Engineering standards |
| OASIS | https://www.oasis-open.org | Open standards |
| Khronos Group | https://www.khronos.org | Graphics/compute APIs |
| OpenSSF | https://openssf.org | Open source security |
| SPDX | https://spdx.dev | License identifiers |
| OSI | https://opensource.org | Open source definition/licenses |
| Coursera | https://www.coursera.org | Courses |
| edX | https://www.edx.org | Courses |
| Udemy | https://www.udemy.com | Courses |
| Khan Academy | https://www.khanacademy.org | Free learning |
| Pluralsight | https://www.pluralsight.com | Professional courses |
| Frontend Masters | https://frontendmasters.com | Web courses |
| egghead.io | https://egghead.io | Short courses |
| Exercism | https://exercism.org | Practice and mentoring |
| LeetCode | https://leetcode.com | Algorithm practice |
| Codewars | https://www.codewars.com | Coding katas |
| Roadmap.sh | https://roadmap.sh | Learning roadmaps |

## 7. Search, Discovery and Code Intelligence

| Service | URL | Notes |
|---|---|---|
| Google | https://www.google.com | General search |
| Bing | https://www.bing.com | General search |
| DuckDuckGo | https://duckduckgo.com | Privacy search |
| Brave Search | https://search.brave.com | Independent index |
| GitHub Search | https://github.com/search | Code/repo/issue search |
| Sourcegraph | https://sourcegraph.com | Cross-repo code search |
| grep.app | https://grep.app | Code search |
| Libraries.io | https://libraries.io | Dependency and package discovery |
| Open Hub (Ohloh) | https://www.openhub.net | OSS project analytics |
| StackShare | https://stackshare.io | Tech stack discovery |
| AlternativeTo | https://alternativeto.net | Software alternatives |
| Slant | https://www.slant.co | Technology comparisons |
| Awesome Lists | https://github.com/sindresorhus/awesome | Curated topic lists |
| npm trends | https://npmtrends.com | Package download trends |
| Google Trends | https://trends.google.com | Search interest |

## 8. Freelance, Employment and Talent Marketplaces

| Platform | URL | Notes |
|---|---|---|
| Upwork | https://www.upwork.com | Freelance marketplace |
| Fiverr | https://www.fiverr.com | Gig marketplace |
| Freelancer | https://www.freelancer.com | Freelance marketplace |
| Toptal | https://www.toptal.com | Vetted freelance network |
| Contra | https://contra.com | Commission-free freelance |
| PeoplePerHour | https://www.peopleperhour.com | Freelance marketplace |
| Guru | https://www.guru.com | Freelance marketplace |
| 99designs | https://99designs.com | Design marketplace |
| Wellfound (AngelList Talent) | https://wellfound.com | Startup jobs |
| LinkedIn Jobs | https://www.linkedin.com/jobs/ | Professional jobs |
| Indeed | https://www.indeed.com | Job search |
| Glassdoor | https://www.glassdoor.com | Jobs and salaries |
| Remote OK | https://remoteok.com | Remote jobs |
| We Work Remotely | https://weworkremotely.com | Remote jobs |
| Hacker News Who is Hiring | https://news.ycombinator.com/jobs | Monthly hiring threads |
| Y Combinator Work at a Startup | https://www.workatastartup.com | Startup jobs |
| Gun.io | https://gun.io | Freelance developers |
| Arc.dev | https://arc.dev | Remote developer jobs |

## 9. Security, Bug Bounty and Vulnerability Data

| Platform | URL | Notes |
|---|---|---|
| HackerOne | https://www.hackerone.com | Bug bounty platform |
| Bugcrowd | https://www.bugcrowd.com | Crowdsourced security |
| Intigriti | https://www.intigriti.com | European bug bounty |
| YesWeHack | https://www.yeswehack.com | Bug bounty |
| Open Bug Bounty | https://www.openbugbounty.org | Coordinated disclosure |
| CVE Program | https://www.cve.org | CVE identifiers |
| NVD | https://nvd.nist.gov | Vulnerability database |
| MITRE ATT&CK | https://attack.mitre.org | Adversary tactics |
| Exploit-DB | https://www.exploit-db.com | Exploit archive |
| OSS-Fuzz | https://github.com/google/oss-fuzz | Continuous fuzzing |
| syzkaller | https://github.com/google/syzkaller | Kernel fuzzing |
| kernel.org CVE feed | https://git.kernel.org/pub/scm/linux/security/vulns.git | Linux CVE data |
| GitHub Advisory Database | https://github.com/advisories | Dependency advisories |
| OSV | https://osv.dev | Open source vulnerabilities |
| VulnCheck | https://vulncheck.com | Vulnerability intelligence |

## 10. Open Source Foundations and Governance

| Foundation | URL | Focus |
|---|---|---|
| Linux Foundation | https://www.linuxfoundation.org | Linux and broad OSS |
| Apache Software Foundation | https://www.apache.org | Apache projects |
| Cloud Native Computing Foundation | https://www.cncf.io | Kubernetes/cloud native |
| Eclipse Foundation | https://www.eclipse.org | IDE and IoT |
| Mozilla | https://www.mozilla.org | Web and Firefox |
| Free Software Foundation | https://www.fsf.org | GNU and free software |
| GNU Project | https://www.gnu.org | GNU operating system |
| Open Source Initiative | https://opensource.org | License stewardship |
| OpenJS Foundation | https://openjsf.org | JavaScript ecosystem |
| Python Software Foundation | https://www.python.org/psf/ | Python |
| Rust Foundation | https://foundation.rust-lang.org | Rust |
| NumFOCUS | https://numfocus.org | Scientific Python |
| Software Freedom Conservancy | https://sfconservancy.org | Copyleft enforcement/support |
| GNOME Foundation | https://foundation.gnome.org | GNOME desktop |
| KDE e.V. | https://ev.kde.org | KDE desktop |
| Document Foundation | https://www.documentfoundation.org | LibreOffice |
| OpenInfra Foundation | https://openinfra.dev | OpenStack, Kata, Zuul |
| OpenSSF | https://openssf.org | Supply-chain security |
| OpenHW Group | https://www.openhwgroup.org | Open hardware |
| RISC-V International | https://riscv.org | Open ISA |

## 11. Specialized Developer Platforms

| Platform | URL | Notes |
|---|---|---|
| Hugging Face | https://huggingface.co | Models, datasets, Spaces |
| Kaggle | https://www.kaggle.com | Datasets and competitions |
| Papers with Code | https://paperswithcode.com | Research with code |
| arXiv | https://arxiv.org | Preprints |
| Zenodo | https://zenodo.org | Research data/software DOIs |
| Figshare | https://figshare.com | Research outputs |
| OSF | https://osf.io | Open Science Framework |
| Apple Developer | https://developer.apple.com | Apple platforms |
| Google Play Console | https://play.google.com/console | Android publishing |
| XDA Developers | https://www.xda-developers.com | Mobile development community |
| Unity Asset Store | https://assetstore.unity.com | Game assets |
| itch.io | https://itch.io | Indie games |
| Roblox Creator Hub | https://create.roblox.com | Roblox development |
| Twitch Developers | https://dev.twitch.tv | Streaming APIs |
| Stripe Developers | https://stripe.com/docs | Payments APIs |
| Postman | https://www.postman.com | API testing and public API network |
| RapidAPI | https://rapidapi.com | API marketplace |
| Zapier | https://zapier.com | Automation integrations |
| n8n | https://n8n.io | Workflow automation |
| Open Collective | https://opencollective.com | OSS funding |
| GitHub Sponsors | https://github.com/sponsors | OSS funding |
| Liberapay | https://liberapay.com | Recurring donations |
| Patreon | https://www.patreon.com | Creator funding |
| Ko-fi | https://ko-fi.com | Creator funding |

---

# Kernel and Operating System Index

## 12. Linux and Linux-Derived Kernels

| Kernel / Project | URL | Notes |
|---|---|---|
| Linux kernel | https://kernel.org | Mainline; Git, mailing lists, releases |
| Linux stable | https://git.kernel.org/pub/scm/linux/kernel/git/stable/linux.git | Stable branches |
| Linux next | https://git.kernel.org/pub/scm/linux/kernel/git/next/linux-next.git | Integration tree |
| LKML | https://lore.kernel.org/lkml/ | Linux Kernel Mailing List archive |
| Patchwork | https://patchwork.kernel.org | Patch tracking |
| Android Common Kernel (ACK) | https://source.android.com/docs/core/architecture/kernel | Android kernel branches |
| Generic Kernel Image (GKI) | https://source.android.com/docs/core/architecture/kernel/generic-kernel-image | Android GKI |
| Android Mainline modules | https://source.android.com/docs/core/architecture/modular-system | Mainline modules |
| Kali NetHunter kernels | https://gitlab.com/kalilinux/nethunter/build-scripts/kali-nethunter-kernels | Mobile pentest kernels |
| postmarketOS kernels | https://gitlab.com/postmarketOS | Mainline-based mobile kernels |
| LineageOS kernels | https://github.com/LineageOS | Android device kernels |
| GrapheneOS | https://grapheneos.org | Hardened Android |
| Asahi Linux | https://asahilinux.org | Apple Silicon Linux |
| Ubuntu kernel | https://kernel.ubuntu.com | Ubuntu kernels |
| Debian kernel | https://salsa.debian.org/kernel-team/linux | Debian kernel packaging |
| Fedora kernel | https://fedoraproject.org/wiki/Kernel | Fedora kernel |
| RHEL kernel | https://gitlab.com/redhat/centos-stream/src/kernel/centos-stream-9 | Enterprise kernel |
| SUSE kernel | https://www.suse.com | SUSE Linux Enterprise |
| Arch Linux kernel | https://gitlab.archlinux.org/archlinux/packaging/packages/linux | Arch packaging |
| Alpine Linux | https://git.alpinelinux.org/aports/tree/main/linux-lts | musl-based distro |
| NixOS kernel | https://github.com/NixOS/nixpkgs/tree/master/pkgs/os-specific/linux/kernel | Declarative distro |
| Clear Linux | https://www.clearlinux.org | Intel-optimized |
| CachyOS kernel | https://github.com/CachyOS/linux-cachyos | Performance patches |
| XanMod | https://xanmod.org | Desktop/gaming kernel |
| Liquorix | https://liquorix.net | Low-latency kernel |
| linux-tkg | https://github.com/Frogging-Family/linux-tkg | Custom kernels |
| Zen Kernel | https://github.com/zen-kernel/zen-kernel | Desktop responsiveness |
| Realtime (PREEMPT_RT) | https://wiki.linuxfoundation.org/realtime/start | Real-time Linux |
| grsecurity / PaX | https://grsecurity.net | Hardening patches |
| OpenWrt | https://openwrt.org | Router kernel/distro |
| Yocto Project | https://www.yoctoproject.org | Embedded Linux builds |
| Buildroot | https://buildroot.org | Embedded Linux builds |
| OpenEmbedded | https://www.openembedded.org | Embedded build framework |

## 13. BSD Family

| Kernel / OS | URL | Notes |
|---|---|---|
| FreeBSD | https://www.freebsd.org | BSD kernel and userland |
| NetBSD | https://www.netbsd.org | Portable BSD |
| OpenBSD | https://www.openbsd.org | Security-focused BSD |
| DragonFly BSD | https://www.dragonflybsd.org | Fork of FreeBSD 4.8 |
| GhostBSD | https://ghostbsd.org | FreeBSD desktop |
| MidnightBSD | https://www.midnightbsd.org | FreeBSD-derived desktop |
| NomadBSD | https://nomadbsd.org | Live USB FreeBSD |
| HardenedBSD | https://hardenedbsd.org | Hardened FreeBSD |
| CheriBSD | https://www.cheribsd.org | Capability-based BSD |
| OPNsense | https://opnsense.org | FreeBSD-based firewall |
| pfSense | https://www.pfsense.org | FreeBSD-based firewall |
| TrueNAS | https://www.truenas.com | FreeBSD/Linux storage |
| helloSystem | https://hellosystem.github.io | FreeBSD desktop |

## 14. Unix, Solaris and Proprietary Systems

| Kernel / OS | Vendor | Notes |
|---|---|---|
| illumos | https://illumos.org | OpenSolaris-derived kernel |
| OpenIndiana | https://www.openindiana.org | illumos distribution |
| SmartOS | https://www.tritondatacenter.com/smartos | illumos + zones/KVM |
| OmniOS | https://omnios.org | illumos server OS |
| Solaris | https://www.oracle.com/solaris/ | Oracle Unix |
| AIX | https://www.ibm.com/products/aix | IBM Power Unix |
| HP-UX | https://www.hpe.com/us/en/servers/hp-ux.html | HPE Unix |
| z/OS | https://www.ibm.com/products/zos | IBM mainframe |
| macOS (XNU) | https://opensource.apple.com | Darwin/XNU kernel |
| iOS / iPadOS (XNU) | https://developer.apple.com | Apple mobile |
| Windows NT | https://learn.microsoft.com/windows/win32/ | ntoskrnl executive |
| Windows Driver Kit | https://learn.microsoft.com/windows-hardware/drivers/ | Driver development |
| ReactOS | https://reactos.org | NT-compatible OSS |
| Haiku | https://www.haiku-os.org | BeOS-compatible |
| ArcaOS | https://www.arcanoae.com | OS/2 successor |
| FreeDOS | https://www.freedos.org | DOS-compatible |
| MenuetOS | https://menuetos.net | Assembly OS |
| KolibriOS | https://kolibrios.org | Assembly OS |

## 15. Microkernels and Capability Systems

| Kernel | URL | Notes |
|---|---|---|
| seL4 | https://sel4.systems | Formally verified microkernel |
| L4 family | https://l4hq.org | L4 microkernel lineage |
| Fiasco.OC | https://genode.org/documentation/articles/l4re | L4Re/Fiasco |
| Pistachio | https://l4hq.org | L4 implementation |
| Mach | https://www.gnu.org/software/hurd/microkernel/mach/gnumach.html | GNU Mach |
| GNU Hurd | https://www.gnu.org/software/hurd/ | GNU microkernel OS |
| Zircon | https://fuchsia.dev/fuchsia-src/concepts/kernel | Fuchsia kernel |
| Redox | https://www.redox-os.org | Rust microkernel OS |
| Genode | https://genode.org | Component-based OS framework |
| Coyotos | https://www.coyotos.org | Capability microkernel research |
| EROS | https://www.eros-os.org | Capability OS research |
| HelenOS | https://www.helenos.org | Portable multiserver OS |
| MINIX 3 | https://www.minix3.org | Microkernel teaching OS |
| QNX Neutrino | https://www.qnx.com | Commercial RTOS microkernel |
| Managarm | https://managarm.org | Async microkernel OS |

## 16. Real-Time Operating Systems (RTOS)

| RTOS | URL | Notes |
|---|---|---|
| FreeRTOS | https://www.freertos.org | Widely used embedded RTOS |
| Zephyr | https://zephyrproject.org | Linux Foundation RTOS |
| Azure RTOS ThreadX | https://azure.microsoft.com/products/rtos | Microsoft RTOS |
| NuttX | https://nuttx.apache.org | Apache RTOS |
| RIOT | https://www.riot-os.org | IoT RTOS |
| ChibiOS | https://www.chibios.org | Embedded RTOS |
| RT-Thread | https://www.rt-thread.io | Chinese OSS RTOS |
| Mbed OS | https://os.mbed.com | Arm IoT OS (end-of-life) |
| Apache Mynewt | https://mynewt.apache.org | IoT OS |
| Contiki-NG | https://contiki-ng.org | IoT OS |
| TinyOS | https://github.com/tinyos/tinyos-main | Sensor networks |
| VxWorks | https://www.windriver.com/products/vxworks | Commercial RTOS |
| embOS | https://www.segger.com/products/rtos/embos/ | SEGGER RTOS |
| FreeRTOS kernel (AWS) | https://github.com/FreeRTOS/FreeRTOS-Kernel | Kernel repo |
| Zephyr kernel | https://github.com/zephyrproject-rtos/zephyr | Kernel repo |
| PX4 | https://px4.io | Drone flight stack/RTOS |
| ArduPilot | https://ardupilot.org | Autopilot |
| RTEMS | https://www.rtems.org | Space/embedded RTOS |
| eCos | https://ecos.sourceware.org | Embedded configurable OS |
| Apache NuttX | https://nuttx.apache.org | POSIX RTOS |

## 17. Unikernels and Lightweight Kernels

| Project | URL | Notes |
|---|---|---|
| Unikraft | https://unikraft.org | Modular unikernel |
| MirageOS | https://mirage.io | OCaml unikernel |
| OSv | https://osv.io | Unikernel for JVM/cloud |
| IncludeOS | https://www.includeos.org | C++ unikernel |
| Nanos | https://nanos.org | Unikernel |
| Hermit | https://hermit-os.org | Rust unikernel |
| Rumprun | https://github.com/rumpkernel/rumprun | NetBSD rump kernels |
| gVisor | https://gvisor.dev | Userspace application kernel |
| Firecracker | https://firecracker-microvm.github.io | MicroVM (KVM-based) |
| Kata Containers | https://katacontainers.io | VM-isolated containers |

## 18. Research, Teaching and Experimental Kernels

| Project | URL | Notes |
|---|---|---|
| xv6 | https://github.com/mit-pdos/xv6-public | MIT teaching Unix |
| xv6-riscv | https://github.com/mit-pdos/xv6-riscv | RISC-V teaching Unix |
| Pintos | https://www.cs.utexas.edu/~ans/classes/cs439/projects/pintos/ | Teaching OS |
| Nachos | https://homes.cs.washington.edu/~tom/nachos/ | Teaching OS |
| JOS | https://pdos.csail.mit.edu/6.828/2018/jos.html | MIT teaching OS |
| OS/161 | https://os161.eecs.harvard.edu | Harvard teaching OS |
| GeekOS | https://geekos.sourceforge.net | Teaching OS |
| Plan 9 | https://9p.io/plan9/ | Distributed OS |
| 9front | https://9front.org | Plan 9 fork |
| Inferno | https://www.vitanuova.com/inferno/ | Distributed OS |
| Oberon System | https://www.projectoberon.com | Component Pascal OS |
| Solaris-derived OpenSolaris | https://opensolaris.org | Legacy |
| SerenityOS | https://serenityos.org | Hobby Unix-like OS |
| Ladybird | https://ladybird.org | Browser (SerenityOS spin-off) |
| ToaruOS | https://toaruos.org | Hobby OS |
| Redox OS | https://www.redox-os.org | Rust OS |
| ReactOS | https://reactos.org | NT-compatible |
| FreeVMS | https://github.com/FreeVMS/FreeVMS | VMS clone |
| GNU Mach | https://www.gnu.org/software/hurd/gnumach.html | Mach for Hurd |

## 19. Hypervisors and Virtualization Adjacent

| Hypervisor | URL | Notes |
|---|---|---|
| KVM | https://www.linux-kvm.org | Linux kernel virtualization |
| Xen | https://xenproject.org | Type-1 hypervisor |
| bhyve | https://bhyve.org | FreeBSD hypervisor |
| Hyper-V | https://learn.microsoft.com/virtualization/hyper-v-on-windows/ | Microsoft |
| VMware ESXi (VMkernel) | https://www.vmware.com/products/esxi-and-esx.html | Commercial |
| QEMU | https://www.qemu.org | Emulator/virtualizer |
| VirtualBox | https://www.virtualbox.org | Desktop virtualization |
| Firecracker | https://firecracker-microvm.github.io | MicroVM |
| Cloud Hypervisor | https://www.cloudhypervisor.org | Rust VMM |
| crosvm | https://crosvm.dev | ChromeOS VMM |
| ACRN | https://projectacrn.org | Embedded hypervisor |
| Jailhouse | https://github.com/siemens/jailhouse | Partitioning hypervisor |
| Xen on Arm | https://xenproject.org | Arm virtualization |

## 20. Networking, eBPF and Kernel-Adjacent Dataplanes

| Project | URL | Notes |
|---|---|---|
| eBPF | https://ebpf.io | In-kernel programmable datapath |
| XDP | https://www.iovisor.org/technology/xdp | Express Data Path |
| DPDK | https://www.dpdk.org | Userspace packet processing |
| VPP | https://wiki.fd.io/view/VPP | Vector Packet Processing |
| Cilium | https://cilium.io | eBPF networking/security |
| bpftrace | https://bpftrace.org | eBPF tracing |
| systemtap | https://sourceware.org/systemtap/ | Kernel tracing |
| perf | https://perf.wiki.kernel.org | Linux profiling |
| ftrace | https://www.kernel.org/doc/html/latest/trace/ftrace.html | Kernel tracing |
| LTTng | https://lttng.org | Tracing |
| Open vSwitch | https://www.openvswitch.org | Virtual switch |
| WireGuard | https://www.wireguard.com | Kernel VPN |
| netfilter | https://www.netfilter.org | Linux packet filtering |
| nftables | https://www.netfilter.org/projects/nftables/ | Packet filtering |
| io_uring | https://kernel.dk/io_uring.pdf | Async I/O interface |

## 21. Kernel Development Resources

| Resource | URL | Notes |
|---|---|---|
| kernel.org | https://kernel.org | Linux releases and Git |
| Gitweb/cgit | https://git.kernel.org | Kernel Git hosting |
| lore.kernel.org | https://lore.kernel.org | Mailing list archive |
| LWN.net | https://lwn.net | Kernel news |
| Kernel Newbies | https://kernelnewbies.org | Beginner resources |
| Linux Kernel Documentation | https://docs.kernel.org | Official docs |
| Linux Kernel Selftests | https://git.kernel.org/pub/scm/linux/kernel/git/torvalds/linux.git/tree/tools/testing/selftests | Tests |
| syzkaller | https://github.com/google/syzkaller | Kernel fuzzing |
| OSS-Fuzz | https://github.com/google/oss-fuzz | Fuzzing |
| KernelCI | https://kernelci.org | Kernel CI |
| 0-Day CI | https://01.org/lkp | Intel kernel testing |
| Linux Plumbers Conference | https://lpc.events | Kernel conference |
| Linux Kernel Summit | https://events.linuxfoundation.org | Kernel summit |
| FreeBSD developer docs | https://docs.freebsd.org/en/books/developers-handbook/ | FreeBSD kernel |
| NetBSD kernel docs | https://www.netbsd.org/docs/kernel/ | NetBSD kernel |
| OpenBSD hacking | https://www.openbsd.org/faq/faq5.html | OpenBSD kernel |
| OSDev Wiki | https://wiki.osdev.org | OS development wiki |
| Writing an OS in Rust | https://os.phil-opp.com | Rust OS tutorial |

## 22. Kali NetHunter Kernels

Kali NetHunter maintains a machine-readable device and kernel registry. The full list of
126 supported devices and their kernel variants is in `docs/nethunter-kernels.md`, generated
from the official source:

- Devices and kernels YAML: https://gitlab.com/kalilinux/nethunter/build-scripts/kali-nethunter-kernels/-/blob/main/devices.yml
- Kernel build scripts: https://gitlab.com/kalilinux/nethunter/build-scripts/kali-nethunter-kernels
- NetHunter installer: https://gitlab.com/kalilinux/nethunter/build-scripts/kali-nethunter-installer
- Kernel documentation: https://www.kali.org/docs/nethunter/nethunter-kernel/
- Porting guide: https://www.kali.org/docs/nethunter/porting-nethunter/
- Kernel builder: https://www.kali.org/docs/nethunter/porting-nethunter-kernel-builder/
- Patching guide: https://www.kali.org/docs/nethunter/nethunter-kernel-1-patching/
- Kernel configuration: https://www.kali.org/docs/nethunter/nethunter-kernel-2-config-1/
- Network configuration: https://www.kali.org/docs/nethunter/nethunter-kernel-3-config-2/
- Wi-Fi configuration: https://www.kali.org/docs/nethunter/nethunter-kernel-4-config-3/
- SDR configuration: https://www.kali.org/docs/nethunter/nethunter-kernel-5-config-4/
- USB (3.x): https://www.kali.org/docs/nethunter/nethunter-kernel-6-config-5/
- USB (4.x): https://www.kali.org/docs/nethunter/nethunter-kernel-7-config-6/
- CAN configuration: https://www.kali.org/docs/nethunter/nethunter-kernel-9-config-8/
- NFS configuration: https://www.kali.org/docs/nethunter/nethunter-kernel-8-config-7/
- Adding a device: https://www.kali.org/docs/nethunter/nethunter-kernel-8-adding-your-device/
- NetHunter statistics: https://nethunter.kali.org/
- Kernel list: https://nethunter.kali.org/kernels.html
- Device modules: https://nethunter.kali.org/device-kernels.html

---

## Notes and Limitations

- Public platforms change frequently. URLs were checked against official sites in October 2026.
- GitHub, GitLab, and similar platforms expose APIs for repository metadata, but this index
  does not enumerate individual developers or scrape personal profiles.
- Kernel support is hardware- and version-specific. For NetHunter, always confirm the exact
  device codename, Android version, and kernel branch in `docs/nethunter-kernels.md` before flashing.
- A kernel page existing does not guarantee a prebuilt image; some entries are source-only.
