# Slides

Talk deck: [building-your-own-chief-of-staff.pptx](building-your-own-chief-of-staff.pptx) (16 slides). The argument is on the slides; after slide 9 you open GitHub for the files.

Run of show: [TALK-FLOW.md](../TALK-FLOW.md) includes the 15- and 30-minute paths, which tabs to pre-open, and live-demo preparation.

Rebuild (needs `python-pptx` and `qrcode`):

```bash
uv pip install --python python3 --target vendor python-pptx qrcode
PYTHONPATH=vendor python3 slides/build_deck.py
```

Speaker notes are on every slide. They cite the Notion pages in `research/SOURCES.md`. The audience never needs those URLs; you do.

Slides 10–13 are portals: each has a clickable GitHub URL and a QR to that page.
