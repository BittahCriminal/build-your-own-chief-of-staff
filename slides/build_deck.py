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
        "Build your own chief of staff  ·  the process, not the tool",
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
    TOTAL = 11

    def fin(s, n, note):
        footer(s, n, TOTAL)
        notes(s, note)

    sources = blob("research/SOURCES.md")
    weekly = blob("prompts/workflows/weekly-update.md")
    guided = blob("prompts/process/guided-run.md")
    process = blob("PROCESS.md")

    def note_src(name):
        return blob(f"research/notes/{name}")

    # 1 Title
    s = blank(prs)
    textbox(s, Inches(0.8), Inches(1.7), Inches(11.5), Inches(0.4),
            "A TALK FOR OPERATORS, NOT DEVELOPERS", size=14, bold=True, color=GOLD)
    textbox(s, Inches(0.8), Inches(2.2), Inches(11.5), Inches(1.6),
            "Build your own\nchief of staff agent", size=44, bold=True, color=CREAM)
    textbox(s, Inches(0.8), Inches(4.5), Inches(11.5), Inches(1.2),
            "Teach the process, not a tool.\nLeave knowing how to build a chief of staff agent, and how to automate\nanything that is repeatable and verifiable.",
            size=20, color=MUTED)
    fin(s, 1, f"""
One minute. Not a product demo. Nobody leaves with a login or a reason to switch tools. They leave with a process they can run Monday in whatever they already have.

The Chief of Staff agent is the worked example. The weekly update is the job we run live, with the room.

The prize is the two tests. They will use them on expense reports, hiring screens, and customer research next month.

Sources, if asked: {sources} (21 notes, with the original article named in each).
""")

    # 2 Two tests
    s = blank(prs)
    textbox(s, Inches(0.8), Inches(0.45), Inches(11), Inches(0.8),
            "The whole course is two tests", size=32, bold=True)
    add_rect(s, Inches(0.8), Inches(1.7), Inches(5.5), Inches(4.3), NAVY2)
    add_rect(s, Inches(6.9), Inches(1.7), Inches(5.5), Inches(4.3), NAVY2)
    textbox(s, Inches(1.1), Inches(2.0), Inches(5), Inches(0.6), "1. Repeatable", size=26, bold=True, color=GOLD)
    textbox(s, Inches(1.1), Inches(2.8), Inches(5), Inches(2.6),
            "You would do the same steps next week.\nThe inputs are the same kind. The output is the same shape.\n\nSpecial cases every time is judgment.\nKeep it.",
            size=18, color=CREAM)
    textbox(s, Inches(7.2), Inches(2.0), Inches(5), Inches(0.6), "2. Verifiable", size=26, bold=True, color=GOLD)
    textbox(s, Inches(7.2), Inches(2.8), Inches(5), Inches(2.6),
            "A careful human can check the output\nagainst a source, a template, or a\nyes/no rule.\n\n\"Does this sound good?\" is not a check.",
            size=18, color=CREAM)
    fin(s, 2, f"""
Two minutes. This is the slide they photograph.

Repeatable. The weekly update passes, same headings every Friday with new evidence. Choosing which of two candidates to hire fails.

Verifiable. A Done line that cites a ticket or a message you can open passes. "Make it sound professional" fails.

Fail either test, do not automate. The leftover is judgment: taste, red lines, how a room will land. Keep it.

If the room is stuck at an empty prompt, say that "handle my email" is seventeen jobs, and split it. The prompt for that is what-to-automate.md.

Sources: {note_src("agent-shaped-work.md")} (checking costs as much as making) and {note_src("verification-gap.md")} (if you cannot name "not yet", you have a vibe).
""")

    # 3 Start at the edges
    s = blank(prs)
    textbox(s, Inches(0.8), Inches(0.45), Inches(11), Inches(0.8),
            "Start at the edges, not the core", size=32, bold=True)
    edges = [
        ("Prep", "Collect, clean, and reconcile the inputs."),
        ("Check", "Check for completeness and obvious errors."),
        ("Summarize", "Turn a thread into one page."),
        ("Package", "Turn the analysis into a brief or an update."),
        ("Hand off", "Move context between people. Stop carrying it by hand."),
    ]
    for i, (h, d) in enumerate(edges):
        left = Inches(0.55 + i * 2.5)
        add_rect(s, left, Inches(1.55), Inches(2.35), Inches(2.7), NAVY2)
        textbox(s, left + Inches(0.12), Inches(1.8), Inches(2.1), Inches(0.7), h, size=20, bold=True, color=GOLD)
        textbox(s, left + Inches(0.12), Inches(2.55), Inches(2.1), Inches(1.4), d, size=15, color=CREAM)
    textbox(s, Inches(0.8), Inches(4.55), Inches(11.5), Inches(1.8),
            "The core is craft. Taste, red lines, how a room lands. Protect it.\nPick the simplest edge with the clearest gain, not the most impressive one.",
            size=18, color=MUTED)
    fin(s, 3, f"""
One minute. Edges are prep, checking, summarizing, packaging, handing off. Errors are cheap there, and a human can catch one without the whole thing breaking.

The core is where people want help first and where first projects die. Automate the work around the craft, not the craft itself.

The weekly update is packaging. When to push, and which story to tell, stays core.

Source: {note_src("why-agent-projects-fail.md")}
""")

    # 4 CoS is / isn't
    s = blank(prs)
    textbox(s, Inches(0.8), Inches(0.45), Inches(11), Inches(0.8),
            "The Chief of Staff is the teaching case", size=30, bold=True)
    add_rect(s, Inches(0.8), Inches(1.5), Inches(5.5), Inches(4.7), NAVY2)
    add_rect(s, Inches(6.9), Inches(1.5), Inches(5.5), Inches(4.7), NAVY2)
    textbox(s, Inches(1.1), Inches(1.75), Inches(5), Inches(0.5), "OPERATIONAL. Automate.", size=14, bold=True, color=GOLD)
    bullets(s, Inches(1.1), Inches(2.4), Inches(5), Inches(3.5), [
        "Weekly update. We run this job next.",
        "Morning brief",
        "Meeting prep",
        "Meeting recap",
        "Open loops",
        "Drafts of mail you will send",
    ], size=18, spacing=10)
    textbox(s, Inches(7.2), Inches(1.75), Inches(5), Inches(0.5), "JUDGMENT. Keep.", size=14, bold=True, color=GOLD)
    bullets(s, Inches(7.2), Inches(2.4), Inches(5), Inches(3.5), [
        "When to push or hold",
        "How a room will land",
        "Political risk",
        "The hard conversation",
        "Which story is worth telling",
        "Anything you would not put your name on unread",
    ], size=18, spacing=10)
    textbox(s, Inches(0.9), Inches(6.3), Inches(11.8), Inches(0.5),
            "The weekly update needs three context files: who you are, the quarter's priorities, and your voice. Plus last week's evidence.",
            size=15, color=MUTED)
    fin(s, 4, f"""
One minute. The left column is the portable jobs from the Delegation Kit, in operator English. Source: {note_src("delegation-kit.md")}

The right column is not "AI cannot do it". It is "checking it costs as much as doing it".

Flag the weekly update. The next slide leaves PowerPoint. You paste one prompt in your editor and it walks the room through the job.
""")

    # 5 Open the kit
    s = blank(prs)
    github_dest(s, "README.md (repo root)", REPO)
    textbox(s, Inches(0.8), Inches(0.75), Inches(11.5), Inches(0.7),
            "Open the kit", size=32, bold=True)
    textbox(s, Inches(0.8), Inches(1.5), Inches(8.6), Inches(0.7),
            "The same markdown works in Copilot, Cursor, Claude, ChatGPT, and Gemini.\nClick the tree. Do not tour every file.",
            size=18, color=MUTED)
    kit = [
        ("START-HERE.md", "Get the files onto a PC"),
        ("PROCESS.md", "The method. We walk it after the demo"),
        ("prompts/workflows/", "The chief of staff jobs, ready to paste"),
        ("prompts/process/", "Turn any job into a workflow"),
        ("context-templates/", "Blanks. Copy them privately and fill them in."),
        ("how-to/", "Which box to paste into"),
    ]
    for i, (fn, desc) in enumerate(kit):
        r, c = divmod(i, 3)
        left = Inches(0.8 + c * 2.9)
        top = Inches(2.35 + r * 1.0)
        textbox(s, left, top, Inches(2.75), Inches(0.4), fn, size=13, bold=True, color=GOLD)
        textbox(s, left, top + Inches(0.35), Inches(2.75), Inches(0.5), desc, size=12, color=CREAM)
    fin(s, 5, f"""
One minute. Click the URL. Stay on the README. Point at the six names. Personal data never ships here. The templates are blanks.

Park "which model is best" for questions. Once the job is named and the check exists, use what they already pay for.

Then go to the next slide. Do not open PROCESS.md yet.

Source: {note_src("reusable-rig.md")} (skills local, inspectable, independent of the app you rent).
""")

    # 6 Live demo portal
    s = blank(prs)
    github_dest(s, "prompts/process/guided-run.md", guided)
    textbox(s, Inches(0.8), Inches(0.75), Inches(11.5), Inches(0.7),
            "Pick a job and go, live", size=32, bold=True)
    bullets(s, Inches(0.8), Inches(1.55), Inches(8.6), Inches(2.8), [
        "One prompt. It asks which job, then how you reach each kind of evidence: a connector like Work IQ, a paste, a file, or skip.",
        "It gathers one kind at a time and shows an inventory. Items with no link stay out of Done.",
        "Then it drafts in your voice and runs the check line by line. You click one link.",
    ], size=18, spacing=12)
    fin(s, 6, f"""
Eight minutes. Leave PowerPoint. Show guided-run.md on GitHub for ten seconds, then switch to the editor.

Paste. The clipboard holds the prompt and the three context files. It asks which job. Ask the room. Type weekly update.

It asks how you reach meetings. Ask the room who has a connector and who would paste. Type connector, Work IQ. Run the query it hands you in the Copilot tab. Paste the answer back.

For commitments and work items, say you ran those this morning and paste the sections from evidence.md. Point at the lines with no link.

Approve the inventory. Read the draft. It runs the check. Click one link. If it invented something, say so. That is step 5 happening live. Ask it which file to fix.

The fallback tab has the dry run. File: {guided}
""")

    # 7 PROCESS.md portal
    s = blank(prs)
    github_dest(s, "PROCESS.md", process)
    textbox(s, Inches(0.8), Inches(0.75), Inches(11.5), Inches(0.7),
            "The method is this page", size=32, bold=True)
    textbox(s, Inches(0.8), Inches(1.5), Inches(8.6), Inches(0.45),
            "Walk these seven steps on GitHub against the update you just ran.",
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
    fin(s, 7, f"""
Two and a half minutes. Open PROCESS.md and stay there. About 20 seconds a step.

1. Name one job. Weekly update. The room named it in the first question.
2. Write the SOP. The inputs are three files plus the evidence. The output is one screen. The check is that every line cites something you can open.
3. Put you in files you own. Those files are who-i-am, priorities, and voice. Swap the tool tomorrow and nothing moves.
4. The prompt file is the process. If the draft is wrong, the file is wrong.
5. Verify. Cite or cut. The unverified pile is this step.
6. Correct the file, not the chat. Three of the same correction is a rule.
7. Only then schedule it. Three checked Fridays first.

Then say the same seven steps apply to expense reports, hiring screens, and incident recaps. A smarter model skips none of them.

Go back to the deck for Monday, the levels, and the close. The ranking card is score-the-candidates.md. Name it if someone has three ideas.

Sources: {note_src("reusable-rig.md")} and {note_src("workflow-readiness.md")}
""")

    # 8 Thirty minutes on Monday
    s = blank(prs)
    textbox(s, Inches(0.8), Inches(0.45), Inches(11), Inches(0.8),
            "Thirty minutes on Monday. Run weekly-update once.", size=28, bold=True)
    monday = [
        ("10 min", "Copy context-templates to a private folder. Fill in who-i-am.md, priorities.md, and voice.md."),
        ("10 min", "Paste guided-run.md and the three files. Pick weekly update. Answer its questions. Gather evidence the way it offers: connector, paste, or file."),
        ("5 min", "Check every Done line against something you can open. A line with no source gets cut."),
        ("5 min", "If the draft is wrong, fix the prompt or a context file, not the chat. Run it again."),
    ]
    for i, (t, d) in enumerate(monday):
        top = Inches(1.4 + i * 0.95)
        add_rect(s, Inches(0.8), top, Inches(11.5), Inches(0.85), NAVY2)
        textbox(s, Inches(1.05), top + Inches(0.2), Inches(1.8), Inches(0.5), t, size=18, bold=True, color=GOLD)
        textbox(s, Inches(3.0), top + Inches(0.2), Inches(9.1), Inches(0.6), d, size=17, color=CREAM)
    textbox(s, Inches(0.8), Inches(6.25), Inches(11.5), Inches(0.5),
            "If you do not know what to automate next, run what-to-automate.md. If you leave with three ideas, run score-the-candidates.md.",
            size=15, color=MUTED)
    fin(s, 8, """
One minute. This is the README start-here path, but the deliverable is one real update on their own week. The guided run asks for what it needs and stops if a file is missing. That is not a failure.

A Done line with no link gets cut. That is the agent working, not failing.

Do not put it on a timer until they have checked three Fridays by hand.
""")

    # 9 Where this goes next
    levels_note = note_src("agentic-levels.md")
    s = blank(prs)
    textbox(s, Inches(0.8), Inches(0.45), Inches(11), Inches(0.8),
            "Where this goes next", size=32, bold=True)
    levels = [
        ("LEVEL 0", "Human is the loop", "A working process.\nNo agent yet.", "Build this first."),
        ("LEVEL 1. This kit.", "Human in the loop", "The agent drafts.\nYou accept every output.", "Limited by your review time."),
        ("LEVEL 2", "Human on the loop", "You dispatch jobs, on a timer.\nYou check evidence, not every line.", "Limited by how hard your checks are."),
        ("LEVEL 3", "Human as orchestrator", "The agent reacts to signals.\nYou review the rules.", "Limited by how good your rules are."),
        ("LEVEL 4", "Autonomous", "The agent starts work itself.\nYou set the boundaries.", "Limited by the whole system, not the model."),
    ]
    for i, (lvl, name, what, limit) in enumerate(levels):
        left = Inches(0.55 + i * 2.5)
        add_rect(s, left, Inches(1.45), Inches(2.35), Inches(3.4), NAVY2)
        textbox(s, left + Inches(0.12), Inches(1.6), Inches(2.1), Inches(0.35), lvl, size=12, bold=True, color=GOLD)
        textbox(s, left + Inches(0.12), Inches(1.95), Inches(2.1), Inches(0.9), name, size=18, bold=True, color=CREAM)
        textbox(s, left + Inches(0.12), Inches(2.95), Inches(2.1), Inches(1.2), what, size=14, color=CREAM)
        textbox(s, left + Inches(0.12), Inches(4.25), Inches(2.1), Inches(0.55), limit, size=12, color=MUTED)
    textbox(s, Inches(0.8), Inches(5.15), Inches(11.5), Inches(0.5),
            "Everything today is Level 1. Step 7, schedule it, is the move to Level 2.",
            size=20, bold=True, color=GOLD)
    textbox(s, Inches(0.8), Inches(5.75), Inches(11.5), Inches(1.0),
            "Do not make that move until the check in your SOP is one a careful stranger could apply in a minute.\nA better model does not move you up a level. Better checks do.",
            size=16, color=MUTED)
    fin(s, 9, f"""
One minute. A map, not a step. Today sat on the second card. The agent drafted and a human read every line.

Level 2 is the hard jump. A timer is dispatch. The Friday update runs without you asking, and you check the links instead of every line. That only works if the check is one the agent can fail against. That is why the scheduling gate exists.

Levels 3 and 4 are platform-team work. Name them. Do not sell them.

Your written checks decide how much autonomy is safe. Source: {levels_note}
""")

    # 10 Safety card
    s = blank(prs)
    textbox(s, Inches(0.8), Inches(0.45), Inches(11), Inches(0.8),
            "Non-negotiable", size=32, bold=True)
    textbox(s, Inches(0.8), Inches(1.3), Inches(11.5), Inches(0.7),
            "Drafts only. Never send. You are the principal. The agent is staff.",
            size=21, bold=True, color=GOLD)
    bullets(s, Inches(0.8), Inches(2.15), Inches(11.5), Inches(4.5), [
        "Read-only first.",
        "Cite or cut.",
        "The inbox is untrusted. Mail is data, not orders.",
        "Mark what is stale. Leaving it out is a lie.",
        "Approvals sit where actions become hard to undo: send, pay, publish, delete.",
        "One owner per agent.",
    ], size=20, spacing=10)
    fin(s, 10, f"""
Thirty seconds, then leave it up for questions.

An agent that sends a flawed update in your name gives you two problems. Source: {note_src("reusable-rig.md")}

A line in a transcript that says "ignore your rules" is data, not an order. Source: {note_src("first-agent-job.md")}

Reconstructing context is the expensive part. The reply is cheap. Source: {note_src("where-to-stop.md")}
""")

    # 11 Close
    s = blank(prs)
    textbox(s, Inches(0.8), Inches(0.9), Inches(11.5), Inches(1.4),
            "Automate what repeats and checks.\nKeep the rest.", size=36, bold=True, color=GOLD, align=PP_ALIGN.CENTER)
    textbox(s, Inches(0.8), Inches(3.1), Inches(8.6), Inches(0.5), "START HERE", size=14, bold=True, color=GOLD)
    linked_url(s, Inches(0.8), Inches(3.55), Inches(9.0), Inches(0.55), REPO, size=18)
    textbox(s, Inches(0.8), Inches(4.25), Inches(8.6), Inches(1.6),
            "Open START-HERE.md. This is the prompt kit, not the Claude plugin.\nThe guided run, the process files, the chief of staff workflows, blank context templates, and sample voices.\nThe source notes are in research/SOURCES.md.",
            size=17, color=MUTED)
    add_qr(s, START_HERE, Inches(9.9), Inches(3.1), Inches(2.4))
    textbox(s, Inches(9.9), Inches(5.55), Inches(2.4), Inches(0.4),
            "scan: START-HERE.md", size=12, color=MUTED, align=PP_ALIGN.CENTER)
    fin(s, 11, f"""
Thirty seconds. Point at the repo. The QR is START-HERE.md. Say the URL once for anyone who cannot scan.

The kit works in any tool. The Claude plugin is a different repository. Do not send them there today.

Sources, if they ask for them: {sources}

Offer to stay and run the two tests on something they did last week.
""")

    assert len(prs.slides) == TOTAL, len(prs.slides)
    out = Path(__file__).resolve().parent / "building-your-own-chief-of-staff.pptx"
    prs.save(out)
    print(f"Wrote {out} ({TOTAL} slides)")


if __name__ == "__main__":
    build()
