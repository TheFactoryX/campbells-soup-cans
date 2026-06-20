"""
Campbell's Soup Can #3970
Produced: 2026-06-20 06:41:09
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
    R = '\033[91m'      # Red
    G = '\033[92m'      # Green
    Y = '\033[93m'      # Yellow
    B = '\033[94m'      # Blue
    M = '\033[95m'      # Magenta
    C = '\033[96m'      # Cyan
    W = '\033[97m'      # White
    GR = '\033[90m'     # Gray
    BO = '\033[1m'      # Bold
    IT = '\033[3m'      # Italic
    UN = '\033[4m'      # Underline
    BL = '\033[5m'      # Blink
    RV = '\033[7m'      # Reverse
    X = '\033[0m'       # Reset

# Woody Allen ASCII portrait
WOODY = f"""
{C.GR}        ╭─────────────╮{C.X}
{C.GR}       ╱ {C.Y}◉{C.GR}     {C.Y}◉{C.GR} ╲{C.X}
{C.GR}      │  {C.M}┌─────┐{C.GR}  │{C.X}
{C.GR}      │  {C.M}│     │{C.GR}  │{C.X}
{C.GR}      ╲  {C.M}└─────┘{C.GR}  ╱{C.X}
{C.GR}       ╲    {C.Y}∿{C.GR}    ╱{C.X}
{C.GR}        ╰─────────────╯{C.X}
{C.GR}         {C.Y}┌───────┐{C.X}
{C.GR}         {C.Y}│       │{C.X}
{C.GR}        {C.Y}╱         ╲{C.X}
"""

# The quote - original Woody-style
QUOTE = (
    "I took a speed-reading course and read 'War and Peace' in twenty minutes. "
    "It involves Russia."
)

# Alternative quotes (pick one randomly)
QUOTES = [
    "I took a speed-reading course and read 'War and Peace' in twenty minutes. It involves Russia.",
    "My therapist told me I have a preoccupation with vengeance. We'll see about that.",
    "I'm not afraid of death. I just don't want to be there when it happens... or pay for parking.",
    "The universe is indifferent. My landlord, however, is very interested in the first of the month.",
    "I have a metaphysical dilemma: if a tree falls in a forest and no one hears it, does my back still hurt?",
    "Eternal nothingness is fine if you're dressed for it. I never am.",
    "I don't believe in an afterlife, but I'm bringing a change of underwear just in case.",
    "My one regret in life is that I'm not someone else. Preferably someone with better health insurance.",
    "Life is a sexually transmitted terminal disease. The symptoms include anxiety and overdue library books.",
    "I've never been an intellectual but I have this look. It's called 'myopic despair.'",
]

def clear_screen():
    print('\033[2J\033[H', end='')

def hide_cursor():
    print('\033[?25l', end='')

def show_cursor():
    print('\033[?25h', end='')

def move_cursor(row, col):
    print(f'\033[{row};{col}H', end='')

def typewriter(text, color=C.W, delay=0.03, bold=False):
    """Typewriter effect with color"""
    prefix = ''
    if bold:
        prefix += C.BO
    prefix += color
    sys.stdout.write(prefix)
    sys.stdout.flush()
    
    for char in text:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(delay + random.uniform(-0.01, 0.01))
    
    sys.stdout.write(C.X)
    sys.stdout.flush()

def rainbow_text(text):
    """Print text with rainbow colors"""
    colors = [C.R, C.Y, C.G, C.C, C.B, C.M]
    for i, char in enumerate(text):
        if char != ' ':
            sys.stdout.write(colors[i % len(colors)] + char + C.X)
        else:
            sys.stdout.write(' ')
        sys.stdout.flush()
        time.sleep(0.01)
    print()

def pulse_text(text, color=C.C, cycles=3):
    """Pulse text brightness"""
    for _ in range(cycles):
        for intensity in [C.GR, C.W, C.BO + C.W, C.W, C.GR]:
            move_cursor(15, 2)
            sys.stdout.write(f'{intensity}{color}{text}{C.X}')
            sys.stdout.flush()
            time.sleep(0.15)

def draw_box(text, width=70, color=C.C, title=""):
    """Draw a fancy box around text"""
    lines = []
    words = text.split(' ')
    current_line = ""
    
    for word in words:
        if len(current_line) + len(word) + 1 <= width - 4:
            current_line += (" " if current_line else "") + word
        else:
            lines.append(current_line)
            current_line = word
    if current_line:
        lines.append(current_line)
    
    # Top border
    if title:
        title_str = f" {title} "
        padding = width - 2 - len(title_str)
        left_pad = padding // 2
        right_pad = padding - left_pad
        print(f"{color}╭{'─' * left_pad}{title_str}{'─' * right_pad}╮{C.X}")
    else:
        print(f"{color}╭{'─' * (width - 2)}╮{C.X}")
    
    # Content lines
    for line in lines:
        padding = width - 4 - len(line)
        print(f"{color}│{C.X}  {line}{' ' * padding}  {color}│{C.X}")
    
    # Bottom border
    print(f"{color}╰{'─' * (width - 2)}╯{C.X}")

def neurotic_loader():
    """A neurotic loading animation"""
    thoughts = [
        "Overthinking...",
        "Second-guessing the quote...",
        "Wondering if I left the stove on...",
        "Questioning existence...",
        "Checking pulse... still anxious...",
        "Replaying awkward moment from 2003...",
        "Calculating probability of catastrophe...",
        "Adjusting glasses nervously...",
    ]
    
    print(f"\n{C.M}{C.IT}Woody's internal monologue:{C.X}\n")
    for i, thought in enumerate(thoughts):
        sys.stdout.write(f"  {C.GR}[{C.Y}•{C.GR}] {C.W}{thought}{C.X}")
        sys.stdout.flush()
        time.sleep(0.4)
        sys.stdout.write(f"\r  {C.GR}[{C.G}✓{C.GR}] {C.GR}{thought}{C.X}\n")
        sys.stdout.flush()
    print()

def main():
    hide_cursor()
    clear_screen()
    
    # Pick a random quote
    quote = random.choice(QUOTES)
    
    # Title animation
    print(f"\n{C.Y}{C.BO}")
    print("    ╔══════════════════════════════════════════════════════════════╗")
    print("    ║                                                               ║")
    print("    ║     W O O D Y ' S   E X I S T E N T I A L   D I S P A T C H  ║")
    print("    ║                                                               ║")
    print("    ╚══════════════════════════════════════════════════════════════╝")
    print(f"{C.X}")
    
    # Show Woody
    print(WOODY)
    
    # Neurotic loader
    neurotic_loader()
    
    # The quote reveal with typewriter effect
    print(f"\n{C.C}{C.BO}┌────────────────────────────────────────────────────────────────┐{C.X}")
    print(f"{C.C}{C.BO}│{C.X}  {C.Y}{C.IT}Here's what keeps me up at 3 AM (besides the radiator noise):{C.X}  {C.C}{C.BO}│{C.X}")
    print(f"{C.C}{C.BO}└────────────────────────────────────────────────────────────────┘{C.X}\n")
    
    # Typewriter the quote
    print(f"  {C.BO}{C.W}″{C.X}", end='')
    sys.stdout.flush()
    typewriter(quote, color=C.Y, delay=0.025, bold=True)
    print(f"{C.BO}{C.W}″{C.X}\n")
    
    # Philosophical footer
    time.sleep(0.5)
    print(f"  {C.GR}{C.IT}— Woody Allen, probably, while waiting for a therapist appointment{C.X}\n")
    
    # Animated existential crisis meter
    print(f"  {C.M}Existential Crisis Level: {C.X}", end='')
    sys.stdout.flush()
    
    meter_width = 40
    for i in range(meter_width + 1):
        filled = '█' * i
        empty = '░' * (meter_width - i)
        if i < meter_width * 0.3:
            color = C.G
        elif i < meter_width * 0.7:
            color = C.Y
        else:
            color = C.R
        move_cursor(22, 28)
        sys.stdout.write(f"{color}{filled}{C.GR}{empty}{C.X} {i*100//meter_width}%")
        sys.stdout.flush()
        time.sleep(0.02)
    
    print(f"\n\n  {C.R}{C.BL}CRITICAL: Existence detected. Proceed with caution.{C.X}\n")
    
    # Final sign-off with rainbow
    print(f"  {C.GR}", end='')
    rainbow_text("  Thank you for your attention. My analyst will bill you.")
    
    # Easter egg - hidden message
    time.sleep(0.5)
    print(f"\n  {C.GR}Press Enter to continue your neurotic existence...{C.X}", end='')
    sys.stdout.flush()
    input()
    
    # Parting thought
    clear_screen()
    parting = random.choice([
        "Remember: You're not paranoid if the universe really IS out to get you.",
        "Death is just nature's way of saying 'Your table is ready.'",
        "I'll be in the lobby. The one with the uncomfortable chairs.",
        "If you don't hear from me, I've either achieved enlightenment or fallen asleep.",
    ])
    print(f"\n\n\n{C.C}{C.BO}{C.IT}")
    print(" " * 15 + "┌" + "─" * 50 + "┐")
    print(" " * 15 + "│" + " " * 50 + "│")
    print(" " * 15 + "│" + parting.center(50) + "│")
    print(" " * 15 + "│" + " " * 50 + "│")
    print(" " * 15 + "└" + "─" * 50 + "┘")
    print(f"{C.X}\n\n")
    
    show_cursor()

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        show_cursor()
        print(f"\n\n{C.R}Interrupted. Typical. Even my programs have commitment issues.{C.X}\n")
    except Exception as e:
        show_cursor()
        print(f"\n{C.R}Error: {e}{C.X}")
        print(f"{C.GR}Even my code has existential crises.{C.X}\n")