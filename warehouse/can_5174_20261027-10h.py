"""
Campbell's Soup Can #5174
Produced: 2026-10-27 10:35:27
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
    RST = '\033[0m'
    BOLD = '\033[1m'
    DIM = '\033[2m'
    ITALIC = '\033[3m'
    RED = '\033[91m'
    GREEN = '\033[92m'
    YELLOW = '\033[93m'
    BLUE = '\033[94m'
    MAGENTA = '\033[95m'
    CYAN = '\033[96m'
    WHITE = '\033[97m'
    GRAY = '\033[90m'
    BG_BLACK = '\033[40m'
    BG_RED = '\033[41m'
    BG_GREEN = '\033[42m'
    BG_YELLOW = '\033[43m'
    BG_BLUE = '\033[44m'
    BG_MAGENTA = '\033[45m'
    BG_CYAN = '\033[46m'
    BG_WHITE = '\033[47m'

# Woody's quote
QUOTE = "The universe called.\nIt said my existential dread\nis past due and there's a\nlate fee payable in insomnia."

WOODY_ASCII = r"""
        ╔══════════════════════════════════════════════════════════════╗
        ║  ▄▄▄▄▄▄▄  ▄▄▄▄▄▄▄  ▄▄▄▄▄▄▄  ▄▄▄▄▄▄▄  ▄▄▄▄▄▄▄  ▄▄▄▄▄▄▄       ║
        ║  █  ▄▄▄ █ █  ▄▄▄ █ █  ▄▄▄ █ █  ▄▄▄ █ █  ▄▄▄ █ █  ▄▄▄ █      ║
        ║  █ █   ██ █ █   ██ █ █   ██ █ █   ██ █ █   ██ █ █   ██      ║
        ║  █ █▄▄▄▄█ █ █▄▄▄▄█ █ █▄▄▄▄█ █ █▄▄▄▄█ █ █▄▄▄▄█ █ █▄▄▄▄█      ║
        ║  █  ▄▄▄▄▄ █  ▄▄▄▄▄ █  ▄▄▄▄▄ █  ▄▄▄▄▄ █  ▄▄▄▄▄ █  ▄▄▄▄▄      ║
        ║  █ █     █ █ █     █ █     █ █     █ █ █     █ █ █         ║
        ║  █▄█     █▄█ █     █▄█     █▄█     █▄█ █     █▄█ █         ║
        ║                                                               ║
        ║    "I'm not afraid of death... I just don't want to be       ║
        ║     there when it happens."  —  Not me, but close enough     ║
        ╚══════════════════════════════════════════════════════════════╝
"""

NEUROTIC_THOUGHTS = [
    "Did I lock the door?",
    "Is that a symptom?",
    "What if I'm wrong about everything?",
    "My left eyebrow feels heavier than my right.",
    "Should I have ordered the salad?",
    "Am I breathing manually now?",
    "The universe is expanding. So is my anxiety.",
    "I should floss more.",
    "What if this quote is pretentious?",
    "My therapist would call this 'catastrophizing.'",
    "I'm catastrophizing about catastrophizing.",
    "Is it hot in here or is it just my mortality?",
]

def clear_screen():
    print('\033[2J\033[H', end='')

def hide_cursor():
    print('\033[?25l', end='')

def show_cursor():
    print('\033[?25h', end='')

def move_cursor(y, x):
    print(f'\033[{y};{x}H', end='')

def typewriter(text, delay=0.03, color=C.WHITE):
    for char in text:
        print(f'{color}{char}{C.RST}', end='', flush=True)
        time.sleep(delay)
    print()

def rainbow_text(text):
    colors = [C.RED, C.YELLOW, C.GREEN, C.CYAN, C.BLUE, C.MAGENTA]
    result = ""
    for i, char in enumerate(text):
        if char != ' ' and char != '\n':
            result += f"{colors[i % len(colors)]}{char}{C.RST}"
        else:
            result += char
    return result

def pulse_text(text, times=3):
    for _ in range(times):
        for intensity in [C.DIM, C.RST, C.BOLD, C.RST]:
            clear_screen()
            print(f"{intensity}{text}{C.RST}")
            time.sleep(0.15)

def animate_neurotic_banner():
    width = 68
    print(f"{C.CYAN}╔{'═' * width}╗{C.RST}")
    print(f"{C.CYAN}║{C.RST} {C.BOLD}{C.YELLOW}NEUROTIC THOUGHT GENERATOR v3.14159{C.RST} {' ' * 28}{C.CYAN}║{C.RST}")
    print(f"{C.CYAN}╚{'═' * width}╝{C.RST}")
    print()

def scrolling_thoughts(duration=2.5):
    start = time.time()
    line = 0
    while time.time() - start < duration:
        thought = random.choice(NEUROTIC_THOUGHTS)
        color = random.choice([C.GRAY, C.RED, C.YELLOW, C.MAGENTA, C.CYAN])
        prefix = random.choice(["[!] ", "[?] ", "[!!] ", "[??] ", "[...] "])
        print(f"{color}{prefix}{thought}{C.RST}")
        time.sleep(0.12)
        line += 1
        if line > 12:
            break

def draw_quote_box():
    lines = QUOTE.split('\n')
    max_len = max(len(line) for line in lines)
    box_w = max_len + 6
    
    # Top border with gradient
    print(f"{C.MAGENTA}╔{'═' * box_w}╗{C.RST}")
    
    # Quote lines with typewriter effect
    for i, line in enumerate(lines):
        padding = max_len - len(line)
        left_pad = " " * 3
        right_pad = " " * (padding + 3)
        
        # Color each line differently
        colors = [C.YELLOW, C.GREEN, C.CYAN, C.MAGENTA]
        color = colors[i % len(colors)]
        
        print(f"{C.MAGENTA}║{C.RST}{left_pad}", end='', flush=True)
        typewriter(line, delay=0.025, color=color)
        print(f"{right_pad}{C.MAGENTA}║{C.RST}", end='')
        print()
        time.sleep(0.15)
    
    # Attribution line
    attrib = "— Woody Allen (probably, in an alternate timeline)"
    padding = max_len - len(attrib)
    print(f"{C.MAGENTA}║{C.RST} {C.DIM}{C.ITALIC}{attrib}{' ' * (padding + 2)}{C.RST}{C.MAGENTA}║{C.RST}")
    
    # Bottom border
    print(f"{C.MAGENTA}╚{'═' * box_w}╝{C.RST}")

def finale_animation():
    messages = [
        (C.RED, "PANIC"),
        (C.YELLOW, "PANIC."),
        (C.GREEN, "PANIC.."),
        (C.CYAN, "PANIC..."),
        (C.BLUE, "PANIC...."),
        (C.MAGENTA, "Acceptance."),
        (C.WHITE, "Whatever."),
    ]
    
    for _ in range(2):
        for color, msg in messages:
            clear_screen()
            print(f"\n\n\n{' ' * 30}{color}{C.BOLD}{msg}{C.RST}")
            time.sleep(0.2)
    
    # Final message
    clear_screen()
    print(f"\n\n{C.GRAY}{' ' * 20}┌{'─' * 30}┐{C.RST}")
    print(f"{C.GRAY}{' ' * 20}│{C.RST} {C.BOLD}{C.WHITE}Thank you for your anxiety{C.RST} {C.GRAY}│{C.RST}")
    print(f"{C.GRAY}{' ' * 20}└{'─' * 30}┘{C.RST}")
    print(f"\n{C.DIM}{' ' * 18}Your existential dread has been logged.{C.RST}")
    print(f"{C.DIM}{' ' * 18}Late fees apply. No refunds.{C.RST}\n")

def main():
    hide_cursor()
    try:
        clear_screen()
        
        # Opening neurotic banner
        animate_neurotic_banner()
        time.sleep(0.5)
        
        # Scrolling neurotic thoughts
        scrolling_thoughts(2.0)
        time.sleep(0.3)
        
        # Transition
        print(f"\n{C.DIM}Processing existential crisis...{C.RST}")
        for i in range(3):
            print(f"{C.DIM}{'.' * (i + 1)}{C.RST}", end='\r')
            time.sleep(0.3)
        print()
        
        # The quote box with typewriter
        print()
        draw_quote_box()
        
        time.sleep(1.5)
        
        # Finale
        finale_animation()
        
    finally:
        show_cursor()

if __name__ == "__main__":
    main()