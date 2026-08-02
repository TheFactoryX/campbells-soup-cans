"""
Campbell's Soup Can #4408
Produced: 2026-08-02 06:46:25
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
Woody Allen's Neurotic Wisdom Generator
A single-file philosophical comedy experience
"""

import sys
import time
import random

# ══════════════════════════════════════════════════════════════════════════════
# ANSI COLOR PALETTE - Neurotic Edition
# ══════════════════════════════════════════════════════════════════════════════

class C:
    RST = '\033[0m'
    BLD = '\033[1m'
    DIM = '\033[2m'
    ITL = '\033[3m'
    UL = '\033[4m'
    BLINK = '\033[5m'
    REV = '\033[7m'
    
    # Woody's palette: anxious neutrals + panic accents
    WOODY_BROWN = '\033[38;5;130m'
    WOODY_TAN = '\033[38;5;180m'
    WOODY_CREAM = '\033[38;5;230m'
    ANXIETY_RED = '\033[38;5;196m'
    EXISTENTIAL_BLUE = '\033[38;5;27m'
    NEUROSIS_YELLOW = '\033[38;5;220m'
    THERAPIST_GREEN = '\033[38;5;35m'
    DEATH_GRAY = '\033[38;5;240m'
    PANIC_PINK = '\033[38;5;213m'
    QUIET_WHITE = '\033[38;5;255m'
    
    # Backgrounds
    BG_DARK = '\033[48;5;233m'
    BG_ANXIETY = '\033[48;5;52m'
    BG_THOUGHT = '\033[48;5;236m'

# ══════════════════════════════════════════════════════════════════════════════
# THE QUOTE - Original Woody Allen Style
# ══════════════════════════════════════════════════════════════════════════════

QUOTE = (
    "I took a course in speed reading and finished "
    "\"War and Peace\" in twenty minutes. "
    "It involves Russia."
)

QUOTE_LINES = [
    "I took a course in speed reading",
    "and finished \"War and Peace\" in twenty minutes.",
    "It involves Russia."
]

# Alternative quotes for variety (but we only print ONE)
ALTERNATIVES = [
    "My therapist says I have a preoccupation with death. "
    "I told him that's ridiculous — I'm preoccupied with not dying. "
    "There's a difference. One is existential dread, the other is just good planning.",
    
    "I don't believe in an afterlife, but just in case, "
    "I'm changing my underwear. You never know who you'll meet "
    "on the other side. My mother, probably. Criticizing the cloud accommodations.",
    
    "The universe is indifferent to our suffering. "
    "Which is fine, really — I'm indifferent to the universe's suffering too. "
    "We have an understanding. It ignores me, I ignore my cholesterol.",
    
    "I asked God for a sign. He sent me a parking ticket. "
    "I said, 'Could you be more specific?' He sent me another one. "
    "I'm pretty sure the message is 'move your car,' but it feels metaphorical.",
    
    "Death is just nature's way of telling you to slow down. "
    "My doctor says the same thing. So does my therapist. "
    "And my accountant. Apparently everyone wants me to slow down. "
    "Even the universe. Especially the universe."
]

# ══════════════════════════════════════════════════════════════════════════════
# ASCII ART - Woody's Glasses & Neurotic Doodles
# ══════════════════════════════════════════════════════════════════════════════

WOODY_FACE = f"""
{C.WOODY_CREAM}       ╭─────────────────╮
      │  {C.WOODY_BROWN}○           ○{C.WOODY_CREAM}  │  ← glasses, prescription: existential
      │  {C.WOODY_BROWN}●           ●{C.WOODY_CREAM}  │     strength: -7.5 diopters of dread
      │      {C.ANXIETY_RED}╭───╮{C.WOODY_CREAM}       │  ← nose, slightly deviated septum
      │     {C.ANXIETY_RED}( •_• ){C.WOODY_CREAM}      │  ← expression: "why did I say that?"
      │      {C.ANXIETY_RED}╰───╯{C.WOODY_CREAM}       │
      ╰─────────────────╯{C.RST}
"""

THOUGHT_BUBBLE = f"""
{C.DIM}         .--.
       / {C.NEUROSIS_YELLOW}◇{C.DIM}   {C.NEUROSIS_YELLOW}◇{C.DIM} \\
      |  {C.EXISTENTIAL_BLUE}▓▓▓{C.DIM}   {C.EXISTENTIAL_BLUE}▓▓▓{C.DIM}  |
      |   {C.PANIC_PINK}░░░{C.DIM}     {C.PANIC_PINK}░░░{C.DIM}  |
       \\      {C.ANXIETY_RED}◆{C.DIM}      /
        `--..--'{C.RST}
"""

PANIC_METER = f"""
{C.DIM}┌────────────────────────────────────┐
│  ANXIETY LEVEL:                      │
│  ████████████████████████████░░░░  94% │
│                                      │
│  [▓▓▓▓▓▓▓▓▓▓] Existential Dread     │
│  [▓▓▓▓▓▓▓▓░░] Fear of Commitment    │
│  [▓▓▓▓▓░░░░░] Hypochondria          │
│  [▓▓▓░░░░░░░] Death Anxiety         │
│  [▓░░░░░░░░░] Regret Over 1987      │
└────────────────────────────────────┘{C.RST}
"""

# ══════════════════════════════════════════════════════════════════════════════
# ANIMATION HELPERS
# ══════════════════════════════════════════════════════════════════════════════

def typewriter(text: str, delay: float = 0.03, color: str = "", end: str = ""):
    """Print text with typewriter effect."""
    for char in text:
        sys.stdout.write(f"{color}{char}{C.RST}")
        sys.stdout.flush()
        time.sleep(delay)
    if end:
        print(end, end="", flush=True)

def typewriter_lines(lines: list, delay: float = 0.025, line_delay: float = 0.4):
    """Print multiple lines with typewriter effect."""
    for i, line in enumerate(lines):
        typewriter(line, delay=delay, color=C.WOODY_CREAM)
        print()
        if i < len(lines) - 1:
            time.sleep(line_delay)

def fade_in(text: str, color: str = "", steps: int = 10, delay: float = 0.05):
    """Fade in text by gradually increasing intensity."""
    for i in range(steps + 1):
        intensity = int(230 + (25 * i / steps))
        # Simulate with dim -> bold progression
        if i < steps // 3:
            prefix = C.DIM
        elif i < 2 * steps // 3:
            prefix = ""
        else:
            prefix = C.BLD
        sys.stdout.write(f"\r{prefix}{color}{text}{C.RST}")
        sys.stdout.flush()
        time.sleep(delay)
    print()

def panic_blink(text: str, times: int = 3):
    """Make text blink with panic colors."""
    for _ in range(times):
        sys.stdout.write(f"\r{C.BLINK}{C.ANXIETY_RED}{C.BG_DARK}{text}{C.RST}")
        sys.stdout.flush()
        time.sleep(0.3)
        sys.stdout.write(f"\r{C.DIM}{text}{C.RST}")
        sys.stdout.flush()
        time.sleep(0.2)
    print()

def clear_screen():
    """Clear terminal screen."""
    sys.stdout.write('\033[2J\033[H')
    sys.stdout.flush()

def hide_cursor():
    sys.stdout.write('\033[?25l')
    sys.stdout.flush()

def show_cursor():
    sys.stdout.write('\033[?25h')
    sys.stdout.flush()

# ══════════════════════════════════════════════════════════════════════════════
# MAIN PRESENTATION
# ══════════════════════════════════════════════════════════════════════════════

def draw_box_top(width: int, color: str = C.WOODY_BROWN) -> str:
    return f"{color}╭{'─' * width}╮{C.RST}"

def draw_box_bottom(width: int, color: str = C.WOODY_BROWN) -> str:
    return f"{color}╰{'─' * width}╯{C.RST}"

def draw_box_middle(text: str, width: int, color: str = C.WOODY_BROWN, 
                    text_color: str = C.WOODY_CREAM, align: str = "center") -> str:
    if align == "center":
        content = text.center(width)
    elif align == "left":
        content = text.ljust(width)
    else:
        content = text.rjust(width)
    return f"{color}│{C.RST}{text_color}{content}{C.RST}{color}│{C.RST}"

def print_quote_box(lines: list):
    """Print the quote in a nice bordered box with Woody styling."""
    max_len = max(len(line) for line in lines)
    box_width = max_len + 4
    
    print()
    print(draw_box_top(box_width, C.WOODY_BROWN))
    print(draw_box_middle("", box_width, C.WOODY_BROWN))
    
    for i, line in enumerate(lines):
        prefix = "❝ " if i == 0 else "   "
        suffix = " ❞" if i == len(lines) - 1 else ""
        print(draw_box_middle(f"{prefix}{line}{suffix}", box_width, 
                              C.WOODY_BROWN, C.QUIET_WHITE))
    
    print(draw_box_middle("", box_width, C.WOODY_BROWN))
    print(draw_box_bottom(box_width, C.WOODY_BROWN))
    print()

def print_attribution():
    """Print the Woody attribution with style."""
    attr_lines = [
        f"{C.ITL}— Woody Allen, probably{C.RST}",
        f"{C.DIM}(delivered while adjusting glasses and checking pulse){C.RST}"
    ]
    for line in attr_lines:
        print(f"                    {line}")
    print()

# ══════════════════════════════════════════════════════════════════════════════
# THE MAIN SHOW
# ══════════════════════════════════════════════════════════════════════════════

def main():
    # Check if terminal supports colors
    if not sys.stdout.isatty():
        # Fallback for non-TTY
        print(QUOTE)
        return
    
    hide_cursor()
    clear_screen()
    
    try:
        # ═══════════════════════════════════════════
        # ACT 1: The Setup - Woody appears
        # ═══════════════════════════════════════════
        
        print(f"{C.WOODY_TAN}")
        print(" " * 20 + "┌─────────────────────────────────────┐")
        print(" " * 20 + "│  WOODY ALLEN'S NEUROTIC WISDOM™     │")
        print(" " * 20 + "│  Est. 1935  •  Anxiety Since Birth  │")
        print(" " * 20 + "└─────────────────────────────────────┘")
        print(f"{C.RST}")
        
        time.sleep(0.5)
        
        # Woody's face slides in
        for frame in WOODY_FACE.split('\n'):
            print(frame)
            time.sleep(0.08)
        
        time.sleep(0.6)
        
        # ═══════════════════════════════════════════
        # ACT 2: The Thought Process
        # ═══════════════════════════════════════════
        
        print(f"\n{C.ITL}{C.EXISTENTIAL_BLUE}  *adjusts glasses nervously*{C.RST}\n")
        time.sleep(0.4)
        
        # Thought bubble appears
        print(THOUGHT_BUBBLE)
        time.sleep(0.5)
        
        # Internal monologue (typewriter)
        thoughts = [
            "Should I say something profound?",
            "No, profound gives me hives.",
            "Maybe just... a joke about mortality.",
            "Death is funny. Right? Right.",
            "Okay. Here goes nothing. Everything. Something."
        ]
        
        for thought in thoughts:
            typewriter(f"  {C.DIM}{C.ITL}{thought}{C.RST}", delay=0.015)
            print()
            time.sleep(0.25)
        
        time.sleep(0.5)
        
        # Panic meter flashes
        print(PANIC_METER)
        time.sleep(0.8)
        
        # ═══════════════════════════════════════════
        # ACT 3: THE QUOTE - The Main Event
        # ═══════════════════════════════════════════
        
        clear_screen()
        
        print(f"{C.WOODY_TAN}")
        print(" " * 15 + "╔═══════════════════════════════════════════════╗")
        print(" " * 15 + "║       TODAY'S NEUROTIC EPIPHANY              ║")
        print(" " * 15 + "╚═══════════════════════════════════════════════╝")
        print(f"{C.RST}\n")
        
        # Dramatic pause
        time.sleep(0.3)
        
        # Print quote with typewriter effect, line by line
        typewriter_lines(QUOTE_LINES, delay=0.03, line_delay=0.5)
        
        time.sleep(0.8)
        
        # ═══════════════════════════════════════════
        # ACT 4: The Aftermath - Reaction
        # ═══════════════════════════════════════════
        
        print()
        reactions = [
            (f"{C.NEUROSIS_YELLOW}  *waits for laughter*", 0.02),
            (f"{C.DIM}  *hears only existential silence*", 0.02),
            (f"{C.ANXIETY_RED}  *checks pulse*", 0.02),
            (f"{C.THERAPIST_GREEN}  *still alive. disappointing.*{C.RST}", 0.02),
        ]
        
        for text, delay in reactions:
            typewriter(text, delay=delay)
            print()
            time.sleep(0.3)
        
        time.sleep(0.5)
        
        # Attribution
        print_attribution()
        
        # ═══════════════════════════════════════════
        # ACT 5: Final Flourish
        # ═══════════════════════════════════════════
        
        # Small animated footer
        footer_frames = [
            f"{C.DIM}  ♦  Press any key to continue therapy  ♦{C.RST}",
            f"{C.NEUROSIS_YELLOW}  ♦  Press any key to continue therapy  ♦{C.RST}",
            f"{C.DIM}  ♦  Press any key to continue therapy  ♦{C.RST}",
            f"{C.PANIC_PINK}  ♦  Session billed to your anxiety  ♦{C.RST}",
        ]
        
        for _ in range(2):
            for frame in footer_frames:
                sys.stdout.write(f"\r{frame}")
                sys.stdout.flush()
                time.sleep(0.4)
        
        print("\n")
        
    finally:
        show_cursor()

# ══════════════════════════════════════════════════════════════════════════════
# ENTRY POINT
# ══════════════════════════════════════════════════════════════════════════════

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        show_cursor()
        print(f"\n\n{C.ANXIETY_RED}*Woody flees the stage* {C.DIM}(stage fright){C.RST}\n")
        sys.exit(0)
    except Exception as e:
        show_cursor()
        print(f"\n{C.ANXIETY_RED}Even the code has anxiety: {e}{C.RST}\n")
        sys.exit(1)