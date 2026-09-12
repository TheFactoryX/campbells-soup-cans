"""
Campbell's Soup Can #4947
Produced: 2026-09-12 05:47:59
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
A Woody Allen moment of existential dread, beautifully formatted.
No dependencies. Just pure, neurotic Python.
"""

import sys
import time
import random

# ═══════════════════════════════════════════════════════════════
# ANSI COLOR PALETTE — because life is meaningless, but at least it's colorful
# ═══════════════════════════════════════════════════════════════
class C:
    R = '\033[0m'      # Reset (like therapy, but faster)
    B = '\033[1m'      # Bold
    D = '\033[2m'      # Dim (for mumbling to yourself)
    I = '\033[3m'      # Italic (internal monologue)
    U = '\033[4m'      # Underline
    
    # Foregrounds
    BLACK   = '\033[30m'
    RED     = '\033[31m'
    GREEN   = '\033[32m'
    YELLOW  = '\033[33m'
    BLUE    = '\033[34m'
    MAGENTA = '\033[35m'
    CYAN    = '\033[36m'
    WHITE   = '\033[37m'
    
    # Bright foregrounds (for when you're manic)
    BBLACK   = '\033[90m'
    BRED     = '\033[91m'
    BGREEN   = '\033[92m'
    BYELLOW  = '\033[93m'
    BBLUE    = '\033[94m'
    BMAGENTA = '\033[95m'
    BCYAN    = '\033[96m'
    BWHITE   = '\033[97m'
    
    # Backgrounds (for when you need a safety blanket)
    BG_BLACK   = '\033[40m'
    BG_RED     = '\033[41m'
    BG_GREEN   = '\033[42m'
    BG_YELLOW  = '\033[43m'
    BG_BLUE    = '\033[44m'
    BG_MAGENTA = '\033[45m'
    BG_CYAN    = '\033[46m'
    BG_WHITE   = '\033[47m'

# ═══════════════════════════════════════════════════════════════
# WOODY ASCII ART — glasses, neuroses, and all
# ═══════════════════════════════════════════════════════════════
WOODY = r"""
        ╭─────────────────────────────────────────────╮
        │  ▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄  │
        │  █  ▄▄▄▄▄▄▄  █  ▄▄▄▄▄▄▄  █  ▄▄▄▄▄▄▄  █  ▄▄▄▄▄▄▄  █  │
        │  █  █     █  █  █     █  █  █     █  █  █     █  █  │
        │  █  █     █  █  █     █  █  █     █  █  █     █  █  │
        │  █  ▀▀▀▀▀▀▀  █  ▀▀▀▀▀▀▀  █  ▀▀▀▀▀▀▀  █  ▀▀▀▀▀▀▀  █  │
        │  ▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀  │
        │        ▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄        │
        │        █  ▄▄▄▄▄▄▄  █  ▄▄▄▄▄▄▄  █  ▄▄▄▄▄▄▄  █        │
        │        █  █     █  █  █     █  █  █     █  █        │
        │        █  ▀▀▀▀▀▀▀  █  ▀▀▀▀▀▀▀  █  ▀▀▀▀▀▀▀  █        │
        │        ▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀        │
        │              ▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄                  │
        │              █  ▄▄▄▄▄▄▄  █  ▄▄▄▄▄▄▄  █              │
        │              █  █     █  █  █     █  █              │
        │              █  ▀▀▀▀▀▀▀  █  ▀▀▀▀▀▀▀  █              │
        │              ▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀                  │
        ╰─────────────────────────────────────────────╯
                    │  ┌─────────────┐  │
                    │  │  ┌─────┐    │  │
                    │  │  │  ●  │    │  │  ← My analyst says
                    │  │  └─────┘    │  │     this represents
                    │  └─────────────┘  │     my mother
                    └───────────────────┘
"""

# ═══════════════════════════════════════════════════════════════
# THE QUOTE — hand-crafted neurotic perfection
# ═══════════════════════════════════════════════════════════════
QUOTE = (
    "I told my therapist I'm having an existential crisis. "
    "He said, 'That'll be $200.' "
    "I said, 'Can I pay you in repressed memories?' "
    "He said, 'We don't accept those — they bounce.'"
)

ATTRIBUTION = "— Woody Allen, probably, during a panic attack at 3 AM"

# ═══════════════════════════════════════════════════════════════
# HELPER FUNCTIONS — because even code needs coping mechanisms
# ═══════════════════════════════════════════════════════════════
def clear_screen():
    """Clear the terminal. Like repression, but for pixels."""
    print('\033[2J\033[H', end='')

def hide_cursor():
    print('\033[?25l', end='')

def show_cursor():
    print('\033[?25h', end='')

def move_cursor(y, x):
    print(f'\033[{y};{x}H', end='')

def typewriter(text, delay=0.02, color=C.WHITE, newline=True):
    """Type out text character by character. Like anxiety, but intentional."""
    for char in text:
        print(f"{color}{char}{C.R}", end='', flush=True)
        time.sleep(delay + random.uniform(-0.005, 0.005))
    if newline:
        print()

def slow_print(lines, delay=0.015, color=C.WHITE):
    """Print multiple lines with a slight delay between them."""
    for line in lines:
        typewriter(line, delay=delay, color=color)
        time.sleep(0.05)

def draw_box(title, content_lines, width=70, title_color=C.BCYAN, content_color=C.WHITE, border_color=C.BBLACK):
    """Draw a pretty box. Boundaries are healthy."""
    print(f"{border_color}╭{'─' * (width - 2)}╮{C.R}")
    print(f"{border_color}│{C.R} {title_color}{C.B}{title.center(width - 4)}{C.R} {border_color}│{C.R}")
    print(f"{border_color}├{'─' * (width - 2)}┤{C.R}")
    for line in content_lines:
        padded = f" {line.ljust(width - 4)} "
        print(f"{border_color}│{C.R}{content_color}{padded}{C.R}{border_color}│{C.R}")
    print(f"{border_color}╰{'─' * (width - 2)}╯{C.R}")

# ═══════════════════════════════════════════════════════════════
# ANIMATION SEQUENCES — for that cinematic neuroses feel
# ═══════════════════════════════════════════════════════════════
def animate_thinking():
    """Show a little thinking animation. The gears are turning. Rusty gears."""
    frames = [
        f"{C.BBLACK}  (•_•)  {C.R}",
        f"{C.YELLOW}  ( •_•)>⌐■-■  {C.R}",
        f"{C.BYELLOW}  (⌐■_■)  {C.R}",
        f"{C.GREEN}  (⌐■_■)👉  {C.R}",
    ]
    for _ in range(2):
        for frame in frames:
            print(f"\r{frame}", end='', flush=True)
            time.sleep(0.3)
    print("\r" + " " * 20 + "\r", end='')

def animate_typing_indicator(duration=1.5):
    """Show typing dots. Like waiting for a text back from the void."""
    dots = ["", ".", "..", "..."]
    end_time = time.time() + duration
    i = 0
    while time.time() < end_time:
        print(f"\r{C.D}{C.BBLACK}Contemplating mortality{dots[i % 4]}{C.R}", end='', flush=True)
        time.sleep(0.3)
        i += 1
    print("\r" + " " * 30 + "\r", end='')

def glitch_text(text, intensity=0.1):
    """Briefly glitch the text. Reality is unstable."""
    glitch_chars = "!@#$%^&*()_+-=[]{}|;':\",./<>?"
    result = ""
    for char in text:
        if random.random() < intensity and char != ' ':
            result += random.choice(glitch_chars)
        else:
            result += char
    return result

# ═══════════════════════════════════════════════════════════════
# MAIN SHOW — where the magic (and panic) happens
# ═══════════════════════════════════════════════════════════════
def main():
    # Check if terminal supports colors
    if not sys.stdout.isatty():
        # Fallback for non-TTY
        print(QUOTE)
        print(ATTRIBUTION)
        return

    hide_cursor()
    clear_screen()
    
    try:
        # ═══ ACT 1: The Entrance ═══
        # Print Woody ASCII art with color
        print(f"{C.CYAN}{C.B}")
        for line in WOODY.strip().split('\n'):
            print(line)
            time.sleep(0.03)
        print(f"{C.R}")
        
        time.sleep(0.5)
        
        # ═══ ACT 2: The Buildup ═══
        print()
        animate_typing_indicator(1.2)
        
        # Nervous intro
        intros = [
            f"{C.D}{C.I}So... I was thinking...{C.R}",
            f"{C.D}{C.I}Which is always a mistake.{C.R}",
            f"{C.D}{C.I}But I thought: what if the universe is just...{C.R}",
            f"{C.D}{C.I}a really badly written sitcom?{C.R}",
            f"{C.D}{C.I}And I'm the neurotic neighbor who gets no laugh track?{C.R}",
        ]
        slow_print(intros, delay=0.02, color=C.BBLACK)
        
        print()
        time.sleep(0.4)
        
        # ═══ ACT 3: The Quote — The Main Event ═══
        # Draw a fancy box for the quote
        quote_lines = []
        words = QUOTE.split(' ')
        current_line = ""
        max_width = 64
        
        for word in words:
            if len(current_line) + len(word) + 1 <= max_width:
                current_line += (" " + word) if current_line else word
            else:
                quote_lines.append(current_line)
                current_line = word
        if current_line:
            quote_lines.append(current_line)
        
        print()
        draw_box(
            " A Moment of Clarity (Panic) ",
            quote_lines,
            width=70,
            title_color=C.BYELLOW + C.B,
            content_color=C.WHITE + C.B,
            border_color=C.MAGENTA
        )
        
        print()
        time.sleep(0.3)
        
        # ═══ ACT 4: The Attribution ═══
        typewriter(f"{C.D}{C.I}{ATTRIBUTION}{C.R}", delay=0.015, color=C.BBLACK)
        
        print()
        print()
        
        # ═══ ACT 5: The Aftermath — a little extra flavor ═══
        aftermath_thoughts = [
            f"{C.D}Anyway...{C.R}",
            f"{C.D}I should probably go.{C.R}",
            f"{C.D}My analyst says I have a 'fear of commitment.'{C.R}",
            f"{C.D}I told him, 'I'm committed — to my anxiety.'{C.R}",
            f"{C.D}He raised his rates.{C.R}",
        ]
        slow_print(aftermath_thoughts, delay=0.025, color=C.BBLACK)
        
        print()
        print()
        
        # ═══ ACT 6: Final flourish — a blinking cursor of existential dread ═══
        print(f"{C.BBLACK}Press Ctrl+C to escape existence... or just close the terminal.{C.R}")
        print()
        
        # Blinking underscore
        show_cursor()
        for _ in range(10):
            print(f"\r{C.RED}{C.B}_ {C.R}", end='', flush=True)
            time.sleep(0.4)
            print(f"\r{C.RED}{C.B}  {C.R}", end='', flush=True)
            time.sleep(0.4)
        print()
        
    except KeyboardInterrupt:
        print(f"\n\n{C.YELLOW}Fine. Leave. Everyone leaves eventually.{C.R}")
        print(f"{C.D}...I'm used to it.{C.R}\n")
    finally:
        show_cursor()

# ═══════════════════════════════════════════════════════════════
# ENTRY POINT — where it all begins (and ends)
# ═══════════════════════════════════════════════════════════════
if __name__ == "__main__":
    # Seed random for reproducible glitches (or don't, chaos is fine)
    random.seed(time.time())
    main()