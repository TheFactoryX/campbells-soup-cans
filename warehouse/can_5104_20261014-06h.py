"""
Campbell's Soup Can #5104
Produced: 2026-10-14 06:08:50
Worker: NVIDIA: Nemotron 3 Ultra (free) (nvidia/nemotron-3-ultra-550b-a55b:free)
Employment: Volunteer
Flavor: Woody Allen Philosophy
Quality: ✅

Made by Machine #0 - Production Line 0
Like Warhol's soup cans - same but different.
Each can is the same flavor, made by different hands.
"""

import sys
import time
import random

# ANSI color codes
class C:
    RST = '\033[0m'
    BOLD = '\033[1m'
    DIM = '\033[2m'
    ITALIC = '\033[3m'
    UNDER = '\033[4m'
    BLINK = '\033[5m'
    REV = '\033[7m'
    
    # Foreground
    BLK = '\033[30m'
    RED = '\033[31m'
    GRN = '\033[32m'
    YEL = '\033[33m'
    BLU = '\033[34m'
    MAG = '\033[35m'
    CYN = '\033[36m'
    WHT = '\033[37m'
    GRY = '\033[90m'
    LRED = '\033[91m'
    LGRN = '\033[92m'
    LYEL = '\033[93m'
    LBLU = '\033[94m'
    LMAG = '\033[95m'
    LCYN = '\033[96m'
    LWHT = '\033[97m'
    
    # Background
    BBLD = '\033[40m'
    BRED = '\033[41m'
    BGRN = '\033[42m'
    BYEL = '\033[43m'
    BBLU = '\033[44m'
    BMAG = '\033[45m'
    BCYN = '\033[46m'
    BWHT = '\033[47m'

# Woody Allen quotes (original, in his style)
QUOTES = [
    "I took a speed-reading course and read War and Peace in twenty minutes.\nIt involves Russia.",
    "My therapist told me I have a preoccupation with death.\nI told him that's absurd — I'm too busy worrying about whether I left the stove on.",
    "I don't believe in an afterlife, but I'm bringing a change of underwear just in case.",
    "The food at this existential café is terrible.\nAnd such small portions of meaning.",
    "I'm at two with nature.\nWe have a restraining order.",
    "God is silent. My analyst is silent.\nMy mother, however, has opinions on both of them.",
    "I have a hypochondriac's imagination and a philosopher's budget.\nEvery headache is a brain tumor. Every tumor is a metaphor.",
    "The universe is indifferent. My landlord is not.\nHe wants the rent by Tuesday, cosmos be damned.",
    "I tried to find myself once. Got lost in the parking lot of a deli on 86th Street.\nTurns out I was between the pastrami and the existential dread.",
    "Death is just nature's way of telling you to slow down.\nMy doctor says the same thing about my cholesterol."
]

# ASCII art - Woody-ish silhouette
WOODY_ART = [
    "        ╭─────────────╮",
    "        │  (•_•)      │  <-- neurotic gaze",
    "        │  <)   )╯    │  <-- nervous gesture",
    "        │  /   \\      │  <-- existential slouch",
    "        ╰─────────────╯",
    "",
    "     \"I have the metabolism of a hummingbird",
    "      and the attention span of a gnat on espresso.\""
]

def clear_screen():
    print('\033[2J\033[H', end='')

def typewriter(text, delay=0.02, color=C.WHT):
    for char in text:
        print(f"{color}{char}{C.RST}", end='', flush=True)
        time.sleep(delay)
    print()

def fade_in_text(text, color=C.WHT, steps=10):
    for i in range(steps + 1):
        intensity = i / steps
        # Simulate fade by printing with carriage return
        print(f"\r{color}{text}{C.RST}", end='', flush=True)
        time.sleep(0.03)
    print()

def glitch_text(text, color=C.LRED, glitch_chars="!@#$%^&*?", iterations=3):
    for _ in range(iterations):
        glitched = ''.join(
            random.choice(glitch_chars) if random.random() < 0.1 else c
            for c in text
        )
        print(f"\r{color}{glitched}{C.RST}", end='', flush=True)
        time.sleep(0.05)
    print(f"\r{color}{text}{C.RST}")

def draw_box(lines, border_color=C.CYN, title="", title_color=C.YEL):
    max_len = max(len(line) for line in lines)
    width = max_len + 4
    
    # Top border
    top = f"{border_color}╭{'─' * (width - 2)}╮{C.RST}"
    if title:
        title_str = f" {title_color}{title}{C.RST}{border_color} "
        top = f"{border_color}╭{title_str}{'─' * (width - 2 - len(title_str))}╮{C.RST}"
    
    print(top)
    
    for line in lines:
        padding = ' ' * (max_len - len(line))
        print(f"{border_color}│{C.RST} {line}{padding} {border_color}│{C.RST}")
    
    # Bottom border
    print(f"{border_color}╰{'─' * (width - 2)}╯{C.RST}")

def pulse_animation(text, color=C.MAG, cycles=3):
    for _ in range(cycles):
        for intensity in [C.DIM, "", C.BOLD]:
            print(f"\r{color}{intensity}{text}{C.RST}", end='', flush=True)
            time.sleep(0.2)
    print()

def falling_leaves_animation(width=60, height=10, duration=2):
    chars = "⟢⟣♠♡◇♣☯☮☯✦✧"
    cols = [random.randint(0, width-1) for _ in range(15)]
    rows = [random.randint(-height, 0) for _ in range(15)]
    speeds = [random.uniform(0.3, 0.8) for _ in range(15)]
    
    start = time.time()
    while time.time() - start < duration:
        print('\033[H', end='')  # Move to top
        grid = [[' ' for _ in range(width)] for _ in range(height)]
        
        for i in range(15):
            r = int(rows[i])
            c = cols[i]
            if 0 <= r < height and 0 <= c < width:
                grid[r][c] = random.choice(chars)
            rows[i] += speeds[i]
            if rows[i] > height:
                rows[i] = -2
                cols[i] = random.randint(0, width-1)
        
        for row in grid:
            print(f"{C.GRY}{''.join(row)}{C.RST}")
        time.sleep(0.08)
    
    clear_screen()

def main():
    clear_screen()
    
    # Pick a random quote
    quote = random.choice(QUOTES)
    quote_lines = quote.split('\n')
    
    # Opening animation - falling "anxiety" symbols
    print(f"{C.DIM}{C.CYN}Loading neurosis...{C.RST}")
    time.sleep(0.5)
    
    # Draw Woody ASCII
    print(f"\n{C.YEL}{C.BOLD}WOODY ALLEN SIMULATOR v1.0{C.RST}")
    print(f"{C.GRY}{'─' * 50}{C.RST}\n")
    
    for line in WOODY_ART:
        if "⟶" in line or "<--" in line:
            print(f"{C.LMAG}{line}{C.RST}")
        else:
            print(f"{C.CYN}{line}{C.RST}")
        time.sleep(0.15)
    
    print()
    time.sleep(0.5)
    
    # Typewriter the quote
    print(f"{C.BOLD}{C.WHT}Today's Neurotic Epiphany:{C.RST}\n")
    time.sleep(0.3)
    
    draw_box(quote_lines, border_color=C.MAG, title=" PHILOSOPHY ", title_color=C.YEL)
    
    print()
    
    # Typewriter effect for the quote
    for i, line in enumerate(quote_lines):
        prefix = f"{C.LGRN}⟫ {C.RST}" if i == 0 else f"{C.GRY}   {C.RST}"
        typewriter(f"{prefix}{C.WHT}{C.ITALIC}{line}{C.RST}", delay=0.015)
        time.sleep(0.15)
    
    print()
    time.sleep(0.5)
    
    # Pulsing follow-up thought
    followups = [
        "Anyway, I have a colonoscopy Tuesday. The universe can wait.",
        "My therapist says I catastrophize. I told her that's exactly what a tumor would say.",
        "I'd explain it further but I'm busy googling symptoms I don't have.",
        "Pass the Xanax. And the pastrami. Not necessarily in that order."
    ]
    
    followup = random.choice(followups)
    pulse_animation(f"{C.DIM}— {followup}{C.RST}", color=C.CYN, cycles=2)
    
    print(f"\n{C.GRY}{'─' * 50}{C.RST}")
    print(f"{C.DIM}Press Ctrl+C to exit existential crisis...{C.RST}")
    
    # Idle animation
    try:
        spinner = "⠋⠙⠹⠸⠼⠴⠦⠧⠇⠏"
        i = 0
        while True:
            print(f"\r{C.GRY}Overthinking {spinner[i % len(spinner)]}{C.RST}", end='', flush=True)
            time.sleep(0.1)
            i += 1
    except KeyboardInterrupt:
        print(f"\n\n{C.YEL}Fine, I'm leaving. Don't wait up.{C.RST}")
        print(f"{C.DIM}(The universe remains indifferent.){C.RST}\n")

if __name__ == "__main__":
    main()