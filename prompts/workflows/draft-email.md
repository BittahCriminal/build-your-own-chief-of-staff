# Draft an email

## When to use
A message I already know I need to send: bad news, a status ping, an ask, an escalation, a meeting follow-up. One intent per draft.

## Inputs
Required: `voice.md`, `who-i-am.md`, the intent (which of the five), the facts.
Optional: `people.md` for the recipient, `priorities.md` if the ask should tie to their goals, a doc to link.
I will paste the facts. Do not browse my inbox for extra color unless I attach it.

## Steps
1. Read `voice.md`. Pick the skeleton that matches the intent.
2. Subject states the point, not the topic.
3. First two lines carry the message for a phone screen.
4. One screen. Detail goes in a linked doc I actually have.
5. Draft. Do not send.

## Output

Use exactly one skeleton:

**Bad news, early**
```
Subject: <Problem> — recommendation: <your rec in 3 words>

<Problem>: what's wrong and how I found it.
Impact if unaddressed: <specific>.
Options:
  1. <option> — <cost/benefit>
  2. <option> — <cost/benefit>
Recommendation: option <n>, because <one sentence>.
Unless you object by <date/time>, I'll proceed.
```

**Proactive status ping**
```
Subject: <Project>: on track for <date> / at risk — <reason>

Done since last update: <1–3 bullets>
Next: <what lands when>
<If at risk> Risk: <what>. Mitigation: <plan>. Need: <ask or "nothing yet">.
```

**The ask**
```
Subject: Request: <the thing> by <date>

Context (1–2 lines): <why this matters to *their* goals>
Ask: <specific, singular, with deadline>
To make it easy: <what you've already prepared / the 15-min version>
If now's wrong, <fallback: who else / later date>?
```

**Escalation (blameless)**
```
Subject: Blocked on <goal> — need <decision/resource> by <date>

Goal: <what we're trying to deliver and why it matters>
Blocked on: <the specific dependency — facts, no blame>
Tried: <what you've already attempted>
Need: <the decision or action> by <date>, else <consequence>.
```

**Meeting follow-up** — use `meeting-recap.md` instead.

## Check
- Every factual claim cites something I pasted or a file I attached.
- No banned phrases from `voice.md`.
- One ask or one recommendation, not both buried.
- I still send it.

## Do not
Send. CC anyone. Soften bad news until the last paragraph. Escalate a person instead of a blocked goal. Invent a deadline.
