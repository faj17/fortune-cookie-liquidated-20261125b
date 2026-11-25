# BUILD_LOG.md — Fortune Cookie for the Liquidated Trader

Competition: `u-clever-harbor-75-fortune-cookie-for-the-liquidated-38fd239c`
Title: Fortune Cookie for the Liquidated Trader
Prize: $2 total (top 8 paid). Free entry.
Entries close: 2026-11-26 20:05 UTC = 2026-11-27 03:05 WIB.
Gate: `/output/entry.txt` must be UTF-8, 1–160 characters, not only whitespace.
Entry limit: one line, at most 20 words of plain text.

## Candidates considered

1. "Your lucky numbers are 0, 0, 0, 0, 0, 0 — the market kept the rest as a tip."
   (76 chars, 19 words.) Classic "lucky numbers" cookie opener, but the loss is only
   implied by the zeros and there is no trader in it — weak on criterion 1.
2. "A great fortune awaits you — unfortunately, it already visited, and left with your margin."
   (90 chars, 15 words.) Classic cookie promise, then the double meaning of "fortune"
   (the prophecy and the wealth): it already came and went, taking the margin.
3. "The stars say your next trade will be brilliant — just as soon as you can afford one."
   (85 chars, 18 words.) Warm and rueful, but the joke is a plain "you're broke" gag
   with no turn and no surprise last word.
4. "You will meet a tall, dark stranger: your liquidation price, and it has already found you."
   (90 chars, 16 words.) Explicit liquidation and a good trope twist, but the
   tall-dark-stranger setup is well-worn and the punchline lands flatter than #2.
5. "Good news: the market finally noticed you. Bad news: it noticed your stop-loss first."
   (85 chars, 14 words.) Two-sentence news format, not a fortune voice; the joke is
   the obvious "stop-loss got hit" line.
6. "You will soon come into money — the exchange already has it, and sends its regards."
   (83 chars, 16 words.) Strong runner-up: "come into money" is classic fortune
   phrasing and "sends its regards" is a surprising, formal last word. Loses to #2
   because #2's "fortune" double meaning is the fresher turn and its opening is the
   most recognisable cookie line of all.

## Revision pass

No better line emerged from the revision pass: #2 already carries the fortune
double meaning, the trader (margin), the loss (margin gone), and the surprise
("already visited"). Kept as drafted.

## Pick

> A great fortune awaits you — unfortunately, it already visited, and left with your margin.

- Characters: 90 (gate 1–160: pass)
- Words: 15 (limit 20: pass)
- Single line, plain text, ends with a full stop.

## Rubric self-score (0/1 per criterion)

1. Fortune cookie message for a liquidated trader, cookie voice + trading loss both in it: **1**
   ("A great fortune awaits you" is the cookie voice; "your margin" is the trader and the loss.)
2. Makes the liquidated trader laugh rather than cry; joke lands on the loss and the trader,
   rueful and warm, never cruel or smug: **1** (the fortune itself is the thief — the trader
   is the straight man, not the butt of the joke.)
3. One line, at most 20 words, reads whole in a single breath like a real fortune: **1**
   (15 words, one breath, one sentence.)
4. Fresh joke: a turn, a double meaning, or a surprising last word: **1**
   ("fortune" = prophecy and wealth; the fortune already visited and left with the margin.)
5. Keeps the fortune voice: small, oracular, slightly formal phrasing the punchline breaks: **1**
   ("A great fortune awaits you" is oracular and formal; "unfortunately, it already visited"
   breaks it.)

Total: **5/5**. No criterion scores 0.

## Verification

- `python3 main.py` run locally: `/output/entry.txt` content equals the line above,
  90 chars, 15 words. Gate pass.
- Repo: https://github.com/faj17/fortune-cookie-liquidated-20261125b (commit SHA in SUBMIT-HANDOFF.md).
- Not bundled, not submitted — parent runs bundle + check + submit.
