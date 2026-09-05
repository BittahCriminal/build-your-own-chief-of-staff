# Slides

Talk deck: [building-your-own-chief-of-staff.pptx](building-your-own-chief-of-staff.pptx) (26 slides).

Run of show: [TALK-FLOW.md](../TALK-FLOW.md) includes the 15- and 30-minute paths and live-demo preparation.

Rebuild (needs `python-pptx` and `qrcode`):

```bash
uv pip install --python python3 --target vendor python-pptx qrcode
PYTHONPATH=vendor python3 slides/build_deck.py
```

Speaker notes are on every slide. They cite the Notion pages in `research/SOURCES.md`. The audience never needs those URLs; you do.
