"""
Campbell's Soup Can #4253
Produced: 2026-07-19 06:42:36
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
    R = '\033[91m'    # Red
    G = '\033[92m'    # Green
    Y = '\033[93m'    # Yellow
    B = '\033[94m'    # Blue
    M = '\033[95m'    # Magenta
    C = '\033[96m'    # Cyan
    W = '\033[97m'    # White
    BOLD = '\033[1m'
    DIM = '\033[2m'
    UNDER = '\033[4m'
    BLINK = '\033[5m'
    RESET = '\033[0m'
    CLEAR = '\033[2J\033[H'
    CURSOR_HIDE = '\033[?25l'
    CURSOR_SHOW = '\033[?25h'

WOODY_QUOTES = [
    "I'm not afraid of death; I just don't want to be there when it happens.\n         My therapist says I have a 'pre-existing condition' called \n         'being alive' — turns out it's terminal.",
    "The universe is indifferent. My landlord is hostile.\n         My analyst charges $300/hour to tell me what my mother\n         told me for free: 'You worry too much.'",
    "I want to achieve immortality through not dying.\n         Failing that, I'll settle for a really good pastrami\n         sandwich and a parking spot in Manhattan.",
    "Life is divided into the horrible and the miserable.\n         The horrible are terminal cases. The miserable is everyone else.\n         I'm currently oscillating between both with a side of acid reflux.",
    "God is silent. My analyst is silent. My refrigerator hums\n         in B-flat. I assume it's a cosmic joke. I'm the punchline.",
    "I took a speed-reading course and read 'War and Peace' in 20 minutes.\n         It involves Russia. Also, I still don't understand the ending.\n         Or the beginning. Or why I paid $400 for the course.",
]

def draw_woody_face():
    """ASCII art of Woody Allen"""
    face = f"""
{C.Y}       ╭─────────────╮{C.RESET}
{C.Y}      │  {C.W}@   @{C.Y}    │{C.RESET}   {C.M}♫  Neurotic Jazz Plays  ♫{C.RESET}
{C.Y}      │  {C.C}( -_- ){C.Y}   │{C.RESET}   {C.DIM}   (imaginary clarinet solo)   {C.RESET}
{C.Y}      │  {C.G}  ▭  {C.Y}    │{C.RESET}
{C.Y}      │ {C.M}┌───┐{C.Y}   │{C.RESET}
{C.Y}      │ │{C.R}♥{C.M}│{C.Y}   │{C.RESET}
{C.Y}      │ └───┘{C.Y}   │{C.RESET}
{C.Y}       ╰─────────────╯{C.RESET}
{C.B}        ▄▄▄▄▄▄▄▄▄▄▄{C.RESET}
{C.B}       █ {C.W}GLASSES{C.B} █{C.RESET}
{C.B}        ▀▀▀▀▀▀▀▀▀{C.RESET}
"""
    return face

def typewriter_print(text, delay=0.02, color=C.W):
    """Print text with typewriter effect"""
    for char in text:
        sys.stdout.write(f"{color}{char}{C.RESET}")
        sys.stdout.flush()
        time.sleep(delay)
    print()

def sparkle_animation(duration=2):
    """Little sparkle animation"""
    sparkles = ['✦', '✧', '★', '☆', '✩', '✪', '✫', '✬', '✭', '✮', '✯']
    end_time = time.time() + duration
    cols = 60
    while time.time() < end_time:
        line = ""
        for _ in range(cols):
            if random.random() < 0.15:
                line += f"{random.choice([C.Y, C.C, M])}{random.choice(sparkles)}{C.RESET}"
            else:
                line += " "
        sys.stdout.write(f"\r{line}")
        sys.stdout.flush()
        time.sleep(0.1)
    print()

def draw_box(text_lines, border_color=C.C, title="WOODY ALLEN WISDOM"):
    """Draw a fancy box around text"""
    max_len = max(len(line) for line in text_lines)
    width = max_len + 4
    
    top = f"{border_color}╭{'─' * (width - 2)}╮{C.RESET}"
    bottom = f"{border_color}╰{'─' * (width - 2)}╯{C.RESET}"
    
    title_line = f"{border_color}│{C.RESET} {C.BOLD}{C.Y}{title:^{width - 4}}{C.RESET} {border_color}│{C.RESET}"
    separator = f"{border_color}├{'─' * (width - 2)}┤{C.RESET}"
    
    lines = [top, title_line, separator]
    for line in text_lines:
        padding = width - 4 - len(line)
        left_pad = padding // 2
        right_pad = padding - left_pad
        lines.append(f"{border_color}│{C.RESET} {' ' * left_pad}{C.W}{line}{C.RESET}{' ' * right_pad} {border_color}│{C.RESET}")
    lines.append(bottom)
    
    return "\n".join(lines)

def main():
    # Clear screen and hide cursor
    sys.stdout.write(C.CLEAR + C.CURSOR_HIDE)
    sys.stdout.flush()
    
    # Pick a random quote
    quote = random.choice(WOODY_QUOTES)
    quote_lines = quote.split('\n')
    
    # Opening animation - sparkles
    print(f"\n{C.M}{C.BOLD}     INITIALIZING EXISTENTIAL DREAD MODULE...{C.RESET}\n")
    time.sleep(0.5)
    sparkle_animation(1.5)
    
    # Draw Woody's face
    print(draw_woody_face())
    time.sleep(0.8)
    
    # Typewriter quote reveal
    print(f"\n{C.C}{C.BOLD}    \"{C.RESET}")
    for i, line in enumerate(quote_lines):
        if i == 0:
            typewriter_print(f"    {line}", 0.015, C.Y)
        else:
            typewriter_print(f"         {line}", 0.015, C.W)
    print(f"{C.C}{C.BOLD}    \"{C.RESET}\n")
    
    time.sleep(0.5)
    
    # Fancy box with the quote
    box = draw_box(quote_lines, C.M, "WOODY ALLEN WISDOM")
    print(box)
    
    # Closing neurotic thought
    neurotic_endings = [
        f"\n{C.DIM}{C.B}...should I have ordered the tuna melt?{C.RESET}",
        f"\n{C.DIM}{C.B}...my left elbow hurts. Is that psychosomatic?{C.RESET}",
        f"\n{C.DIM}{C.B}...did I lock the door? The universe is unlocked.{C.RESET}",
        f"\n{C.DIM}{C.B}...I need to call my mother. And my analyst. And a plumber.{C.RESET}",
        f"\n{C.DIM}{C.B}...existential dread: $0. Therapy: $300. Pastrami: priceless.{C.RESET}",
    ]
    time.sleep(1)
    typewriter_print(random.choice(neurotic_endings), 0.03, C.M)
    
    # Final sparkle fade
    print(f"\n{C.C}")
    sparkle_animation(1)
    
    # Show cursor
    sys.stdout.write(C.CURSOR_SHOW)
    sys.stdout.flush()
    
    print(f"\n{C.G}{C.BOLD}    [PROCESS COMPLETE: NEUROSIS LEVEL CRITICAL]{C.RESET}\n")

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        sys.stdout.write(C.CURSOR_SHOW + C.RESET + "\n\n    Interrupted. Typical.\n")
        sys.stdout.flush()