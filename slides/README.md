# Slides

Talk deck: [building-your-own-chief-of-staff.pptx](building-your-own-chief-of-staff.pptx)

Rebuild (needs `python-pptx`):

```bash
uv pip install --python python3 --target vendor python-pptx
PYTHONPATH=vendor python3 slides/build_deck.py
```

Speaker notes are on every slide. They cite the Notion pages in `research/SOURCES.md`. The audience never needs those URLs; you do.
