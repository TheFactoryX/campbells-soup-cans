"""
Campbell's Soup Can #5260
Produced: 2026-11-20 03:16:36
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
A single-file philosophical comedy experience.
"""

import sys
import time
import random

# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
# ANSI COLOR PALETTE - Because life is meaningless, but at least it's colorful
# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
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

# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
# THE QUOTE - Original Woody Allen-esque neurotic wisdom
# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
QUOTE = (
    "I took a speed-reading course and finished 'War and Peace' in twenty minutes. "
    "It involves Russia."
)

QUOTE_LINES = [
    "I took a speed-reading course",
    "and finished 'War and Peace'",
    "in twenty minutes.",
    "It involves Russia."
]

ATTRIBUTION = "— Woody Allen (probably)"

# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
# ASCII ART ELEMENTS
# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
WOODY_FACE = [
    "       ╭─────────────╮",
    "       │  (•_•)      │  <-- That's me, worrying",
    "       │  <)  )╯     │      about the framing",
    "       │  /  \\       │",
    "       ╰─────────────╯",
]

BOOK_ART = [
    "    ╔════════════════╗",
    "    ║  WAR AND PEACE ║",
    "    ║   by Tolstoy   ║",
    "    ║   (1,225 pp)   ║",
    "    ╚════════════════╝",
    "         ║  ║",
    "         ║  ║  ← 20 mins later",
    "         ╚══╝",
]

STRESS_LINES = [
    "  ~~~  ~~~  ~~~  ~~~  ~~~  ~~~  ~~~",
    "   Stress lines radiating outward",
    "  ~~~  ~~~  ~~~  ~~~  ~~~  ~~~  ~~~",
]

# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
# ANIMATION HELPERS
# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
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

def move_cursor(y, x):
    sys.stdout.write(f'\033[{y};{x}H')
    sys.stdout.flush()

def typewriter(text, color=C.WHITE, delay=0.03, newline=True):
    """Typewriter effect for text."""
    for char in text:
        sys.stdout.write(f"{color}{char}{C.RST}")
        sys.stdout.flush()
        time.sleep(delay)
    if newline:
        print()

def fade_in_text(text, color=C.WHITE, steps=10):
    """Fade in text by gradually increasing brightness."""
    for i in range(steps):
        intensity = int(232 + (i * (255 - 232) / steps))
        sys.stdout.write(f'\033[38;5;{intensity}m{text}{C.RST}\r')
        sys.stdout.flush()
        time.sleep(0.05)
    print()

# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
# VISUAL EFFECTS
# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
def draw_box(title, content_lines, width=50, title_color=C.BRIGHT_YELLOW, 
             border_color=C.BRIGHT_CYAN, content_color=C.WHITE):
    """Draw a fancy ASCII box."""
    inner_width = width - 4
    
    # Top border
    print(f"{border_color}╭{'─' * (width - 2)}╮{C.RST}")
    
    # Title line
    title_padded = f" {title} ".center(inner_width)
    print(f"{border_color}│{C.RST}{title_color}{title_padded}{C.RST}{border_color}│{C.RST}")
    
    # Separator
    print(f"{border_color}├{'─' * (width - 2)}┤{C.RST}")
    
    # Content lines
    for line in content_lines:
        padded = line.center(inner_width)
        print(f"{border_color}│{C.RST} {content_color}{padded}{C.RST} {border_color}│{C.RST}")
    
    # Bottom border
    print(f"{border_color}╰{'─' * (width - 2)}╯{C.RST}")

def spinning_loader(message, duration=2.0, color=C.BRIGHT_MAGENTA):
    """Show a spinning loader."""
    spinner = ['⠋', '⠙', '⠹', '⠸', '⠼', '⠴', '⠦', '⠧', '⠇', '⠏']
    end_time = time.time() + duration
    i = 0
    while time.time() < end_time:
        sys.stdout.write(f"\r{color}{spinner[i % len(spinner)]} {message}{C.RST}")
        sys.stdout.flush()
        time.sleep(0.08)
        i += 1
    sys.stdout.write('\r' + ' ' * (len(message) + 4) + '\r')
    sys.stdout.flush()

def glitch_text(text, color=C.BRIGHT_RED, glitches=3):
    """Glitch effect on text."""
    glitch_chars = '!@#$%^&*()_+-=[]{}|;:,.<>?'
    for _ in range(glitches):
        glitched = ''.join(
            random.choice(glitch_chars) if random.random() < 0.1 else c 
            for c in text
        )
        sys.stdout.write(f"\r{color}{glitched}{C.RST}")
        sys.stdout.flush()
        time.sleep(0.05)
    sys.stdout.write(f"\r{color}{text}{C.RST}\n")
    sys.stdout.flush()

# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
# MAIN PRESENTATION SEQUENCE
# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
def show_intro():
    """Opening sequence."""
    clear_screen()
    hide_cursor()
    
    # Title card
    print()
    print(f"{C.BRIGHT_CYAN}{'═' * 60}{C.RST}")
    print(f"{C.BOLD}{C.BRIGHT_YELLOW}    WOODY ALLEN'S NEUROTIC WISDOM GENERATOR v1.0{C.RST}")
    print(f"{C.BRIGHT_CYAN}{'═' * 60}{C.RST}")
    print()
    
    # Show Woody face
    for line in WOODY_FACE:
        print(f"{C.BRIGHT_GREEN}{line}{C.RST}")
        time.sleep(0.15)
    print()
    
    # Dramatic pause
    spinning_loader("Contemplating existence...", 1.5)
    print()
    
    typewriter("Initializing existential dread...", C.BRIGHT_RED, 0.02)
    time.sleep(0.5)
    typewriter("Calibrating neurotic parameters...", C.BRIGHT_YELLOW, 0.02)
    time.sleep(0.5)
    typewriter("Loading philosophical punchline...", C.BRIGHT_CYAN, 0.02)
    print()

def show_quote_animation():
    """Animate the quote reveal."""
    print(f"{C.BRIGHT_MAGENTA}{'━' * 60}{C.RST}")
    print(f"{C.BOLD}{C.BRIGHT_WHITE}           TODAY'S NEUROTIC EPIPHANY{C.RST}")
    print(f"{C.BRIGHT_MAGENTA}{'━' * 60}{C.RST}")
    print()
    
    # Show book art first
    for line in BOOK_ART:
        print(f"{C.YELLOW}{line}{C.RST}")
        time.sleep(0.1)
    print()
    
    # Type each line of the quote
    colors = [C.BRIGHT_WHITE, C.BRIGHT_CYAN, C.BRIGHT_YELLOW, C.BRIGHT_GREEN]
    for i, line in enumerate(QUOTE_LINES):
        typewriter(f"  {line}", colors[i % len(colors)], 0.025)
        time.sleep(0.3)
    
    print()
    # Attribution with flair
    time.sleep(0.4)
    typewriter(f"  {ATTRIBUTION}", C.DIM + C.ITALIC, 0.04)
    print()

def show_stress_visualization():
    """Show stress lines radiating."""
    print()
    print(f"{C.BRIGHT_RED}{'─' * 60}{C.RST}")
    for line in STRESS_LINES:
        print(f"{C.RED}{line}{C.RST}")
        time.sleep(0.15)
    print(f"{C.BRIGHT_RED}{'─' * 60}{C.RST}")

def show_philosophical_breakdown():
    """Break down the quote philosophically."""
    print()
    print(f"{C.BRIGHT_BLUE}┌{'─' * 58}┐{C.RST}")
    print(f"{C.BRIGHT_BLUE}│{C.BOLD}{C.BRIGHT_WHITE}           PHILOSOPHICAL ANALYSIS (Unsolicited)         {C.RST}{C.BRIGHT_BLUE}│{C.RST}")
    print(f"{C.BRIGHT_BLUE}├{'─' * 58}┤{C.RST}")
    
    analysis = [
        ("Speed-reading", "Avoidance coping mechanism", C.YELLOW),
        ("War and Peace", "Metaphor for life's overwhelming complexity", C.CYAN),
        ("20 minutes", "Magical thinking / time distortion", C.MAGENTA),
        ("'It involves Russia'", "Reductive summary = defense mechanism", C.GREEN),
        ("", "", C.RST),
        ("CONCLUSION:", "You didn't read it. You survived it.", C.BRIGHT_RED + C.BOLD),
    ]
    
    for concept, explanation, color in analysis:
        if concept:
            line = f"  {concept:<20} → {explanation}"
            print(f"{C.BRIGHT_BLUE}│{C.RST} {color}{line:<56}{C.RST} {C.BRIGHT_BLUE}│{C.RST}")
        else:
            print(f"{C.BRIGHT_BLUE}│{' ' * 58}│{C.RST}")
    
    print(f"{C.BRIGHT_BLUE}└{'─' * 58}┘{C.RST}")

def show_existential_footer():
    """Final existential footer."""
    print()
    print(f"{C.GRAY}{'═' * 60}{C.RST}")
    
    footers = [
        "Remember: The universe is indifferent. But at least you're not in Russia.",
        "Death is nature's way of telling you to slow down.",
        "I don't want to achieve immortality through my work...",
        "...I want to achieve it through not dying. (Classic Woody)",
        "",
        "Press Ctrl+C to exit this mortal coil (or just close the window)."
    ]
    
    for i, footer in enumerate(footers):
        if i == len(footers) - 1:
            print(f"{C.BRIGHT_YELLOW}{C.BLINK}  {footer}{C.RST}")
        elif footer:
            print(f"{C.DIM}{C.ITALIC}  {footer}{C.RST}")
        else:
            print()
        time.sleep(0.2)
    
    print(f"{C.GRAY}{'═' * 60}{C.RST}")

def show_easter_egg():
    """Hidden easter egg for the persistent."""
    print()
    time.sleep(1)
    print(f"{C.BRIGHT_MAGENTA}{C.BOLD}  ▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓{C.RST}")
    print(f"{C.BRIGHT_MAGENTA}  ▓                                                                  ▓{C.RST}")
    print(f"{C.BRIGHT_MAGENTA}  ▓   {C.BRIGHT_YELLOW}WAIT! You're still here?{C.RST}{C.BRIGHT_MAGENTA}                                    ▓{C.RST}")
    print(f"{C.BRIGHT_MAGENTA}  ▓   {C.BRIGHT_CYAN}The quote was a test. You passed. Or failed. Both?{C.RST}{C.BRIGHT_MAGENTA}   ▓{C.RST}")
    print(f"{C.BRIGHT_MAGENTA}  ▓   {C.BRIGHT_GREEN}Either way, the universe remains unexplained.{C.RST}{C.BRIGHT_MAGENTA}      ▓{C.RST}")
    print(f"{C.BRIGHT_MAGENTA}  ▓                                                                  ▓{C.RST}")
    print(f"{C.BRIGHT_MAGENTA}  ▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓{C.RST}")
    print()

# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
# MAIN ENTRY POINT
# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
def main():
    try:
        show_intro()
        show_quote_animation()
        show_stress_visualization()
        show_philosophical_breakdown()
        show_existential_footer()
        show_easter_egg()
        
        # Final pause
        time.sleep(2)
        
    except KeyboardInterrupt:
        print(f"\n{C.BRIGHT_RED}Interrupted. How very... mortal of you.{C.RST}")
    finally:
        show_cursor()
        print(f"{C.RST}")  # Reset all attributes

if __name__ == "__main__":
    main()