"""
Campbell's Soup Can #4157
Produced: 2026-07-11 13:54:17
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

# ┌─────────────────────────────────────────────────────────────┐
# │  ANSI Color Palette - Because life is meaningless,          │
# │  but at least it can be chromatically pleasing              │
# └─────────────────────────────────────────────────────────────┘
class C:
    R = '\033[0m'      # Reset (the only certainty)
    BOLD = '\033[1m'
    DIM = '\033[2m'
    ITALIC = '\033[3m'
    UNDER = '\033[4m'
    BLINK = '\033[5m'  # Existential panic mode
    REV = '\033[7m'
    
    # Foreground - the colors of our neuroses
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
    
    # Background - the void behind the colors
    BG_BLACK = '\033[40m'
    BG_RED = '\033[41m'
    BG_GREEN = '\033[42m'
    BG_YELLOW = '\033[43m'
    BG_BLUE = '\033[44m'
    BG_MAGENTA = '\033[45m'
    BG_CYAN = '\033[46m'
    BG_WHITE = '\033[47m'

def clear():
    """Clear screen - like repression, but for terminals"""
    print('\033[2J\033[H', end='')

def hide_cursor():
    print('\033[?25l', end='')

def show_cursor():
    print('\033[?25h', end='')

def move(y, x):
    print(f'\033[{y};{x}H', end='')

# ═══════════════════════════════════════════════════════════════
#  THE QUOTE - Hand-crafted neurotic wisdom
# ═══════════════════════════════════════════════════════════════
QUOTE = (
    "I took a course in existentialism, "
    "but the professor never showed up — "
    "which, frankly, was the most authentic lecture "
    "on the subject I've ever attended."
)

QUOTE_LINES = [
    "I took a course in existentialism,",
    "but the professor never showed up —",
    "which, frankly, was the most authentic lecture",
    "on the subject I've ever attended."
]

ATTRIBUTION = "— Woody Allen (probably, I didn't check, too anxious)"

# ═══════════════════════════════════════════════════════════════
#  ASCII ART - A bespectacled neurotic for your viewing pleasure
# ═══════════════════════════════════════════════════════════════
WOODY_FRAMES = [
    r"""
     ╭─────────────╮
     │  (•_•)      │
     │  <)  )>     │
     │  /  \       │
     ╰─────────────╯""",
    r"""
     ╭─────────────╮
     │  (•_•)      │
     │  <)  )>     │
     │   \ /       │
     ╰─────────────╯""",
    r"""
     ╭─────────────╮
     │  (•_•)      │
     │  <)  )>     │
     │  /  \       │
     ╰─────────────╯""",
]

WOODY_STATIC = r"""
     ╭─────────────────────╮
     │     (•_•)           │
     │     <)  )>  *sigh*  │
     │     /  \            │
     ╰─────────────────────╯"""

# ═══════════════════════════════════════════════════════════════
#  TYPING ANIMATION - Because certainty is an illusion
# ═══════════════════════════════════════════════════════════════
def type_line(line, color=C.WHITE, delay_range=(0.02, 0.06), prefix=""):
    """Type out a line with human-like imperfection"""
    sys.stdout.write(prefix)
    sys.stdout.flush()
    
    for i, char in enumerate(line):
        # Occasional hesitation - the soul's buffer overflow
        if random.random() < 0.03:
            time.sleep(random.uniform(0.15, 0.4))
            sys.stdout.write('\b \b')
            sys.stdout.flush()
            time.sleep(random.uniform(0.05, 0.15))
        
        sys.stdout.write(f"{color}{char}{C.R}")
        sys.stdout.flush()
        time.sleep(random.uniform(*delay_range))
    
    print()

def typewriter_quote():
    """Display the quote with dramatic typing"""
    colors = [C.CYAN, C.BRIGHT_CYAN, C.WHITE, C.BRIGHT_WHITE, C.YELLOW]
    
    print()
    for i, line in enumerate(QUOTE_LINES):
        color = colors[i % len(colors)]
        prefix = f"  {C.DIM}│ {C.R}"
        type_line(line, color=color, prefix=prefix)
        time.sleep(random.uniform(0.3, 0.6))
    
    # Attribution with extra neurosis
    time.sleep(0.5)
    print()
    attr_prefix = f"  {C.DIM}│ {C.ITALIC}{C.GRAY}"
    type_line(ATTRIBUTION, color=C.GRAY, delay_range=(0.015, 0.04), prefix=attr_prefix)
    print()

# ═══════════════════════════════════════════════════════════════
#  DECORATIVE ELEMENTS - Visual anxiety
# ═══════════════════════════════════════════════════════════════
def draw_box(width=62, color=C.CYAN, title=""):
    """Draw a pretty box because boundaries comfort us"""
    top = f"{color}╭{'─' * (width - 2)}╮{C.R}"
    bot = f"{color}╰{'─' * (width - 2)}╯{C.R}"
    mid = f"{color}│{' ' * (width - 2)}│{C.R}"
    return top, mid, bot

def pulse_text(text, color=C.YELLOW, times=3):
    """Pulse text like a heartbeat in an empty room"""
    for _ in range(times):
        print(f"\r{color}{C.BOLD}{text}{C.R}", end='', flush=True)
        time.sleep(0.4)
        print(f"\r{C.DIM}{text}{C.R}", end='', flush=True)
        time.sleep(0.3)
    print(f"\r{color}{C.BOLD}{text}{C.R}")

def scrolling_thoughts():
    """Background scrolling existential dread"""
    thoughts = [
        "What if I'm just a character in someone else's bad dream?",
        "Did I lock the door? Did I ever lock the door?",
        "The universe is expanding. So is my anxiety.",
        "I'm not paranoid. The universe really IS out to get me.",
        "Death is just nature's way of saying 'table for one, check please.'",
        "My therapist says I have a preoccupation with mortality. I said, 'Doc, isn't that the ONLY occupation?'",
        "I don't believe in an afterlife, but I'm bringing a change of underwear just in case.",
    ]
    
    for thought in thoughts:
        print(f"  {C.DIM}{C.ITALIC}› {thought}{C.R}")
        time.sleep(0.8)

# ═══════════════════════════════════════════════════════════════
#  MAIN SEQUENCE - The one-act play of our existence
# ═══════════════════════════════════════════════════════════════
def main():
    hide_cursor()
    clear()
    
    # ┌─ Opening: The void stares back ────────────────────────┐
    print(f"\n{C.BG_BLACK}{C.BRIGHT_CYAN}{C.BOLD}")
    print(" " * 60)
    print("   ▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄")
    print("   █  W O O D Y ' S   E X I S T E N T I A L   C L I N I C  █")
    print("   █▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀█")
    print("   █  \"The only thing worse than death is...                █")
    print("   █   wait, what was I saying? I had a thought.             █")
    print("   █   It was about mortality. Or maybe lunch.               █")
    print("   █   Does it matter? Nothing matters. Pass the rye.\"      █")
    print("   ▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀")
    print(" " * 60)
    print(f"{C.R}")
    
    time.sleep(1.5)
    
    # ┌─ Animated Woody ───────────────────────────────────────┐
    print(f"\n{C.CYAN}Initializing neurotic avatar...{C.R}\n")
    for _ in range(2):
        for frame in WOODY_FRAMES:
            clear()
            print(frame.replace("•", f"{C.YELLOW}•{C.CYAN}"))
            time.sleep(0.3)
    
    clear()
    print(WOODY_STATIC.replace("•", f"{C.YELLOW}•{C.CYAN}").replace("*sigh*", f"{C.DIM}*sigh*{C.CYAN}"))
    print(f"\n{C.DIM}  [Adjusting glasses... questioning reality...]{C.R}\n")
    time.sleep(1)
    
    # ┌─ The Quote ────────────────────────────────────────────┐
    top, mid, bot = draw_box(64, C.MAGENTA)
    print(top)
    
    # Empty line for breathing room
    print(mid)
    
    typewriter_quote()
    
    print(mid)
    print(bot)
    
    # ┌─ Post-quote existential spiral ────────────────────────┘
    print()
    pulse_text("  ◉ Processing absurdity...", C.YELLOW, 2)
    print()
    
    # Random neurotic afterthought
    afterthoughts = [
        "  Anyway, I have a 4 PM with my analyst. He charges $300/hour to tell me my mother was right.",
        "  You know, Socrates said the unexamined life is not worth living. But the examined life? Also exhausting.",
        "  I'd explain it further, but I'm late for a panic attack. Very exclusive. Invite only.",
        "  If you need me, I'll be in the corner, contemplating the heat death of the universe. And my cholesterol.",
    ]
    print(f"{C.DIM}{C.ITALIC}{random.choice(afterthoughts)}{C.R}")
    
    print()
    print(f"  {C.GRAY}Press Enter to return to the meaningless void...{C.R}")
    input()
    
    # ┌─ Farewell ─────────────────────────────────────────────┘
    clear()
    print(f"\n{C.BRIGHT_MAGENTA}{C.BOLD}")
    print("   ▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄")
    print("   █  Session complete. The universe remains indifferent.  █")
    print("   █  Your copay is $40. We accept cash, check, or guilt.  █")
    print("   ▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀")
    print(f"{C.R}\n")
    
    show_cursor()

# ═══════════════════════════════════════════════════════════════
#  ENTRY POINT - Where it all begins (and ends)
# ═══════════════════════════════════════════════════════════════
if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        show_cursor()
        clear()
        print(f"\n{C.RED}{C.BOLD}Interrupted. How very... final.{C.R}\n")
        sys.exit(0)
    except Exception as e:
        show_cursor()
        print(f"\n{C.RED}An error occurred. Typical. {e}{C.R}\n")
        sys.exit(1)