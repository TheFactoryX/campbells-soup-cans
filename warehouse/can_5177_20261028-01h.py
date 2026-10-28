"""
Campbell's Soup Can #5177
Produced: 2026-10-28 01:22:51
Worker: Free Models Router (openrouter/free)
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

# ┌─────────────────────────────────────────────────────────────────────┐
# │  ANSI Color Palette - Woody's Neurotic Neurosis Collection          │
# └─────────────────────────────────────────────────────────────────────┘
class C:
    R = '\033[0m'       # Reset (therapy)
    B = '\033[1m'       # Bold (panic)
    D = '\033[2m'       # Dim (depression)
    I = '\033[3m'       # Italic (introspection)
    U = '\033[4m'       # Underline (underlying dread)
    
    # Foreground - the emotional spectrum
    BLK = '\033[30m'    # Void
    RED = '\033[31m'    # Anxiety
    GRN = '\033[32m'    # Hypochondria
    YEL = '\033[33m'    # Neurosis
    BLU = '\033[34m'    # Existential dread
    MAG = '\033[35m'    # Freudian slip
    CYN = '\033[36m'    # Cynicism
    WHT = '\033[37m'    # White noise
    
    # Bright variants - for when the panic attacks
    BRED = '\033[91m'
    BGRN = '\033[92m'
    BYEL = '\033[93m'
    BBLU = '\033[94m'
    BMAG = '\033[95m'
    BCYN = '\033[96m'
    BWHT = '\033[97m'
    
    # Background - the stage of life
    BG_BLK = '\033[40m'
    BG_RED = '\033[41m'
    BG_GRN = '\033[42m'
    BG_YEL = '\033[43m'
    BG_BLU = '\033[44m'
    BG_MAG = '\033[45m'
    BG_CYN = '\033[46m'
    BG_WHT = '\033[47m'

# ┌─────────────────────────────────────────────────────────────────────┐
# │  Woody's Quote - Fresh from the Neurosis Factory                    │
# └─────────────────────────────────────────────────────────────────────┘
WOODY_QUOTE = (
    "I took a course in speed reading and finished 'War and Peace' "
    "in twenty minutes. It involves Russia."
)

# Alternative quotes (pick your poison)
QUOTES = [
    "I took a course in speed reading and finished 'War and Peace' in twenty minutes. It involves Russia.",
    "My therapist says I have a preoccupation with death. I told her that's absurd — I'm too busy dying to think about it.",
    "I don't believe in the afterlife, but I'm bringing a change of underwear just in case.",
    "Life is divided into the horrible and the miserable. The horrible are terminal cases. The miserable is everyone else. I'm grateful to be miserable.",
    "I'm not afraid of death. I just don't want to be there when it happens. Especially if there's a cover charge.",
    "The universe is indifferent. My mother, however, is very interested. She calls every Sunday to ask why the universe hasn't called.",
    "I have a hypochondriac's imagination. A headache is a tumor. A typo is early dementia. This code? Definitely a virus.",
    "Eternal nothingness is fine if you're dressed for it. I, however, am never dressed for anything.",
]

# ┌─────────────────────────────────────────────────────────────────────┐
# │  ASCII Art: Woody's Glasses (Iconic, Neurotic, Slightly Crooked)    │
# └─────────────────────────────────────────────────────────────────────┘
GLASSES_FRAMES = [
    r"""
     ╔═════════════════════════════════════════════════════════════╗
     ║  ▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄  ║
     ║  █  ╭─────────────╮     ╭─────────────╮  █  █              ║
     ║  █  │  ░░░░░░░░░  │     │  ░░░░░░░░░  │  █  █   *twitch*   ║
     ║  █  │  ░  WOODY  ░│     │  ░  SEES   ░│  █  █              ║
     ║  █  │  ░  DOOM   ░│     │  ░  DOOM   ░│  █  █              ║
     ║  █  ╰─────────────╯     ╰─────────────╯  █  █              ║
     ║  ▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀  ║
     ╚═════════════════════════════════════════════════════════════╝
    """,
    r"""
     ╔═════════════════════════════════════════════════════════════╗
     ║  ▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄  ║
     ║  █  ╭─────────────╮     ╭─────────────╮  █  █              ║
     ║  █  │  ░░░░░░░░░  │     │  ░░░░░░░░░  │  █  █   *blink*    ║
     ║  █  │  ░  WOODY  ░│     │  ░  SEES   ░│  █  █              ║
     ║  █  │  ░  DOOM   ░│     │  ░  DOOM   ░│  █  █              ║
     ║  █  ╰─────────────╯     ╰─────────────╯  █  █              ║
     ║  ▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀  ║
     ╚═════════════════════════════════════════════════════════════╝
    """,
]

# Neurotic thought bubbles
THOUGHT_BUBBLES = [
    "  (  )  ",
    " (    ) ",
    "(      )",
    " (    ) ",
    "  (  )  ",
]

# ┌─────────────────────────────────────────────────────────────────────┐
# │  Animation Utilities - Because Life Is a Series of Nervous Tics     │
# └─────────────────────────────────────────────────────────────────────┘
def hide_cursor():
    sys.stdout.write('\033[?25l')
    sys.stdout.flush()

def show_cursor():
    sys.stdout.write('\033[?25h')
    sys.stdout.flush()

def clear_screen():
    sys.stdout.write('\033[2J\033[H')
    sys.stdout.flush()

def move_cursor(y, x):
    sys.stdout.write(f'\033[{y};{x}H')
    sys.stdout.flush()

def save_cursor():
    sys.stdout.write('\033[s')
    sys.stdout.flush()

def restore_cursor():
    sys.stdout.write('\033[u')
    sys.stdout.flush()

def typewriter(text, delay=0.03, color=C.WHT, end_color=C.R, jitter=0.01):
    """Type text character by character with neurotic timing."""
    for char in text:
        sys.stdout.write(f'{color}{char}{end_color}')
        sys.stdout.flush()
        # Woody's typing is erratic - sometimes fast, sometimes *panic pause*
        if char in '.!?,':
            time.sleep(delay * 4)  # Dramatic pause
        elif char == ' ':
            time.sleep(delay * 0.5)
        else:
            time.sleep(delay + random.uniform(-jitter, jitter * 2))
    sys.stdout.write(end_color)
    sys.stdout.flush()

def pulse_color(text, colors, cycles=3, delay=0.15):
    """Make text pulse with anxiety."""
    for _ in range(cycles):
        for color in colors:
            sys.stdout.write(f'\r{color}{text}{C.R}')
            sys.stdout.flush()
            time.sleep(delay)

def breathe_animation(frames, cycles=2, delay=0.4):
    """Animate Woody's glasses breathing with anxiety."""
    for _ in range(cycles):
        for frame in frames:
            clear_screen()
            sys.stdout.write(frame)
            sys.stdout.flush()
            time.sleep(delay)

# ┌─────────────────────────────────────────────────────────────────────┐
# │  The Main Event: Woody's One-Man Show                               │
# └─────────────────────────────────────────────────────────────────────┘
def woody_intro():
    """Set the stage: dim lights, nervous energy, glasses adjust."""
    clear_screen()
    hide_cursor()
    
    # Opening nervous energy
    intro_lines = [
        (f"{C.D}{C.CYN}    *clears throat nervously*", 0.5),
        (f"{C.D}{C.CYN}    *adjusts glasses for the 47th time*", 0.5),
        (f"{C.D}{C.CYN}    *wonders if the glasses are prescription or just a prop*", 0.5),
        (f"{C.D}{C.CYN}    *realizes everything is a prop in this absurd theater*", 0.5),
        (f"{C.D}{C.CYN}    *has panic attack about the nature of props*", 0.5),
        ("", 0.3),
    ]
    
    for line, pause in intro_lines:
        sys.stdout.write(f'\r{line}')
        sys.stdout.flush()
        time.sleep(pause)
    
    # Glasses animation
    breathe_animation(GLASSES_FRAMES, cycles=2, delay=0.5)
    clear_screen()

def woody_quote_reveal(quote):
    """Reveal the quote with maximum neurotic flair."""
    # Draw the quote box
    box_width = 70
    padding = 2
    inner_width = box_width - 2 * padding - 2  # borders
    
    # Word wrap the quote
    words = quote.split()
    lines = []
    current = ""
    for word in words:
        test = current + (" " if current else "") + word
        if len(test) <= inner_width:
            current = test
        else:
            lines.append(current)
            current = word
    if current:
        lines.append(current)
    
    # Top border
    top = f"{C.MAG}╔{'═' * box_width}╗{C.R}"
    sys.stdout.write(top + "\n")
    sys.stdout.flush()
    time.sleep(0.2)
    
    # Empty line for breathing room
    empty = f"{C.MAG}║{C.R}{' ' * box_width}{C.MAG}║{C.R}"
    sys.stdout.write(empty + "\n")
    sys.stdout.flush()
    time.sleep(0.1)
    
    # Type each line
    for i, line in enumerate(lines):
        prefix = f"{C.MAG}║{C.R}  {C.YEL}{C.I}"
        suffix = f"{C.R}{' ' * (box_width - len(line) - 4)}{C.MAG}║{C.R}"
        
        sys.stdout.write(prefix)
        sys.stdout.flush()
        
        # Typewriter effect with Woody's rhythm
        typewriter(line, delay=0.025, color=C.YEL + C.I, end_color=C.R)
        
        sys.stdout.write(suffix + "\n")
        sys.stdout.flush()
        
        # Pause between lines - existential contemplation
        if i < len(lines) - 1:
            time.sleep(0.6)
            # Nervous tic
            sys.stdout.write(f"\r{C.MAG}║{C.R}  {C.D}*swallows hard*{C.R}{' ' * (box_width - 14)}{C.MAG}║{C.R}\n")
            sys.stdout.flush()
            time.sleep(0.3)
            # Go back up one line
            sys.stdout.write('\033[F\033[K')
            sys.stdout.write(prefix)
            typewriter(line, delay=0.01, color=C.YEL + C.I, end_color=C.R)
            sys.stdout.write(suffix + "\n")
            sys.stdout.flush()
    
    # Bottom empty line
    sys.stdout.write(empty + "\n")
    sys.stdout.flush()
    time.sleep(0.1)
    
    # Bottom border with signature
    sig = "— Woody Allen (probably, I didn't fact-check, I have anxiety)"
    sig_line = f"{C.MAG}║{C.R}  {C.D}{C.CYN}{sig}{C.R}{' ' * (box_width - len(sig) - 4)}{C.MAG}║{C.R}"
    sys.stdout.write(sig_line + "\n")
    sys.stdout.flush()
    time.sleep(0.2)
    
    bottom = f"{C.MAG}╚{'═' * box_width}╝{C.R}"
    sys.stdout.write(bottom + "\n")
    sys.stdout.flush()

def woody_aftermath():
    """Post-quote existential spiral."""
    time.sleep(1.5)
    
    aftermath = [
        (f"\n{C.D}{C.CYN}    *stares into the middle distance*", 0.8),
        (f"{C.D}{C.CYN}    *wonders if the quote was too long*", 0.6),
        (f"{C.D}{C.CYN}    *wonders if the quote was too short*", 0.6),
        (f"{C.D}{C.CYN}    *wonders if 'too long' and 'too short' are the same thing*", 0.8),
        (f"{C.D}{C.CYN}    *has existential crisis about string length*", 0.6),
        (f"{C.D}{C.CYN}    *remembers mortality*", 1.0),
        (f"\n{C.B}{C.RED}    *THE VOID STARES BACK*", 0.5),
        (f"{C.D}{C.CYN}    *adjusts glasses*", 0.4),
        (f"{C.D}{C.CYN}    *exits stage left, tripping over own shadow*", 0.6),
    ]
    
    for line, pause in aftermath:
        sys.stdout.write(f'\r{line}')
        sys.stdout.flush()
        time.sleep(pause)
    
    time.sleep(0.5)
    
    # Final fade
    final_messages = [
        f"{C.D}{C.BLK}    The universe remains indifferent. Your therapist called. She's worried.{C.R}",
        f"{C.D}{C.BLK}    Also, you left the stove on. Probably. Maybe. Definitely.{C.R}",
        f"{C.D}{C.BLK}    Goodnight, neurotic traveler.{C.R}",
    ]
    
    for msg in final_messages:
        sys.stdout.write(msg + "\n")
        sys.stdout.flush()
        time.sleep(0.4)

def main():
    """Orchestrate the neuroses."""
    try:
        # Pick a quote (or use the classic)
        quote = random.choice(QUOTES)
        
        # Run the show
        woody_intro()
        woody_quote_reveal(quote)
        woody_aftermath()
        
    except KeyboardInterrupt:
        # User fled the anxiety
        sys.stdout.write(f"\n\n{C.RED}*WOODY FLEES THE SCENE* {C.D}(you pressed Ctrl+C, how rude){C.R}\n")
    finally:
        show_cursor()
        sys.stdout.write(C.R)
        sys.stdout.flush()

# ┌─────────────────────────────────────────────────────────────────────┐
# │  Entry Point - The Show Must Go On (Unfortunately)                  │
# └─────────────────────────────────────────────────────────────────────┘
if __name__ == "__main__":
    # Check if terminal supports ANSI
    if not sys.stdout.isatty():
        # Fallback for non-TTY
        print(WOODY_QUOTE)
        sys.exit(0)
    
    main()