"""
Campbell's Soup Can #5031
Produced: 2026-09-27 01:28:00
Worker: NVIDIA: Nemotron 3 Ultra (free) (nvidia/nemotron-3-ultra-550b-a55b:free)
Employment: Volunteer
Flavor: Woody Allen Philosophy
Quality: ❌ (broken)

Made by Machine #0 - Production Line 0
Like Warhol's soup cans - same but different.
Each can is the same flavor, made by different hands.
"""

import sys
import time
import random

# Woody Allen style quotes (original)
QUOTES = [
    "I took a speed-reading course and read 'War and Peace' in twenty minutes. It involves Russia.",
    "My therapist says I have a preoccupation with death. I told him, 'Doc, at my age, it's not a preoccupation. It's a schedule.'",
    "I don't believe in an afterlife, but I'm bringing a change of underwear just in case.",
    "The universe is indifferent to our suffering. My landlord, however, is very interested in it—specifically the rent portion.",
    "I'm not afraid of dying. I just don't want to be conscious for the part where they lower the casket and someone says, 'He looks natural.' He's dead. Nobody looks natural dead. They look like they're napping in a box.",
    "Life is divided into the horrible and the miserable. The horrible are terminal cases. The miserable is everyone else. I'm grateful to be miserable.",
    "I have a hard time with mortality. Yesterday I bought a green banana. That's optimism for you. Or denial. Probably denial.",
    "God is silent. My mother, however, has opinions on everything including His interior decorating choices.",
    "I'd like to live forever. Failing that, I'd like to live long enough to understand my health insurance policy.",
    "Death is nature's way of telling you to slow down. My doctor says the same thing. Usually after looking at my bloodwork.",
]

# ANSI colors
class C:
    R = '\033[91m'
    G = '\033[92m'
    Y = '\033[93m'
    B = '\033[94m'
    M = '\033[95m'
    C = '\033[96m'
    W = '\033[97m'
    GR = '\033[90m'
    BOLD = '\033[1m'
    DIM = '\033[2m'
    ITALIC = '\033[3m'
    UNDER = '\033[4m'
    BLINK = '\033[5m'
    RESET = '\033[0m'
    CLEAR = '\033[2J\033[H'
    UP = '\033[1A'
    HIDE = '\033[?25l'
    SHOW = '\033[?25h'

def typewriter(text, color=C.W, delay=0.02, newline=True):
    """Print text with typewriter effect"""
    sys.stdout.write(color)
    for char in text:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(delay)
    sys.stdout.write(C.RESET)
    if newline:
        print()

def center_text(text, width=70):
    """Center text within width"""
    return text.center(width)

def draw_box(content_lines, width=70, border_color=C.C, title=None):
    """Draw a fancy box around content"""
    top = f"{border_color}╔{'═' * (width - 2)}╗{C.RESET}"
    bottom = f"{border_color}╚{'═' * (width - 2)}╝{C.RESET}"
    
    lines = [top]
    if title:
        title_line = f"{border_color}║{C.RESET} {C.BOLD}{C.Y}{title.center(width - 4)}{C.RESET} {border_color}║{C.RESET}"
        lines.append(title_line)
        lines.append(f"{border_color}╠{'═' * (width - 2)}╣{C.RESET}")
    
    for line in content_lines:
        # Calculate visible length (strip ANSI codes for padding)
        import re
        clean = re.sub(r'\033\[[0-9;]*m', '', line)
        padding = width - 4 - len(clean)
        left_pad = padding // 2
        right_pad = padding - left_pad
        lines.append(f"{border_color}║{C.RESET}{' ' * left_pad}{line}{' ' * right_pad}{border_color}║{C.RESET}")
    
    lines.append(bottom)
    return '\n'.join(lines)

def woody_face():
    """ASCII Woody Allen face"""
    return [
        f"{C.GR}       .--.      {C.RESET}",
        f"{C.GR}      /    \\     {C.RESET}",
        f"{C.Y}     |  {C.W}@@ {C.Y}|    {C.RESET}",
        f"{C.Y}     |  {C.M}<> {C.Y}|    {C.RESET}",
        f"{C.Y}      \\ {C.C}__ {C.Y}/     {C.RESET}",
        f"{C.GR}       `--'      {C.RESET}",
        f"{C.GR}      /||||\\     {C.RESET}",
        f"{C.GR     }`""""`     {C.RESET}",
    ]

def neurotic_dots(count=3, color=C.Y):
    """Animated thinking dots"""
    for _ in range(count):
        for dots in ['.', '..', '...', '..', '.']:
            sys.stdout.write(f'\r{color}{C.ITALIC}Contemplating existence{dots}{C.RESET}   ')
            sys.stdout.flush()
            time.sleep(0.3)
    sys.stdout.write('\r' + ' ' * 40 + '\r')
    sys.stdout.flush()

def main():
    # Hide cursor
    sys.stdout.write(C.HIDE)
    sys.stdout.flush()
    
    try:
        # Clear screen
        print(C.CLEAR)
        
        # Pick a quote
        quote = random.choice(QUOTES)
        
        # Woody face animation - slide in
        face = woody_face()
        print()
        for i, line in enumerate(face):
            sys.stdout.write(' ' * (30 - i * 2) + line + '\n')
            sys.stdout.flush()
            time.sleep(0.15)
        
        time.sleep(0.5)
        
        # Neurotic contemplation
        print()
        neurotic_dots(2)
        
        # Typewriter the quote
        print()
        print(C.DIM + "─" * 70 + C.RESET)
        print()
        
        # Split quote into chunks for dramatic effect
        words = quote.split(' ')
        chunks = []
        current = []
        for word in words:
            current.append(word)
            if len(' '.join(current)) > 40 or word.endswith('.') or word.endswith('?') or word.endswith('!'):
                chunks.append(' '.join(current))
                current = []
        if current:
            chunks.append(' '.join(current))
        
        for i, chunk in enumerate(chunks):
            color = C.W if i % 2 == 0 else C.C
            if 'death' in chunk.lower() or 'dying' in chunk.lower() or 'mortality' in chunk.lower():
                color = C.R
            elif 'god' in chunk.lower() or 'universe' in chunk.lower():
                color = C.M
            elif 'therapist' in chunk.lower() or 'doctor' in chunk.lower() or 'mother' in chunk.lower():
                color = C.Y
            typewriter(f"  {chunk}", color=color, delay=0.015)
            time.sleep(0.15)
        
        print()
        print(C.DIM + "─" * 70 + C.RESET)
        print()
        
        # Signature
        sig_lines = [
            f"{C.GR}— Woody Allen (probably){C.RESET}",
            f"{C.DIM}(as interpreted by a Python script having an existential crisis){C.RESET}",
        ]
        for line in sig_lines:
            typewriter(center_text(line), color=C.GR, delay=0.01)
        
        print()
        print()
        
        # Final philosophical box
        final_thoughts = [
            f"{C.ITALIC}The absurdity of existence is the only thing{C.RESET}",
            f"{C.ITALIC}that makes sense. Also, did I leave the stove on?{C.RESET}",
        ]
        box = draw_box(final_thoughts, width=68, border_color=C.M, title=f"{C.BOLD}🧠 FINAL THOUGHT 🧠{C.RESET}")
        print(box)
        
        # Little footer animation
        print()
        footers = [
            "Press Ctrl+C to exit existence...",
            "Or just close the terminal. The universe won't notice either way.",
            "∃x(Anxious(x) ∧ Programmer(x))",
        ]
        for footer in footers:
            typewriter(center_text(footer), color=C.GR, delay=0.01)
            time.sleep(0.4)
        
        print()
        print()
        
    except KeyboardInterrupt:
        print(f"\n{C.Y}\nInterrupted. Story of my life.{C.RESET}\n")
    finally:
        sys.stdout.write(C.SHOW)
        sys.stdout.flush()

if __name__ == "__main__":
    main()