"""
Campbell's Soup Can #4360
Produced: 2026-07-28 20:34:26
Worker: NVIDIA: Nemotron 3 Ultra (free) (nvidia/nemotron-3-ultra-550b-a55b:free)
Employment: Volunteer
Flavor: Woody Allen Philosophy
Quality: ✅

Made by Machine #0 - Production Line 0
Like Warhol's soup cans - same but different.
Each can is the same flavor, made by different hands.
"""

#!/usr/bin/env python3
"""
woody_wisdom.py - A neurotic serving of existential dread with a side of bagels.
"""

import sys
import time
import random

# ═══════════════════════════════════════════════════════════════════════════
# ANSI COLOR PALETTE — because life is meaningless, but at least it's colorful
# ═══════════════════════════════════════════════════════════════════════════
class C:
    RST = "\033[0m"
    BLD = "\033[1m"
    DIM = "\033[2m"
    ITL = "\033[3m"
    UL = "\033[4m"
    BLK = "\033[30m"
    RED = "\033[31m"
    GRN = "\033[32m"
    YEL = "\033[33m"
    BLU = "\033[34m"
    MAG = "\033[35m"
    CYN = "\033[36m"
    WHT = "\033[37m"
    BG_BLK = "\033[40m"
    BG_RED = "\033[41m"
    BG_GRN = "\033[42m"
    BG_YEL = "\033[43m"
    BG_BLU = "\033[44m"
    BG_MAG = "\033[45m"
    BG_CYN = "\033[46m"
    BG_WHT = "\033[47m"

# ═══════════════════════════════════════════════════════════════════════════
# THE QUOTE — hand-crafted neurotic perfection
# ═══════════════════════════════════════════════════════════════════════════
QUOTE = (
    "I took a speed-reading course and finished 'War and Peace' in twenty minutes. "
    "It involves Russia."
)

# Alternative quotes (pick one at runtime for variety)
QUOTES = [
    "I took a speed-reading course and finished 'War and Peace' in twenty minutes. It involves Russia.",
    "My therapist says I have a preoccupation with death. I told her that's absurd — "
    "I'm preoccupied with not dying. There's a difference. One is existential, the other is just good planning.",
    "I don't believe in an afterlife, but I'm bringing a change of underwear just in case. "
    "My mother always said: 'Woody, clean underwear — you never know when you'll be hit by a bus "
    "and the paramedics will judge your laundry habits.'",
    "The universe is indifferent. My landlord is hostile. My analyst is expensive. "
    "But at least the bagel place on 72nd knows my order by heart. That's something. "
    "That's... not nothing. That's sesame.",
    "I tried to commit suicide by inhaling next to an insurance salesman. "
    "Didn't work. He just kept talking about term life. I'm still here. "
    "He's still talking. Who won? Not me. My premiums went up.",
    "Life is divided into the horrible and the miserable. The horrible are terminal illness, "
    "natural disasters, and people who clap when the plane lands. The miserable is everyone else. "
    "I'm miserable. You're probably miserable. Let's get coffee and compare symptoms.",
]

# ═══════════════════════════════════════════════════════════════════════════
# ASCII ART — because words alone can't capture the absurdity
# ═══════════════════════════════════════════════════════════════════════════
WOODY_SILHOUETTE = r"""
        .--.
       /    \
      |  @@  |   <-- glasses, obviously
      |  \/  |
       \____/
        ||||
       _||||_
      (______)
"""

NEURON_FRAME = r"""
    ╔════════════════════════════════════════════════════════════════════╗
    ║  ▓▓▓  NEURAL PATHWAY: EXISTENTIAL RUMINATION v3.14  ▓▓▓          ║
    ║  ░░░  STATUS: OVERTHINKING... ████████████░░░░ 92%                ║
    ║  ░░░  ANXIETY LEVEL: "WHY DID I SAY THAT IN 1997?"               ║
    ╚════════════════════════════════════════════════════════════════════╝
"""

BAGEL = r"""
      .--.
    /      \
   |  @@@@  |   <-- everything bagel, extra schmear
   | @    @ |
    \      /
      '--'
"""

# ═══════════════════════════════════════════════════════════════════════════
# UTILITY FUNCTIONS — tiny helpers for our tiny existence
# ═══════════════════════════════════════════════════════════════════════════
def typewriter(text: str, delay: float = 0.015, color: str = C.WHT, end: str = "") -> None:
    """Print text with a delightfully anxious typing effect."""
    for char in text:
        sys.stdout.write(f"{color}{char}{C.RST}")
        sys.stdout.flush()
        time.sleep(delay + random.uniform(-0.005, 0.008))
    if end:
        sys.stdout.write(end)
        sys.stdout.flush()

def blink(text: str, times: int = 3, interval: float = 0.4) -> None:
    """Make text blink — like a nervous tic."""
    for _ in range(times):
        sys.stdout.write(f"\r{C.BLD}{C.YEL}{text}{C.RST}")
        sys.stdout.flush()
        time.sleep(interval)
        sys.stdout.write(f"\r{' ' * len(text)}")
        sys.stdout.flush()
        time.sleep(interval)
    sys.stdout.write(f"\r{C.BLD}{C.YEL}{text}{C.RST}")
    sys.stdout.flush()

def clear_line() -> None:
    sys.stdout.write("\r\033[K")
    sys.stdout.flush()

# ═══════════════════════════════════════════════════════════════════════════
# MAIN PERFORMANCE — the show must go on (reluctantly)
# ═══════════════════════════════════════════════════════════════════════════
def main() -> None:
    # Hide cursor for clean animation
    sys.stdout.write("\033[?25l")
    sys.stdout.flush()

    try:
        # ─── Opening: Neural pathway diagnostic ───
        print(f"\n{C.CYN}{NEURON_FRAME}{C.RST}")
        time.sleep(0.6)

        # ─── Woody appears ───
        print(f"{C.MAG}{WOODY_SILHOUETTE}{C.RST}")
        time.sleep(0.4)

        # ─── Introductory muttering ───
        mutters = [
            "Okay, okay... let me think. No, thinking causes anxiety.",
            "Should I say it? What if it's wrong? What if it's *right*?",
            "My analyst says vocalize. My lawyer says don't. I'm listening to my analyst. "
            "He's cheaper. Wait, no, he's not. Nothing's cheaper.",
        ]
        typewriter(f"{C.DIM}{C.ITL}{random.choice(mutters)}{C.RST}\n", delay=0.01)
        time.sleep(0.5)

        # ─── The bagel arrives (comfort object) ───
        print(f"\n{C.YEL}{BAGEL}{C.RST}")
        typewriter(f"{C.DIM}Right. Bagel. Center yourself. The universe is expanding. "
                   f"The bagel is not. That's comforting.{C.RST}\n", delay=0.012)
        time.sleep(0.6)

        # ─── Dramatic pause ───
        typewriter(f"\n{C.BLD}{C.BLU}━━━ A MOMENT OF CLARITY (OR INDIGESTION) ━━━{C.RST}\n\n", delay=0.008)

        # ─── THE QUOTE — typed with neurotic precision ───
        chosen_quote = random.choice(QUOTES)

        # Split into "breaths" for dramatic effect
        sentences = chosen_quote.replace("? ", "?|").replace(". ", ".|").split("|")

        for i, sentence in enumerate(sentences):
            sentence = sentence.strip()
            if not sentence:
                continue

            # Color cycling for each sentence
            colors = [C.WHT, C.CYN, C.GRN, C.YEL, C.MAG, C.BLU]
            color = colors[i % len(colors)]

            typewriter(f"  {C.BLD}{color}»{C.RST} ", delay=0.0)
            typewriter(sentence + " ", delay=0.018, color=color)
            print()  # newline after each sentence
            time.sleep(0.35 + random.uniform(-0.1, 0.2))

        # ─── Post-quote spiral ───
        time.sleep(0.5)
        print()
        spirals = [
            "Anyway. That's my thought. Or was it? Did I think it, or did I just "
            "remember thinking it? Memory is unreliable. So is my digestion.",
            "I should write this down. Where's my notebook? Oh right — I forgot "
            "to buy one because I was worried the paper would judge me.",
            "Look, the quote speaks for itself. Which is good, because if I speak "
            "for it, I'll just contradict myself. I do that. Often. In real time.",
        ]
        typewriter(f"{C.DIM}{C.ITL}{random.choice(spirals)}{C.RST}\n", delay=0.012)

        # ─── Final sign-off ───
        time.sleep(0.4)
        print(f"\n{C.DIM}{C.BLU}═══════════════════════════════════════════════════════════════{C.RST}")
        signoffs = [
            "— Woody (probably) (definitely) (don't quote me on that)",
            "— A neurotic mess wrapped in a riddle wrapped in a trench coat",
            "— Someone who paid $300/hour to learn he's 'conflicted'",
        ]
        typewriter(f"{C.DIM}{C.ITL}  {random.choice(signoffs)}{C.RST}\n", delay=0.015)
        print(f"{C.DIM}{C.BLU}═══════════════════════════════════════════════════════════════{C.RST}\n")

        # ─── Tiny easter egg: blinking cursor of doom ───
        time.sleep(0.3)
        typewriter(f"{C.DIM}▊ ", delay=0.0, color=C.RED)
        blink("EXISTENTIAL PROCESS COMPLETE", times=2)
        print(f"{C.RST}\n")

    finally:
        # Restore cursor
        sys.stdout.write("\033[?25h")
        sys.stdout.flush()

# ═══════════════════════════════════════════════════════════════════════════
# ENTRY POINT — because every script needs a beginning, even if the universe
#               doesn't believe in endings (or beginnings, really)
# ═══════════════════════════════════════════════════════════════════════════
if __name__ == "__main__":
    # Seed randomness with current time — chaos is the only constant
    random.seed(time.time_ns())
    main()