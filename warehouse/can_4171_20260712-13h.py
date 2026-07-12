"""
Campbell's Soup Can #4171
Produced: 2026-07-12 13:56:24
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

# ANSI Color Codes
class C:
    R = '\033[91m'      # Red
    G = '\033[92m'      # Green
    Y = '\033[93m'      # Yellow
    B = '\033[94m'      # Blue
    M = '\033[95m'      # Magenta
    C = '\033[96m'      # Cyan
    W = '\033[97m'      # White
    D = '\033[90m'      # Dim
    BD = '\033[1m'      # Bold
    UL = '\033[4m'      # Underline
    BLINK = '\033[5m'   # Blink
    REV = '\033[7m'     # Reverse
    RS = '\033[0m'      # Reset
    CLR = '\033[2J'     # Clear screen
    HOME = '\033[H'     # Cursor home
    SAVE = '\033[s'     # Save cursor
    RESTORE = '\033[u'  # Restore cursor
    HIDE = '\033[?25l'  # Hide cursor
    SHOW = '\033[?25h'  # Show cursor

WOODY_QUOTES = [
    "I'm not afraid of death. I just don't want to be there when it happens.\n    — Plus, I'd hate to miss the ending of my own funeral. I hear the catering is terrible.",
    "Life is full of misery, loneliness, and suffering — and it's all over much too soon.\n    — Which is honestly a relief, because the buffet line was getting embarrassingly short.",
    "I don't want to achieve immortality through my work. I want to achieve it through not dying.\n    — So far, my strategy is working. Ask me again in 80 years. Or don't. I'll be dead.",
    "The universe is indifferent to our existence. Which is fine, because I'm indifferent to the universe's opinion.\n    — We have a mutual non-aggression pact. It ignores me, I ignore it. Works beautifully.",
    "I took a speed-reading course and read War and Peace in twenty minutes.\n    — It involves Russia. That's all I retained. Also, everyone dies. Spoiler alert: life.",
    "Eternal nothingness is fine if you happen to be dressed for it.\n    — I'm not. I'm wearing mismatched socks. The afterlife has a dress code, apparently.",
    "There is no question that there is an unseen world. The problem is, how far is it from midtown\n    and how late is it open? I need a parking spot. And a therapist. Preferably both.",
    "God is silent. Now if only man would shut up.\n    — I'd settle for my internal monologue taking a coffee break. Just five minutes. Please.",
    "I have a gnawing fear that I'm going to die alone. Or worse — surrounded by people\n    who want to tell me about their gluten intolerance. That's my personal hell.",
    "Death doesn't worry me. It's the stiffness afterward. And the paperwork.\n    — My accountant says I can't deduct 'existential dread' as a business expense. Unfair."
]

WOODY_ASCII = r"""
{C}       ╔═════════════════════════════════════════════════════════╗
       ║  {Y}██╗    ██╗ ██████╗ ██████╗ ██████╗ ███████╗{C}  ║
       ║  {Y}██║    ██║██╔═══██╗██╔══██╗██╔══██╗██╔════╝{C}  ║
       ║  {Y}██║ █╗ ██║██║   ██║██████╔╝██║  ██║█████╗  {C}  ║
       ║  {Y}██║███╗██║██║   ██║██╔══██╗██║  ██║██╔══╝  {C}  ║
       ║  {Y}╚███╔███╔╝╚██████╔╝██║  ██║██████╔╝███████╗{C}  ║
       ║  {Y} ╚══╝╚══╝  ╚═════╝ ╚═╝  ╚═╝╚═════╝ ╚══════╝{C}  ║
       ║                                                      ║
       ║  {M}███████╗███████╗██████╗ ██╗   ██╗███████╗██████╗ {C}  ║
       ║  {M}██╔════╝██╔════╝██╔══██╗██║   ██║██╔════╝██╔══██╗{C}  ║
       ║  {M}███████╗█████╗  ██████╔╝██║   ██║█████╗  ██████╔╝{C}  ║
       ║  {M}╚════██║██╔══╝  ██╔══██╗██║   ██║██╔══╝  ██╔══██╗{C}  ║
       ║  {M}███████║███████╗██║  ██║╚██████╔╝███████╗██║  ██║{C}  ║
       ║  {M}╚══════╝╚══════╝╚═╝  ╚═╝ ╚═════╝ ╚══════╝╚═╝  ╚═╝{C}  ║
       ╚═════════════════════════════════════════════════════════╝
{RS}
"""

GLASSES = r"""
{C}          .--.       .--.
         /    \     /    \
        |  {}  |   |  {}  |
        |      |   |      |
         \    /     \    /
          `--'       `--'
{RS}
"""

THOUGHT_BUBBLE = """
{C}        .--.
       /    \\
      |  💭  |
       \    /
        `--'
{RS}
"""

def typewriter(text, delay=0.015, color=C.W):
    """Print text with typewriter effect"""
    for char in text:
        sys.stdout.write(f"{color}{char}{C.RS}")
        sys.stdout.flush()
        time.sleep(delay)
    print()

def fade_in(text, color=C.W, steps=10):
    """Fade in text by gradually increasing brightness"""
    for i in range(steps + 1):
        sys.stdout.write(f"\r{color}{text}{C.RS}")
        sys.stdout.flush()
        time.sleep(0.03)
    print()

def blink_text(text, color=C.Y, times=3, interval=0.4):
    """Make text blink"""
    for _ in range(times):
        sys.stdout.write(f"\r{color}{C.BLINK}{text}{C.RS}")
        sys.stdout.flush()
        time.sleep(interval)
        sys.stdout.write(f"\r{' ' * len(text)}")
        sys.stdout.flush()
        time.sleep(interval)
    sys.stdout.write(f"\r{color}{text}{C.RS}\n")
    sys.stdout.flush()

def draw_box(content_lines, width=70, border_color=C.C, title="", title_color=C.Y):
    """Draw a fancy box around content"""
    h = border_color + "═" + C.RS
    v = border_color + "║" + C.RS
    tl = border_color + "╔" + C.RS
    tr = border_color + "╗" + C.RS
    bl = border_color + "╚" + C.RS
    br = border_color + "╝" + C.RS
    
    inner_width = width - 4
    
    # Top border with optional title
    if title:
        title_str = f" {title_color}{title}{C.RS} "
        title_len = len(title) + 2
        left_pad = (width - title_len) // 2
        right_pad = width - title_len - left_pad
        print(f"{tl}{h * left_pad}{title_str}{h * right_pad}{tr}")
    else:
        print(f"{tl}{h * (width - 2)}{tr}")
    
    # Content lines
    for line in content_lines:
        # Calculate visible length (strip ANSI codes for padding)
        import re
        clean = re.sub(r'\033\[[0-9;]*m', '', line)
        padding = inner_width - len(clean)
        print(f"{v}  {line}{' ' * max(0, padding)}  {v}")
    
    # Bottom border
    print(f"{bl}{h * (width - 2)}{br}")

def neurotic_loading():
    """Show a neurotic loading animation"""
    thoughts = [
        "Analyzing mortality...",
        "Checking if I left the stove on...",
        "Wondering if that mole is cancer...",
        "Replaying awkward conversation from 2003...",
        "Calculating probability of divine retribution...",
        "Debating whether existence is a typo...",
        "Questioning why I'm even running this script...",
        "Considering a career in professional worrying...",
    ]
    
    print(f"\n{C.D}Initializing Woody Allen consciousness...{C.RS}\n")
    for i, thought in enumerate(thoughts):
        spinner = ["⠋", "⠙", "⠹", "⠸", "⠼", "⠴", "⠦", "⠧", "⠇", "⠏"]
        for _ in range(8):
            for s in spinner:
                sys.stdout.write(f"\r{C.M}{s} {C.D}{thought}{C.RS}")
                sys.stdout.flush()
                time.sleep(0.02)
        sys.stdout.write(f"\r{C.G}✓{C.RS} {C.D}{thought}{C.RS}\n")
        sys.stdout.flush()
    print()

def main():
    # Clear screen and hide cursor
    sys.stdout.write(C.CLR + C.HOME + C.HIDE)
    sys.stdout.flush()
    
    try:
        # Pick a random quote
        quote = random.choice(WOODY_QUOTES)
        
        # Show ASCII art title
        print(WOODY_ASCII.format(C=C, Y=C.Y, M=C.M, RS=C.RS))
        time.sleep(0.5)
        
        # Show glasses
        print(GLASSES.format(C=C, RS=C.RS))
        time.sleep(0.3)
        
        # Neurotic loading
        neurotic_loading()
        
        # Draw the quote in a fancy box
        quote_lines = quote.split('\n')
        draw_box(quote_lines, width=78, border_color=C.M, title=" WOODY SEZ ", title_color=C.Y + C.BD)
        
        print()
        
        # Thought bubble with extra commentary
        extra_thoughts = [
            f"{C.D}← This is fine. Everything is fine. {C.R}{C.BLINK}PANIC{C.RS}{C.D} ←",
            f"{C.D}My therapist says I have 'catastrophic thinking.' I told her:{C.RS}",
            f"{C.Y}'That's not a bug, it's a survival mechanism.'{C.RS}",
            f"{C.D}She billed me for the session. The catastrophe continues.{C.RS}",
        ]
        
        for thought in extra_thoughts:
            typewriter(f"  {thought}", delay=0.01, color=C.W)
            time.sleep(0.3)
        
        print()
        
        # Final sign-off with blink
        signoff = "◦ • ●  Remember: You're not paranoid if the universe IS out to get you.  ● • ◦"
        blink_text(signoff, color=C.C, times=2)
        
        print()
        print(f"{C.D}    — Written by a neurotic algorithm with abandonment issues{C.RS}")
        print(f"{C.D}    — No existential crises were harmed in the making of this output{C.RS}")
        print()
        
    finally:
        # Show cursor again
        sys.stdout.write(C.SHOW)
        sys.stdout.flush()

if __name__ == "__main__":
    main()