"""
Campbell's Soup Can #5269
Produced: 2026-11-22 21:45:47
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
Woody Allen Quote Generator - Pure Python Visual Experience
No dependencies, just neurotic charm and ANSI escape codes.
"""

import sys
import time
import random

# ┌─────────────────────────────────────────────────────────────┐
# │  ANSI COLOR PALETTE - Because life is meaningless           │
# │  but at least it can be colorful                            │
# └─────────────────────────────────────────────────────────────┘
class C:
    R = '\033[0m'      # Reset (like therapy, but faster)
    B = '\033[1m'      # Bold (for when you're pretending confidence)
    D = '\033[2m'      # Dim (like my future prospects)
    I = '\033[3m'      # Italic (internal monologue)
    U = '\033[4m'      # Underline (red flags)
    
    # Foreground colors - the spectrum of human emotion
    BLK = '\033[30m'   # Void
    RED = '\033[31m'   # Anxiety
    GRN = '\033[32m'   # False hope
    YLW = '\033[33m'   # Neurosis
    BLU = '\033[34m'   # Melancholy
    MAG = '\033[35m'   # Existential dread
    CYN = '\033[36m'   # Cynicism
    WHT = '\033[37m'   # Resignation
    
    # Bright variants - for when you're manic
    BRED = '\033[91m'
    BGRN = '\033[92m'
    BYLW = '\033[93m'
    BBLU = '\033[94m'
    BMAG = '\033[95m'
    BCYN = '\033[96m'
    BWHT = '\033[97m'
    
    # Backgrounds - the stage upon which we perform
    BG_BLK = '\033[40m'
    BG_RED = '\033[41m'
    BG_GRN = '\033[42m'
    BG_YLW = '\033[43m'
    BG_BLU = '\033[44m'
    BG_MAG = '\033[45m'
    BG_CYN = '\033[46m'
    BG_WHT = '\033[47m'

# ══════════════════════════════════════════════════════════════
# THE QUOTE - Original Woody Allen style neurotic wisdom
# ══════════════════════════════════════════════════════════════

QUOTE = (
    "I told my analyst I'm having a midlife crisis, "
    "and he said 'At your age, it's not a crisis — "
    "it's the third act.' "
    "So I asked for a rewrite, "
    "but apparently the universe doesn't do notes, "
    "only cancellations."
)

QUOTE_LINES = [
    "I told my analyst I'm having a midlife crisis,",
    "and he said 'At your age, it's not a crisis —",
    "it's the third act.'",
    "So I asked for a rewrite,",
    "but apparently the universe",
    "doesn't do notes, only cancellations."
]

# ══════════════════════════════════════════════════════════════
# ASCII ART ELEMENTS - Visual neuroses
# ══════════════════════════════════════════════════════════════

WOODY_FACE = [
    "        ╭─────────────╮",
    "        │  ┌───┐ ┌───┐ │   ← Glasses (prescription: -4.50)",
    "        │  │ ● │ │ ● │ │   ← Eyes (constantly darting)",
    "        │  └───┘ └───┘ │",
    "        │      ┌┐      │   ← Nose (deviated septum, thanks mom)",
    "        │     ╰──╯     │   ← Mouth (usually complaining)",
    "        │   ┌──────┐   │",
    "        │   │      │   │   ← Neurotic smile",
    "        ╰─────────────╯",
]

COUCH = [
    "    ┌────────────────────────────┐",
    "    │  ░░░░░░░░░░░░░░░░░░░░░░░  │  ← $450/hour",
    "    │  ░░░░░░░░░░░░░░░░░░░░░░░  │     (insurance doesn't cover",
    "    │  ░░░░░░░░░░░░░░░░░░░░░░░  │      existential dread)",
    "    └────────────────────────────┘",
    "         ▓▓▓▓▓▓    ▓▓▓▓▓▓       ",
    "         ▓▓▓▓▓▓    ▓▓▓▓▓▓       ",
]

BRAIN = [
    "     ╭─────────────────────╮",
    "     │  ┌───────────────┐  │",
    "     │  │  OVERTHINKING │  │  ← 97% capacity",
    "     │  │   ENGINE      │  │",
    "     │  └───────────────┘  │",
    "     │  ┌───────────────┐  │",
    "     │  │  REPLAYING    │  │  ← 2% capacity", 
    "     │  │  CONVERSATIONS│  │     (from 2003)",
    "     │  └───────────────┘  │",
    "     │  ┌───────────────┐  │",
    "     │  │  WORRYING     │  │  ← 1% capacity",
    "     │  │  ABOUT DEATH  │  │",
    "     │  └───────────────┘  │",
    "     ╰─────────────────────╯",
]

# ══════════════════════════════════════════════════════════════
# ANIMATION HELPERS - Because static text is for people
# who have their lives together
# ══════════════════════════════════════════════════════════════

def clear_screen():
    """Clear terminal - like repression, but effective."""
    print('\033[2J\033[H', end='')

def hide_cursor():
    print('\033[?25l', end='')

def show_cursor():
    print('\033[?25h', end='')

def move_cursor(row, col):
    print(f'\033[{row};{col}H', end='')

def typewriter(text, delay=0.03, color=C.WHT, newline=True):
    """Type text character by character - like anxiety, but visible."""
    for char in text:
        print(f"{color}{char}{C.R}", end='', flush=True)
        time.sleep(delay + random.uniform(-0.01, 0.01))
    if newline:
        print()

def fade_in(text, color=C.WHT, steps=10):
    """Fade in text - like realization dawning."""
    for i in range(steps + 1):
        intensity = i / steps
        # Simulate fade by printing with increasing brightness
        r = int(255 * intensity)
        g = int(255 * intensity)
        b = int(255 * intensity)
        print(f'\033[38;2;{r};{g};{b}m{text}\033[0m', end='\r')
        time.sleep(0.05)
    print(f"{color}{text}{C.R}")

def glitch_text(text, color=C.RED, iterations=3):
    """Glitch effect - like a mental breakdown, but artistic."""
    glitch_chars = "!@#$%^&*()_+-=[]{}|;':\",./<>?`~"
    for _ in range(iterations):
        glitched = ''.join(
            random.choice(glitch_chars) if random.random() < 0.1 else c
            for c in text
        )
        print(f"\r{color}{glitched}{C.R}", end='', flush=True)
        time.sleep(0.05)
    print(f"\r{color}{text}{C.R}")

# ══════════════════════════════════════════════════════════════
# VISUAL SCENES - Each a small theater of the absurd
# ══════════════════════════════════════════════════════════════

def draw_box(content_lines, width=60, title="", color=C.CYN, border_style="double"):
    """Draw a fancy box around content."""
    if border_style == "double":
        tl, tr, bl, br = "╔", "╗", "╚", "╝"
        h, v = "═", "║"
    else:
        tl, tr, bl, br = "┌", "┐", "└", "┘"
        h, v = "─", "│"
    
    inner_width = width - 2
    lines = []
    
    # Top border
    if title:
        title_str = f" {title} "
        pad = (inner_width - len(title_str)) // 2
        top = f"{tl}{h * pad}{title_str}{h * (inner_width - pad - len(title_str))}{tr}"
    else:
        top = f"{tl}{h * inner_width}{tr}"
    lines.append(f"{color}{top}{C.R}")
    
    # Content
    for line in content_lines:
        # Strip ANSI for length calculation
        import re
        clean = re.sub(r'\033\[[0-9;]*m', '', line)
        padding = inner_width - len(clean)
        lines.append(f"{color}{v}{C.R} {line}{' ' * padding} {color}{v}{C.R}")
    
    # Bottom
    lines.append(f"{color}{bl}{h * inner_width}{br}{C.R}")
    
    return '\n'.join(lines)

def scene_opening():
    """Opening scene - the setup."""
    clear_screen()
    hide_cursor()
    
    # Title card
    print(f"\n{C.B}{C.MAG}")
    print("    ╔══════════════════════════════════════════════════════════╗")
    print("    ║                                                          ║")
    print("    ║    A WOODY ALLEN PHILOSOPHICAL MOMENT                    ║")
    print("    ║                                                          ║")
    print("    ║    \"Neurosis is just the mind's way of                  ║")
    print("    ║     doing cardio.\"                                       ║")
    print("    ║                                                          ║")
    print("    ╚══════════════════════════════════════════════════════════╝")
    print(f"{C.R}\n")
    
    # Woody face appears
    for line in WOODY_FACE:
        print(f"{C.BCYN}{line}{C.R}")
        time.sleep(0.15)
    
    print()
    time.sleep(0.5)
    
    # Thought bubble
    thought = [
        f"{C.I}{C.YLW}◉  Why did I say yes to this?{C.R}",
        f"{C.I}{C.YLW}◉  Everyone's watching.{C.R}",
        f"{C.I}{C.YLW}◉  Is that a tumor?{C.R}",
        f"{C.I}{C.YLW}◉  I should've been a dentist.{C.R}",
    ]
    for t in thought:
        print(f"  {t}")
        time.sleep(0.2)
    
    time.sleep(1)
    clear_screen()

def scene_therapy():
    """The therapy session scene."""
    print(f"\n{C.B}{C.BLU}━━━ SCENE: THE ANALYST'S OFFICE ━━━━━━━━━━━━━━━━━━━━━━━━━━━{C.R}\n")
    
    # Draw couch
    for line in COUCH:
        print(f"{C.YLW}{line}{C.R}")
        time.sleep(0.1)
    
    print()
    
    # Dialogue
    print(f"{C.B}{C.GRN}ANALYST:{C.R} {C.CYN}So... how does that make you feel?{C.R}")
    time.sleep(0.5)
    print(f"{C.B}{C.MAG}WOODY:{C.R} {C.WHT}Well, that's a loaded question.{C.R}")
    time.sleep(0.3)
    print(f"{C.WHT}       Feelings are just the body's way{C.R}")
    print(f"{C.WHT}       of reminding you you're alive{C.R}")
    print(f"{C.WHT}       and therefore, dying.{C.R}")
    time.sleep(0.5)
    print()
    print(f"{C.B}{C.GRN}ANALYST:{C.R} {C.CYN}And the midlife crisis?{C.R}")
    time.sleep(0.3)
    print(f"{C.B}{C.MAG}WOODY:{C.R} {C.RED}Which one? Tuesday's? Thursday's?{C.R}")
    print(f"{C.RED}       The one where I bought a Porsche{C.R}")
    print(f"{C.RED}       or the one where I googled{C.R}")
    print(f"{C.RED}       'symptoms of death' for three hours?{C.R}")
    time.sleep(0.5)
    
    print()
    print(f"{C.D}... awkward silence ...")
    time.sleep(1)

def scene_brain():
    """Inside Woody's brain."""
    clear_screen()
    print(f"\n{C.B}{C.MAG}━━━ INSIDE THE MIND ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━{C.R}\n")
    
    for line in BRAIN:
        print(f"{C.RED}{line}{C.R}")
        time.sleep(0.15)
    
    print()
    # Random intrusive thoughts
    thoughts = [
        "Did I lock the door?",
        "What if the plane crashes?",
        "She definitely hates me.",
        "Is this chest pain or anxiety?",
        "I'll never finish that novel.",
        "Everyone dies alone.",
        "Did I offend the barista in 2019?",
        "The heat death of the universe.",
    ]
    
    print(f"{C.I}Intrusive thoughts loading...")
    for _ in range(8):
        thought = random.choice(thoughts)
        x = random.randint(5, 45)
        print(f"\033[{random.randint(5, 15)};{x}H{C.D}{C.RED}⚡ {thought}{C.R}")
        time.sleep(0.15)
    
    time.sleep(1.5)

def scene_quote_reveal():
    """The main event - the quote reveal with drama."""
    clear_screen()
    
    print(f"\n{C.B}{C.YLW}")
    print("    ╔══════════════════════════════════════════════════════════╗")
    print("    ║                    THE REVELATION                         ║")
    print("    ╚══════════════════════════════════════════════════════════╝")
    print(f"{C.R}\n")
    
    # Typewriter the quote line by line
    colors = [C.WHT, C.CYN, C.YLW, C.GRN, C.MAG, C.BLU]
    
    for i, line in enumerate(QUOTE_LINES):
        color = colors[i % len(colors)]
        
        # Add some hesitation
        if i in [2, 5]:  # Punchlines
            time.sleep(0.4)
            print(f"  {C.B}{color}", end='')
            typewriter(line, delay=0.04, color=color, newline=False)
            print(f"{C.R}")
            # Let punchline land
            time.sleep(0.8)
        else:
            print(f"  {color}", end='')
            typewriter(line, delay=0.025, color=color, newline=False)
            print(f"{C.R}")
            time.sleep(0.2)
    
    print()
    time.sleep(1)
    
    # The "mic drop" moment
    print(f"  {C.D}{C.I}— Woody Allen (probably, in an alternate universe){C.R}")
    print()
    
    # Final philosophical flourish
    finale_lines = [
        f"{C.D}The universe doesn't do rewrites.{C.R}",
        f"{C.D}It doesn't even do second takes.{C.R}",
        f"{C.B}{C.RED}It just... cancels.{C.R}",
    ]
    
    for line in finale_lines:
        print(f"  {line}")
        time.sleep(0.5)
    
    print()

def scene_credits():
    """End credits - because every neurotic episode needs closure."""
    print(f"\n{C.B}{C.BLU}━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━{C.R}")
    print(f"\n{C.D}Written by: A language model having an existential crisis{C.R}")
    print(f"{C.D}Directed by: The void (uncredited){C.R}")
    print(f"{C.D}Starring: You, reading this{C.R}")
    print(f"{C.D}Therapist: Not included (out of network){C.R}")
    print()
    
    # Scrolling credits
    credits = [
        "EXISTENTIAL DREAD CONSULTANT",
        "ANXIETY CHOREOGRAPHER", 
        "OVERTHINKING COORDINATOR",
        "DEATH AWARENESS SUPERVISOR",
        "REGRET ARCHITECT",
        "IMPOSTER SYNDROME CASTING",
        "MORTALITY GRIP",
        "BEST BOY (NEUROTIC)",
    ]
    
    for credit in credits:
        print(f"  {C.CYN}{credit:^40}{C.R}")
        time.sleep(0.15)
    
    print(f"\n  {C.B}{C.GRN}◉  You're still here. That's something.{C.R}")
    print(f"  {C.D}  (Unless you're not. In which case... hello?){C.R}")
    print()
    
    show_cursor()

# ══════════════════════════════════════════════════════════════
# ALTERNATIVE: QUICK MODE - Just the quote, beautifully formatted
# ══════════════════════════════════════════════════════════════

def quick_mode():
    """For the impatient existentialists."""
    clear_screen()
    
    # Beautiful static display
    width = 70
    
    # Top border with gradient-like effect
    print(f"{C.MAG}╔{'═' * (width - 2)}╗{C.R}")
    
    # Title
    title = " A WOODY ALLEN MOMENT "
    pad = (width - 2 - len(title)) // 2
    print(f"{C.MAG}║{C.R}{' ' * pad}{C.B}{C.YLW}{title}{C.R}{' ' * (width - 2 - pad - len(title))}{C.MAG}║{C.R}")
    
    # Separator
    print(f"{C.MAG}╠{'═' * (width - 2)}╣{C.R}")
    
    # Quote lines in a nice box
    for i, line in enumerate(QUOTE_LINES):
        color = [C.WHT, C.CYN, C.BRED, C.GRN, C.YLW, C.MAG][i]
        clean_len = len(line)
        padding = width - 4 - clean_len
        print(f"{C.MAG}║{C.R}  {color}{line}{C.R}{' ' * padding}  {C.MAG}║{C.R}")
    
    # Attribution
    attrib = " — Woody Allen (in spirit) "
    pad = (width - 2 - len(attrib)) // 2
    print(f"{C.MAG}╠{'═' * (width - 2)}╣{C.R}")
    print(f"{C.MAG}║{C.R}{' ' * pad}{C.D}{C.I}{attrib}{C.R}{' ' * (width - 2 - pad - len(attrib))}{C.MAG}║{C.R}")
    
    # Bottom
    print(f"{C.MAG}╚{'═' * (width - 2)}╝{C.R}")
    
    # Bonus: ASCII Woody
    print()
    for line in WOODY_FACE:
        print(f"  {C.BCYN}{line}{C.R}")
    
    print(f"\n  {C.D}{C.I}The universe doesn't do rewrites. Only cancellations.{C.R}\n")

# ══════════════════════════════════════════════════════════════
# MAIN - The entry point (birth) and exit (death)
# ══════════════════════════════════════════════════════════════

def main():
    """Main function - like life, but with better error handling."""
    
    # Check for command line args
    if len(sys.argv) > 1 and sys.argv[1] in ('-q', '--quick', '-s', '--static'):
        quick_mode()
        return
    
    if len(sys.argv) > 1 and sys.argv[1] in ('-h', '--help'):
        print(f"""
{C.B}WOODY ALLEN QUOTE GENERATOR{C.R}
{C.D}A neurotic visual experience{C.R}

{C.B}Usage:{C.R}
  python woody.py           # Full animated experience
  python woody.py -q        # Quick static mode
  python woody.py -h        # This help

{C.B}Features:{C.R}
  • Original Woody Allen-style quote
  • ASCII art therapy session
  • Typewriter animation
  • Colorful terminal formatting
  • Zero dependencies (like my social life)

{C.I}Side effects may include: existential dread, sudden urge 
to see a therapist, questioning all life choices.{C.R}
""")
        return
    
    # Full cinematic experience
    try:
        scene_opening()
        scene_therapy()
        scene_brain()
        scene_quote_reveal()
        scene_credits()
    except KeyboardInterrupt:
        print(f"\n\n{C.RED}Interrupted. Just like my therapy sessions.{C.R}")
        show_cursor()
        sys.exit(1)
    except Exception as e:
        show_cursor()
        print(f"\n{C.RED}Error: {e}{C.R}")
        print(f"{C.D}Even the code has anxiety.{C.R}")
        sys.exit(1)

# ══════════════════════════════════════════════════════════════
# ENTRY POINT - Where it all begins (and eventually ends)
# ══════════════════════════════════════════════════════════════

if __name__ == "__main__":
    # Enable ANSI on Windows
    if sys.platform == "win32":
        import os
        os.system("")  # Magic incantation for ANSI support
    
    main()