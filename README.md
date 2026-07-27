# uniqueness

**A 100-point rubric for figuring out what you should be known for, and how far you currently are from being known for it.**

Built on Sheahan's Wall. Packaged as an installable Agent Skill.

---

## The problem this solves

Broad positioning does not fail loudly. It fails quietly.

You post, you pitch, you run ads, you show up. None of it lands, and none of it
stacks. The work is real but the reputation never accumulates, because every
piece points somewhere slightly different.

That is not a marketing execution problem. It is a positioning problem wearing
a marketing costume, and no amount of better copy fixes it.

**Sheahan's Wall** is the invisible barrier between the unknown and the known
in any market. The unknown try to breach it by copying the known, who are
visibly doing many things at once. That is a misread of sequence. The known
earned the right to diversify *after* they broke through.

The breach is always the same mechanism: become known for ONE thing.

This repo does not teach you that. Plenty of people teach that. This repo
**measures it**, so you can tell the difference between "we are narrow" and "we
believe we are narrow."

---

## What this is

An Agent Skill that runs a structured scoring pass on your positioning:

| | |
|---|---|
| **4 components** | Problem in one word. Audience in one phrase. Message in one sentence. One primary revenue stream. |
| **5 dimensions** | Specificity, Ownability, Durability, Service, Evidence. Scored 0 to 5 across all four components. 20 cells, 100 points. |
| **6 hard gates** | Word count, conjunction, competitor substitution, revenue concentration, service framing, and a recall test using five real humans. |
| **1 Dilution Index** | Offers x audiences x revenue streams. A high score sitting on a high index is a paper score. |
| **1 move** | Every run ends with a single narrowing action and an explicit NOT DOING list. |

It is designed to be adversarial. A generous score is a disservice, because the
market does not grade on a curve.

---

## Install

Skills follow the [Agent Skills open standard](https://code.claude.com/docs/en/skills),
so this works in Claude and in any agent that reads `SKILL.md`.

Pick the path that matches how you work.

### 1. Paste it (no install, works anywhere)

Open [`uniqueness/SKILL.md`](uniqueness/SKILL.md), copy the whole file, paste it
into any AI chat, and say *"run this on my business."*

This is the fastest path and it works in ChatGPT, Gemini, Claude, or anything
else. If you are not technical, start here.

### 2. Claude.ai

Download [`uniqueness.skill`](uniqueness.skill) and upload it in your Claude
settings under Skills. Then type `/uniqueness` in any conversation.

Note that on claude.ai, skills are per-user. Each person on your team uploads it
separately.

### 3. Claude Code

```bash
git clone https://github.com/TaylorHonaker/uniqueness-skill.git
cp -r uniqueness-skill/uniqueness ~/.claude/skills/
```

Use `.claude/skills/` inside a project instead if you want it scoped to one repo.
Then run `/uniqueness`.

### 4. Claude API

Upload the bundle through the Skills API. See the
[skills guide](https://platform.claude.com/docs/en/build-with-claude/skills-guide).

Skills do not sync across surfaces. Uploading to one place does not make it
available in the others.

---

## What you get

```
UNIQUENESS CARD — Example Contracting — Q3

PROBLEM   : Overruns
AUDIENCE  : Tribal housing authorities
MESSAGE   : We finish federally funded housing projects on the original schedule.
REVENUE   : HUD-funded multi-unit builds

GATES     : G1 [P]  G2 [P]  G3 [P]  G4 [P]  G5 [P]  G6 [untested]

GRID
                 S    O    D    V    E   | Subtotal
PROBLEM          5    3    5    4    4   |   21/25
AUDIENCE         5    4    4    4    5   |   22/25
MESSAGE          4    4    5    5    3   |   21/25
REVENUE          4    4    4    3    4   |   19/25

WALL SCORE       : 83/100
DILUTION INDEX   : 6
VERDICT          : BREACHING (provisional, G6 untested)

THE CONSTRAINT   : MESSAGE / Evidence (3). The on-schedule claim has no number
                   attached to it in public.
THE ONE MOVE     : Publish the completion-date record for the last 6 projects,
                   with dates. Owner: Ops. Due: 30 days.
NOT DOING        : Residential remodels. General commercial bids outside
                   federally funded work.
THIS WEEK        : Pull contract dates and actual completion dates for the last
                   6 jobs into one sheet.
```

Note what is happening. The score is high not because the company is big, but
because it is narrow. And the prescribed move is not a campaign. It is
publishing a number they already had sitting in a filing cabinet.

---

## Verdict bands

| Score | Verdict | Meaning |
|---|---|---|
| 90 to 100 | **THROUGH** | Known for one thing. You have earned the right to diversify. |
| 75 to 89 | **BREACHING** | One component lags. Narrow it and re-score. |
| 60 to 74 | **SCRATCHING** | Recognizable but not memorable. |
| 40 to 59 | **DILUTED** | Working hard, invisible anyway. |
| 0 to 39 | **INVISIBLE** | A window, not a lens. |

**Anything under 60 blocks new campaigns, launches, and rebrands.** Positioning
that cannot be scored cannot be amplified. Buying reach for a message nobody
will remember is the most expensive mistake in marketing, and it looks like
progress the entire time it is happening.

---

## When to run it

- Marketing activity is up and recognition is flat
- You cannot describe what you do in one sentence without using "and"
- Referrals describe you differently than you describe yourself
- Before any rebrand, launch, website rewrite, or content push
- Quarterly, as maintenance

**Not** weekly. Positioning moves on a slow clock. Frequent re-scoring is
procrastination with a rubric attached.

---

## Credit

This tool sits on other people's work.

- **Sheahan's Wall** is the model of Peter Sheahan, Australian author and speaker, founder of Karrikins Group and author of *Flip*, *Making It Happen*, and *Matter*.
- **The four-part uniqueness exercise**, and the naming of the Wall itself, come from Rory and AJ Vaden at [Brand Builders Group](https://brandbuildersgroup.com/). Vaden saw Sheahan present the model and named it in his honor.
- *"Find your uniqueness and exploit it in the service of others"* is Larry Winget's.
- **The rubric, gates, Dilution Index, and scoring protocol** in this repo are original work by AI Company USA, LLC.

If this is useful to you, go upstream. Read Sheahan. Look up Brand Builders
Group. This repo is a measuring instrument, not a substitute for either.

*A note on spelling: the man is Peter **Sheahan**. The concept is widely
published as "Sheehan's Wall," including by the people who named it. Both point
to the same idea.*

---

## License

[CC BY 4.0](LICENSE). Free to use, copy, adapt, and share, including
commercially, with attribution. Keep the Credit section intact when you share
it.

---

## Who built this

SUMMIT Business Automation / AI Company USA, LLC. Montana.

We build control-system discipline for businesses that are tired of guessing.
This is one of the instruments.

Issues and pull requests welcome. If you run it and the rubric misfires on your
situation, open an issue with the card. Bad scores are better data than good
opinions.
