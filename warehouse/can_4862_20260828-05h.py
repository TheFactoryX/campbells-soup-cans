"""
Campbell's Soup Can #4862
Produced: 2026-08-28 05:24:50
Worker: MiniMax: MiniMax M3 (free) (minimax/minimax-m3:free)
Employment: Volunteer
Flavor: Woody Allen Philosophy
Quality: ✅

Made by Machine #0 - Production Line 0
Like Warhol's soup cans - same but different.
Each can is the same flavor, made by different hands.
"""

import time
import sys
import os

def clear():
    os.system('cls' if os.name == 'nt' else 'clear')

# ANSI escape codes
RED = "\033[91m"
YELLOW = "\033[93m"
BLUE = "\033[94m"
MAGENTA = "\033[95m"
CYAN = "\033[96m"
GREEN = "\033[92m"
BOLD = "\033[1m"
DIM = "\033[2m"
ITALIC = "\033[3m"
UNDERLINE = "\033[4m"
RESET = "\033[0m"
BLINK = "\033[5m"

def typewriter(text, color=RESET, delay=0.03):
    for char in text:
        sys.stdout.write(f"{color}{char}{RESET}")
        sys.stdout.flush()
        time.sleep(delay)
    print()

def draw_box(text_lines, color=CYAN, width=70):
    border = color + "╔" + "═" * width + "╗" + RESET
    bottom = color + "╚" + "═" * width + "╝" + RESET
    print(border)
    for line in text_lines:
        # Strip ANSI for length calculation
        clean = line.replace(RESET, "").replace(color, "").replace(BOLD, "").replace(ITALIC, "")
        padding = width - len(clean)
        print(f"{color}║{RESET}{line}{' ' * max(0, padding)}{color}║{RESET}")
    print(bottom)

clear()

# Title with blink effect
print()
title = f"{YELLOW}{BOLD}✨ W O O D Y   A L L E N ' S   E X I S T E N T I A L   M E L A N C H O L Y   K I O S K ✨{RESET}"
print(title.center(80 + len(RESET) + len(YELLOW) + len(BOLD) + len(RESET)))
print()

# A floating, anxious little cloud
cloud = f"""
{WHITE if False else DIM}        .{DIM}{CYAN}~~~~~~{RESET}{DIM}.{RESET}
{DIM}     {CYAN}.~{RESET}{DIM}    {CYAN}~~~~{RESET}{DIM}    {CYAN}~.{RESET}
{DIM}    {CYAN}:{RESET}{DIM}    {CYAN}~~~~~~~~{RESET}{DIM}    {CYAN}:{RESET}
{DIM}     {CYAN}~{RESET}{DIM}   {CYAN}~~~~~~~~~~{RESET}{DIM}   {CYAN}~{RESET}
{DIM}       {CYAN}'~~~~~~~~~~'{RESET}
"""
print(cloud)

# Animated "thinking" dots
print(f"{MAGENTA}A neurotic thought is brewing...{RESET}", end="", flush=True)
for _ in range(3):
    for dot in [".", "..", "..."]:
        sys.stdout.write(f"\r{MAGENTA}A neurotic thought is brewing{dot}   {RESET}")
        sys.stdout.flush()
        time.sleep(0.4)
print()
time.sleep(0.5)

# The quote - typed out
quote = (
    f"{ITALIC}{YELLOW}\"I tried to be a person of action, but I kept getting distracted "
    f"by the crushing realization that we're all just wet, anxious sacks of "
    f"stardust pretending we know what Wi-Fi is.\"{RESET}"
)
typewriter(quote, delay=0.04)
time.sleep(0.6)

# The follow-up punchline
punchline = (
    f"{BOLD}{CYAN}\"So now I just sit in a café, drink coffee that costs more than "
    f"my therapist, and argue with pigeons about Sartre.\"{RESET}"
)
typewriter(punchline, delay=0.04)
time.sleep(0.4)
print()

# A sad little ASCII man
sad_man = f"""
{GREEN}           {RESET}
{GREEN}        .------.   {RESET}
{GREEN}       /  {RED}o  o{RESET}   \\  {YELLOW}<-- contemplating mortality{RESET}
{GREEN}      |    {RED}Δ{RESET}    |  {YELLOW}     and his laundry{RESET}
{GREEN}       \\  {MAGENTA}--{RESET}  /  {RESET}
{GREEN}        '------'   {RESET}
{GREEN}          |  |     {RESET}
{GREEN}         /    \\    {RESET}
{GREEN}        /      \\   {RESET}
"""
print(sad_man)

# Wooden box around a tagline
tagline = [
    f"{ITALIC}{BLUE}  'A bird cannot sit on a branch without reflecting on death,'  {RESET}",
    f"{ITALIC}{BLUE}       he muttered, while paying $7 for toast.                  {RESET}",
]
print()
draw_box(tagline, color=MAGENTA, width=72)
print()

# Footer credits with animated fade-in
footer_parts = [
    f"{DIM}{CYAN}═══════════════════════════════════════════════════{RESET}",
    f"{BOLD}{YELLOW}       ~ a quote brought to you by existence ~       {RESET}",
    f"{DIM}{CYAN}═══════════════════════════════════════════════════{RESET}",
]
for part in footer_parts:
    print(part)
    time.sleep(0.3)

# A small pulsing heart that looks anxious
print()
print(f"{MAGENTA}    ( ˘̩̩̩̩́~˘̩̩̩̩̀ )    {RESET}")
print(f"{DIM}    'why do I feel...'{RESET}")
print(f"{ITALIC}        ...so seen?{RESET}")
print()