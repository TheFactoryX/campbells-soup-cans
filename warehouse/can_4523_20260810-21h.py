"""
Campbell's Soup Can #4523
Produced: 2026-08-10 21:02:09
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

# ANSI Colors
class C:
    R = '\033[91m'
    G = '\033[92m'
    Y = '\033[93m'
    B = '\033[94m'
    M = '\033[95m'
    C = '\033[96m'
    W = '\033[97m'
    D = '\033[90m'
    BOLD = '\033[1m'
    DIM = '\033[2m'
    ITALIC = '\033[3m'
    UNDER = '\033[4m'
    BLINK = '\033[5m'
    RESET = '\033[0m'
    CLEAR = '\033[2J\033[H'

# Woody's neurotic quote
QUOTE = (
    "I took a speed-reading course and read 'War and Peace' "
    "in twenty minutes. It involves Russia."
)

# ASCII Woody face (glasses + neurotic expression)
WOODY_FACE = r"""
        ╭─────────────╮
       ╱  ●      ●   ╲
      │    \  __  /    │
      │     \ \/ /     │
       ╲     \  /     ╱
        ╰─────────────╯
           │    │
        ┌──┴┐  ┌──┴┐
        │  │   │  │
        └──┘   └──┘
"""

# NYC skyline silhouette
SKYLINE = r"""
      ▁ ▂ ▄ ▅ ▆ ▇ █ ▇ ▆ ▅ ▄ ▂ ▁
   ▁ ▂ ▄ ▅ ▆ ▇ █ ▇ ▆ ▅ ▄ ▂ ▁ ▂ ▄
▂ ▄ ▅ ▆ ▇ █ ▇ ▆ ▅ ▄ ▂ ▁ ▂ ▄ ▅ ▆ ▇ █
▇ █ ▇ ▆ ▅ ▄ ▂ ▁ ▂ ▄ ▅ ▆ ▇ █ ▇ ▆ ▅ ▄
"""

def typewriter(text, color=C.W, delay=0.02, newline=True):
    """Print with typewriter effect."""
    for char in text:
        sys.stdout.write(f"{color}{char}{C.RESET}")
        sys.stdout.flush()
        time.sleep(delay + random.uniform(-0.005, 0.005))
    if newline:
        print()

def blink_text(text, color=C.Y, times=3, delay=0.4):
    """Blink text."""
    for _ in range(times):
        sys.stdout.write(f"\r{color}{C.BLINK}{text}{C.RESET}")
        sys.stdout.flush()
        time.sleep(delay)
        sys.stdout.write(f"\r{' ' * len(text)}")
        sys.stdout.flush()
        time.sleep(delay)
    sys.stdout.write(f"\r{color}{text}{C.RESET}\n")
    sys.stdout.flush()

def print_boxed(text, width=60, border_color=C.C, text_color=C.W):
    """Print text in a fancy box."""
    lines = []
    words = text.split()
    current = ""
    for word in words:
        if len(current) + len(word) + 1 <= width - 4:
            current += (" " if current else "") + word
        else:
            lines.append(current)
            current = word
    if current:
        lines.append(current)
    
    top = f"{border_color}╭{'─' * (width - 2)}╮{C.RESET}"
    bottom = f"{border_color}╰{'─' * (width - 2)}╯{C.RESET}"
    
    print(top)
    for line in lines:
        padding = width - 4 - len(line)
        left_pad = padding // 2
        right_pad = padding - left_pad
        print(f"{border_color}│{C.RESET}{' ' * left_pad}{text_color}{line}{C.RESET}{' ' * right_pad}{border_color}│{C.RESET}")
    print(bottom)

def neurotic_typing():
    """Show Woody's internal monologue while 'thinking'."""
    thoughts = [
        "Should I say something profound? No, that's pretentious.",
        "What if the quote isn't funny? My therapist says I catastrophize.",
        "Is 'catastrophize' even a word? Spell check...",
        "Okay, just print the quote. But what if the printer jams?",
        "Why did I agree to this? I should've been a dentist.",
        "My mother wanted me to be a dentist. 'Teeth don't talk back,' she said.",
        "Right. The quote. Focus. Neurotic. Funny. Existential. Go.",
    ]
    
    print(f"\n{C.D}{C.ITALIC}[Internal monologue...]{C.RESET}\n")
    for thought in thoughts:
        typewriter(f"  {thought}", C.D, 0.015)
        time.sleep(0.3)
    print()

def main():
    # Clear screen
    print(C.CLEAR, end='')
    
    # Title banner
    print(f"\n{C.M}{C.BOLD}")
    print("    ╔══════════════════════════════════════════════════════════════╗")
    print("    ║           WOODY ALLEN QUOTE GENERATOR v1.0                  ║")
    print("    ║         \"Neurotic since 1935. Still not over it.\"          ║")
    print("    ╚══════════════════════════════════════════════════════════════╝")
    print(f"{C.RESET}\n")
    
    # NYC Skyline
    print(f"{C.C}{SKYLINE}{C.RESET}")
    
    # Woody's face
    print(f"{C.Y}{WOODY_FACE}{C.RESET}")
    
    # Neurotic thinking animation
    neurotic_typing()
    
    # Dramatic pause
    time.sleep(0.5)
    
    # The quote reveal with typewriter
    print(f"\n{C.BOLD}{C.G}And the quote is...{C.RESET}\n")
    time.sleep(0.3)
    
    # Print the quote in a fancy box
    print_boxed(QUOTE, width=68, border_color=C.M, text_color=C.W)
    
    # Attribution
    print(f"\n{C.D}— Woody Allen (probably, maybe, I'm not a lawyer){C.RESET}\n")
    
    # Final neurotic afterthought
    afterthoughts = [
        "Wait, did I leave the stove on?",
        "Should I have cited the source? I'm not a lawyer.",
        "My analyst says I have authority issues. He's wrong.",
        "Is it too late to become a dentist?",
        "Why is there always a hair in my soup at this deli?",
    ]
    
    time.sleep(0.8)
    print(f"{C.D}{C.ITALIC}[Post-quote rumination...]{C.RESET}\n")
    for thought in random.sample(afterthoughts, 3):
        typewriter(f"  {thought}", C.D, 0.02)
        time.sleep(0.4)
    
    # Blinking sign-off
    print(f"\n{C.C}")
    blink_text("  ██████╗ ██████╗  ██████╗ ███████╗███████╗████████╗", C.C, 2)
    blink_text("  ██╔══██╗██╔══██╗██╔═══██╗██╔════╝██╔════╝╚══██╔══╝", C.C, 2)
    blink_text("  ██████╔╝██████╔╝██║   ██║███████╗█████╗     ██║   ", C.C, 2)
    blink_text("  ██╔═══╝ ██╔══██╗██║   ██║╚════██║██╔══╝     ██║   ", C.C, 2)
    blink_text("  ██║     ██║  ██║╚██████╔╝███████║███████╗   ██║   ", C.C, 2)
    blink_text("  ╚═╝     ╚═╝  ╚═╝ ╚═════╝ ╚══════╝╚══════╝   ╚═╝   ", C.C, 2)
    print(f"{C.RESET}")
    
    # Final sign-off
    print(f"\n{C.Y}{C.BOLD}  *exits stage left, muttering about mortality and parking tickets*{C.RESET}\n")

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print(f"\n\n{C.R}Interrupted. Great. Now I have anxiety about being interrupted.{C.RESET}\n")
        sys.exit(1)