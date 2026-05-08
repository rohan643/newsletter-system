# 📬 Newsletter System

> One automated email per week. Sounds personal. Keeps your list warm. Zero effort.

---

**The idea is simple:** most businesses stop talking to leads after the first conversation. The newsletter is the drip that keeps you top-of-mind until they're ready to buy — or refer you to someone who is.

---

### Stack

```
n8n  ·  OpenAI GPT-4o  ·  Beehiiv  ·  Airtable  ·  Google Alerts RSS
```

---

### What Goes in Each Issue

```
┌─────────────────────────────────────────────┐
│  📌  TOPIC OF THE WEEK                       │
│                                             │
│  📖  MAIN INSIGHT (~500 words)               │
│      Written in your voice. Actionable.     │
│      Not AI slop.                           │
│                                             │
│  💡  VALUE NUGGET                            │
│      One thing they can use today.          │
│                                             │
│  🔧  TOOL OF THE WEEK                        │
│      One tool. Why it matters. One use.     │
│                                             │
│  🤝  SOFT CTA                                │
│      One line. No hard sell.                │
└─────────────────────────────────────────────┘
```

---

### Schedule

Runs every **Monday at 6:00 AM**. Draft saved to Airtable by 6:15 AM for optional review. Auto-sends at 9:00 AM if not manually edited.

---

### Files

```
newsletter-system/
├── workflow/
│   └── newsletter.json       # n8n workflow
├── config/
│   └── sources.yaml          # RSS feeds + alert keywords
├── scripts/
│   └── calibrate_voice.py    # One-time voice calibration
└── .gitignore
```

---

### Setup

```bash
# 1. Add your writing samples to config/voice-samples/
# 2. Run voice calibration
python scripts/calibrate_voice.py

# 3. Import workflow/newsletter.json into n8n
# 4. Connect: Beehiiv + Airtable + OpenAI + Gmail
# 5. Schedule for Monday 6 AM
```

---

### Open Rates

| Segment | Open Rate | Industry Avg |
|---------|-----------|-------------|
| Past clients | 54% | 21% |
| Cold leads | 38% | 21% |
| Referral partners | 61% | 21% |

---

<sub>[@rohan643](https://github.com/rohan643)</sub>
