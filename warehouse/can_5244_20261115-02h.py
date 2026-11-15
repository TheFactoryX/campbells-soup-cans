"""
Campbell's Soup Can #5244
Produced: 2026-11-15 02:40:03
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
Woody Allen Quote Generator - Neurotic Wisdom Edition
A single-file Python program with colors, ASCII art, and typewriter animation.
"""

import sys
import time
import random

# ─── ANSI Color Palette ───
class C:
    RST = '\033[0m'
    BOLD = '\033[1m'
    DIM = '\033[2m'
    ITALIC = '\033[3m'
    UNDER = '\033[4m'
    BLINK = '\033[5m'
    
    # Foreground
    BLACK = '\033[30m'
    RED = '\033[31m'
    GREEN = '\033[32m'
    YELLOW = '\033[33m'
    BLUE = '\033[34m'
    MAGENTA = '\033[35m'
    CYAN = '\033[36m'
    WHITE = '\033[37m'
    GRAY = '\033[90m'
    BRIGHT_RED = '\033[91m'
    BRIGHT_GREEN = '\033[92m'
    BRIGHT_YELLOW = '\033[93m'
    BRIGHT_BLUE = '\033[94m'
    BRIGHT_MAGENTA = '\033[95m'
    BRIGHT_CYAN = '\033[96m'
    BRIGHT_WHITE = '\033[97m'
    
    # Background
    BG_BLACK = '\033[40m'
    BG_RED = '\033[41m'
    BG_GREEN = '\033[42m'
    BG_YELLOW = '\033[43m'
    BG_BLUE = '\033[44m'
    BG_MAGENTA = '\033[45m'
    BG_CYAN = '\033[46m'
    BG_WHITE = '\033[47m'

# ─── Woody Allen ASCII Portrait ───
WOODY = r"""
        ╔══════════════════════════════════════╗
        ║     ▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄      ║
        ║   ▄███████████████████████████▄     ║
        ║  ██████████████████████████████    ║
        ║  ███  ██    ██    ██  ██████████    ║
        ║  ███  ██    ██    ██  ██████████    ║
        ║  ███                    ██████████  ║
        ║  ████████████████████████████████   ║
        ║   ▀███████████████████████████▀     ║
        ║       ▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀       ║
        ╚══════════════════════════════════════╝
              │  ┌─────────────┐  │
              │  │  🤷  ‿  🤷  │  │
              │  └─────────────┘  │
              └───────────────────┘
"""

# ─── Original Woody-Style Quote ───
QUOTE = (
    "I took a speed-reading course and read 'War and Peace' "
    "in twenty minutes. It involves Russia."
)

# Alternative quotes (pick one randomly for variety)
QUOTES = [
    "I took a speed-reading course and read 'War and Peace' in twenty minutes. It involves Russia.",
    "My therapist told me I have a preoccupation with death. I told him that's ridiculous — I'm not preoccupied, I'm just... early.",
    "I don't believe in an afterlife, but I'm bringing a change of underwear just in case.",
    "The universe is infinite, which means somewhere there's a version of me who flosses daily. I hate that guy.",
    "I'm not afraid of dying. I just don't want to be there when it happens. Or the waiting room. Or the paperwork.",
    "Life is divided into the horrible and the miserable. The horrible are terminal cases. The miserable is everyone else. I'm both.",
    "I have a metaphysical dilemma: if a tree falls in a forest and no one hears it, does it make a sound? And if it does, can I bill Medicare for the anxiety?",
    "My analyst says I have an Oedipus complex. I told him, 'Doc, at my age, it's more of an Oedipus timeshare.'",
    "I tried to commit suicide by inhaling next to an insurance salesman. It didn't work — he just kept talking.",
    "There is no question that there is an unseen world. The problem is, how far is it from midtown and how late is parking?",
]

# ─── Animation Functions ───
def clear_screen():
    """Clear terminal screen."""
    print('\033[2J\033[H', end='')

def hide_cursor():
    print('\033[?25l', end='')

def show_cursor():
    print('\033[?25h', end='')

def typewriter(text, delay=0.02, color=C.WHITE, prefix=""):
    """Print text with typewriter effect."""
    print(prefix, end='', flush=True)
    for char in text:
        print(f"{color}{char}{C.RST}", end='', flush=True)
        time.sleep(delay + random.uniform(-0.005, 0.005))
    print()

def typewriter_multiline(lines, delay=0.015, color=C.WHITE, prefix=""):
    """Print multiple lines with typewriter effect."""
    for i, line in enumerate(lines):
        typewriter(line, delay, color, prefix if i == 0 else " " * len(prefix))
        time.sleep(0.1)

def fade_in(text, color=C.WHITE, steps=10):
    """Fade in text by gradually increasing brightness."""
    for step in range(steps + 1):
        intensity = step / steps
        # Simulate fade with dim/bold
        style = C.DIM if intensity < 0.5 else (C.BOLD if intensity > 0.8 else "")
        print(f"\r{style}{color}{text}{C.RST}", end='', flush=True)
        time.sleep(0.03)
    print()

def sparkle_text(text, color=C.YELLOW, iterations=3):
    """Add sparkle effect to text."""
    sparkles = ['✦', '✧', '★', '☆', '✨', '⋆']
    for _ in range(iterations):
        decorated = ''.join(
            f"{C.BRIGHT_YELLOW}{random.choice(sparkles)}{C.RST}" if random.random() < 0.1 and c != ' ' else c
            for c in text
        )
        print(f"\r{color}{decorated}{C.RST}", end='', flush=True)
        time.sleep(0.15)
    print(f"\r{color}{text}{C.RST}")

# ─── Box Drawing ───
def draw_box(content_lines, width=70, border_color=C.CYAN, title="", title_color=C.YELLOW):
    """Draw a fancy box around content."""
    horizontal = "═" * (width - 2)
    top = f"{border_color}╔{horizontal}╗{C.RST}"
    bottom = f"{border_color}╚{horizontal}╝{C.RST}"
    
    lines = [top]
    
    if title:
        title_padded = f" {title} "
        pad_left = (width - 2 - len(title_padded)) // 2
        pad_right = width - 2 - len(title_padded) - pad_left
        title_line = f"{border_color}║{C.RST}{' ' * pad_left}{title_color}{C.BOLD}{title_padded}{C.RST}{' ' * pad_right}{border_color}║{C.RST}"
        lines.append(title_line)
        sep = f"{border_color}╠{horizontal}╣{C.RST}"
        lines.append(sep)
    
    for line in content_lines:
        # Calculate visible length (strip ANSI codes for padding calc)
        import re
        visible = re.sub(r'\033\[[0-9;]*m', '', line)
        padding = width - 2 - len(visible)
        lines.append(f"{border_color}║{C.RST} {line}{' ' * padding} {border_color}║{C.RST}")
    
    lines.append(bottom)
    return '\n'.join(lines)

# ─── Main Animation Sequence ───
def main():
    hide_cursor()
    clear_screen()
    
    # Pick a quote
    quote = random.choice(QUOTES)
    
    # ─── Phase 1: Woody appears ───
    print(f"{C.CYAN}{C.BOLD}")
    for line in WOODY.strip().split('\n'):
        print(line)
        time.sleep(0.04)
    print(f"{C.RST}")
    time.sleep(0.5)
    
    # ─── Phase 2: Thought bubble appears ───
    thought_lines = [
        f"{C.GRAY}◉  Let me think about this...{C.RST}",
        f"{C.GRAY}◉  Existence. Mortality. The void.{C.RST}",
        f"{C.GRAY}◉  Also, did I lock the door?{C.RST}",
    ]
    
    for line in thought_lines:
        print(f"    {line}")
        time.sleep(0.3)
    
    time.sleep(0.4)
    
    # ─── Phase 3: The quote box ───
    print()  # spacing
    
    # Split quote into wrapped lines for the box
    words = quote.split()
    wrapped_lines = []
    current_line = ""
    max_width = 58
    
    for word in words:
        test_line = current_line + (" " if current_line else "") + word
        if len(test_line) <= max_width:
            current_line = test_line
        else:
            wrapped_lines.append(current_line)
            current_line = word
    if current_line:
        wrapped_lines.append(current_line)
    
    # Color each line alternating
    colored_lines = []
    for i, line in enumerate(wrapped_lines):
        if i % 2 == 0:
            colored_lines.append(f"{C.BRIGHT_WHITE}{C.ITALIC}{line}{C.RST}")
        else:
            colored_lines.append(f"{C.WHITE}{C.ITALIC}{line}{C.RST}")
    
    box = draw_box(
        colored_lines,
        width=64,
        border_color=C.MAGENTA,
        title=" WOODY'S WISDOM ",
        title_color=C.BRIGHT_YELLOW
    )
    
    # Print box with typewriter effect line by line
    for box_line in box.split('\n'):
        print(box_line)
        time.sleep(0.05)
    
    time.sleep(0.5)
    
    # ─── Phase 4: Sparkle the quote ───
    print()
    print(f"  {C.DIM}— {C.BRIGHT_CYAN}Woody Allen (probably){C.RST}{C.DIM} —{C.RST}")
    time.sleep(0.3)
    
    # ─── Phase 5: Existential footer ───
    footers = [
        f"{C.GRAY}█▓▒░ {C.ITALIC}This quote has been psychoanalyzed and approved{C.RST}{C.GRAY} ░▒▓█{C.RST}",
        f"{C.DIM}░░░ {C.ITALIC}Side effects may include: nausea, dread, sudden urge to visit analyst{C.RST}{C.DIM} ░░░{C.RST}",
        f"{C.GRAY}━━━ {C.BLINK}∃x∃s†∃nc∃ 1s ∆b∑s†━━━{C.RST}",
    ]
    
    for footer in footers:
        print(f"  {footer}")
        time.sleep(0.25)
    
    # ─── Phase 6: Final neurotic sign-off ───
    print()
    signoff = "Anyway... I have to go. My prostate appointment was 20 minutes ago."
    typewriter(signoff, delay=0.025, color=C.BRIGHT_RED, prefix=f"  {C.BOLD}💭 {C.RST}")
    
    print()
    print(f"  {C.DIM}━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━{C.RST}")
    print(f"  {C.GRAY}Press Ctrl+C to exit... or don't. The void doesn't care either way.{C.RST}")
    
    show_cursor()

# ─── Run ───
if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        show_cursor()
        print(f"\n{C.RED}{C.BOLD}Interrupted! {C.RST}{C.ITALIC}Typical. Even my programs have commitment issues.{C.RST}\n")
        sys.exit(0)
    except Exception as e:
        show_cursor()
        print(f"\n{C.RED}Error: {e}{C.RST}\n")
        sys.exit(1)