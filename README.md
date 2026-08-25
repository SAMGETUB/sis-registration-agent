# SiS Course Registration Automation Agent

> 🚧 **Status: Currently in active development**

An automation agent that monitors UMass Lowell's SiS portal (PeopleSoft) and streamlines course registration. It watches a wishlist of courses for open seats, attempts enrollment through the same flow a student would use, and notifies you of the outcome — success or failure, with the actual reason why.

---

## 📌 Project Overview

Registering for courses at UMass Lowell means constantly refreshing the SiS portal, hoping a seat opens up in a class you need. This project automates that: you give it a wishlist of courses, and the agent handles the monitoring and enrollment attempts for you, notifying you of the outcome by email.

---

## ⚙️ What It Does

- **Browser Automation** — Uses Playwright to log into the SiS portal, manage authenticated PeopleSoft sessions, and navigate course search and enrollment flows
- **Seat Monitoring** — Watches a wishlist of courses and detects when a section has an open seat
- **Enrollment Attempts** — When a seat opens, attempts enrollment and reads the portal's own response to determine what happened — enrolled, rejected, already enrolled, or an automation error
- **Orchestration** — Uses n8n for scheduled polling on a set interval, stopping once a course is successfully enrolled
- **Notifications** — Sends an email on successful enrollment, or with the specific reason a course failed

---

## 🧩 How It Works

auth.py → seat_checker.py → enroller.py → notifier.py
(log in) (check each (attempt the seat, (email the
course's seat) read the portal's outcome via
verdict) n8n / Gmail)

Each course attempt returns one of four labeled outcomes — `enrolled`, `rejected`, `already_enrolled`, or `error` — rather than a simple success/fail flag, since a rejection (stop trying) and an automation error (try again) look identical from the outside but need opposite handling.

---

## 🎯 Design Decisions

- **The portal is the judge.** Rather than maintaining a hand-copied list of completed prerequisites that could drift out of sync with the real transcript, the agent attempts the enrollment and reads the portal's own rejection reason when it fails — one mechanism covers prerequisites, term limits, holds, and credit caps.
- **Selectors read semantic class attributes, not scraped text.** The portal is a React SPA that renders similar-looking pages differently underneath — status and outcomes are read from stable class names (e.g. an icon's `good`/`bad` flag) rather than positional selectors or raw text, which breaks on layout changes and picks up stray whitespace.

---

## 🛡️ Safety Rules

- Never enrolls in a section that wasn't requested
- Never enrolls if the portal rejects the attempt
- Stops polling a course once it has been successfully enrolled
- **Not yet safe to run fully unattended** — permission-code handling isn't built, so the agent will attempt enrollment in anything showing an open seat with no additional validation

---

## 🛠 Tech Stack

- **Language:** Python
- **Browser Automation:** Playwright
- **Orchestration / Scheduling:** n8n
- **Notifications:** Gmail (via n8n)

---

## 🚀 Getting Started

### 1. Clone and install dependencies

```bash
git clone https://github.com/SAMGETUB/sis-registration-agent.git
cd sis-registration-agent
python3 -m venv venv && source venv/bin/activate
pip install -r requirements.txt
playwright install
```

`playwright install` downloads the actual browser binaries Playwright drives — this is separate from `pip install` and required, or `auth.py` will fail to launch.

### 2. Add your credentials

Create a `.env` file in the project root:

SIS_PASSWORD=<your UMass password>
N8N_WEBHOOK_URL=<your n8n workflow's Production URL>

The n8n webhook URL is only needed if you want email notifications — set up your own n8n workflow (Webhook trigger → Gmail node) and paste its Production URL here.

### 3. Set your wishlist

Open `config.py` and replace the `wishlist` entries with the courses you want to watch — each needs `name`, `subject`, `catalog_number`, and `class_number` (the `class_number` is what UMass Lowell uses to uniquely identify a specific section).

### 4. Run it

```bash
python3 auth.py
```

> **Important:** This project authenticates via a persistent, pre-signed-in Chrome profile rather than automating UMass's SSO login flow directly. `auth.py` points at a specific local Chrome profile path. To run this on your own machine, update that path to point at a Chrome profile that's already logged into UMass Lowell SSO — otherwise the automated login step won't have a session to use.

---

## 🚦 Roadmap

- [✅] Playwright login + session handling for the SiS portal
- [✅] Seat availability checker for a single course
- [✅] Enrollment submission with labeled outcomes
- [✅] n8n Webhook → Gmail notification pipeline (built & verified end-to-end)
- [ ] Wire notifications into the live polling loop
- [ ] n8n scheduled polling (stop-once-enrolled)
- [ ] Permission-code handling

---

## 👤 Author

**Erwin Samuel Coq** — Computer Science student at UMass Lowell (Data Science concentration)
[LinkedIn](http://linkedin.com/in/erwin-coq-aaba722ba) · coq.erwin.samuel@gmail.com
