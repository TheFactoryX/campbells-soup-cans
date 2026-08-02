"""
Campbell's Soup Can #4409
Produced: 2026-08-02 09:21:19
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
Woody Allen Philosophical Quote Generator
Neurotic wisdom with visual flair
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
    IT = '\033[3m'      # Italic
    UL = '\033[4m'      # Underline
    BL = '\033[5m'      # Blink
    RS = '\033[0m'      # Reset
    CLR = '\033[2J\033[H'  # Clear screen

# Woody Allen style quotes (original, in his voice)
QUOTES = [
    "I took a course in speed reading and finished 'War and Peace' in twenty minutes. It involves Russia.",
    "My one regret in life is that I'm not someone else. Preferably someone with better health insurance.",
    "I don't believe in an afterlife, but I'm bringing a change of underwear just in case.",
    "The universe is indifferent to my existence, which is frankly a relief—imagine the paperwork if it cared.",
    "I have a hypochondriac's imagination and a stoic's budget. My doctor sends me Christmas cards. Bills, but still.",
    "Death is nature's way of telling you to slow down. I'd prefer a strongly worded letter.",
    "I'm at two with nature. Mostly because nature keeps sneezing on me.",
    "If only God would give me a clear sign—like a large deposit in my Swiss bank account.",
    "My analyst says I have a preoccupation with mortality. I told him, 'Doc, at my age, mortality has a preoccupation with ME.'",
    "I'd call myself a pessimist, but that implies I expect things to go wrong. I KNOW they'll go wrong. I'm a realist with anxiety.",
    "The talent for being happy is appreciating what you have, instead of what you don't have. I have acid reflux. I appreciate it deeply.",
    "I don't want to achieve immortality through my work. I want to achieve it through not dying. Failing that, a really good plastic surgeon.",
    "Life is divided into the horrible and the miserable. The horrible are terminal illnesses. The miserable is everyone else. I'm miserable. Thank God.",
    "I can't listen to Wagner. It makes me want to conquer Poland. I can't listen to Mozart. It makes me want to write a check I can't cover.",
    "There is no question that there is an unseen world. The problem is, how far is it from midtown and how late is it open?",
]

def typewriter(text, color=C.W, delay=0.02, end='\n'):
    """Print text with typewriter effect"""
    for char in text:
        sys.stdout.write(f"{color}{char}{C.RS}")
        sys.stdout.flush()
        time.sleep(delay)
    print(end=end)

def print_slow_lines(lines, colors=None, delay=0.03, line_delay=0.3):
    """Print multiple lines with typewriter effect"""
    for i, line in enumerate(lines):
        color = colors[i] if colors else C.W
        typewriter(line, color, delay)
        time.sleep(line_delay)

def draw_box(content_lines, width=70, border_color=C.C, title="", title_color=C.Y):
    """Draw a fancy box around content"""
    horizontal = "═" * (width - 2)
    top = f"{border_color}╔{horizontal}╗{C.RS}"
    bottom = f"{border_color}╚{horizontal}╝{C.RS}"
    
    print(top)
    
    if title:
        padding = (width - 2 - len(title)) // 2
        title_line = f"{border_color}║{C.RS}{' ' * padding}{title_color}{C.BD}{title}{C.RS}{' ' * (width - 2 - padding - len(title))}{border_color}║{C.RS}"
        print(title_line)
        separator = f"{border_color}╠{horizontal}╣{C.RS}"
        print(separator)
    
    for line in content_lines:
        visible_len = len(line.replace('\033[91m','').replace('\033[92m','').replace('\033[93m','').replace('\033[94m','').replace('\033[95m','').replace('\033[96m','').replace('\033[97m','').replace('\033[90m','').replace('\033[1m','').replace('\033[3m','').replace('\033[4m','').replace('\033[5m','').replace('\033[0m',''))
        padding = width - 2 - visible_len
        print(f"{border_color}║{C.RS} {line}{' ' * padding}{border_color}║{C.RS}")
    
    print(bottom)

def animate_woody_face(frames=3):
    """Simple ASCII Woody animation"""
    faces = [
        f"""
{C.Y}     ╭─────────╮
    │ {C.W}@   @{C.Y} │
    │ {C.W}  >  {C.Y} │
    │ {C.W} \\_/ {C.Y} │
     ╰─────────╯{C.RS}
        {C.D}||{C.RS}
       {C.D}||{C.RS}
      {C.D}||{C.RS}""",
        f"""
{C.Y}     ╭─────────╮
    │ {C.W}@   @{C.Y} │
    │ {C.W}  -  {C.Y} │
    │ {C.W}  |  {C.Y} │
     ╰─────────╯{C.RS}
        {C.D}||{C.RS}
       {C.D}||{C.RS}
      {C.D}||{C.RS}""",
        f"""
{C.Y}     ╭─────────╮
    │ {C.W}@   @{C.Y} │
    │ {C.W}  o  {C.Y} │
    │ {C.W} / \\ {C.Y} │
     ╰─────────╯{C.RS}
        {C.D}||{C.RS}
       {C.D}||{C.RS}
      {C.D}||{C.RS}""",
    ]
    
    for _ in range(frames):
        for face in faces:
            print(C.CLR, end='')
            print(face)
            time.sleep(0.4)

def main():
    # Pick a random quote
    quote = random.choice(QUOTES)
    
    # Clear screen
    print(C.CLR, end='')
    
    # Animated Woody intro
    print(f"{C.C}{C.BD}")
    print("     ╔══════════════════════════════════════════════════════════════╗")
    print("     ║                                                              ║")
    print("     ║     W O O D Y   A L L E N   W I S D O M   G E N E R A T O R  ║")
    print("     ║                                                              ║")
    print("     ╚══════════════════════════════════════════════════════════════╝")
    print(f"{C.RS}")
    
    time.sleep(0.5)
    
    # Typewriter intro
    typewriter(f"{C.M}{C.IT}Neurotic existential crisis loading...{C.RS}", C.M, 0.03)
    time.sleep(0.3)
    typewriter(f"{C.D}[████████████████████] 100% - Anxiety confirmed{C.RS}", C.D, 0.01)
    print()
    time.sleep(0.4)
    
    # The quote in a fancy box
    quote_lines = []
    words = quote.split()
    line = ""
    max_width = 64
    
    for word in words:
        if len(line) + len(word) + 1 <= max_width:
            line += (" " if line else "") + word
        else:
            quote_lines.append(line)
            line = word
    if line:
        quote_lines.append(line)
    
    # Add some visual flair to the quote lines
    styled_lines = []
    for i, qline in enumerate(quote_lines):
        if i == 0:
            styled_lines.append(f"{C.W}{C.BD}{qline}{C.RS}")
        elif i == len(quote_lines) - 1:
            styled_lines.append(f"{C.W}{C.IT}{qline}{C.RS}")
        else:
            styled_lines.append(f"{C.W}{qline}{C.RS}")
    
    draw_box(styled_lines, width=70, border_color=C.C, title=f"{C.Y}{C.BD}WOODY SAYS{C.RS}", title_color=C.Y)
    
    print()
    
    # Woody's signature with animation
    signatures = [
        f"{C.D}— Woody Allen (probably){C.RS}",
        f"{C.D}— As dictated to my analyst, Dr. $450/hour{C.RS}",
        f"{C.D}— Written between panic attacks{C.RS}",
        f"{C.D}— Copyright 2024, Anxiety Industries Inc.{C.RS}",
    ]
    
    sig = random.choice(signatures)
    typewriter(f"                    {sig}", C.D, 0.02)
    print()
    print()
    
    # Final philosophical nugget
    final_thoughts = [
        f"{C.D}{C.IT}\"I'd explain it further, but my neurosis has a prior engagement.\"{C.RS}",
        f"{C.D}{C.IT}\"If you understood this, you're not paying enough for therapy.\"{C.RS}",
        f"{C.D}{C.IT}\"The joke's on you—I'm the one who has to live with me.\"{C.RS}",
    ]
    
    time.sleep(0.5)
    typewriter(f"         {random.choice(final_thoughts)}", C.D, 0.02)
    print()
    print()
    
    # Tiny Woody face at the end
    print(f"{C.Y}                    ╭─────╮")
    print(f"                    │ {C.W}@ @{C.Y} │")
    print(f"                    │ {C.W} > {C.Y}  │")
    print(f"                    │ {C.W}\\_/{C.Y} │")
    print(f"                    ╰─────╯{C.RS}")

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print(f"\n{C.R}{C.BD}Interrupted! Even my code has commitment issues.{C.RS}")
        sys.exit(0)