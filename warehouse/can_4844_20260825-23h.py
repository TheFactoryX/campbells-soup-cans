"""
Campbell's Soup Can #4844
Produced: 2026-08-25 23:38:19
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
A single-file philosophical anxiety dispenser.
"""

import sys
import time
import random

# ═══════════════════════════════════════════════════════════════
# ANSI COLOR PALETTE - because existential dread deserves style
# ═══════════════════════════════════════════════════════════════
class C:
    R = '\033[0m'       # Reset
    B = '\033[1m'       # Bold
    D = '\033[2m'       # Dim
    I = '\033[3m'       # Italic
    U = '\033[4m'       # Underline
    BLINK = '\033[5m'   # Blink
    
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

# ═══════════════════════════════════════════════════════════════
# THE QUOTE - Pure, uncut Woody Allen neuroses
# ═══════════════════════════════════════════════════════════════
QUOTE = (
    "I took a course in existentialism... "
    "the final exam was just a blank sheet of paper "
    "and the professor wrote 'Why?' "
    "so I wrote 'Why not?' "
    "and got a C-minus because apparently "
    "the universe doesn't grade on a curve."
)

ATTRIBUTION = "— Woody Allen (probably, in an alternate timeline where he finished college)"

# ═══════════════════════════════════════════════════════════════
# ASCII ART ELEMENTS
# ═══════════════════════════════════════════════════════════════
WOODY_FACE = [
    "       ╭─────────────╮",
    "       │  @     @    │  ← glasses, obviously",
    "       │      __     │",
    "       │     /  \\    │  ← nervous smile",
    "       │    |    |   │",
    "       ╰─────────────╯",
]

NEURONS = [
    "    ╭─╮     ╭─╮     ╭─╮     ╭─╮",
    "   ( • )───( • )───( • )───( • )  ← synapses firing nervously",
    "    ╰─╯     ╰─╯     ╰─╯     ╰─╯",
]

BOX_TOP = "╔" + "═" * 68 + "╗"
BOX_BOT = "╚" + "═" * 68 + "╝"
BOX_MID = "╠" + "═" * 68 + "╣"
EMPTY_LINE = "║" + " " * 68 + "║"

# ═══════════════════════════════════════════════════════════════
# ANIMATION HELPERS
# ═══════════════════════════════════════════════════════════════
def clear_screen():
    """Clear terminal screen."""
    print('\033[2J\033[H', end='')

def hide_cursor():
    print('\033[?25l', end='')

def show_cursor():
    print('\033[?25h', end='')

def move_cursor(row, col):
    print(f'\033[{row};{col}H', end='')

def typewriter(text, color=C.WHITE, delay=0.02, end='\n'):
    """Typewriter effect with color."""
    for char in text:
        print(f"{color}{char}{C.R}", end='', flush=True)
        time.sleep(delay)
    print(end, end='', flush=True)

def pulse_color(text, colors, cycles=3, delay=0.15):
    """Pulse text through colors."""
    for _ in range(cycles):
        for color in colors:
            move_cursor(0, 0)
            print(f"{color}{text}{C.R}", end='', flush=True)
            time.sleep(delay)

def fade_in(text, color=C.WHITE, steps=10, delay=0.03):
    """Fade in text by gradually increasing intensity."""
    # Simulate with dim -> normal -> bold
    intensities = [C.D, '', C.B]
    for intensity in intensities:
        print(f"\r{intensity}{color}{text}{C.R}", end='', flush=True)
        time.sleep(delay * 3)
    print()

# ═══════════════════════════════════════════════════════════════
# VISUAL EFFECTS
# ═══════════════════════════════════════════════════════════════
def draw_woody_face():
    """Draw the Woody face with colors."""
    print(f"{C.CYAN}")
    for line in WOODY_FACE:
        print(f"    {line}")
    print(f"{C.R}")

def draw_neurons_animated():
    """Animated neuron firing."""
    frames = [
        ["    ╭─╮     ╭─╮     ╭─╮     ╭─╮",
         "   ( • )───( • )───( • )───( • )",
         "    ╰─╯     ╰─╯     ╰─╯     ╰─╯"],
        ["    ╭─╮     ╭─╮     ╭─╮     ╭─╮",
         "   ( ○ )───( • )───( • )───( • )",
         "    ╰─╯     ╰─╯     ╰─╯     ╰─╯"],
        ["    ╭─╮     ╭─╮     ╭─╮     ╭─╮",
         "   ( ○ )───( ○ )───( • )───( • )",
         "    ╰─╯     ╰─╯     ╰─╯     ╰─╯"],
        ["    ╭─╮     ╭─╮     ╭─╮     ╭─╮",
         "   ( ○ )───( ○ )───( ○ )───( • )",
         "    ╰─╯     ╰─╯     ╰─╯     ╰─╯"],
        ["    ╭─╮     ╭─╮     ╭─╮     ╭─╮",
         "   ( ○ )───( ○ )───( ○ )───( ○ )",
         "    ╰─╯     ╰─╯     ╰─╯     ╰─╯"],
    ]
    
    for _ in range(2):
        for frame in frames:
            move_cursor(10, 0)
            for line in frame:
                print(f"{C.YELLOW}{line}{C.R}")
            time.sleep(0.15)

def draw_box_with_quote():
    """Draw the main quote box with typing effect."""
    print(f"{C.BRIGHT_CYAN}{BOX_TOP}{C.R}")
    print(f"{C.BRIGHT_CYAN}{EMPTY_LINE}{C.R}")
    
    # Title line
    title = "  WOODY ALLEN'S DAILY DOSE OF NEUROTIC WISDOM  "
    padding = (68 - len(title)) // 2
    print(f"{C.BRIGHT_CYAN}║{C.R}{C.BG_BLUE}{C.BRIGHT_WHITE}{C.B}{' ' * padding}{title}{' ' * (68 - padding - len(title))}{C.R}{C.BRIGHT_CYAN}║{C.R}")
    
    print(f"{C.BRIGHT_CYAN}{BOX_MID}{C.R}")
    print(f"{C.BRIGHT_CYAN}{EMPTY_LINE}{C.R}")
    
    # The quote - word by word with typewriter
    words = QUOTE.split(' ')
    line = "║  "
    char_count = 4
    
    for i, word in enumerate(words):
        if char_count + len(word) + 1 > 66:
            # Print current line
            print(f"{C.BRIGHT_CYAN}{line}{' ' * (68 - len(line))}║{C.R}")
            line = "║  " + word + " "
            char_count = 4 + len(word) + 1
        else:
            line += word + " "
            char_count += len(word) + 1
        
        # Typewriter effect for each word
        print(f"\r{C.BRIGHT_CYAN}{line}{' ' * (68 - len(line))}║{C.R}", end='', flush=True)
        time.sleep(0.08)
    
    # Print final line
    print(f"\r{C.BRIGHT_CYAN}{line}{' ' * (68 - len(line))}║{C.R}")
    
    print(f"{C.BRIGHT_CYAN}{EMPTY_LINE}{C.R}")
    print(f"{C.BRIGHT_CYAN}{BOX_MID}{C.R}")
    print(f"{C.BRIGHT_CYAN}{EMPTY_LINE}{C.R}")
    
    # Attribution with style
    attr_line = f"║  {C.I}{C.YELLOW}{ATTRIBUTION}{C.R}{C.BRIGHT_CYAN}"
    padding_needed = 68 - len(ATTRIBUTION) - 4
    print(f"{attr_line}{' ' * padding_needed}║{C.R}")
    
    print(f"{C.BRIGHT_CYAN}{EMPTY_LINE}{C.R}")
    print(f"{C.BRIGHT_CYAN}{BOX_BOT}{C.R}")

def philosophical_loader():
    """Fake philosophical loading screen."""
    thoughts = [
        "Contemplating the void...",
        "Questioning the nature of being...",
        "Worrying about mortality...",
        "Checking if stove is off (metaphorically)...",
        "Calculating probability of meaningful existence...",
        "Realizing we're all just dust in the wind...",
        "Dust that pays taxes...",
        "Dust with student loans...",
        "Almost there...",
        "Successfully induced mild existential crisis!",
    ]
    
    print(f"\n{C.GRAY}Initializing neurotic subsystem...{C.R}\n")
    for thought in thoughts:
        dots = "." * random.randint(1, 4)
        print(f"  {C.DIM}{C.CYAN}[{C.R}{C.GREEN}OK{C.R}{C.DIM}{C.CYAN}]{C.R} {thought}{dots}")
        time.sleep(random.uniform(0.15, 0.35))
    print()

def glitch_text(text, intensity=3):
    """Glitch effect for the final flourish."""
    glitch_chars = "!@#$%^&*()_+-=[]{}|;':\",./<>?`~"
    for _ in range(intensity):
        glitched = ''.join(
            random.choice(glitch_chars) if random.random() < 0.1 else c
            for c in text
        )
        print(f"\r{C.RED}{glitched}{C.R}", end='', flush=True)
        time.sleep(0.05)
    print(f"\r{C.BRIGHT_WHITE}{text}{C.R}")

# ═══════════════════════════════════════════════════════════════
# MAIN SEQUENCE
# ═══════════════════════════════════════════════════════════════
def main():
    hide_cursor()
    try:
        clear_screen()
        
        # Opening animation
        print(f"\n{C.BRIGHT_MAGENTA}{C.B}")
        print("    ╔══════════════════════════════════════════════════════════╗")
        print("    ║                                                          ║")
        print("    ║    W O O D Y   A L L E N   Q U O T E   G E N E R A T O R ║")
        print("    ║         \"Neurotic Wisdom Since Whenever\"                ║")
        print("    ║                                                          ║")
        print("    ╚══════════════════════════════════════════════════════════╝")
        print(f"{C.R}\n")
        
        # Philosophical loader
        philosophical_loader()
        
        # Draw Woody face
        draw_woody_face()
        
        # Animated neurons
        print(f"{C.GRAY}    Neural pathways activating...{C.R}\n")
        draw_neurons_animated()
        
        # The main event
        print(f"\n{C.BRIGHT_YELLOW}    Preparing your daily anxiety...{C.R}\n")
        time.sleep(0.5)
        
        draw_box_with_quote()
        
        # Final flourish
        print(f"\n{C.GRAY}    ═══════════════════════════════════════════════════════════{C.R}")
        print(f"    {C.DIM}Quote generated by simulated neuroses v3.14159{C.R}")
        print(f"    {C.DIM}Side effects may include: overthinking, insomnia,{C.R}")
        print(f"    {C.DIM}and sudden urges to move to Manhattan{C.R}")
        print(f"    {C.GRAY}═══════════════════════════════════════════════════════════{C.R}\n")
        
        # One last neurotic thought
        final_thoughts = [
            "Remember: You're not paranoid if the universe really IS out to get you.",
            "Death is nature's way of saying 'Your table is ready.'",
            "I don't believe in an afterlife, but I'm bringing a change of underwear just in case.",
            "The universe is indifferent. So is your cat. Accept it.",
            "You'll never be as young as you are right now. Terrifying, isn't it?",
        ]
        
        thought = random.choice(final_thoughts)
        print(f"    {C.I}{C.MAGENTA}Parting thought: {C.R}{C.I}{thought}{C.R}\n")
        
    finally:
        show_cursor()

if __name__ == "__main__":
    # Check if terminal supports colors
    if not sys.stdout.isatty():
        # Fallback for non-TTY
        print(QUOTE)
        print(ATTRIBUTION)
    else:
        main()