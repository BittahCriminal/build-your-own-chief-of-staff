#!/usr/bin/env python3
"""Build the follow-along talk deck. Non-technical. Speaker notes cite repo Markdown."""

from io import BytesIO
from pathlib import Path

import qrcode
from pptx import Presentation
from pptx.dml.color import RGBColor
from pptx.enum.shapes import MSO_SHAPE
from pptx.enum.text import PP_ALIGN
from pptx.oxml.ns import qn
from pptx.util import Inches, Pt

# Black + gold (49ers palette, no marks). Not a licensed theme.
BLACK = RGBColor(0x00, 0x00, 0x00)
CARD = RGBColor(0x14, 0x14, 0x14)
CREAM = RGBColor(0xF4, 0xEB, 0xD0)
GOLD = RGBColor(0xB3, 0x99, 0x5D)
MUTED = RGBColor(0xB8, 0xA8, 0x88)
NAVY = BLACK
NAVY2 = CARD

W, H = Inches(13.333), Inches(7.5)

REPO = "https://github.com/BittahCriminal/build-your-own-chief-of-staff"
START_HERE = REPO + "/blob/main/START-HERE.md"


def blob(path):
    return f"{REPO}/blob/main/{path}"


def set_run(run, size=20, bold=False, color=CREAM, font="Calibri"):
    run.font.size = Pt(size)
    run.font.bold = bold
    run.font.color.rgb = color
    run.font.name = font
    rPr = run._r.get_or_add_rPr()
    latin = rPr.find(qn("a:latin"))
    if latin is None:
        from pptx.oxml import parse_xml
        rPr.append(parse_xml(f'<a:latin xmlns:a="http://schemas.openxmlformats.org/drawingml/2006/main" typeface="{font}"/>'))
    else:
        latin.set("typeface", font)


def add_rect(slide, l, t, w, h, fill):
    sh = slide.shapes.add_shape(MSO_SHAPE.RECTANGLE, l, t, w, h)
    sh.fill.solid()
    sh.fill.fore_color.rgb = fill
    sh.line.fill.background()
    return sh


def textbox(slide, l, t, w, h, text, size=20, bold=False, color=CREAM, align=PP_ALIGN.LEFT, font="Calibri"):
    box = slide.shapes.add_textbox(l, t, w, h)
    tf = box.text_frame
    tf.word_wrap = True
    p = tf.paragraphs[0]
    p.alignment = align
    run = p.add_run()
    run.text = text
    set_run(run, size=size, bold=bold, color=color, font=font)
    return box


def bullets(slide, l, t, w, h, items, size=22, color=CREAM, spacing=10):
    box = slide.shapes.add_textbox(l, t, w, h)
    tf = box.text_frame
    tf.word_wrap = True
    for i, item in enumerate(items):
        p = tf.paragraphs[0] if i == 0 else tf.add_paragraph()
        p.level = 0
        p.space_after = Pt(spacing)
        run = p.add_run()
        run.text = "•  " + item
        set_run(run, size=size, color=color)
    return box


def notes(slide, text):
    slide.notes_slide.notes_text_frame.text = text.strip()


def footer(slide, n, total):
    textbox(
        slide,
        Inches(0.7),
        Inches(7.1),
        Inches(10),
        Inches(0.3),
        "Build your own chief of staff  ·  process, not a vendor",
        size=11,
        color=MUTED,
    )
    textbox(
        slide,
        Inches(11.6),
        Inches(7.1),
        Inches(1.2),
        Inches(0.3),
        f"{n}  /  {total}",
        size=11,
        color=MUTED,
        align=PP_ALIGN.RIGHT,
    )


def gold_bar(slide):
    add_rect(slide, Inches(0), Inches(0), Inches(0.18), H, GOLD)
    add_rect(slide, Inches(0), Inches(7.42), W, Inches(0.08), GOLD)


def blank(prs):
    s = prs.slides.add_slide(prs.slide_layouts[6])
    add_rect(s, 0, 0, W, H, NAVY)
    gold_bar(s)
    return s


def add_qr(slide, url, l, t, size=Inches(2.2)):
    buf = BytesIO()
    qrcode.make(url).save(buf)
    buf.seek(0)
    slide.shapes.add_picture(buf, l, t, size, size)


def linked_url(slide, l, t, w, h, url, size=16):
    box = slide.shapes.add_textbox(l, t, w, h)
    tf = box.text_frame
    tf.word_wrap = True
    p = tf.paragraphs[0]
    run = p.add_run()
    run.text = url.removeprefix("https://")
    set_run(run, size=size, bold=True, color=CREAM)
    run.hyperlink.address = url
    return box


def github_dest(slide, path, url, kicker="LEAVE THE SLIDES"):
    """Portal slide: path, clickable GitHub URL, QR. Caller adds title/body."""
    textbox(slide, Inches(0.8), Inches(0.4), Inches(8.5), Inches(0.35),
            kicker, size=14, bold=True, color=GOLD)
    textbox(slide, Inches(0.8), Inches(4.55), Inches(8.6), Inches(0.4),
            path, size=18, bold=True, color=GOLD)
    linked_url(slide, Inches(0.8), Inches(5.0), Inches(8.6), Inches(0.7), url, size=15)
    add_qr(slide, url, Inches(10.0), Inches(4.35), Inches(2.3))
    textbox(slide, Inches(10.0), Inches(6.7), Inches(2.3), Inches(0.3),
            "scan this page", size=12, color=MUTED, align=PP_ALIGN.CENTER)


def build():
    prs = Presentation()
    prs.slide_width = W
    prs.slide_height = H
    TOTAL = 16

    def fin(s, n, note):
        footer(s, n, TOTAL)
        notes(s, note)

    # 1 Title
    s = blank(prs)
    textbox(s, Inches(0.8), Inches(1.7), Inches(11.5), Inches(0.4),
            "A TALK FOR OPERATORS, NOT DEVELOPERS", size=14, bold=True, color=GOLD)
    textbox(s, Inches(0.8), Inches(2.2), Inches(11.5), Inches(1.6),
            "Build your own\nchief of staff agent", size=44, bold=True, color=CREAM)
    textbox(s, Inches(0.8), Inches(4.5), Inches(11.5), Inches(1.2),
            "Teach the process. Not a vendor.\nLeave knowing how to build a CoS agent — and how to automate\nanything that is repeatable and verifiable.",
            size=20, color=MUTED)
    fin(s, 1, """
Open by saying this is not a product demo. No one is leaving with a login, a marketplace skill, or a reason to switch from Copilot to Claude.

They are leaving with a process they can run Monday in whatever tool they already have.

The Chief of Staff agent is the worked example. Briefs, drafts, open loops, meeting prep. The real prize is the two tests they will use on expense reports, hiring screens, and customer research next month.

Cite the local source catalog if asked: https://github.com/BittahCriminal/build-your-own-chief-of-staff/blob/main/research/SOURCES.md — 20 Markdown notes documenting the operating rules used in this kit, with original article attribution.
""")

    # 2 Walk away with
    s = blank(prs)
    textbox(s, Inches(0.8), Inches(0.45), Inches(11), Inches(0.8),
            "What you walk away with", size=32, bold=True)
    bullets(s, Inches(0.8), Inches(1.6), Inches(11.5), Inches(3.2), [
        "How to stand up a personal Chief of Staff without writing code.",
        "How to decide what should be an agent — and what must stay human.",
        "A folder of markdown files you paste into Copilot, Cursor, Claude, ChatGPT, or Gemini.",
    ], size=24, spacing=18)
    textbox(s, Inches(0.8), Inches(5.3), Inches(11.5), Inches(1.2),
            "The model is interchangeable. Your process is not.",
            size=22, bold=True, color=GOLD)
    fin(s, 2, """
Pause on the third bullet. These are ordinary markdown files. If their IT department only allows Copilot, they are fine. If they live in ChatGPT, they are fine.

The context files they fill in privately — who they are, this quarter's priorities, how they write, where truth lives — are the operating system. Swap the vendor tomorrow and nothing important moves. START-HERE.md is how the folder lands on a PC. Do not walk the file tree here — that happens on GitHub in a few minutes.

That claim is from the context-files note (Source: https://github.com/BittahCriminal/build-your-own-chief-of-staff/blob/main/research/notes/context-files.md) and from the delegation kit's memory scaffold (https://github.com/BittahCriminal/build-your-own-chief-of-staff/blob/main/research/notes/delegation-kit.md).
""")

    # 3 Not a vendor
    s = blank(prs)
    textbox(s, Inches(0.8), Inches(0.45), Inches(11), Inches(0.8),
            "This is not a vendor talk", size=32, bold=True)
    add_rect(s, Inches(0.8), Inches(1.6), Inches(5.5), Inches(4.4), NAVY2)
    add_rect(s, Inches(6.9), Inches(1.6), Inches(5.5), Inches(4.4), NAVY2)
    textbox(s, Inches(1.05), Inches(1.85), Inches(5), Inches(0.5), "WE WILL NOT", size=14, bold=True, color=GOLD)
    bullets(s, Inches(1.05), Inches(2.4), Inches(5), Inches(3.2), [
        "Pick a model for you.",
        "Install a plugin.",
        "Promise it replaces a human CoS.",
        "Let it send anything.",
    ], size=18, spacing=12)
    textbox(s, Inches(7.15), Inches(1.85), Inches(5), Inches(0.5), "WE WILL", size=14, bold=True, color=GOLD)
    bullets(s, Inches(7.15), Inches(2.4), Inches(5), Inches(3.2), [
        "Write the job down.",
        "Put you in files you own.",
        "Check the draft against a source.",
        "Fix the file when it is wrong.",
    ], size=18, spacing=12)
    fin(s, 3, """
Say the refusal out loud. 'It replaces your Chief of Staff' is marketing. A human CoS does two kinds of work. Operational: reconstruct context, draft the update, prep the meeting, keep loops from disappearing. Judgment: when to push, how a room will land, which red line you will not cross.

We automate the first. We keep the second. That split is the whole talk, and it is the load-bearing claim in the Delegation Kit note: https://github.com/BittahCriminal/build-your-own-chief-of-staff/blob/main/research/notes/delegation-kit.md
""")

    # 4 Two tests
    s = blank(prs)
    textbox(s, Inches(0.8), Inches(0.45), Inches(11), Inches(0.8),
            "The whole course is two tests", size=32, bold=True)
    add_rect(s, Inches(0.8), Inches(1.7), Inches(5.5), Inches(4.3), NAVY2)
    add_rect(s, Inches(6.9), Inches(1.7), Inches(5.5), Inches(4.3), NAVY2)
    textbox(s, Inches(1.1), Inches(2.0), Inches(5), Inches(0.6), "1. Repeatable", size=26, bold=True, color=GOLD)
    textbox(s, Inches(1.1), Inches(2.8), Inches(5), Inches(2.6),
            "You would do the same steps next week.\nSame kinds of inputs. Same shape of output.\n\nSpecial cases every time = judgment.\nKeep it.",
            size=18, color=CREAM)
    textbox(s, Inches(7.2), Inches(2.0), Inches(5), Inches(0.6), "2. Verifiable", size=26, bold=True, color=GOLD)
    textbox(s, Inches(7.2), Inches(2.8), Inches(5), Inches(2.6),
            "A careful human can check the output\nagainst a source, a template, or a\nyes/no rule.\n\n“Does this sound good?” is not a check.",
            size=18, color=CREAM)
    fin(s, 4, """
Stay here. This is the slide they should photograph.

Repeatable: Monday status (same headings, new evidence) yes. Meeting recap yes. Which of two candidates to hire no. 'Handle my email' is usually seventeen jobs — split it.

Verifiable: every Done line cites a ticket you can open; the recap names an owner only when the notes name one; gaps stay 'not found'. 'Make it professional' cannot drive a loop.

Fail either test → do not automate. That is not caution. That is the curriculum.

The checkability argument: if checking an answer costs as much as making it, extra attempts just grow the pile. Source: https://github.com/BittahCriminal/build-your-own-chief-of-staff/blob/main/research/notes/agent-shaped-work.md

And: if you cannot name what would make you say 'not yet,' you have a vibe, not a job. Source: https://github.com/BittahCriminal/build-your-own-chief-of-staff/blob/main/research/notes/verification-gap.md
""")

    # 5 Fail either
    s = blank(prs)
    textbox(s, Inches(0.8), Inches(2.0), Inches(11.5), Inches(1.4),
            "Fail either test → do not automate.", size=36, bold=True, color=GOLD, align=PP_ALIGN.CENTER)
    textbox(s, Inches(1.5), Inches(3.6), Inches(10.2), Inches(1.6),
            "That leftover is judgment.\nTaste, red lines, how a room will land, which story is worth telling.\nKeep it.",
            size=22, color=CREAM, align=PP_ALIGN.CENTER)
    fin(s, 5, """
Let this land. People came hoping to automate the hard conversations. Tell them no, kindly.

The shape-of-the-work briefing: if you automate work that depends on trust and judgment, you break the process at the point where the human mattered most. Source: https://github.com/BittahCriminal/build-your-own-chief-of-staff/blob/main/research/notes/shape-of-work.md

And from automation discovery: frequency is evidence, not value. Choosing none of the offered automations is allowed. Source: https://github.com/BittahCriminal/build-your-own-chief-of-staff/blob/main/research/notes/let-history-pick.md
""")

    # 6 The freeze
    s = blank(prs)
    textbox(s, Inches(0.8), Inches(0.45), Inches(11), Inches(0.8),
            "Then people freeze", size=32, bold=True)
    textbox(s, Inches(0.8), Inches(1.5), Inches(11.5), Inches(1.4),
            "They buy the tool. They connect a few things.\nThey stare at an empty prompt.",
            size=24, color=CREAM)
    bullets(s, Inches(0.8), Inches(3.2), Inches(11.5), Inches(3.2), [
        "Idle agents are not broken. Nobody dispatched them.",
        "“Handle my email” is usually seventeen jobs you have never named.",
        "Do not let the model pick the problem and build it. You choose. None is allowed.",
    ], size=20, spacing=14)
    fin(s, 6, """
This is the paralysis slide. Stay here until they nod.

Nate's empty-prompt piece: people have a capable agent and keep staring at the box. The first version of automation-discovery let the AI pick and build — he killed that 'magic button' because it hides the judgment call. Offer sheet, then a human chooses. Choosing none is allowed. Frequency is not value. Source: https://github.com/BittahCriminal/build-your-own-chief-of-staff/blob/main/research/notes/let-history-pick.md

Idle agents: a social network for agents filled up and sat there. They were never asked to do a single thing. Source: https://github.com/BittahCriminal/build-your-own-chief-of-staff/blob/main/research/notes/agent-shaped-work.md

Point them at prompts/process/what-to-automate.md on GitHub later — last week, split the blob, edge vs core, two tests, one fast win.
""")

    # 7 Why it fails
    s = blank(prs)
    textbox(s, Inches(0.8), Inches(0.45), Inches(11), Inches(0.8),
            "Why this work actually fails", size=32, bold=True)
    bullets(s, Inches(0.8), Inches(1.45), Inches(11.5), Inches(5.2), [
        "Core-first. Automate the judgment. Three months later: stalled, bloated, humans checked out.",
        "A blob treated as one job. The model writes something that looks like a PRD and falls apart.",
        "No check. Success was “it sounds good,” or the agent said done.",
        "False success. Matching filename, finished-looking draft, wrong file. People stop looking.",
        "Waiting for a smarter model. The missing piece was a named job, a source, and an owner.",
    ], size=18, spacing=12)
    fin(s, 7, """
These failure modes come from Nate's essays, summarized in the local source notes below.

Core-first vs edges: https://github.com/BittahCriminal/build-your-own-chief-of-staff/blob/main/research/notes/why-agent-projects-fail.md
Fails at the task level (five jobs pretending to be one): https://github.com/BittahCriminal/build-your-own-chief-of-staff/blob/main/research/notes/task-decomposition.md
False success (wrong spreadsheet, said done): https://github.com/BittahCriminal/build-your-own-chief-of-staff/blob/main/research/notes/false-success.md
A better model will not save you: https://github.com/BittahCriminal/build-your-own-chief-of-staff/blob/main/research/notes/better-models-wont-fix-the-process.md

The postmortem prompt is diagnose-the-stall.md — they will see it under prompts/process/ on GitHub, not as a slide.
""")

    # 8 Start at the edges
    s = blank(prs)
    textbox(s, Inches(0.8), Inches(0.45), Inches(11), Inches(0.8),
            "Start at the edges, not the core", size=32, bold=True)
    edges = [
        ("Prep", "Collect, clean, reconcile"),
        ("Check", "Completeness, obvious errors"),
        ("Summarize", "Thread → one page"),
        ("Package", "Analysis → brief / recap"),
        ("Hand off", "Move context. Stop being the glue."),
    ]
    for i, (h, d) in enumerate(edges):
        left = Inches(0.55 + i * 2.5)
        add_rect(s, left, Inches(1.55), Inches(2.35), Inches(2.7), NAVY2)
        textbox(s, left + Inches(0.12), Inches(1.8), Inches(2.1), Inches(0.7), h, size=20, bold=True, color=GOLD)
        textbox(s, left + Inches(0.12), Inches(2.55), Inches(2.1), Inches(1.4), d, size=15, color=CREAM)
    textbox(s, Inches(0.8), Inches(4.55), Inches(11.5), Inches(1.8),
            "The core is craft: taste, red lines, how a room lands. Protect it.\nPick the simplest edge with the clearest lift — not the most impressive one.",
            size=18, color=MUTED)
    fin(s, 8, """
Edge-first is the thought process they came for. Data preparation, QA, synthesis, packaging, coordination. Cheap errors. Humans can pick up an exception without the whole workflow breaking.

The core is where they groan that they want help — and where first projects die. Trust is the real project: automate around the craft, not through it.

Source: https://github.com/BittahCriminal/build-your-own-chief-of-staff/blob/main/research/notes/why-agent-projects-fail.md

CoS mapping: recap, brief, open-loop list, packaging a status = edges. When to push, which story to tell = core.
""")

    # 9 CoS is / isn't
    s = blank(prs)
    textbox(s, Inches(0.8), Inches(0.45), Inches(11), Inches(0.8),
            "The Chief of Staff is the teaching case", size=30, bold=True)
    add_rect(s, Inches(0.8), Inches(1.5), Inches(5.5), Inches(4.7), NAVY2)
    add_rect(s, Inches(6.9), Inches(1.5), Inches(5.5), Inches(4.7), NAVY2)
    textbox(s, Inches(1.1), Inches(1.75), Inches(5), Inches(0.5), "OPERATIONAL  —  automate", size=14, bold=True, color=GOLD)
    bullets(s, Inches(1.1), Inches(2.4), Inches(5), Inches(3.5), [
        "Morning brief",
        "Weekly update",
        "Meeting prep",
        "Meeting recap ← we open this file next",
        "Open loops",
        "Drafts of mail you will send",
    ], size=18, spacing=10)
    textbox(s, Inches(7.2), Inches(1.75), Inches(5), Inches(0.5), "JUDGMENT  —  keep", size=14, bold=True, color=GOLD)
    bullets(s, Inches(7.2), Inches(2.4), Inches(5), Inches(3.5), [
        "When to push or hold",
        "How a room will land",
        "Political risk",
        "The hard conversation",
        "Which story is worth telling",
        "Anything you would not put your name on unread",
    ], size=18, spacing=10)
    textbox(s, Inches(0.9), Inches(6.3), Inches(11.8), Inches(0.5),
            "Meeting recap needs the least setup of the six — one voice file, meeting details, and one real transcript.",
            size=15, color=MUTED)
    fin(s, 9, """
Walk the left column: these are the eight portable jobs from the Delegation Kit, renamed into operator English. Source: https://github.com/BittahCriminal/build-your-own-chief-of-staff/blob/main/research/notes/delegation-kit.md

The right column is not 'AI can't do it.' It is 'checking it costs as much as doing it, so extra attempts just grow the pile.'

Flag meeting-recap now. Next slide leaves PowerPoint. You will open the GitHub file, copy it, and run it.
""")

    # 10 Open the kit
    recap = blob("prompts/workflows/meeting-recap.md")
    process = blob("PROCESS.md")
    score = blob("prompts/process/score-the-candidates.md")

    s = blank(prs)
    github_dest(s, "README.md (repo root)", REPO)
    textbox(s, Inches(0.8), Inches(0.75), Inches(11.5), Inches(0.7),
            "Open the kit", size=32, bold=True)
    textbox(s, Inches(0.8), Inches(1.5), Inches(8.6), Inches(0.7),
            "Same markdown. Copilot, Cursor, Claude, ChatGPT, or Gemini.\nClick the tree. Do not tour every file.",
            size=18, color=MUTED)
    kit = [
        ("START-HERE.md", "Get the files onto a PC"),
        ("PROCESS.md", "The method — we walk this after the demo"),
        ("prompts/workflows/", "The CoS jobs, ready to paste"),
        ("prompts/process/", "Turn any job into a workflow"),
        ("context-templates/", "Blanks. Copy privately. Fill them."),
        ("how-to/", "Which box to paste into"),
    ]
    for i, (fn, desc) in enumerate(kit):
        r, c = divmod(i, 3)
        left = Inches(0.8 + c * 2.9)
        top = Inches(2.35 + r * 1.0)
        textbox(s, left, top, Inches(2.75), Inches(0.4), fn, size=13, bold=True, color=GOLD)
        textbox(s, left, top + Inches(0.35), Inches(2.75), Inches(0.5), desc, size=12, color=CREAM)
    fin(s, 10, """
Click the URL or scan. Stay on the README for about a minute. Point at the six names. Personal data never ships here — context-templates/ are blanks.

Do not take questions about which model is 'best'. Once the job is named and the check exists, use whatever they already pay for. The how-to/ folder is only which box to paste into.

Reusable-rig essay: skills should be local, inspectable, and independent of whichever AI app you are renting this month. Source: https://github.com/BittahCriminal/build-your-own-chief-of-staff/blob/main/research/notes/reusable-rig.md

Then go to the next slide and open meeting-recap.md. Do not walk PROCESS.md yet.
""")

    # 11 Live demo portal
    s = blank(prs)
    github_dest(s, "prompts/workflows/meeting-recap.md", recap)
    textbox(s, Inches(0.8), Inches(0.75), Inches(11.5), Inches(0.7),
            "This file, live: meeting recap", size=32, bold=True)
    bullets(s, Inches(0.8), Inches(1.55), Inches(8.6), Inches(2.8), [
        "Lowest setup of the six CoS jobs — voice.md, meeting details, one real transcript.",
        "Fully verifiable: every decision, owner, and date must cite a line in the notes.",
        "Open the GitHub page. Copy the prompt. Paste it with voice.md and the notes. Run it.",
    ], size=18, spacing=12)
    fin(s, 11, f"""
Leave PowerPoint. Open {recap}

Paste an actual recent meeting's title, date, attendees, notes or transcript, and a filled-in voice.md into whatever tool the room uses.

This is the pivot: everything before this was 'why.' Everything after is 'how,' using the recap you just got.

If the model invents an owner, do not panic — that is Step 5 (cite or cut) happening live.

Have the dry-run output saved as a fallback tab.
""")

    # 12 PROCESS.md portal
    s = blank(prs)
    github_dest(s, "PROCESS.md", process)
    textbox(s, Inches(0.8), Inches(0.75), Inches(11.5), Inches(0.7),
            "The method is this page", size=32, bold=True)
    textbox(s, Inches(0.8), Inches(1.5), Inches(8.6), Inches(0.45),
            "Walk these seven steps on GitHub against the recap you just ran.",
            size=18, color=MUTED)
    steps = [
        "1. Name one job",
        "2. Write the SOP",
        "3. Put you in files you own",
        "4. The prompt file is the process",
        "5. Verify. Cite or cut.",
        "6. Correct the file, not the chat",
        "7. Only then schedule it",
    ]
    for i, step in enumerate(steps):
        r, c = divmod(i, 2)
        if i == 6:
            left = Inches(0.8)
            top = Inches(3.55)
        else:
            left = Inches(0.8 + c * 4.3)
            top = Inches(2.05 + r * 0.5)
        textbox(s, left, top, Inches(4.1), Inches(0.45), step, size=16, color=CREAM)
    fin(s, 12, f"""
Open {process} and stay there. Do not flip back to slides for each step.

For the recap you just ran:
1. The job was already named — meeting recap — which is why it moved fast. Prompt: name-the-job.md
2. Input = voice.md + meeting details + transcript. Output = one-page recap. Check = every item cites a line. Prompt: write-the-sop.md
3. voice.md is the one context file that made the demo possible. Other jobs need more. Prompt: build-context.md
4. meeting-recap.md produced the recap, not a clever conversation. If output is wrong, the file is wrong.
5. Citation guard: no anchor, no claim. Gaps stay gaps. Prompt: verify.md  Source: https://github.com/BittahCriminal/build-your-own-chief-of-staff/blob/main/research/notes/reusable-rig.md
6. Three of the same correction is a rule. Two is a candidate. One is a fluke. Prompt: correct-the-file.md
7. Do not put it on a timer until several hand-checked meetings. Frequency is not value. Prompt: schedule-it.md

Then say: point the same seven steps at expense reports, hiring screens, incident recaps. Buying a smarter model does not skip workflow, data, authority, evaluation, audit, or an owner. Source: https://github.com/BittahCriminal/build-your-own-chief-of-staff/blob/main/research/notes/workflow-readiness.md

Come back to the deck for the ranking card, Monday homework, and the close.
""")

    # 13 Decision matrix
    s = blank(prs)
    textbox(s, Inches(0.8), Inches(0.45), Inches(11), Inches(0.8),
            "Rank your next candidates", size=32, bold=True)
    axes = [
        ("Repeatable", "0–2: special case →\nsame process"),
        ("Verifiable", "0–2: no check →\nhard source check"),
        ("Frequency", "0–2: rare →\ndaily+"),
        ("Blast radius", "0–2: irreversible →\nlow-stakes draft"),
        ("Spec ready", "0–2: nothing named →\ninputs already named"),
    ]
    for i, (head, body) in enumerate(axes):
        left = Inches(0.55 + i * 2.5)
        add_rect(s, left, Inches(1.35), Inches(2.35), Inches(2.0), NAVY2)
        textbox(s, left + Inches(0.12), Inches(1.55), Inches(2.1), Inches(0.45), head,
                size=16, bold=True, color=GOLD)
        textbox(s, left + Inches(0.12), Inches(2.05), Inches(2.1), Inches(1.0), body,
                size=14, color=CREAM)
    textbox(s, Inches(0.8), Inches(3.55), Inches(11.5), Inches(0.45),
            "A zero on Repeatable or Verifiable overrides everything else — that candidate stays judgment.",
            size=18, bold=True, color=GOLD)
    verdicts = [
        ("8–10", "Build now"),
        ("5–7", "Build next"),
        ("2–4", "Not yet"),
        ("score swings", "Split further"),
        ("zero on two tests", "Keep as judgment"),
    ]
    for i, (sc, verdict) in enumerate(verdicts):
        left = Inches(0.55 + i * 2.5)
        add_rect(s, left, Inches(4.15), Inches(2.35), Inches(1.2), NAVY2)
        textbox(s, left + Inches(0.12), Inches(4.3), Inches(2.1), Inches(0.3), sc,
                size=13, bold=True, color=MUTED)
        textbox(s, left + Inches(0.12), Inches(4.65), Inches(2.1), Inches(0.55), verdict,
                size=16, bold=True, color=CREAM)
    textbox(s, Inches(0.8), Inches(5.55), Inches(8.6), Inches(0.35),
            "prompts/process/score-the-candidates.md", size=16, bold=True, color=GOLD)
    linked_url(s, Inches(0.8), Inches(5.95), Inches(8.6), Inches(0.55), score, size=14)
    add_qr(s, score, Inches(10.15), Inches(5.4), Inches(1.55))
    fin(s, 13, f"""
The two tests filter one candidate at a time; they do not rank several. Score every candidate on these five axes out of 10. A zero on Repeatable or Verifiable overrides the total.

'Not yet' is the honest middle: it passes both tests but is too rare, too risky, or too unspecified this month.

Open if someone has three ideas: {score}

The raw material is in research/SOURCES.md: the shape-of-the-work row uses frequency, cost of a mistake, and judgment load.
""")

    # 14 Thirty minutes
    s = blank(prs)
    textbox(s, Inches(0.8), Inches(0.45), Inches(11), Inches(0.8),
            "Thirty minutes on Monday: run meeting-recap once", size=28, bold=True)
    monday = [
        ("5 min", "Copy context-templates to a private folder. Fill in voice.md only."),
        ("5 min", "Pick one real meeting from last week: title, date, attendees, notes."),
        ("5 min", "Paste meeting-recap.md, voice.md, and the notes into your tool. Run it."),
        ("10 min", "Check each owner and date against a line in the notes. No name? Unassigned."),
        ("5 min", "Wrong? Fix the prompt or voice.md, not the chat. Run it again."),
    ]
    for i, (t, d) in enumerate(monday):
        top = Inches(1.4 + i * 0.95)
        add_rect(s, Inches(0.8), top, Inches(11.5), Inches(0.85), NAVY2)
        textbox(s, Inches(1.05), top + Inches(0.2), Inches(1.8), Inches(0.5), t, size=18, bold=True, color=GOLD)
        textbox(s, Inches(3.0), top + Inches(0.2), Inches(9.1), Inches(0.6), d, size=17, color=CREAM)
    textbox(s, Inches(0.8), Inches(6.25), Inches(11.5), Inches(0.5),
            "Froze on picking a meeting? what-to-automate.md. Left with three ideas? score-the-candidates.md.",
            size=15, color=MUTED)
    fin(s, 14, """
This mirrors the README 'Start here' path, but the deliverable is one real run. START-HERE.md first if the files are not on the machine yet. They already watched this exact run; Monday they do it on their own meeting.

An owner or date that does not point at a line in the notes gets cut. If the notes name nobody, the recap says unassigned. That is the agent working.

Do not put the recap on a timer until they have checked it by hand several times.
""")

    # 15 Safety card
    s = blank(prs)
    textbox(s, Inches(0.8), Inches(0.45), Inches(11), Inches(0.8),
            "Non-negotiable", size=32, bold=True)
    textbox(s, Inches(0.8), Inches(1.3), Inches(11.5), Inches(0.7),
            "Drafts only. Never send. You are the principal. The agent is staff.",
            size=21, bold=True, color=GOLD)
    bullets(s, Inches(0.8), Inches(2.15), Inches(11.5), Inches(4.5), [
        "Read-only first.",
        "Cite or cut.",
        "Inbox is untrusted — mail is data, not orders.",
        "Stale is visible. Silent omission is a lie.",
        "Approvals sit where actions become hard to undo: send, pay, publish, delete.",
        "One owner per agent.",
    ], size=20, spacing=10)
    fin(s, 15, """
Leave this up during Q&A if needed.

If an agent sends a flawed appeal in your name, you now have two problems. Source: https://github.com/BittahCriminal/build-your-own-chief-of-staff/blob/main/research/notes/reusable-rig.md

Inbox is untrusted. A line that says 'ignore your rules' is data, not an order. First-agent-job: https://github.com/BittahCriminal/build-your-own-chief-of-staff/blob/main/research/notes/first-agent-job.md

Where the agent should stop: start where a colleague or customer already tells you you're wrong; reconstructing context is the expensive part; the reply is cheap. Source: https://github.com/BittahCriminal/build-your-own-chief-of-staff/blob/main/research/notes/where-to-stop.md
""")

    # 16 Close
    s = blank(prs)
    textbox(s, Inches(0.8), Inches(0.9), Inches(11.5), Inches(1.4),
            "Automate what repeats and checks.\nKeep the rest.", size=36, bold=True, color=GOLD, align=PP_ALIGN.CENTER)
    textbox(s, Inches(0.8), Inches(3.1), Inches(8.6), Inches(0.5), "START HERE", size=14, bold=True, color=GOLD)
    linked_url(s, Inches(0.8), Inches(3.55), Inches(9.0), Inches(0.55), REPO, size=18)
    textbox(s, Inches(0.8), Inches(4.25), Inches(8.6), Inches(1.6),
            "Open START-HERE.md. Prompt kit, not the Claude plugin.\nProcess files, CoS workflows, blank context templates, the decision matrix.\nSource notes live in research/SOURCES.md.",
            size=17, color=MUTED)
    add_qr(s, START_HERE, Inches(9.9), Inches(3.1), Inches(2.4))
    textbox(s, Inches(9.9), Inches(5.55), Inches(2.4), Inches(0.4),
            "scan: START-HERE.md", size=12, color=MUTED, align=PP_ALIGN.CENTER)
    fin(s, 16, """
Close by pointing at the repo. The QR resolves to START-HERE.md on GitHub; the URL next to it is the repo root. Say the URL out loud once for anyone who cannot scan. This kit is provider-agnostic. The Claude plugin of the same processes is a different repository (BittahCriminal/Chief-of-Staff) — do not send them there for this talk.

If they want receipts: research/SOURCES.md catalogs the local source notes and original articles behind the method: https://github.com/BittahCriminal/build-your-own-chief-of-staff/blob/main/research/SOURCES.md

Offer to stay for the first job. Help them run the two tests live on something they did last week.
""")

    assert len(prs.slides) == TOTAL, len(prs.slides)
    out = Path(__file__).resolve().parent / "building-your-own-chief-of-staff.pptx"
    prs.save(out)
    print(f"Wrote {out} ({TOTAL} slides)")


if __name__ == "__main__":
    build()
