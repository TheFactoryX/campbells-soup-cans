"""
Campbell's Soup Can #4019
Produced: 2026-06-26 16:27:32
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
Woody Allen Quote Generator - Neurotic Edition
Because existence is meaningless, but at least the colors are pretty.
"""

import sys
import time
import random

# ═══════════════════════════════════════════════════════════════════════════
# ANSI COLOR PALETTE - because life needs more escape codes
# ═══════════════════════════════════════════════════════════════════════════

class C:
    R = '\033[0m'       # Reset (like therapy, but faster)
    B = '\033[1m'       # Bold (for emphasis, like my hypochondria)
    D = '\033[2m'       # Dim (like my prospects)
    I = '\033[3m'       # Italic (for internal monologue)
    U = '\033[4m'       # Underline (for things I'll worry about later)
    
    # Foreground - neurotic rainbow
    BLK = '\033[30m'
    RED = '\033[31m'    # Panic
    GRN = '\033[32m'    # False hope
    YEL = '\033[33m'    # Anxiety
    BLU = '\033[34m'    # Existential dread
    MAG = '\033[35m'    # Neurosis
    CYN = '\033[36m'    # Cynicism
    WHT = '\033[37m'    # Resignation
    
    # Bright variants - for when the dread intensifies
    BRED = '\033[91m'
    BGRN = '\033[92m'
    BYEL = '\033[93m'
    BBLU = '\033[94m'
    BMAG = '\033[95m'
    BCYN = '\033[96m'
    BWHT = '\033[97m'
    
    # Background - for highlighting my failures
    BG_BLK = '\033[40m'
    BG_RED = '\033[41m'
    BG_GRN = '\033[42m'
    BG_YEL = '\033[43m'
    BG_BLU = '\033[44m'
    BG_MAG = '\033[45m'
    BG_CYN = '\033[46m'
    BG_WHT = '\033[47m'


# ═══════════════════════════════════════════════════════════════════════════
# THE QUOTE - hand-crafted artisanal neurosis
# ═══════════════════════════════════════════════════════════════════════════

WOODY_QUOTE = (
    "I took a speed-reading course and read 'War and Peace' "
    "in twenty minutes. It involves Russia."
)

# Alternative quotes (commented out, like my social life)
# WOODY_QUOTE = "The universe is indifferent. So is my analyst. He charges $300/hour to not care."
# WOODY_QUOTE = "I don't believe in an afterlife, but I'm bringing a change of underwear just in case."
# WOODY_QUOTE = "My one regret in life is that I'm not someone else. Preferably someone with better health insurance."
# WOODY_QUOTE = "Death is just nature's way of telling you to slow down. Which I already do. Excessively."


# ═══════════════════════════════════════════════════════════════════════════
# ASCII ART - because words alone can't capture the absurdity
# ════════════════════════════════════════════════════════════════════════════

WOODY_FACE = [
    "        ╭─────────────╮",
    "        │  ▄▄    ▄▄   │  ← glasses (prescription: existential)",
    "        │  ▀▀    ▀▀   │",
    "        │      __     │",
    "        │     /  \\    │  ← nervous smile",
    "        │    |    |   │",
    "        ╰─────────────╯",
]

THOUGHT_BUBBLE = [
    "           .--.",
    "          /    \\",
    "         |  💭  |",
    "          \\    /",
    "           '--'",
]

DIVIDER_TOP = "╭" + "─" * 68 + "╮"
DIVIDER_MID = "├" + "─" * 68 + "┤"
DIVIDER_BOT = "╰" + "─" * 68 + "╯"


# ═══════════════════════════════════════════════════════════════════════════
# ANIMATION HELPERS - because instant gratification is for optimists
# ═══════════════════════════════════════════════════════════════════════════

def clear_screen():
    """Clear terminal - like repression, but for text."""
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


def typewriter_print(text, delay=0.03, color=C.WHT, end='\n'):
    """Print character by character - like thoughts forming, painfully slow."""
    for char in text:
        sys.stdout.write(f'{color}{char}{C.R}')
        sys.stdout.flush()
        time.sleep(delay + random.uniform(-0.01, 0.01))
    if end:
        sys.stdout.write(end)
        sys.stdout.flush()


def typewriter_print_line(text, delay=0.02, color=C.WHT):
    """Print a line with typewriter effect."""
    typewriter_print(text, delay, color, end='')


def pulse_text(text, cycles=3, colors=None):
    """Make text pulse - like my blood pressure."""
    if colors is None:
        colors = [C.RED, C.YEL, C.GRN, C.CYN, C.BLU, C.MAG]
    
    for _ in range(cycles):
        for color in colors:
            move_cursor(1, 1)
            sys.stdout.write(f'{color}{text}{C.R}')
            sys.stdout.flush()
            time.sleep(0.15)
    move_cursor(1, 1)
    sys.stdout.write(f'{C.WHT}{text}{C.R}')
    sys.stdout.flush()


def glitch_text(text, intensity=0.1):
    """Glitch effect - like my mental state."""
    chars = '█▓▒░@#$%&*'
    result = []
    for char in text:
        if char != ' ' and random.random() < intensity:
            result.append(random.choice(chars))
        else:
            result.append(char)
    return ''.join(result)


# ═══════════════════════════════════════════════════════════════════════════
# VISUAL COMPONENTS - the theater of the absurd
# ═══════════════════════════════════════════════════════════════════════════

def draw_woody_face():
    """Draw Woody's face with color cycling."""
    for i, line in enumerate(WOODY_FACE):
        color = [C.CYN, C.BLU, C.MAG, C.YEL][i % 4]
        print(f'{color}{line}{C.R}')
    print()


def draw_thought_bubble():
    """Draw a thought bubble."""
    for line in THOUGHT_BUBBLE:
        print(f'{C.DIM}{line}{C.R}')
    print()


def draw_boxed_quote(quote, width=68):
    """Draw the quote in a fancy box with typing animation."""
    # Word wrap the quote
    words = quote.split()
    lines = []
    current_line = []
    current_length = 0
    
    for word in words:
        if current_length + len(word) + 1 > width - 4:  # -4 for padding
            lines.append(' '.join(current_line))
            current_line = [word]
            current_length = len(word)
        else:
            current_line.append(word)
            current_length += len(word) + 1
    if current_line:
        lines.append(' '.join(current_line))
    
    # Print top border
    print(f'{C.BCYN}{DIVIDER_TOP}{C.R}')
    
    # Print empty line for breathing room
    print(f'{C.BCYN}│{C.R} {" " * width} {C.BCYN}│{C.R}')
    
    # Print quote lines with typewriter effect
    for line in lines:
        padding = width - len(line)
        left_pad = padding // 2
        right_pad = padding - left_pad
        
        sys.stdout.write(f'{C.BCYN}│{C.R} {" " * left_pad}')
        sys.stdout.flush()
        
        # Typewriter effect for the quote
        for char in line:
            # Random color variation for that neurotic feel
            char_color = random.choice([C.BWHT, C.CYN, C.WHT, C.BCYN])
            sys.stdout.write(f'{char_color}{char}{C.R}')
            sys.stdout.flush()
            time.sleep(0.025 + random.uniform(-0.005, 0.01))
        
        sys.stdout.write(f'{" " * right_pad} {C.BCYN}│{C.R}\n')
        sys.stdout.flush()
        time.sleep(0.15)  # Pause between lines - for dramatic effect
    
    # Empty line
    print(f'{C.BCYN}│{C.R} {" " * width} {C.BCYN}│{C.R}')
    
    # Attribution line
    attrib = "— Woody Allen (probably, I didn't fact-check, I have anxiety)"
    attrib_padding = width - len(attrib)
    print(f'{C.BCYN}│{C.R} {" " * attrib_padding}{C.D}{C.I}{attrib}{C.R} {C.BCYN}│{C.R}')
    
    # Bottom border
    print(f'{C.BCYN}{DIVIDER_BOT}{C.R}')


def draw_neurotic_footer():
    """Draw a footer with neurotic statistics."""
    footer_items = [
        f"{C.DIM}┌─ Neurotic Metadata ────────────────────────────────────────┐{C.R}",
        f"{C.DIM}│{C.R} {C.RED}♥{C.R} Heart rate: Elevated    {C.YEL}☕{C.R} Coffee: 4 cups    {C.BLU}😰{C.R} Anxiety: Critical  {C.DIM}│{C.R}",
        f"{C.DIM}│{C.R} {C.MAG}💊{C.R} Meds: Checked           {C.GRN}🛏{C.R} Sleep: 3 hours    {C.RED}💀{C.R} Mortality: Pending {C.DIM}│{C.R}",
        f"{C.DIM}└────────────────────────────────────────────────────────────┘{C.R}",
    ]
    for line in footer_items:
        print(line)


def draw_existential_particles():
    """Draw floating existential particles."""
    particles = ['∴', '∵', '∴', '∵', '?', '!', '...', '??', '💭', '🧠', '😰', '☕']
    line = ''
    for _ in range(12):
        p = random.choice(particles)
        color = random.choice([C.DIM, C.RED, C.YEL, C.BLU, C.MAG, C.CYN])
        line += f'{color}{p}  {C.R}'
    print(f'{C.DIM}{line.center(70)}{C.R}')


# ═══════════════════════════════════════════════════════════════════════════
# MAIN SEQUENCE - the performance
# ═══════════════════════════════════════════════════════════════════════════

def main():
    # Hide cursor for clean animation
    hide_cursor()
    
    try:
        # Clear screen
        clear_screen()
        
        # Small delay for effect
        time.sleep(0.3)
        
        # Title sequence - neurotic intro
        title_lines = [
            (C.BMAG + C.B, "    ╔═══════════════════════════════════════════════════════════════╗"),
            (C.BMAG + C.B, "    ║                                                           ║"),
            (C.BYEL + C.B, "    ║      W O O D Y   A L L E N   Q U O T E   G E N E R A T O R║"),
            (C.BMAG + C.B, "    ║              Neurotic Edition v1.0 (unmedicated)          ║"),
            (C.BMAG + C.B, "    ║                                                           ║"),
            (C.BMAG + C.B, "    ╚═══════════════════════════════════════════════════════════════╝"),
        ]
        
        for color, line in title_lines:
            print(f'{color}{line}{C.R}')
            time.sleep(0.08)
        
        print()
        time.sleep(0.2)
        
        # Draw Woody's face
        draw_woody_face()
        time.sleep(0.3)
        
        # Thought bubble forming
        print(f'{C.DIM}    A thought forms...{C.R}')
        time.sleep(0.4)
        draw_thought_bubble()
        time.sleep(0.3)
        
        # The quote - main event
        draw_boxed_quote(WOODY_QUOTE)
        
        print()
        time.sleep(0.3)
        
        # Existential particles
        draw_existential_particles()
        print()
        
        # Neurotic footer
        draw_neurotic_footer()
        
        print()
        print(f'{C.DIM}    Press Enter to return to your regularly scheduled anxiety...{C.R}')
        input()
        
    except KeyboardInterrupt:
        print(f'\n{C.RED}Interrupted. Even my programs have commitment issues.{C.R}')
    finally:
        show_cursor()
        clear_screen()
        # Final parting thought
        print(f'{C.I}{C.CYN}"I\'m not afraid of death; I just don\'t want to be there when it happens."{C.R}')
        print(f'{C.DIM}    — The real Woody Allen{C.R}\n')


if __name__ == '__main__':
    # Check if terminal supports ANSI
    if not sys.stdout.isatty():
        # Fallback for non-TTY
        print(WOODY_QUOTE)
        print("\n— Woody Allen (probably)")
    else:
        main()