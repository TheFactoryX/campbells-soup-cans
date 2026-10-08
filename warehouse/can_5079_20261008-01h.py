"""
Campbell's Soup Can #5079
Produced: 2026-10-08 01:56:28
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
    D = '\033[90m'      # Dim/Gray
    BD = '\033[1m'      # Bold
    IT = '\033[3m'      # Italic
    UL = '\033[4m'      # Underline
    BL = '\033[5m'      # Blink
    RS = '\033[0m'      # Reset
    BG_D = '\033[100m'  # Dark gray background
    BG_B = '\033[44m'   # Blue background

# Woody Allen ASCII art
WOODY = f"""{C.C}{C.BD}
     ╔══════════════════════════════════════════════════════════════╗
     ║                                                              ║
     ║        {C.Y}██████╗ ██████╗  █████╗ ████████╗███████╗{C.C}        ║
     ║        {C.Y}██╔══██╗██╔══██╗██╔══██╗╚══██╔══╝██╔════╝{C.C}        ║
     ║        {C.Y}██████╔╝██████╔╝███████║   ██║   █████╗  {C.C}        ║
     ║        {C.Y}██╔═══╝ ██╔══██╗██╔══██║   ██║   ██╔══╝  {C.C}        ║
     ║        {C.Y}██║     ██║  ██║██║  ██║   ██║   ███████╗{C.C}        ║
     ║        {C.Y}╚═╝     ╚═╝  ╚═╝╚═╝  ╚═╝   ╚═╝   ╚══════╝{C.C}        ║
     ║                                                              ║
     ║         {C.W}██╗   ██╗ █████╗ ██╗   ██╗███████╗██████╗ {C.C}        ║
     ║         {C.W}██║   ██║██╔══██╗██║   ██║██╔════╝██╔══██╗{C.C}        ║
     ║         {C.W}██║   ██║███████║██║   ██║█████╗  ██████╔╝{C.C}        ║
     ║         {C.W}╚██╗ ██╔╝██╔══██║╚██╗ ██╔╝██╔══╝  ██╔══██╗{C.C}        ║
     ║         {C.W} ╚████╔╝ ██║  ██║ ╚████╔╝ ███████╗██║  ██║{C.C}        ║
     ║         {C.W}  ╚═══╝  ╚═╝  ╚═╝  ╚═══╝  ╚══════╝╚═╝  ╚═╝{C.C}        ║
     ║                                                              ║
     ║     {C.M}╭──────────────────────────────────────────────╮{C.C}     ║
     ║     │  {C.Y}◉{C.C}  {C.D}┌────────────────────────────────────┐{C.C} {C.Y}◉{C.C}  │     ║
     ║     │  {C.Y}│{C.C}  {C.W}  ▄▄▄▄▄▄▄  ▄▄▄▄▄▄▄  ▄▄▄▄▄▄▄  {C.C}{C.D}│{C.C} {C.Y}│{C.C}  │     ║
     ║     │  {C.Y}│{C.C}  {C.W} █       █ █       █ █       █ {C.C}{C.D}│{C.C} {C.Y}│{C.C}  │     ║
     ║     │  {C.Y}│{C.C}  {C.W} █  ● ●  █ █  ● ●  █ █  ● ●  █ {C.C}{C.D}│{C.C} {C.Y}│{C.C}  │     ║
     ║     │  {C.Y}│{C.C}  {C.W} █   ▽   █ █   ▽   █ █   ▽   █ {C.C}{C.D}│{C.C} {C.Y}│{C.C}  │     ║
     ║     │  {C.Y}│{C.C}  {C.W} █ ▓▓▓▓▓ █ █ ▓▓▓▓▓ █ █ ▓▓▓▓▓ █ {C.C}{C.D}│{C.C} {C.Y}│{C.C}  │     ║
     ║     │  {C.Y}│{C.C}  {C.W} █       █ █       █ █       █ {C.C}{C.D}│{C.C} {C.Y}│{C.C}  │     ║
     ║     │  {C.Y}│{C.C}  {C.W} ▀▀▀▀▀▀▀  ▀▀▀▀▀▀▀  ▀▀▀▀▀▀▀  {C.C}{C.D}│{C.C} {C.Y}│{C.C}  │     ║
     ║     │  {C.Y}│{C.C}  {C.D}└────────────────────────────────────┘{C.C} {C.Y}│{C.C}  │     ║
     ║     ╰──────────────────────────────────────────────╯      ║
     ║                                                              ║
     ║         {C.D}"I'm not a hypochondriac, I'm an... enthusiast"{C.C}      ║
     ║         {C.D}         {C.Y}— of catastrophic interpretations{C.C}          ║
     ║                                                              ║
     ╚══════════════════════════════════════════════════════════════╝
{C.RS}"""

QUOTE = (
    "I told my analyst I was having an identity crisis. "
    "He said, 'That'll be two hundred dollars.' "
    "I said, 'Who's asking?' "
    "He said, 'Your ego.' "
    "I said, 'My ego couldn't afford me... "
    "so I sent my superego to negotiate. "
    "It came back with a receipt and a lecture on fiscal responsibility.'"
)

def typewriter(text, delay_range=(0.01, 0.04), color=C.W):
    """Print text with typewriter effect"""
    for char in text:
        sys.stdout.write(f"{color}{char}{C.RS}")
        sys.stdout.flush()
        time.sleep(random.uniform(*delay_range))
    print()

def slow_type_lines(lines, base_delay=0.02, line_pause=0.4):
    """Type multiple lines with varying speeds"""
    for i, line in enumerate(lines):
        # Vary speed slightly per line
        delay = base_delay * random.uniform(0.8, 1.3)
        typewriter(line, delay_range=(delay * 0.7, delay * 1.3), color=C.W)
        if i < len(lines) - 1:
            time.sleep(line_pause * random.uniform(0.7, 1.2))

def breathe_box():
    """Make the box breathe with subtle color shifts"""
    colors = [C.C, C.B, C.M, C.B, C.C]
    for _ in range(3):
        for col in colors:
            sys.stdout.write(f"\r{col}█{C.RS}")
            sys.stdout.flush()
            time.sleep(0.15)

def sparkle(text, times=3):
    """Add sparkle effect around text"""
    sparkles = ['✦', '✧', '⋆', '✦', '✧']
    for _ in range(times):
        s1 = random.choice(sparkles)
        s2 = random.choice(sparkles)
        sys.stdout.write(f"\r{C.Y}{s1}{C.RS} {text} {C.Y}{s2}{C.RS}")
        sys.stdout.flush()
        time.sleep(0.3)
    print()

def main():
    # Clear screen
    sys.stdout.write('\033[2J\033[H')
    sys.stdout.flush()
    
    # Print Woody art
    print(WOODY)
    time.sleep(0.5)
    
    # Quote box top
    print(f"{C.M}╔{'═' * 70}╗{C.RS}")
    
    # Split quote into dramatic lines
    quote_lines = [
        "I told my analyst I was having an identity crisis.",
        "He said, 'That'll be two hundred dollars.'",
        "I said, 'Who's asking?'",
        "He said, 'Your ego.'",
        "I said, 'My ego couldn't afford me...",
        "so I sent my superego to negotiate.",
        "It came back with a receipt",
        "and a lecture on fiscal responsibility.'"
    ]
    
    # Type the quote with dramatic pauses
    for i, line in enumerate(quote_lines):
        if i == 4:  # The ellipsis line - slower
            typewriter(f"{C.M}║ {C.IT}{line}{C.RS}{C.M} {' ' * (68 - len(line))}║{C.RS}", 
                       delay_range=(0.03, 0.06), color='')
        elif i in [2, 3]:  # Dialogue lines - snappy
            typewriter(f"{C.M}║ {C.Y}{line}{C.RS}{C.M} {' ' * (68 - len(line))}║{C.RS}", 
                       delay_range=(0.015, 0.03), color='')
        else:
            typewriter(f"{C.M}║ {C.W}{line}{C.RS}{C.M} {' ' * (68 - len(line))}║{C.RS}", 
                       delay_range=(0.02, 0.04), color='')
        time.sleep(0.25 if i != 3 else 0.5)
    
    # Quote box bottom
    print(f"{C.M}╚{'═' * 70}╝{C.RS}")
    
    print()
    
    # Final philosophical punchline with sparkle
    time.sleep(0.4)
    punchlines = [
        "The universe doesn't bill by the hour...",
        "but my therapist definitely does.",
        "",
        "Existential dread: now accepting Visa, Mastercard, and Amex."
    ]
    
    for line in punchlines:
        if line:
            typewriter(f"{C.D}{C.IT}{' ' * 12}{line}{C.RS}", 
                       delay_range=(0.02, 0.05))
            time.sleep(0.3)
        else:
            print()
    
    print()
    
    # Little breathing animation at the end
    print(f"{C.D}    ────────────────────────────────────────────────────────────{C.RS}")
    print(f"{C.D}    {C.Y}◉{C.D}  Neurotic since 1935  •  Currently between crises  •  {C.Y}◉{C.RS}")
    print(f"{C.D}    ────────────────────────────────────────────────────────────{C.RS}")
    
    # Final cursor blink
    for _ in range(4):
        sys.stdout.write(f"\r{C.D}    {C.Y}▮{C.D}  Press Ctrl+C to continue spiraling... {C.Y}▮{C.RS}")
        sys.stdout.flush()
        time.sleep(0.4)
        sys.stdout.write(f"\r{C.D}    {C.Y}▯{C.D}  Press Ctrl+C to continue spiraling... {C.Y}▯{C.RS}")
        sys.stdout.flush()
        time.sleep(0.4)
    print()

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print(f"\n\n{C.R}{C.BD}Interrupted! The void stares back.{C.RS}")
        print(f"{C.D}Your analyst has been notified.{C.RS}\n")