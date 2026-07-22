# SiS Course Registration Automation Agent

> 🚧 **Status: Currently in active development**

An automation agent that monitors UMass Lowell's SiS portal (PeopleSoft) and streamlines course registration. It watches a wishlist of courses for open seats, validates prerequisites, handles permission codes, and auto-enrolls when conditions are met — sending notifications on success or failure.

---

## 📌 Project Overview

Registering for courses at UMass Lowell means constantly refreshing the SiS portal hoping a seat opens up in a class you need. This project automates that process end to end: you give it a wishlist of courses, and the agent handles the monitoring and enrollment for you, notifying you of the outcome.

---

## ⚙️ What It Does

- **Browser Automation** — Uses Playwright to log into the SiS portal, manage authenticated PeopleSoft sessions, and navigate course search and enrollment flows
- **Seat Monitoring** — Watches a wishlist of courses and detects when a section has an open seat
- **Prerequisite Validation** — Checks that prerequisites are met before attempting enrollment
- **Permission Codes** — Uses a permission code when one is required and provided; skips and logs the course when a required code is missing
- **Orchestration** — Uses n8n for scheduled polling on a set interval, stopping once a course is successfully enrolled
- **Notifications** — Sends a notification on successful enrollment or with the specific reason a course failed

---

## 🛡️ Safety Rules

- Never enrolls in a section that wasn't requested
- Never enrolls if prerequisites aren't met
- Stops polling a course once it has been successfully enrolled

---

## 🛠 Tech Stack

- **Language:** Python
- **Browser Automation:** Playwright
- **Orchestration / Scheduling:** n8n
- **Notifications:** Gmail API

---

## 🚀 Roadmap

- [ ] Playwright login + session handling for the SiS portal
- [ ] Seat availability checker for a single course
- [ ] Prerequisite and permission-code validation
- [ ] Enrollment submission
- [ ] n8n scheduling and polling loop
- [ ] Gmail notifications on success / failure

---

## 👤 Author

**Erwin Samuel Coq** — Computer Science student at UMass Lowell (Data Science concentration)  
[LinkedIn](http://linkedin.com/in/erwin-coq-aaba722ba) · coq.erwin.samuel@gmail.com
