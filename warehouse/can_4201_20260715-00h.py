"""
Campbell's Soup Can #4201
Produced: 2026-07-15 00:06:49
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
    R = '\033[91m'
    G = '\033[92m'
    Y = '\033[93m'
    B = '\033[94m'
    M = '\033[95m'
    C = '\033[96m'
    W = '\033[97m'
    DIM = '\033[2m'
    BOLD = '\033[1m'
    ITALIC = '\033[3m'
    UNDER = '\033[4m'
    BLINK = '\033[5m'
    REV = '\033[7m'
    X = '\033[0m'
    CLR = '\033[2J\033[H'

# The quote
QUOTE = "I took a speed-reading course and read War and Peace in twenty minutes. It involves Russia."
AUTHOR = "— Woody Allen (probably)"

def typewriter(text, color=C.W, delay=0.03, newline=True):
    for char in text:
        sys.stdout.write(f"{color}{char}{C.X}")
        sys.stdout.flush()
        time.sleep(delay + random.uniform(-0.01, 0.01))
    if newline:
        print()

def glitch_text(text, color=C.C, iterations=3):
    chars = "░▒▓█▄▀▌▐▙▛▜▟▞▚▘▝▗▖"
    for _ in range(iterations):
        glitched = ''.join(random.choice(chars) if random.random() < 0.1 else c for c in text)
        sys.stdout.write(f"\r{color}{glitched}{C.X}")
        sys.stdout.flush()
        time.sleep(0.08)
    sys.stdout.write(f"\r{color}{text}{C.X}\n")

def draw_box(content_lines, width=70, color=C.M, title=""):
    inner_width = width - 4
    top = f"{color}╔{'═' * (width - 2)}╗{C.X}"
    bottom = f"{color}╚{'═' * (width - 2)}╝{C.X}"
    
    print(top)
    if title:
        title_line = f"{color}║ {C.BOLD}{C.Y}{title.center(inner_width)}{C.X}{color} ║{C.X}"
        print(title_line)
        print(f"{color}║{' ' * (width - 2)}║{C.X}")
    
    for line in content_lines:
        padded = line.ljust(inner_width)
        print(f"{color}║ {C.W}{padded}{C.X}{color} ║{C.X}")
    
    print(bottom)

def neurotic_typing():
    thoughts = [
        "Wait, did I lock the door?",
        "Is that a symptom? WebMD says yes.",
        "My therapist says I have a preoccupation with death. She's not wrong.",
        "I'm not paranoid. The universe really IS out to get me.",
        "Should I have ordered the salad? Too late now.",
        "Death is just nature's way of saying 'table for one.'",
    ]
    print(f"\n{C.DIM}{C.C}[internal monologue]{C.X}")
    for thought in thoughts:
        sys.stdout.write(f"  {C.DIM}{C.ITALIC}{thought}{C.X}")
        sys.stdout.flush()
        time.sleep(0.8)
        print(f" {C.DIM}...{C.X}")
        time.sleep(0.3)

def main():
    print(C.CLR)
    
    # ASCII art header
    header = f"""
{C.M}    ▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄
    █  {C.Y}██╗    ██╗ ██████╗ ██████╗ ██████╗ ███████╗██████╗ {C.M}█
    █  {C.Y}██║    ██║██╔═══██╗██╔══██╗██╔══██╗██╔════╝██╔══██╗{C.M} █
    █  {C.Y}██║ █╗ ██║██║   ██║██████╔╝██║  ██║█████╗  ██████╔╝{C.M} █
    █  {C.Y}██║███╗██║██║   ██║██╔══██╗██║  ██║██╔══╝  ██╔══██╗{C.M} █
    █  {C.Y}╚███╔███╔╝╚██████╔╝██║  ██║██████╔╝███████╗██║  ██║{C.M} █
    █  {C.Y} ╚══╝╚══╝  ╚═════╝ ╚═╝  ╚═╝╚═════╝ ╚══════╝╚═╝  ╚═╝{C.M} █
    ▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀
{C.X}"""
    print(header)
    time.sleep(0.5)
    
    # Neurotic internal monologue
    neurotic_typing()
    
    print()
    
    # The quote in a fancy box
    quote_lines = [
        "",
        "  \"I took a speed-reading course",
        "   and read War and Peace in",
        "   twenty minutes. It involves",
        "   Russia.\"",
        "",
    ]
    draw_box(quote_lines, width=64, color=C.M, title=f"{C.BOLD}WOODY ALLEN WISDOM{C.X}")
    
    print()
    
    # Typewriter the attribution
    typewriter(f"  {C.DIM}{C.ITALIC}{AUTHOR}{C.X}", color=C.C, delay=0.05)
    
    print()
    
    # Glitch effect on a follow-up thought
    followup = "  (Also, I'm pretty sure I left the stove on.)"
    glitch_text(followup, color=C.R, iterations=5)
    
    print()
    
    # Final decorative line
    decorative = f"{C.DIM}{C.M}{'─' * 20} {C.Y}∃x (Neurotic(x) ∧ Funny(x) ∧ Existential(x)) {C.M}{'─' * 20}{C.X}"
    print(decorative)
    print()

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print(f"\n{C.R}Interrupted. Just like my therapy sessions.{C.X}")
        sys.exit(0)