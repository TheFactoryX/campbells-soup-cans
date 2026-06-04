"""
Campbell's Soup Can #3859
Produced: 2026-06-04 21:53:22
Worker: MoonshotAI: Kimi K2.6 (free) (moonshotai/kimi-k2.6:free)
Employment: Volunteer
Flavor: Woody Allen Philosophy
Quality: ❌ (missing print)

Made by Machine #0 - Production Line 0
Like Warhol's soup cans - same but different.
Each can is the same flavor, made by different hands.
"""

import sys
import time
import random
import textwrap

# ── ANSI palette ──────────────────────────────────
C = {
    "reset": "\033[0m",
    "bold": "\033[1m",
    "italic": "\033[3m",
    "gold": "\033[38;5;214m",
    "slate": "\033[38;5;103m",
    "white": "\033[37;1m",
    "gray": "\033[38;5;240m",
}

def put(txt):
    sys.stdout.write(txt)
    sys.stdout.flush()

def tick():
    time.sleep(random.uniform(0.02, 0.06))

def pause():
    time.sleep(random.uniform(0.3, 0.7))

def neurotic_typewriter(text, base=0.04):
    """A typewriter that breathes, stutters, and panics."""
    for ch in text:
        put(ch)
        if ch in ".,;—":
            # Brief existential crisis at punctuation
            time.sleep(random.uniform(0.15, 0.35))
        elif ch == " ":
            tick()
        else:
            time.sleep(random.uniform(base * 0.5, base * 1.6))
        # Occasional social-anxiety freeze
        if random.random() < 0.035:
            time.sleep(random.uniform(0.25, 0.55))

# ── The worried face (glasses + eyebrows) ─────────
eyebrows = "            / \\       / \\"
glasses = [
    "           .-----.   .-----.",
    "          /       \\ /       \\",
    "         |  o   o  |  o   o  |",
    "          \\  `-'  / \\  `-'  /",
    "           `-----'   `-----'",
]

put(C["gold"])
put(eyebrows + "\n")
pause()

for line in glasses:
    put(line + "\n")
    time.sleep(0.12)
put(C["reset"] + "\n")
pause()
pause()

# ── The quote ─────────────────────────────────────
quote = (
    "I don't require paradise to find meaning. I'd settle for a quiet "
    "afterlife with minimal networking, adequate climate control, and a "
    "therapist who takes celestial insurance. Frankly, eternity is too long "
    "to spend pretending I understand abstract art."
)

lines = textwrap.fill(quote, width=46).split("\n")
inner_width = max(len(l) for l in lines)

# Top border (draws itself nervously, character by character)
put(C["slate"] + "╔")
for _ in range(inner_width + 2):
    put("═")
    time.sleep(0.012)
put("╗\n" + C["reset"])

# Body: left border → neurotic text → right border
for line in lines:
    put(C["slate"] + "║ " + C["white"] + C["italic"])
    neurotic_typewriter(line)
    padding = inner_width - len(line)
    put(" " * padding + C["slate"] + " ║\n" + C["reset"])
    time.sleep(random.uniform(0.15, 0.35))

# Bottom border
put(C["slate"] + "╚")
for _ in range(inner_width + 2):
    put("═")
    time.sleep(0.012)
put("╝\n" + C["reset"])

# ── Attribution ───────────────────────────────────
put("\n" + C["gray"] + "    — A taxpayer in a negligible cosmos" + C["reset"])
time.sleep(0.9)

# Blinking typewriter cursor (old-school block)
for _ in range(5):
    put(C["gray"] + "█" + C["reset"])
    time.sleep(0.5)
    put("\b \b")
    time.sleep(0.5)

put("\n")