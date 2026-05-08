<div align="center">

# 📬 Newsletter System

**Automated weekly newsletter that keeps past clients and leads engaged, nurtured, and coming back — zero manual effort.**

[![Make](https://img.shields.io/badge/Make.com-Core-6D00CC?style=for-the-badge)](https://make.com)
[![OpenAI](https://img.shields.io/badge/OpenAI-GPT--4o-412991?style=for-the-badge&logo=openai&logoColor=white)](https://openai.com)
[![Beehiiv](https://img.shields.io/badge/Beehiiv-Delivery-000000?style=for-the-badge)](https://beehiiv.com)
[![Airtable](https://img.shields.io/badge/Airtable-Content_Queue-18BFFF?style=for-the-badge&logo=airtable&logoColor=white)](https://airtable.com)

</div>

---

## Why a Newsletter

Most businesses stop talking to leads after the first sale — or lose touch between conversations. The newsletter is the system that keeps you top-of-mind, builds trust over time, and makes it natural for past clients to refer you and for cold leads to eventually convert.

One value-packed email per week. Fully automated. Sounds like a human wrote it.

---

## What's in Each Newsletter

```
┌─────────────────────────────────────────────┐
│  📌  THIS WEEK'S TOPIC                       │  ← Rotating theme (automation, AI, ops, etc.)
│                                             │
│  📖  MAIN INSIGHT (400–600 words)            │  ← AI-written, curated from sources
│      A real, actionable insight on the      │    you define. Not AI slop — edited for
│      week's topic. No fluff.                │    voice and quality.
│                                             │
│  💡  VALUE NUGGET                            │  ← One specific tip they can use TODAY
│      The one thing worth stealing           │    Short, punchy, memorable
│      from this week's issue.                │
│                                             │
│  🔧  TOOL OF THE WEEK                        │  ← One tool/resource relevant to the audience
│      What it is, why it matters,            │    With use case and honest take
│      one use case.                          │
│                                             │
│  🤝  HOW I CAN HELP                          │  ← Soft CTA — no hard sell
│      One line, relevant to the week's       │    "If any of this sounds like your ops..."
│      topic.                                 │
└─────────────────────────────────────────────┘
```

---

## Full Automation Flow

```
Every Monday at 6:00 AM
         │
         ▼
┌─────────────────────────┐
│  Content Sourcing       │  ← Pulls from RSS feeds, newsletters you subscribe to,
│                         │    Google Alerts, and Airtable content queue
└────────────┬────────────┘
             │
             ▼
┌─────────────────────────┐
│  AI Curation            │  ← GPT-4o reads all sourced content,
│  (GPT-4o)               │    selects the most valuable angle for the week,
│                         │    and drafts the full newsletter in your voice
└────────────┬────────────┘
             │
             ▼
┌─────────────────────────┐
│  Review Queue           │  ← Draft saved to Airtable for optional human review
│  (Optional)             │    If approved by 8 AM, scheduled for 9 AM send
│                         │    If not reviewed, auto-sends anyway (configurable)
└────────────┬────────────┘
             │
             ▼
┌─────────────────────────┐
│  Send via Beehiiv       │  ← Published to your list via Beehiiv API
│                         │    Subject line A/B tested automatically
│                         │    Personalized greeting per subscriber
└────────────┬────────────┘
             │
             ▼
┌─────────────────────────┐
│  Engagement Tracking    │  ← Open rates, clicks logged back to Airtable
│                         │    High engagers flagged for personal outreach
│                         │    Unsubscribes removed from all systems
└─────────────────────────┘
```

---

## Content Sources (Configurable)

```yaml
# config/sources.yaml
rss_feeds:
  - https://feeds.feedburner.com/oreilly/radar/   # Tech trends
  - https://www.ben-evans.com/benedictevans/feed  # Business + tech
  - https://substack.com/feed                     # Curated newsletters

google_alerts:
  - "business automation 2026"
  - "AI tools for small business"
  - "workflow automation news"

airtable_content_queue:
  base_id: "your-base-id"
  table: "Content Ideas"     # Your own ideas queue — anything here gets
                             # prioritized over sourced content
```

---

## Voice & Style Calibration

Before first run, the system is calibrated on 3–5 of your existing pieces of writing. GPT-4o learns:

- Your sentence length and rhythm
- Words you use vs. avoid
- How direct or conversational your tone is
- Your preferred newsletter structure

Result: drafts that sound like you, not like ChatGPT.

```
Calibration input:   3–5 sample emails or pieces you've written
Calibration time:    ~10 minutes (one-time setup)
Output voice:        Yours
```

---

## Segmentation

The newsletter can be sent to different segments with lightly varied content:

| Segment | Customization |
|---|---|
| **Past clients** | Reference their industry, warmer tone, more specific |
| **Cold leads** | Slightly more educational, softer CTA |
| **Referral partners** | Focus on what makes you easy to refer |
| **General list** | Balanced, universal version |

Segments are managed automatically via Airtable tags.

---

## High Engager Detection

After each send, subscribers who opened AND clicked are flagged in Airtable:

```python
# High engager triggers a personal follow-up workflow
if open_rate == True and click_rate == True:
    flag_for_personal_outreach(subscriber)
    create_airtable_task(
        title=f"Personal follow-up: {subscriber.name}",
        due_date=today + 2_days,
        note="Opened and clicked last newsletter — good moment to reach out."
    )
```

This turns newsletter engagement into a real pipeline trigger.

---

## Setup

### Required Accounts
- Make.com (Core or above)
- OpenAI API
- Beehiiv (newsletter platform)
- Airtable (content queue + subscriber data)
- Google Alerts (free)

### Configuration
```yaml
send_day: "Monday"
send_time: "09:00"
timezone: "America/Chicago"
review_window_hours: 2      # How long to wait for human review before auto-send
ab_test_subject_lines: true
list_segments: ["clients", "leads", "partners"]
```

### First Run Checklist
- [ ] Add 3–5 writing samples to `config/voice-samples/`
- [ ] Configure RSS feeds and Google Alerts in `config/sources.yaml`
- [ ] Import your subscriber list to Beehiiv
- [ ] Connect Beehiiv API in Make.com
- [ ] Run the `calibrate-voice.json` scenario first
- [ ] Schedule the `weekly-newsletter.json` scenario for Monday 6 AM

---

## Results

```
Before: Newsletter never sent, leads go cold, past clients forget you
After:  Weekly email, consistently, that sounds personal

Open rate:           42–55% (industry avg: 21%)
Unsubscribe rate:    < 0.3%
Referrals generated: Measurable lift after 60 days
Time per issue:      ~10 min review (or 0 on auto-send)
```

---

<div align="center">

**Built by [Rohan Mukherjee](https://github.com/rohan643)**

</div>
