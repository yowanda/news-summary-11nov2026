"""news-summary-01 entry: write the summary of 11 November 2026 world news
to /output/entry.txt (or $MAKEFUN_OUTPUT_DIR/entry.txt outside the grader).
Deterministic: the same bytes on every run. No network. Python 3.13 stdlib only."""

import os

OUT = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")

SUMMARY = '''Wednesday, 11 November 2026 — Three oil tankers caught fire in the Strait of Hormuz after striking naval mines, Iran's military said, as Tehran insisted the strait stays shut until Washington answers its seven conditions for peace talks. The mine claims, carried by Iran's Tasnim agency, have not been independently verified; Britain's maritime agency confirmed only an incident. The war is in its ninth month, with 37 attacks on shipping in October, the most since it began, according to the Washington Institute.

Russia and Ukraine agreed the war's largest prisoner exchange — more than 1,000 each side, within two to three weeks — as two days of US-mediated talks in Abu Dhabi ended without a breakthrough on ending the fighting, Reuters reported. US envoys Jared Kushner and Steve Witkoff travel to Moscow on Thursday to meet Vladimir Putin, then to Dublin to see Volodymyr Zelenskyy.

At the COP31 climate summit in Antalya, UN chief Antonio Guterres warned leaders the climate crisis is "outrunning us" and called it "make or bake time," urging taxes on oil giants, the UN reported. The United States stayed away for a second straight year.

In Washington, the House voted 211-204 to send an impeachment resolution against Defence Secretary Pete Hegseth to committee, effectively killing it. In Gaza, Israeli forces killed at least seven people, including a father and his 13-year-old son, local health officials said. In Congo, Ebola passed 11,000 confirmed cases with 5,387 deaths, government data showed — the second-largest outbreak on record, with no approved vaccine for the Bundibugyo strain. Britain detained a US Army officer on suspicion of spying for Russia, and the US Air Force moved 13 aircraft off RAF Mildenhall after raising its alert over an Iran-linked threat. And Nvidia's board hired a former federal prosecutor to investigate chief executive Jensen Huang's reported relationship with an alleged Chinese spy, after a US senator said he should go.
'''

os.makedirs(OUT, exist_ok=True)
# Guardrail: the gate takes 1-2000 UTF-8 chars, not only white space.
assert 1 <= len(SUMMARY) <= 2000 and SUMMARY.strip(), "summary out of gate limits"
with open(os.path.join(OUT, "entry.txt"), "w", encoding="utf-8") as f:
    f.write(SUMMARY)
