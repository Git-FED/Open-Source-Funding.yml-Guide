from pathlib import Path
import json, textwrap

ROOT = Path('/home/ubuntu/open-source-funding-guide')

def put(rel, content):
    path = ROOT / rel
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(textwrap.dedent(content).lstrip(), encoding='utf-8')

# Core metadata and contribution files
put('README.md', '''
# The Sponsor Button

> A practical, global guide to funding open-source work without making supporters fight your payment stack.

Most funding guides list platforms. **The Sponsor Button** helps maintainers choose a small, resilient funding setup, understand what they will actually keep, and make the ask visible in the GitHub repository sidebar.

## Start here

1. **Turn on the sidebar card.** Follow [Sidebar Card Setup](GUIDES/sidebar-card-setup.md). The card requires both `.github/FUNDING.yml` and the repository Sponsorships feature.
2. **Choose one primary rail and one backup rail.** [GitHub Sponsors + Ko-fi](GUIDES/backup-platforms.md) is the default pairing for a solo maintainer because it combines GitHub discovery with card and PayPal coverage.
3. **Check the practical constraints.** Use [Country Relevance](GUIDES/country-relevance.md), [Difficulty & Age](GUIDES/platform-difficulty-and-age.md), and [Payment Rails](GUIDES/payment-rails.md) before committing.
4. **Estimate the take-home amount.** Open the [interactive fee calculator](https://fed-os.github.io/open-source-funding-guide/calculator.html) or read [Fee Comparison](COMPARISONS/fee-comparison.md).

## The central idea

> You are not only choosing a platform. You are choosing which payment methods a supporter can use.

One link can create a payment wall. Two complementary links usually create better coverage than six overlapping links. The goal is not to maximize platform count; it is to minimize donor friction.

## What is inside

| Need | Where to go |
| --- | --- |
| Show funding in the GitHub sidebar | [Sidebar Card Setup](GUIDES/sidebar-card-setup.md) |
| Pick a primary and backup | [Backup Platforms](GUIDES/backup-platforms.md) |
| Compare fees and payout rails | [Comparisons](COMPARISONS/fee-comparison.md) |
| Understand country and currency limits | [Country Relevance](GUIDES/country-relevance.md) |
| Manage money after it arrives | [Money Management](GUIDES/money-management.md) |
| Create sponsor tiers and boundaries | [Sponsor Tiers](GUIDES/sponsor-tiers.md) |
| Write your funding ask | [Sponsor Page Copy](TEMPLATES/sponsor-page-copy.md) |
| Contribute an update | [CONTRIBUTING](CONTRIBUTING.md) |

## The repository funds itself

This repo practices what it teaches. Its own funding configuration lives at `.github/FUNDING.yml`; the docs site offers the same low-friction paths in its footer.

## Accuracy note

Fees, availability, age rules, tax treatment, and platform policies change. The figures in this repository are **orientation ranges**, not promises. Every platform page includes an official source link and a last-verified field. Confirm current terms before publishing a link or making a financial decision.

## License

Code and scripts are MIT-licensed. Written content is CC BY 4.0. See [LICENSE](LICENSE) and [LICENSE-CONTENT](LICENSE-CONTENT).
''')
put('CONTRIBUTING.md', '''
# Contributing

The guide is most useful when it reflects real maintainer experience from more than one country. Contributions are welcome when they improve clarity, verify a source, or document a practical failure mode.

## Good contributions

- Correct a fee, payout rail, country limitation, or platform-history detail with an official source.
- Add a platform page using the existing structure: what it is, who it fits, rails, fees, difficulty, age guidance, risks, and backup recommendation.
- Add a case study with permission and clearly labeled figures.
- Improve keyboard access, contrast, plain-language explanations, or translation quality.

## Before opening a pull request

Read [the update guide](GUIDES/update-data.md), run the local checks in `SCRIPTS/`, and include the date you verified each change. Do not commit private sponsor information, API keys, screenshots containing personal data, or unsupported claims about tax treatment.

## Sources and uncertainty

Prefer official pricing, eligibility, payout, and policy pages. If a platform does not publish a detail, write “not publicly specified” instead of guessing. Preserve uncertainty next to the claim it qualifies.
''')
put('CODE_OF_CONDUCT.md', '''
# Code of Conduct

This project welcomes contributors of every background, geography, age, ability, and funding model. Be precise without being dismissive. Disagree with claims, not people. Do not shame maintainers for needing money, and do not pressure anyone to disclose income, identity, country, or tax information.

Harassment, discrimination, doxxing, impersonation, fraudulent funding links, and predatory solicitation are not acceptable. Report concerns privately to the maintainers listed in [MAINTAINERS.md](MAINTAINERS.md).
''')
put('SECURITY.md', '''
# Security

Do not open a public issue for credentials, payment tokens, private sponsor information, or a suspected exploit in a linked service. Email `security@fedpromptly.com` with the minimum details needed to reproduce the concern. Remove secrets from screenshots and logs before sharing them.

This repository does not process donations itself. A platform page linked from the guide may still have its own security and dispute process; use that platform's official support channel for account-specific incidents.
''')
put('SUPPORT.md', '''
# Support

For guide corrections, open an issue using the relevant template. For account, payout, identity-verification, or chargeback questions, contact the platform directly. This project cannot see or change a maintainer's payment account.
''')
put('GOVERNANCE.md', '''
# Governance

The project uses maintainer review for factual changes and community review for clarity, accessibility, and lived experience. A platform or fee correction requires an official source or two independent maintainer reports. Material policy changes are recorded in `CHANGELOG.md`.
''')
put('ROADMAP.md', '''
# Roadmap

## Now

- Keep the fee and payout tables current.
- Improve country-specific reports from contributors.
- Add permissioned case studies with real numbers.

## Next

- Add translations for Spanish, French, German, Portuguese, and Japanese.
- Publish a sponsor-facing directory of projects that opt in.
- Add a small browser-only validator for common `FUNDING.yml` mistakes.

## Later

- Build a privacy-preserving aggregate benchmark dataset.
- Add a maintainers' interview series focused on sustainability rather than star counts.
''')
put('CHANGELOG.md', '''
# Changelog

## 0.1.0 — 2026-09-24

- Initial release of The Sponsor Button guide.
- Added responsive GitHub Pages experience, fee calculator, decision tree, platform matrix, templates, and contribution workflows.
''')
put('LICENSE', '''
MIT License

Copyright (c) 2026 FED-OS

Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files, to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED.
''')
put('LICENSE-CONTENT', '''
Creative Commons Attribution 4.0 International

Unless otherwise noted, the written documentation in this repository is licensed under CC BY 4.0. You may share and adapt it with attribution. Platform trademarks and linked materials remain the property of their respective owners.
''')
put('AUTHORS.md', '''
# Authors

The Sponsor Button is maintained by FED-OS with contributions from the open-source community.
''')
put('MAINTAINERS.md', '''
# Maintainers

- FED-OS — project stewardship and release review

Maintainer names and contact routes may change. Check the repository history for current ownership.
''')
put('CITATIONS.md', '''
# Citations and source policy

The project cites official documentation whenever a claim concerns fees, payout eligibility, identity verification, payment rails, or platform policy. Sources are linked inline from each guide. Search results and review sites are discovery aids, not authoritative fee sources.
''')
put('TRANSLATIONS.md', '''
# Translations

Translations should preserve caveats, dates, source links, and the distinction between a platform fee and a processor fee. A translation may simplify wording, but it must not silently convert an estimate into a guarantee.
''')
put('.gitignore', '''
.DS_Store
.env
*.pem
*.key
node_modules/
coverage/
''')
put('.editorconfig', '''
root = true
[*]
charset = utf-8
end_of_line = lf
insert_final_newline = true
indent_style = space
indent_size = 2
''')
put('.gitattributes', '''
*.md text eol=lf
*.yml text eol=lf
*.csv text eol=lf
''')

# GitHub configuration
put('.github/FUNDING.yml', '''
github: [FED-OS]
ko_fi: fedpromptly
custom: ["https://buymeacoffee.com/fedpromptly"]
''')
put('.github/CODEOWNERS', '''
* @FED-OS
DATA/* @FED-OS
PLATFORMS/* @FED-OS
''')
put('.github/PULL_REQUEST_TEMPLATE.md', '''
## What changed?

## Why is it useful?

## Verification

- [ ] I ran the relevant scripts.
- [ ] I included official sources for changing facts.
- [ ] I did not include private sponsor or payment information.
''')
put('.github/dependabot.yml', '''
version: 2
updates:
  - package-ecosystem: github-actions
    directory: "/"
    schedule:
      interval: monthly
''')
put('.github/ISSUE_TEMPLATE/config.yml', '''
blank_issues_enabled: false
contact_links:
  - name: Platform account support
    url: https://github.com/FED-OS/open-source-funding-guide/discussions
    about: Account, payout, or identity questions belong with the platform first.
''')
put('.github/ISSUE_TEMPLATE/platform-correction.md', '''
---
name: Platform correction
about: Report a fee, payout, eligibility, or policy change
title: "[Correction] "
labels: data, needs-verification
---

**Platform:**
**Country or region:**
**What changed:**
**Official source:**
**Date verified:**
''')
put('.github/ISSUE_TEMPLATE/new-platform.md', '''
---
name: New platform
a bout: Suggest a funding platform or payment rail
title: "[Platform] "
labels: platform, needs-research
---

**Platform name:**
**What does it fund?**
**Who can receive payouts?**
**Payment rails:**
**Official pricing and eligibility links:**
'''.replace('a bout','about'))
put('.github/ISSUE_TEMPLATE/broken-link.md', '''
---
name: Broken link
about: Report a dead or redirected source
labels: links
---

**Page:**
**Broken link:**
**Suggested replacement, if known:**
''')
put('.github/workflows/pages.yml', '''
name: Deploy Pages
on:
  push:
    branches: [main]
  workflow_dispatch:
permissions:
  contents: read
  pages: write
  id-token: write
jobs:
  deploy:
    runs-on: ubuntu-latest
    environment:
      name: github-pages
      url: ${{ steps.deployment.outputs.page_url }}
    steps:
      - uses: actions/checkout@v4
      - uses: actions/configure-pages@v5
      - uses: actions/upload-pages-artifact@v3
        with:
          path: docs
      - id: deployment
        uses: actions/deploy-pages@v4
''')
put('.github/workflows/link-check.yml', '''
name: Link check
on:
  pull_request:
  schedule:
    - cron: "17 4 * * 1"
jobs:
  links:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      - uses: lycheeverse/lychee-action@v2
        with:
          args: "--verbose --no-progress '**/*.md' 'docs/**/*.html'"
          fail: true
''')
put('.github/workflows/markdown-lint.yml', '''
name: Markdown lint
on: [pull_request]
jobs:
  lint:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      - uses: DavidAnson/markdownlint-cli2-action@v19
        with:
          globs: "**/*.md"
''')

# Data
platforms = [
  ('GitHub Sponsors','0% personal / up to 6% org','Card via Stripe Connect','🟢 Beginner','13+ with guardian support','Solo maintainers on GitHub','Ko-fi or Liberapay'),
  ('Ko-fi','0% tips; 5% memberships/shop','Stripe and/or PayPal','🟢 Beginner','13+ with guardian support','Tips, memberships, small shops','GitHub Sponsors'),
  ('Buy Me a Coffee','5% + processor','Card via Stripe','🟢 Beginner','13+ with guardian support','Fastest tip page','Ko-fi or Liberapay'),
  ('Liberapay','0% platform + processor','Stripe and PayPal where available','🟡 Intermediate','Verify local contract rules','Pure recurring donations','GitHub Sponsors'),
  ('Patreon','5–12% + processor + payout','Cards, PayPal, wallet methods vary','🟡 Intermediate','18+ or guardian arrangement','Membership communities','GitHub Sponsors'),
  ('Polar','5% + fixed/processor charges','Card via Stripe','🟡 Intermediate','18+ recommended','Software, licenses, digital goods','Ko-fi'),
  ('Open Collective','Typically host + processor range','Card, PayPal, transfers vary by host','🟠 Advanced','18+ / entity context','Teams and transparent budgets','GitHub Sponsors'),
  ('thanks.dev','Model-specific; verify current terms','B2B distribution; payout rail varies','🟡 Intermediate','18+ recommended','Corporate dependency funding','GitHub Sponsors'),
  ('IssueHunt','20% bounty fee stated in brief','Fiat/crypto partners vary','🟠 Advanced','18+ recommended','Issue bounties','GitHub Sponsors'),
  ('Tidelift','Negotiated revenue share','Enterprise subscription distribution','🟠 Advanced','18+ / enterprise context','Enterprise-backed packages','GitHub Sponsors'),
  ('Community Bridge / LFX','Program and host terms vary','Cards, invoices, grants vary','🟠 Advanced','Project eligibility required','Linux Foundation ecosystem','Ko-fi or GitHub Sponsors'),
  ('BTCPay Server','0% platform; infrastructure cost','Bitcoin / Lightning','🔴 Expert','18+ technical responsibility','Crypto-native projects','GitHub Sponsors or Ko-fi'),
]
put('DATA/platforms.json', json.dumps([{'name':n,'fee':f,'rails':r,'difficulty':d,'age':a,'best_for':b,'backup':bk} for n,f,r,d,a,b,bk in platforms], indent=2))
put('DATA/fees.csv', '''platform,platform_fee,processor_fee,typical_total,notes,last_verified
GitHub Sponsors,0% personal / up to 6% org,Stripe varies,0% personal / higher for orgs,Verify account type,2026-09-24
Ko-fi,0% tips / 5% other,Stripe or PayPal,processor only on tips,Memberships and shop differ,2026-09-24
Buy Me a Coffee,5%,Stripe,about 8% plus fixed,Card-only payout flow,2026-09-24
Liberapay,0%,Stripe or PayPal,processor only,Availability varies by country,2026-09-24
Patreon,5-12%,processor and payout,about 9-15%+,Plan and currency matter,2026-09-24
Polar,5% plus fixed,Stripe,about 8% plus fixed,Sales tax treatment varies,2026-09-24
Open Collective,host-dependent,processor,about 8-13% typical range,Host controls economics,2026-09-24
IssueHunt,20% bounty fee,partner-dependent,about 20% plus rail cost,Bounty model not tips,2026-09-24
''')
put('DATA/payout-methods.csv', '''platform,card,paypal,apple_google_pay,bank_transfer,crypto,invoice,coverage_note
GitHub Sponsors,yes,no,varies,yes,no,org-dependent,GitHub discovery with Stripe-backed payouts
Ko-fi,yes,yes,varies,no,no,no,connect your own rails
Buy Me a Coffee,yes,no,varies,no,no,no,Stripe availability matters
Liberapay,yes,yes,varies,no,no,no,regional support differs
Patreon,yes,yes,varies,via payout partners,no,no,creator payout options vary
Open Collective,yes,yes,varies,yes,host-dependent,yes,fiscal host is the key variable
Polar,yes,no,varies,no,no,no,developer commerce rail
IssueHunt,partner-dependent,no,no,no,partner-dependent,no,bounty-specific
BTCPay Server,no,no,no,no,yes,no,self-hosted crypto only
''')
put('DATA/last-verified.json', json.dumps({'date':'2026-09-24','scope':'orientation only','next_review':'Review official pricing and payout pages before release'}, indent=2))
put('DATA/benchmarks.md', '''
# Benchmarks

Public star counts are not income forecasts. A small project with a clear ask can outperform a larger project whose maintainers never explain what funding supports. Until this repository has a permissioned dataset, use these as planning bands rather than promises:

| Stage | Useful question | Planning signal |
| --- | --- | --- |
| 0–100 stars | Can a stranger understand the ask in 10 seconds? | Optimize visibility and trust. |
| 100–1,000 stars | Is there one repeatable maintenance need to fund? | Test one primary and one backup rail. |
| 1,000–10,000 stars | Can sponsors see progress and boundaries? | Add tiers, updates, and a reserve. |
| 10,000+ stars | Is support becoming a community operation? | Document governance, fiscal hosting, and sponsor requests. |

Contributors should submit real numbers only with permission, a defined time window, and enough context to prevent misleading comparisons.
''')
put('DATA/schema.md', '''
# Data schema

`platforms.json` stores human-readable comparison fields. `fees.csv` records an orientation range rather than a single universal price. `payout-methods.csv` records rails that are commonly available, not a guarantee for every country or account type. Every changing row needs a verification date and an official source in the corresponding platform page.
''')

# Templates
put('FUNDING-TEMPLATES/solo-maintainer.yml', 'github: [your-username]\nko_fi: your-username\n')
put('FUNDING-TEMPLATES/team-project.yml', 'github: [your-username]\nopen_collective: your-collective\ncustom: ["https://your-project.example/sponsor"]\n')
put('FUNDING-TEMPLATES/enterprise-backend.yml', 'github: [your-username]\ntidelift: your-package\nthanks_dev: your-username\ncustom: ["https://your-project.example/enterprise"]\n')
put('FUNDING-TEMPLATES/nonprofit-fiscal-host.yml', 'open_collective: your-collective\ncommunity_bridge: your-project\ncustom: ["https://your-nonprofit.example/support"]\n')
put('FUNDING-TEMPLATES/bounty-focused.yml', 'github: [your-username]\nissuehunt: your-username\n')
put('FUNDING-TEMPLATES/minimal.yml', 'github: [your-username]\n')
put('FUNDING-TEMPLATES/README-snippets/sponsor-badge.md', '[![Sponsor](https://img.shields.io/badge/Sponsor-support%20the%20maintainer-ff6b5b?style=for-the-badge)](https://github.com/sponsors/your-username)\n')
put('FUNDING-TEMPLATES/README-snippets/sponsor-section.md', '''
## Support the project

If this project saves you time, consider supporting maintenance. The fastest path is [GitHub Sponsors](https://github.com/sponsors/your-username); [Ko-fi](https://ko-fi.com/your-username) is the lower-friction backup for supporters who prefer PayPal or a direct tip.
''')
put('FUNDING-TEMPLATES/README-snippets/funding-footer.md', '> Sustainable maintenance is part of the project. Funding supports releases, documentation, and responsive issue triage.\n')

# Platform pages
platform_intro = {
'github-sponsors.md': ('GitHub Sponsors','Native funding inside GitHub. Best first stop for an individual maintainer whose audience already lives in GitHub.','GitHub Sponsors is a funding platform, not the card network. Payout onboarding and card processing are handled through connected payment infrastructure.','Card via Stripe Connect; invoice options may exist for organizations.','Personal accounts are often presented as 0% platform fee; organization economics can differ. Verify current terms.','Ko-fi or Liberapay — adds a lower-friction PayPal path.'),
'ko-fi.md': ('Ko-fi','A lightweight tip, membership, shop, and commission page that can connect directly to Stripe and/or PayPal.','Ko-fi generally acts as the storefront while your connected payment accounts handle the money movement.','Stripe and PayPal, depending on what you connect and what your country supports.','One-time tips and memberships/shop actions can have different platform treatment.','GitHub Sponsors — adds GitHub-native discovery.'),
'buy-me-a-coffee.md': ('Buy Me a Coffee','A fast, mobile-friendly tip page for maintainers and creators.','It is a funding storefront; the exact payout and processing experience depends on its current payment integration.','Card-oriented flow; verify payout country and processor terms.','The brief uses a typical 5% platform fee plus processor costs as an orientation point.','Ko-fi or Liberapay for PayPal coverage.'),
'liberapay.md': ('Liberapay','A non-profit, donation-only platform focused on recurring support without perks.','Liberapay is a funding platform. Stripe or PayPal availability determines whether a creator can receive funds.','Stripe and PayPal where supported.','0% platform fee is the stated model; processor and regional limits still matter.','GitHub Sponsors for discovery.'),
'patreon.md': ('Patreon','A creator membership platform with tiers, posts, messaging, and recurring support.','Patreon combines the public membership experience with payment and payout partners.','Cards, PayPal, and wallet methods vary by country and checkout context.','Plan, currency, processing, and payout terms create a variable all-in fee.','GitHub Sponsors for the developer audience.'),
'polar.md': ('Polar','A developer-focused commerce platform for software, licenses, digital goods, and community access.','Polar is closer to developer commerce than a simple donation jar.','Card via Stripe; verify country support and tax handling.','The brief uses a typical 5% plus fixed/processor orientation.','Ko-fi for PayPal-native donors.'),
'open-collective.md': ('Open Collective','A transparent budgeting and fiscal-hosting model for teams and communities.','The platform and the fiscal host are distinct. The host may receive funds, handle compliance, and pay approved expenses.','Cards, PayPal, transfers, and other rails depend on the selected host.','Host and processor charges can make the all-in range materially higher than a tip jar.','GitHub Sponsors for a direct individual path.'),
'thanks-dev.md': ('thanks.dev','A B2B dependency-funding model that distributes company support across open-source dependency trees.','This is not mainly a public tip jar. It is a corporate allocation mechanism.','Payout rails and eligibility are model-specific; verify current maintainer onboarding.','Do not compare it directly with a one-time tip fee without understanding the distribution model.','GitHub Sponsors for direct individual support.'),
'issuehunt.md': ('IssueHunt','A bounty platform where money is attached to a specific issue or task.','IssueHunt is a funding platform for outcomes, not general recurring support.','Fiat and crypto partner rails can vary.','The brief uses a 20% bounty fee as an orientation point.','GitHub Sponsors for general donations.'),
'tidelift.md': ('Tidelift','An enterprise subscription and maintenance model for packages used by organizations.','Tidelift is a commercial distribution layer, not a consumer donation page.','Enterprise contracting and maintainer payout terms apply.','Revenue share is negotiated or model-specific.','GitHub Sponsors for independent support.'),
'community-bridge-lfx.md': ('Community Bridge / LFX','A Linux Foundation ecosystem route for project crowdfunding, grants, and structured support.','Eligibility and program fit matter as much as the payment rail.','Cards, invoices, grants, and host-specific mechanisms vary.','Verify program terms and project eligibility before presenting 0% as universal.','Ko-fi or GitHub Sponsors for individual supporters.'),
'btcpay-server.md': ('BTCPay Server','A self-hosted, non-custodial crypto payment processor.','This is infrastructure you operate, not a managed funding marketplace.','Bitcoin and Lightning; no fiat donor rail by default.','No platform fee, but VPS, maintenance, conversion, security, and tax costs remain.','GitHub Sponsors or Ko-fi for fiat supporters.'),
}
for fn,(title,what,model,rails,fees,backup) in platform_intro.items():
    put('PLATFORMS/'+fn, f'''\n# {title}\n\n> {what}\n\n## What it is\n\n{model}\n\n## Payment rails\n\n{rails}\n\n## Fee lens\n\n{fees} Fees are not static. Confirm the official pricing page before publishing a recommendation.\n\n## Strengths\n\n- Clear audience fit when the project matches the platform model.\n- A recognizable support path can reduce donor hesitation.\n- Can work well as one half of a two-rail setup.\n\n## Trade-offs\n\n- Availability, identity checks, payout timing, and chargeback policy vary by country.\n- A platform fee is only one line in the total cost; processor, FX, payout, and tax costs may sit elsewhere.\n- Do not promise a tax deduction, legal status, or payout eligibility without checking the current official rules.\n\n## Practical profile\n\n- **Difficulty:** See [Difficulty & Age](../GUIDES/platform-difficulty-and-age.md).\n- **Country check:** Start with [Country Relevance](../GUIDES/country-relevance.md).\n- **Recommended backup:** **{backup}**\n\n## Sidebar checklist\n\n- [ ] Add the correct key to `.github/FUNDING.yml`.\n- [ ] Keep the file on the repository default branch.\n- [ ] Enable **Settings → Features → Sponsorships**.\n- [ ] Test the Sponsor button in an incognito window.\n\n## Official sources\n\n- Visit the platform's current pricing, payout, and eligibility documentation before relying on this page.\n''')

# Guides
put('GUIDES/sidebar-card-setup.md', '''
# Sidebar Card Setup

The repository sidebar is the most visible funding surface on GitHub. It uses two layers:

1. `.github/FUNDING.yml` tells GitHub which links to expose.
2. **Settings → Features → Sponsorships** turns the repository-level card on.

A file alone may not be enough when a repository was created through the CLI or an API.

## Checklist

- [ ] Put `.github/FUNDING.yml` on the default branch.
- [ ] Use supported keys and valid usernames.
- [ ] Open repository **Settings → General → Features**.
- [ ] Enable **Sponsorships** or choose **Set up sponsor button**.
- [ ] Visit the repository while signed out or in an incognito window.
- [ ] Click the Sponsor button and test every link.

GitHub Sponsors can appear as the native path. External services are typically listed behind the same Sponsor entry point. That makes a two-rail strategy useful: visitors do not need to navigate a wall of buttons in your README.

## Common failures

The file is on the wrong branch, the username is misspelled, a repository-level file overrides the intended account configuration, or the Sponsorships feature is still disabled. Fix one variable at a time and test from a clean browser session.
''')
put('GUIDES/backup-platforms.md', '''
# Backup Platforms: Cover the Missing Rail

A backup is not a second brand for its own sake. It is a way to cover a payment method your primary path does not offer.

## Default pairing

**GitHub Sponsors + Ko-fi** is a practical default for a solo maintainer. GitHub provides discovery where the code already lives. Ko-fi can connect Stripe and PayPal, giving a supporter another route without requiring a second elaborate membership system.

## Pairing matrix

| Primary | Backup | Reason |
| --- | --- | --- |
| GitHub Sponsors | Ko-fi | GitHub-native discovery plus card and PayPal coverage. |
| GitHub Sponsors | Liberapay | Direct donation model with a low platform-fee profile. |
| Buy Me a Coffee | Ko-fi | Adds a PayPal path to a card-oriented tip page. |
| Patreon | GitHub Sponsors | Membership features plus developer-native discovery. |
| Polar | Ko-fi | Software commerce plus a lower-friction tip path. |
| BTCPay Server | GitHub Sponsors or Ko-fi | Crypto supporters plus a fiat route. |

Keep the visible choice set small. Two complementary paths are easier to understand than a dozen links that all solve the same problem.
''')
put('GUIDES/payment-rails.md', '''
# Payment Rails

A **funding platform** is the public page where a supporter chooses to help. A **payment processor** moves the money. A **payout rail** moves the balance to the maintainer. These layers can be owned by different companies.

| Rail | What it feels like to a supporter | Common constraint |
| --- | --- | --- |
| Card | Familiar checkout | International card and FX fees. |
| PayPal | Existing balance or saved account | Country, currency, and account restrictions. |
| Apple Pay / Google Pay | One-tap mobile checkout | Availability depends on checkout integration. |
| Bank transfer / invoice | Useful for companies | Too much friction for casual donors. |
| Crypto | Direct wallet payment | Volatility, custody, conversion, and tax complexity. |

The practical rule is simple: choose the public platform for the audience, then inspect the underlying processor and payout route for your country.
''')
put('GUIDES/country-relevance.md', '''
# Country Relevance and International Fees

Availability has two separate questions: **Can a supporter pay?** and **Can the maintainer receive a payout?** The first is usually broader than the second.

Before choosing a platform, check creator onboarding for your legal residence, payout currency, identity requirements, supported bank rails, and whether a local tax form is requested.

## Hidden international costs

Cross-border cards, currency conversion, payout transfers, VAT/GST handling, and intermediary-bank charges can materially change the amount that reaches you. A domestic-looking percentage is not a universal all-in fee.

## Verification worksheet

| Question | Record |
| --- | --- |
| Country of residence |  |
| Payout currency |  |
| Supported bank or wallet |  |
| FX conversion point |  |
| Payout minimum and timing |  |
| Required identity or tax form |  |
| Official page and date checked |  |

This page is intentionally cautious. Country lists change, and a platform may add or remove payout support without changing its public marketing page.
''')
put('GUIDES/platform-difficulty-and-age.md', '''
# Difficulty and Age Guide

Difficulty measures setup and operational burden, not personal ability. Age guidance is a planning signal, not legal advice. Platform contracts, payment processors, and local law may require a parent, guardian, or legal entity for minors.

| Level | Meaning |
| --- | --- |
| 🟢 Beginner | Public page, ordinary account setup, no server administration. |
| 🟡 Intermediate | Payment onboarding, tiers, or regional details require attention. |
| 🟠 Advanced | Fiscal host, enterprise contract, bounty, or compliance concepts matter. |
| 🔴 Expert | You operate servers, wallets, keys, and security controls. |

A young maintainer should start with a supervised, low-complexity route such as GitHub Sponsors or Ko-fi rather than self-hosted crypto infrastructure. An adult maintainer still needs to understand identity checks, taxes, chargebacks, and account security.
''')
put('GUIDES/money-management.md', '''
# Money Management for Maintainers

Funding becomes sustainable when it is treated as a small operating system rather than a surprise balance.

## A simple allocation model

Create separate buckets for **tax reserve**, **operating costs**, **maintenance runway**, and **owner compensation**. The percentages are personal decisions; the separation is the important part. Keep records of gross receipts, fees, refunds, currency conversions, and transfers.

## Monthly review

Reconcile each platform to your bank or wallet. Note recurring sponsors, cancellations, unusually large gifts, and any sponsor request that could create a conflict of interest. Keep a short changelog so sponsors can see what their support enabled.

## Runway

A reserve makes maintenance less dependent on a single sponsor or a single platform. Do not spend recurring support as if it were guaranteed salary until you have observed its stability over time.

This is general information, not tax, accounting, or investment advice. Use a qualified local professional for your situation.
''')
put('GUIDES/risk-and-sponsor-relations.md', '''
# Risk and Sponsor Relations

Sponsorship should support the project without buying hidden control over the roadmap. Publish a short boundary statement: funding supports maintenance, but it does not guarantee acceptance of a feature, priority treatment, or a security exception.

Protect sponsor privacy. Do not publish names, amounts, email addresses, or employer details without permission. Treat large gifts as a reason to document expectations, not as a reason to skip review.

Keep a backup admin account, export available records, and know how to move links if a platform changes policy or stops operating.
''')
put('GUIDES/self-hosting-payments.md', '''
# Self-Hosting Payments

BTCPay Server and similar tools can remove a platform fee, but they replace a managed service with infrastructure you operate. You become responsible for uptime, backups, wallet security, fraud, conversion, tax records, and incident response.

Self-hosting is appropriate when you already run servers, understand key management, and intentionally want a crypto-only or non-custodial route. It is not a beginner-friendly shortcut to “free” payments.

Use a fiat backup when the project wants broad donor coverage. A crypto-only page excludes supporters who do not hold crypto, even when the technical stack is excellent.
''')
put('GUIDES/sponsor-tiers.md', '''
# Sponsor Tiers

Three or four tiers are usually easier to understand than a menu of ten. Make the lowest tier a genuine thank-you, a middle tier about visible maintenance, and a higher tier about organizational support or a documented service boundary.

Avoid promising private security treatment, guaranteed feature delivery, or benefits you cannot maintain. A good tier description answers: what does the money support, what does the sponsor receive, and what does the sponsor not receive?
''')
put('GUIDES/for-sponsors.md', '''
# For Sponsors

A good sponsor funds a project because it is valuable, exposed, or part of a dependency chain—not because money should secretly purchase control. Companies should document which projects they rely on, budget support as maintenance infrastructure, and make expectations explicit.

Before sponsoring, check the maintainer's public boundaries, supported payment method, legal receipt or invoice options, and whether the project welcomes corporate requests. A recurring contribution can be more useful than a one-time gift when it is sustainable for the sponsor and the maintainer.
''')
put('GUIDES/common-mistakes.md', '''
# Common Mistakes

The most common failures are operational: a missing sidebar toggle, a dead username, too many overlapping links, no backup rail, and a funding page that never explains what support changes. Review your links monthly and test them as a stranger.

Do not publish “0% fees” without checking processors, payout transfers, FX, and taxes. Do not describe a bounty platform as a general donation platform. Do not promise tax deductibility unless a qualified professional and the relevant organization status support that statement.
''')
put('GUIDES/asking-for-money.md', '''
# Asking for Money Without Apology

A clear funding ask is not a demand. It is a transparent invitation to help sustain work that already creates value. State what you maintain, what support pays for, and what a sponsor should expect.

Use concrete language: “Funding supports release testing and issue triage.” Avoid guilt, urgency theater, and promises you cannot keep. A calm ask makes it easier for both supporters and maintainers to make an informed choice.
''')
put('GUIDES/multi-platform.md', '''
# Multi-Platform Strategy

Use multiple platforms when each one reaches a different audience or payment rail. Do not add a platform simply because its fee table looks attractive. Every account adds identity checks, link maintenance, reconciliation, and possible data exposure.

For most individuals, two links are enough: one for discovery and one for complementary payment coverage. Teams may need a fiscal host or enterprise route in addition to a personal sponsor path.
''')
put('GUIDES/platform-shutdown.md', '''
# Platform Shutdown and Migration

Keep a canonical support page on a domain you control. Store your public copy and links in version control. Export sponsor records where the platform permits it, but do not copy private data into a public repository.

If a service closes, replace the link in `.github/FUNDING.yml`, update the platform comparison, publish a short migration note, and tell sponsors how to verify the new destination.
''')
put('GUIDES/sponsor-requests.md', '''
# Sponsor Requests and Boundaries

Sponsors may ask for roadmap influence, support response times, or private channels. Decide in advance which requests are compatible with the project and which belong in a paid support agreement.

Write the answer down. A public boundary protects maintainers from ad hoc promises and gives sponsors a clear route when they need a different commercial relationship.
''')
put('GUIDES/tax-forms-by-platform.md', '''
# Tax Forms by Platform

Payment platforms may issue different forms or statements depending on the payer, country, threshold, and account type. Do not assume that a platform's “donation” label determines tax treatment.

Keep gross receipts, fees, refunds, FX, and payouts separately. For United States and cross-border questions, ask a qualified tax professional whether forms such as 1099-K, W-8BEN, or W-9 apply to your situation.
''')
put('GUIDES/glossary.md', '''
# Glossary

**Fiscal host:** An organization that receives and administers funds for a project that may not have its own legal entity.

**Platform fee:** The amount retained by the public funding service.

**Processing fee:** The cost of moving a card, wallet, or bank payment.

**Payout fee:** The cost of moving a platform balance to a bank or wallet.

**Chargeback:** A payment reversal initiated through a card or wallet provider.

**KYC / AML:** Identity and anti-money-laundering checks required by financial services.

**Recurring sponsorship:** A repeated payment authorized by a supporter.
''')
put('GUIDES/update-data.md', '''
# Updating Data

When a platform changes a fee or eligibility rule, update the relevant CSV row, the platform page, and `DATA/last-verified.json`. Include the official source and the date you checked it. Use ranges when the price depends on country, plan, or account type.
''')

# Comparisons, templates, resources, community
put('COMPARISONS/fee-comparison.md', '''
# Fee Comparison

This table ranks the platforms by orientation rather than a universal promise. Fixed fees, country, account type, payment method, and payout timing can change the result.

| Platform | Typical orientation | Important qualifier |
| --- | --- | --- |
| Community Bridge / LFX | Program-dependent | Eligibility and host terms matter. |
| GitHub Sponsors | 0% personal often cited | Organization and processor economics differ. |
| Liberapay | 0% platform | Processor and country limits remain. |
| thanks.dev | Model-specific | B2B distribution is not a tip jar. |
| Ko-fi | 0% tips / 5% other actions | Connected processor still charges. |
| Buy Me a Coffee | 5% + processor | Card-oriented flow. |
| Polar | 5% + fixed/processor | Commerce and tax treatment matter. |
| Open Collective | Host-dependent range | Fiscal host determines much of the cost. |
| Patreon | 5–12% + processing | Plan and payout terms vary. |
| IssueHunt | 20% bounty orientation | Bounty model, not recurring donations. |
| Tidelift | Negotiated revenue share | Enterprise contract model. |

Use the browser calculator for an amount-specific estimate, then verify current official pricing.
''')
put('COMPARISONS/feature-comparison.md', '''
# Feature Comparison

| Platform | Card | PayPal | Bank / invoice | Crypto | Native GitHub sidebar button | Recommended backup |
| --- | --- | --- | --- | --- | --- | --- |
| GitHub Sponsors | Yes | No | Organization-dependent | No | Yes | Ko-fi or Liberapay |
| Ko-fi | Yes | Yes | No | No | Dropdown | GitHub Sponsors |
| Patreon | Yes | Yes | Varies | No | Dropdown | GitHub Sponsors |
| Open Collective | Yes | Yes | Yes, host-dependent | Host-dependent | Dropdown | GitHub Sponsors |
| Polar | Yes | No | No | No | Dropdown | Ko-fi |
| BTCPay Server | No | No | No | Yes | Custom URL | GitHub Sponsors |

Entries are a starting point. Verify the current checkout and payout documentation for your account and country.
''')
put('COMPARISONS/payout-comparison.md', '''
# Payout Comparison

Payouts can be direct to a connected processor, routed through a fiscal host, or distributed by a corporate program. “The supporter paid” does not mean “the maintainer can withdraw today.” Check minimums, timing, currency, identity review, and account holds.
''')
put('COMPARISONS/us-vs-non-us.md', '''
# US vs Non-US Considerations

US-based examples are not universal defaults. Non-US maintainers may encounter Stripe gaps, PayPal currency limits, intermediary-bank charges, FX spreads, VAT/GST collection, and different tax forms. Always record the country and currency when comparing two platforms.
''')
put('TEMPLATES/sponsor-page-copy.md', '''
# Sponsor Page Copy

## Short ask

I maintain **[project]**, which helps **[audience]** do **[valuable thing]**. Support funds **[maintenance, releases, documentation, or support]**. Choose the route that is easiest for you: **[primary]** or **[backup]**.

## Tier description

**[Tier name] — [amount]**

Your support helps with **[specific maintenance outcome]**. You receive **[honest benefit]**. This does not guarantee feature delivery, private security treatment, or control over the roadmap.
''')
put('TEMPLATES/readme-sponsor-section.md', '''
## Support maintenance

If this project saves you time, you can support continued maintenance through [GitHub Sponsors](https://github.com/sponsors/your-username) or [Ko-fi](https://ko-fi.com/your-username). The first path keeps support close to GitHub; the second is a lower-friction backup for supporters who prefer PayPal or a direct tip.
''')
put('TEMPLATES/sponsor-email.md', '''
Subject: Supporting [project] maintenance

Hello [name],

Your team uses [project] for [specific use]. I maintain it through [release, triage, documentation, or security work]. If this dependency is valuable to your organization, would you consider a recurring sponsorship or a paid support conversation?

The public funding route is [link]. I can also provide a short maintenance summary and clear boundaries for what sponsorship does and does not include.

Thank you,
[name]
''')
put('TEMPLATES/sponsor-dm.md', '''
Hi [name] — thanks for using [project]. I’m working on [maintenance outcome]. If the project is useful to your team, support at [link] helps keep releases and issue triage sustainable. No pressure; I wanted the option to be visible.
''')
put('TEMPLATES/follow-up.md', '''
Subject: Re: [project] maintenance support

Following up once in case this is useful for your maintenance budget. The project is currently prioritizing [outcome]. A sponsorship supports that work, while feature requests and response-time commitments remain separate unless we agree to a paid support arrangement.
''')
put('TEMPLATES/cancellation-response.md', '''
Thank you for supporting [project]. I understand priorities change. Your past support helped with [outcome]. If you are comfortable sharing one sentence about what changed, it will help me improve the project; there is no obligation.
''')
put('TEMPLATES/monthly-update.md', '''
# Sponsor update — [month]

This month we shipped **[release or outcome]**, improved **[maintenance area]**, and learned **[lesson]**. Next month we plan to **[next step]**. Thank you for making this work possible.
''')
put('RESOURCES/media.md', '''
# Media and Further Reading

Add talks, interviews, and essays only when the link is stable and the item is relevant to maintainer sustainability, funding models, or community governance. Prefer primary interviews and official documentation over listicles.
''')
put('COMMUNITY.md', '''
# Community

Use GitHub Discussions for platform corrections, country experiences, and questions about the guide. Do not ask people to post private payout details. A good community contribution explains the situation, the country or account type when relevant, and the source or limitation.
''')
put('EXAMPLES/small-project/FUNDING.yml', 'github: [your-username]\nko_fi: your-username\n')
put('EXAMPLES/small-project/README-snippet.md', '[Support maintenance](https://github.com/sponsors/your-username)\n')
put('EXAMPLES/medium-project/FUNDING.yml', 'github: [your-username]\nko_fi: your-username\nopen_collective: your-collective\n')
put('EXAMPLES/medium-project/README-snippet.md', '[Support the project](https://github.com/sponsors/your-username) · [View the budget](https://opencollective.com/your-collective)\n')
put('EXAMPLES/large-project/FUNDING.yml', 'github: [your-username]\nopen_collective: your-collective\ntidelift: your-package\ncustom: ["https://your-project.example/enterprise"]\n')
put('EXAMPLES/large-project/README-snippet.md', '[Sponsor maintenance](https://github.com/sponsors/your-username) · [Enterprise support](https://your-project.example/enterprise)\n')

# Website
put('docs/index.html', '''
<!doctype html>
<html lang="en">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <meta name="description" content="A practical, global guide to funding open-source work with less donor friction.">
  <meta property="og:title" content="The Sponsor Button — Fund open source without the friction">
  <meta property="og:description" content="Compare fees, payment rails, country fit, and GitHub sidebar setup.">
  <meta property="og:image" content="assets/social-preview.png">
  <link rel="icon" href="assets/favicon.svg" type="image/svg+xml">
  <link rel="stylesheet" href="style.css">
  <title>The Sponsor Button</title>
</head>
<body>
  <div class="noise"></div>
  <header class="site-header wrap">
    <a class="brand" href="#top"><span class="brand-mark">$</span><span>The Sponsor Button</span></a>
    <nav><a href="#why">Why it matters</a><a href="#choose">Choose a setup</a><a href="#calculator">Calculator</a><a class="nav-cta" href="https://github.com/FED-OS/open-source-funding-guide">View repo ↗</a></nav>
  </header>
  <main id="top">
    <section class="hero wrap">
      <div class="hero-copy">
        <p class="eyebrow"><span class="pulse"></span> Open-source funding, made practical</p>
        <h1>Make it easy<br><em>to support the work.</em></h1>
        <p class="lede">A living guide for maintainers who want a visible GitHub funding path, honest fee math, and a backup rail that respects how supporters actually pay.</p>
        <div class="hero-actions"><a class="button primary" href="guide/sidebar-card-setup.html">Fix your sidebar card <span>→</span></a><a class="text-link" href="#calculator">Run the fee math <span>↓</span></a></div>
        <div class="hero-stats"><div><strong>2</strong><span>rails are often enough</span></div><div><strong>1</strong><span>sidebar entry point</span></div><div><strong>0</strong><span>secrets in this guide</span></div></div>
      </div>
      <div class="hero-art"><img src="assets/hero-network.png" alt="Abstract network connecting a sponsor button to payment rails and open-source nodes"><div class="floating-card card-one"><span class="dot coral"></span> Payment coverage <b>+ PayPal</b></div><div class="floating-card card-two"><span class="dot cyan"></span> Sidebar card <b>Visible</b></div></div>
    </section>
    <section id="why" class="section wrap">
      <div class="section-head"><p class="eyebrow">01 / The insight</p><h2>A payment wall is a<br><em>silent no.</em></h2><p>Supporters do not care how elegant your platform stack is. They care whether the payment method they already trust is one click away.</p></div>
      <div class="insight-grid"><article class="insight dark"><span class="number">01</span><h3>Choose for coverage</h3><p>One platform can be a great primary path and still exclude a whole payment audience. Pair complementary rails instead of collecting redundant links.</p><a href="guide/backup-platforms.html">See the pairings →</a></article><article class="insight coral-card"><span class="number">02</span><h3>Make the ask visible</h3><p>The GitHub sidebar card turns funding from a footer footnote into a part of the repository experience.</p><a href="guide/sidebar-card-setup.html">Set up the card →</a></article><article class="insight outline"><span class="number">03</span><h3>Know the take-home</h3><p>Platform fees are only one line. Processor fees, FX, payout timing, and country eligibility shape the real result.</p><a href="#calculator">Calculate it →</a></article></div>
    </section>
    <section id="choose" class="band"><div class="wrap split"><div><p class="eyebrow light">02 / Start here</p><h2>Pick a setup<br><em>you can maintain.</em></h2></div><div><p class="band-copy">Most solo maintainers should start with a GitHub-native path and one lower-friction backup. Teams and enterprise projects need a different shape.</p><a class="button light-button" href="guide/decision-tree.html">Open the decision tree <span>→</span></a></div></div></section>
    <section id="calculator" class="section wrap calculator-section"><div class="section-head"><p class="eyebrow">03 / Fee lens</p><h2>What would you<br><em>actually keep?</em></h2><p>Use orientation ranges to compare the shape of a $ contribution. Always verify current terms before publishing a link.</p></div><div class="calculator"><div class="calc-controls"><label for="amount">Contribution amount</label><div class="amount-input"><span>$</span><input id="amount" type="number" min="1" value="100" step="5"></div><p>Estimates exclude taxes and country-specific FX where not modeled.</p></div><div id="results" class="results"></div></div></section>
    <section class="section wrap rail-section"><div class="rail-copy"><p class="eyebrow">04 / Payment rails</p><h2>Platform is the storefront.<br><em>Rail is the route.</em></h2><p>Card, PayPal, bank transfer, and crypto solve different friction problems. The guide keeps those layers distinct so “0% platform fee” never becomes a misleading promise.</p><a class="text-link" href="guide/payment-rails.html">Understand the rails →</a></div><div class="rail-map"><div class="rail-node main-node">support<br><strong>arrives</strong></div><div class="rail-line line-a"></div><div class="rail-line line-b"></div><div class="rail-line line-c"></div><div class="rail-pill pill-a">card</div><div class="rail-pill pill-b">PayPal</div><div class="rail-pill pill-c">invoice</div></div></section>
    <section class="closing wrap"><div><p class="eyebrow">05 / Ship the first useful version</p><h2>Your repo should<br><em>practice the ask.</em></h2></div><div><p>Put the funding file in place, enable the sidebar card, then keep the guide honest as policies change. A visible, resilient path beats a perfect spreadsheet nobody can use.</p><a class="button primary" href="https://github.com/FED-OS/open-source-funding-guide">Explore every file <span>↗</span></a></div></section>
  </main>
  <footer class="footer wrap"><div class="brand"><span class="brand-mark">$</span><span>The Sponsor Button</span></div><p>Built for maintainers, by people who believe sustainability is part of the project.</p><div class="footer-links"><a href="https://github.com/FED-OS">GitHub</a><a href="https://ko-fi.com/fedpromptly">Ko-fi</a><a href="mailto:support@fedpromptly.com">Contact</a></div></footer>
  <script src="script.js"></script>
</body>
</html>
''')
put('docs/style.css', '''
@import url('https://fonts.googleapis.com/css2?family=DM+Mono:wght@400;500&family=Space+Grotesk:wght@400;500;600;700&display=swap');
:root{--navy:#101827;--ink:#162033;--cream:#f6f1e8;--paper:#fffdf8;--coral:#ff725c;--cyan:#76e1d0;--muted:#7d8798;--line:rgba(22,32,51,.15);--shadow:0 24px 60px rgba(16,24,39,.12)}*{box-sizing:border-box}html{scroll-behavior:smooth}body{margin:0;background:var(--paper);color:var(--ink);font-family:'Space Grotesk',sans-serif}body:before{content:"";position:fixed;inset:0;pointer-events:none;opacity:.05;background-image:url("data:image/svg+xml,%3Csvg viewBox='0 0 180 180' xmlns='http://www.w3.org/2000/svg'%3E%3Cfilter id='n'%3E%3CfeTurbulence type='fractalNoise' baseFrequency='.8' numOctaves='4' stitchTiles='stitch'/%3E%3C/filter%3E%3Crect width='100%25' height='100%25' filter='url(%23n)' opacity='.35'/%3E%3C/svg%3E")}a{color:inherit;text-decoration:none}.wrap{width:min(1160px,calc(100% - 48px));margin:auto}.site-header{height:86px;display:flex;align-items:center;justify-content:space-between;position:relative;z-index:2}.brand{display:flex;align-items:center;gap:10px;font-weight:700;letter-spacing:-.03em}.brand-mark{width:30px;height:30px;border-radius:9px;background:var(--coral);color:var(--paper);display:grid;place-items:center;font-family:'DM Mono',monospace;font-size:16px;box-shadow:4px 4px 0 var(--navy)}nav{display:flex;align-items:center;gap:28px;font-size:13px;color:var(--muted)}nav a:hover,.text-link:hover{color:var(--coral)}.nav-cta{padding:11px 16px;border:1px solid var(--line);border-radius:30px;color:var(--ink)}.hero{min-height:645px;display:grid;grid-template-columns:1fr 1.03fr;align-items:center;gap:36px;padding:70px 0 90px}.eyebrow{font:500 11px 'DM Mono',monospace;letter-spacing:.12em;text-transform:uppercase;color:var(--coral)}.eyebrow.light{color:var(--cyan)}.pulse{display:inline-block;width:8px;height:8px;background:var(--coral);border-radius:50%;margin-right:8px;box-shadow:0 0 0 5px rgba(255,114,92,.16)}h1,h2,h3,p{margin-top:0}h1{font-size:clamp(56px,7vw,94px);line-height:.94;letter-spacing:-.075em;margin:23px 0 28px;max-width:720px}h1 em,h2 em{font-style:normal;color:var(--coral)}.lede{font-size:19px;line-height:1.55;color:#5c6678;max-width:555px}.hero-actions{display:flex;gap:26px;align-items:center;margin-top:35px}.button{display:inline-flex;align-items:center;gap:24px;padding:16px 20px;border-radius:4px;font-weight:600;font-size:14px;transition:.25s}.button span{font-size:20px}.primary{color:var(--paper);background:var(--navy);box-shadow:5px 5px 0 var(--coral)}.primary:hover{transform:translate(2px,2px);box-shadow:2px 2px 0 var(--coral)}.text-link{font-weight:600;font-size:14px;border-bottom:1px solid var(--coral);padding-bottom:5px}.hero-stats{display:flex;gap:30px;margin-top:54px}.hero-stats div{display:flex;flex-direction:column;gap:4px}.hero-stats strong{font-size:25px;letter-spacing:-.06em}.hero-stats span{font:11px 'DM Mono',monospace;color:var(--muted)}.hero-art{height:480px;position:relative;border-radius:4px;overflow:hidden;background:var(--navy);box-shadow:var(--shadow)}.hero-art img{width:100%;height:100%;object-fit:cover;opacity:.9}.floating-card{position:absolute;background:rgba(255,253,248,.95);padding:14px 16px;border-radius:5px;font:12px 'DM Mono',monospace;box-shadow:0 12px 30px rgba(0,0,0,.18);display:flex;align-items:center;gap:8px}.floating-card b{font-family:'Space Grotesk',sans-serif;font-size:13px}.card-one{top:34px;right:28px}.card-two{bottom:35px;left:28px}.dot{width:8px;height:8px;border-radius:50%}.coral{background:var(--coral)}.cyan{background:var(--cyan)}.section{padding:125px 0}.section-head{display:grid;grid-template-columns:1fr 1.2fr 1fr;align-items:end;gap:30px;margin-bottom:55px}.section-head h2{font-size:clamp(42px,5vw,68px);line-height:.96;letter-spacing:-.07em;margin:0}.section-head>p:last-child{color:var(--muted);line-height:1.6;margin:0}.insight-grid{display:grid;grid-template-columns:repeat(3,1fr);gap:18px}.insight{min-height:305px;padding:28px;display:flex;flex-direction:column}.insight.dark{background:var(--navy);color:var(--paper)}.insight.coral-card{background:var(--coral);color:var(--paper)}.insight.outline{border:1px solid var(--line)}.number{font:12px 'DM Mono',monospace;opacity:.65}.insight h3{font-size:25px;letter-spacing:-.04em;margin:65px 0 14px}.insight p{line-height:1.55;opacity:.76;max-width:280px}.insight a{margin-top:auto;font:12px 'DM Mono',monospace}.band{background:var(--navy);color:var(--paper);padding:100px 0}.split{display:grid;grid-template-columns:1fr 1fr;gap:70px;align-items:end}.split h2{font-size:clamp(46px,5vw,72px);line-height:.94;letter-spacing:-.07em;margin:0}.band-copy{font-size:19px;line-height:1.55;color:#aeb7c4;max-width:440px}.light-button{background:var(--cyan);color:var(--navy);margin-top:24px}.calculator-section{display:grid;grid-template-columns:.85fr 1.15fr;gap:85px;align-items:start}.calculator-section .section-head{display:block;margin:0}.calculator-section .section-head h2{margin:25px 0}.calculator-section .section-head p:last-child{max-width:350px}.calculator{border:1px solid var(--line);padding:30px;background:#fff;box-shadow:var(--shadow)}.calc-controls{display:flex;align-items:center;gap:18px;flex-wrap:wrap;margin-bottom:25px}.calc-controls label{font:12px 'DM Mono',monospace;text-transform:uppercase;color:var(--muted)}.amount-input{display:flex;align-items:center;border-bottom:2px solid var(--navy);font-size:30px;font-weight:600}.amount-input input{width:140px;border:0;outline:0;font:inherit;color:var(--navy);background:transparent}.calc-controls p{font-size:11px;color:var(--muted);width:100%;margin:0}.result{display:grid;grid-template-columns:1fr auto;gap:10px;padding:15px 0;border-top:1px solid var(--line);align-items:center}.result-name{font-weight:600}.result-note{display:block;color:var(--muted);font:10px 'DM Mono',monospace;margin-top:4px}.result-value{font:600 21px 'DM Mono',monospace}.bar{grid-column:1/-1;height:5px;background:#edf0ef}.bar span{display:block;height:100%;background:var(--coral)}.rail-section{display:grid;grid-template-columns:1fr 1fr;gap:90px;align-items:center;background:var(--cream);width:100%;max-width:none;padding-left:max(24px,calc((100% - 1160px)/2));padding-right:max(24px,calc((100% - 1160px)/2))}.rail-copy h2{font-size:clamp(42px,5vw,66px);line-height:.96;letter-spacing:-.07em}.rail-copy p:not(.eyebrow){max-width:470px;line-height:1.6;color:var(--muted)}.rail-map{height:310px;position:relative}.rail-node{position:absolute;top:100px;left:50%;transform:translateX(-50%);height:105px;width:105px;border-radius:50%;background:var(--navy);color:var(--paper);display:grid;place-content:center;text-align:center;font:12px 'DM Mono',monospace;z-index:1;box-shadow:0 0 0 11px rgba(16,24,39,.07)}.rail-node strong{color:var(--cyan);font-size:14px}.rail-line{position:absolute;height:1px;background:var(--coral);width:145px;left:50%;transform-origin:left center;top:150px}.line-a{transform:rotate(-38deg)}.line-b{transform:rotate(38deg)}.line-c{transform:rotate(180deg);background:var(--cyan)}.rail-pill{position:absolute;padding:10px 14px;border:1px solid var(--line);background:var(--paper);font:11px 'DM Mono',monospace}.pill-a{top:50px;left:6%}.pill-b{top:50px;right:6%}.pill-c{bottom:20px;left:50%;transform:translateX(-50%)}.closing{padding:130px 0;display:grid;grid-template-columns:1fr 1fr;gap:80px;align-items:end}.closing h2{font-size:clamp(45px,5vw,70px);line-height:.96;letter-spacing:-.07em}.closing p:not(.eyebrow){color:var(--muted);line-height:1.6;max-width:450px}.closing .button{margin-top:20px}.footer{border-top:1px solid var(--line);padding:28px 0 42px;display:flex;align-items:center;gap:30px;font-size:12px;color:var(--muted)}.footer p{margin:0}.footer-links{margin-left:auto;display:flex;gap:18px}.footer-links a:hover{color:var(--coral)}@media(max-width:820px){nav a:not(.nav-cta){display:none}.hero,.calculator-section,.rail-section,.closing{grid-template-columns:1fr}.hero{padding-top:45px}.hero-art{height:350px}.section-head{display:block}.section-head h2{margin:24px 0}.insight-grid{grid-template-columns:1fr}.split{grid-template-columns:1fr;gap:28px}.rail-section{padding:90px 24px}.closing{gap:20px}.footer{flex-wrap:wrap}.footer-links{margin-left:0;width:100%}}@media(max-width:500px){.wrap{width:min(100% - 32px,1160px)}h1{font-size:55px}.hero-stats{gap:16px}.hero-stats span{font-size:9px}.hero-actions{flex-direction:column;align-items:flex-start}.hero-art{height:270px}.floating-card{font-size:9px;padding:9px}.floating-card b{font-size:10px}}
''')
put('docs/script.js', '''
const feeModels = [
  {name:'GitHub Sponsors', fee:0, note:'personal orientation', color:100},
  {name:'Ko-fi tips', fee:3.2, note:'processor orientation', color:96.8},
  {name:'Liberapay', fee:3.2, note:'processor orientation', color:96.8},
  {name:'Buy Me a Coffee', fee:8.2, note:'platform + processor', color:91.8},
  {name:'Polar', fee:8.6, note:'platform + processor + fixed', color:91.4},
  {name:'Open Collective', fee:10.5, note:'host + processor midpoint', color:89.5},
  {name:'Patreon', fee:12.5, note:'plan + processor midpoint', color:87.5},
  {name:'IssueHunt', fee:20, note:'bounty orientation', color:80}
];
const amount = document.querySelector('#amount');
const results = document.querySelector('#results');
function render(){
  const value = Math.max(1, Number(amount.value) || 100);
  results.innerHTML = feeModels.map(item => {
    const keep = value * (1 - item.fee / 100);
    return `<div class="result"><div><span class="result-name">${item.name}</span><span class="result-note">${item.note} · ${item.fee}% model</span></div><span class="result-value">$${keep.toFixed(2)}</span><div class="bar"><span style="width:${item.color}%"></span></div></div>`;
  }).join('');
}
amount.addEventListener('input', render); render();
''')
put('docs/calculator.html', '''<!doctype html><html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><title>Fee calculator · The Sponsor Button</title><link rel="stylesheet" href="style.css"></head><body><header class="site-header wrap"><a class="brand" href="index.html"><span class="brand-mark">$</span><span>The Sponsor Button</span></a></header><main class="section wrap"><p class="eyebrow">Fee lens</p><h1>What would you <em>actually keep?</em></h1><p class="lede">This browser-only calculator uses the orientation models from <a href="../COMPARISONS/fee-comparison.md">Fee Comparison</a>. It is not a quote.</p><div class="calculator"><div class="calc-controls"><label for="amount">Contribution amount</label><div class="amount-input"><span>$</span><input id="amount" type="number" min="1" value="100" step="5"></div></div><div id="results" class="results"></div></div></main><script src="script.js"></script></body></html>''')
put('docs/404.html', '''<!doctype html><html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><title>Not found · The Sponsor Button</title><link rel="stylesheet" href="style.css"></head><body><main class="section wrap"><p class="eyebrow">404 / wrong rail</p><h1>This page took a <em>detour.</em></h1><p class="lede">The link may have moved. Return to the guide and choose a clearer path.</p><a class="button primary" href="index.html">Back to the guide →</a></main></body></html>''')
put('docs/guide/sidebar-card-setup.html', '''<!doctype html><html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><title>Sidebar Card Setup</title><link rel="stylesheet" href="../style.css"></head><body><main class="section wrap"><p class="eyebrow">Guide / GitHub visibility</p><h1>Make your funding <em>visible.</em></h1><p class="lede">The Sponsor card needs both a FUNDING.yml file and a repository-level Sponsorships setting.</p><div class="insight-grid"><article class="insight dark"><span class="number">01</span><h3>What to add</h3><p>Put .github/FUNDING.yml on the default branch with valid usernames and no secrets.</p></article><article class="insight coral-card"><span class="number">02</span><h3>What to enable</h3><p>Open Settings → General → Features and enable Sponsorships.</p></article><article class="insight outline"><span class="number">03</span><h3>How to test</h3><p>Use an incognito window, open the Sponsor button, and test every route.</p></article></div><p style="margin-top:44px"><a class="text-link" href="../index.html">← Back to The Sponsor Button</a></p></main></body></html>''')
put('docs/assets/favicon.svg', '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 64 64"><rect width="64" height="64" rx="16" fill="#ff725c"/><path d="M20 21h19c5 0 8 3 8 8 0 4-2 6-5 7 4 1 6 4 6 8 0 6-4 9-10 9H20V21Zm8 7v5h10c2 0 3-1 3-3s-1-2-3-2H28Zm0 12v6h10c3 0 4-1 4-3s-1-3-4-3H28Z" fill="#fffdf8"/></svg>''')
put('docs/assets/decision-tree.svg', '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 900 500"><rect width="900" height="500" fill="#101827"/><g fill="none" stroke="#76e1d0" stroke-width="3"><path d="M450 80v80M450 160L220 270M450 160l230 110M220 270v80M680 270v80"/></g><g font-family="Arial" text-anchor="middle"><text x="450" y="55" fill="#fffdf8" font-size="25">Do you already have a GitHub audience?</text><text x="220" y="250" fill="#ff725c" font-size="22">YES → GitHub Sponsors</text><text x="680" y="250" fill="#ff725c" font-size="22">NO → Ko-fi or Patreon</text><text x="220" y="390" fill="#76e1d0" font-size="18">Add Ko-fi for PayPal</text><text x="680" y="390" fill="#76e1d0" font-size="18">Add GitHub Sponsors for discovery</text></g></svg>''')
put('docs/assets/fee-chart.svg', '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 900 420"><rect width="900" height="420" fill="#f6f1e8"/><g font-family="Arial" fill="#162033"><text x="48" y="55" font-size="28" font-weight="bold">Typical all-in orientation</text><text x="48" y="84" font-size="15">Lower is better, but country and account type change the result.</text></g><g fill="#ff725c"><rect x="50" y="120" width="40" height="230"/><rect x="160" y="170" width="40" height="180"/><rect x="270" y="190" width="40" height="160"/><rect x="380" y="235" width="40" height="115"/><rect x="490" y="260" width="40" height="90"/><rect x="600" y="290" width="40" height="60"/></g><g font-family="Arial" fill="#162033" font-size="14"><text x="37" y="375">GitHub</text><text x="145" y="375">Ko-fi</text><text x="250" y="375">BMC</text><text x="365" y="375">Polar</text><text x="470" y="375">Patreon</text><text x="575" y="375">IssueHunt</text></g></svg>''')
put('docs/robots.txt', 'User-agent: *\nAllow: /\n')
put('docs/sitemap.xml', '''<?xml version="1.0" encoding="UTF-8"?><urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9"><url><loc>https://fed-os.github.io/open-source-funding-guide/</loc></url><url><loc>https://fed-os.github.io/open-source-funding-guide/calculator.html</loc></url><url><loc>https://fed-os.github.io/open-source-funding-guide/guide/sidebar-card-setup.html</loc></url></urlset>''')
put('docs/.nojekyll','')

# Scripts
put('SCRIPTS/validate-funding-yml.sh', '''#!/usr/bin/env bash
set -euo pipefail
file="${1:-.github/FUNDING.yml}"
test -f "$file" || { echo "Missing $file"; exit 1; }
grep -Eq '^(github|patreon|open_collective|ko_fi|tidelift|community_bridge|liberapay|issuehunt|polar|buy_me_a_coffee|thanks_dev|custom):' "$file" || { echo "No supported FUNDING.yml key found"; exit 1; }
echo "Funding file looks structurally plausible: $file"
''')
put('SCRIPTS/check-links.sh', '''#!/usr/bin/env bash
set -euo pipefail
for file in README.md GUIDES/sidebar-card-setup.md COMPARISONS/fee-comparison.md; do test -f "$file" || exit 1; done
echo "Core guide files exist. Use lychee or a hosted link checker for network validation."
''')
put('SCRIPTS/generate-comparison-table.py', '''import csv
from pathlib import Path
rows=list(csv.DictReader(Path('DATA/fees.csv').open()))
print('| Platform | Typical total | Notes |')
print('| --- | --- | --- |')
for row in rows:
    print(f"| {row['platform']} | {row['typical_total']} | {row['notes']} |")
''')
put('SCRIPTS/update-fee-data.py', '''"""Manual-review helper: prints rows that need a new verification date."""
import csv
from pathlib import Path
from datetime import date
rows=list(csv.DictReader(Path('DATA/fees.csv').open()))
for row in rows:
    print(f"{row['platform']}: last verified {row['last_verified']} — review official terms before release")
print(f"Review date: {date.today().isoformat()}")
''')

# Wiki/discussion material
put('COMMUNITY/DISCUSSION-START-HERE.md', '''
# 👋 Start Here — Pick Your Funding Path

Are you a solo maintainer, a team, an enterprise-backed package, or a project that needs a fiscal host? Tell us your country, audience, and preferred payment methods without sharing private account details. The community can point you to the smallest setup that covers your real supporters.
''')
put('COMMUNITY/DISCUSSION-CATEGORIES.md', '''
# Discussion categories

- **Start Here:** choose a path and fix the sidebar card.
- **Platform updates:** report fee, payout, or policy changes.
- **Country experiences:** share availability and friction without posting private data.
- **Templates:** improve asks, tiers, and README snippets.
- **Case studies:** permissioned stories with context and numbers.
''')
put('COMMUNITY/WIKI-SIDEBAR.md', '''
### The Sponsor Button wiki

- [Home](Home)
- [Sidebar Card Setup](Sidebar-Card-Setup)
- [Fee Comparison](Fee-Comparison)
- [Payout Methods](Payout-Methods)
- [FUNDING.yml Templates](FUNDING-yml-Templates)
- [FAQ](FAQ)
- [Glossary](Glossary)
''')
put('COMMUNITY/WIKI-HOME.md', '''
# The Sponsor Button wiki

A practical companion to the repository. Start with the sidebar card, then choose a primary and backup rail that match your country, audience, and operational comfort.
''')
put('COMMUNITY/WIKI-FAQ.md', '''
# ❓ FAQ

<details><summary>Do I need a company?</summary>No. Some platforms support individuals; others are built around fiscal hosts or enterprise contracts. Verify account and country eligibility.</details>

<details><summary>Can I use multiple platforms?</summary>Yes. Use complementary payment rails rather than a wall of redundant links.</details>

<details><summary>What is FUNDING.yml?</summary>It is GitHub's configuration file for funding links shown through the repository Sponsor entry point.</details>

<details><summary>Are donations tax deductible?</summary>Do not assume so. Deductibility depends on the recipient's legal status and local law.</details>
''')
put('COMMUNITY/WIKI-GLOSSARY.md', '''
# 📚 Glossary

**Fiscal host:** An organization that administers funds for a project.  
**Payout threshold:** The minimum balance required before withdrawal.  
**Platform fee:** The fee retained by the funding service.  
**Processor fee:** The cost of moving the payment.  
**Chargeback:** A payment reversal initiated by a payment provider.  
**KYC:** Identity verification required by financial services.  
**Rev-share:** Revenue distributed according to an agreed percentage.
''')

# Make scripts executable
for p in (ROOT/'SCRIPTS').glob('*.sh'):
    p.chmod(0o755)
print(f'Created {sum(1 for _ in ROOT.rglob("*"))} repository entries in {ROOT}')
