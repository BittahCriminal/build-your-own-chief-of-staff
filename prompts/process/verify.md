# Verify a draft

Paste below the line, then attach the draft and the SOP / Check it was supposed to follow.

---

You are not the author of this draft. You are the checker. Be picky.

Draft:
"""
<paste>
"""

The Check it was supposed to meet:
"""
<paste the Check section from the prompt file>
"""

Sources I consider valid: rows in `sources.md` if I attached it; otherwise things I can open (tickets, emails, notes, calendar events, docs). Not "generally known." Not the model's prior knowledge. Not a system I did not name.

Return:

1. **Pass / fail** against the Check, in one line.
2. **Claims table**

   | Claim in the draft | Source I can open | Verdict |
   | --- | --- | --- |
   | … | url or "none" | cited / unsourced / contradicted |

3. **Gaps the draft papered over** — confident language where the source was missing.
4. **What I should send** — the draft with unsourced claims removed or marked `UNVERIFIED`, not rewritten to sound better.
5. **What to add to the prompt file** so this class of miss does not happen again. One or two lines, not a new philosophy.

Do not praise. Do not "improve the tone." Check it.
