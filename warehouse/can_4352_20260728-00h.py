"""
Campbell's Soup Can #4352
Produced: 2026-07-28 00:10:43
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
    D = '\033[90m'      # Dim
    BD = '\033[1m'      # Bold
    IT = '\033[3m'      # Italic
    UL = '\033[4m'      # Underline
    BLINK = '\033[5m'   # Blink
    REV = '\033[7m'     # Reverse
    RS = '\033[0m'      # Reset
    CLR = '\033[2J\033[H'  # Clear screen

# Woody Allen quotes (original, in his style)
QUOTES = [
    "I took a speed-reading course and read War and Peace in twenty minutes. It involves Russia.",
    "My therapist says I have a preoccupation with death. I told her, 'Doc, at my age, it's not a preoccupation — it's a schedule.'",
    "I don't believe in an afterlife, although I'm bringing a change of underwear just in case.",
    "The food here is terrible... and such small portions!",
    "I'm not afraid of dying. I just don't want to be there when it happens. Or the week before. Or the month before, really.",
    "Life is divided into the horrible and the miserable. The horrible are terminal cases. The miserable is everyone else. I'm miserable. You should be so lucky.",
    "I have a terrible memory. Or is it a terrible memory? I forget.",
    "My analyst says I'm a narcissist. I said, 'That's impossible — I'm too fascinating to be a narcissist.'",
    "I don't want to achieve immortality through my work. I want to achieve it through not dying. Or at least through a very long nap.",
    "There are two types of people in this world: those who worry about everything, and those who don't worry because they're already dead. I'm the first type. Sometimes I aspire to the second.",
    "I was thrown out of college for cheating on the metaphysics exam. I looked into the soul of the boy sitting next to me.",
    "Death is one of the few things that can be done as easily lying down. Which is good, because I'm usually lying down anyway.",
]

def typewriter(text, color=C.W, delay=0.02, newline=True):
    """Print text with typewriter effect"""
    for char in text:
        sys.stdout.write(f"{color}{char}{C.RS}")
        sys.stdout.flush()
        time.sleep(delay)
    if newline:
        print()

def sparkle_line(width=60):
    """Print a decorative line with sparkles"""
    chars = ['✦', '✧', '★', '☆', '✵', '✶', '✷', '✸', '✹', '✺']
    line = ''.join(random.choice(chars) for _ in range(width))
    print(f"{C.M}{C.D}{line}{C.RS}")

def woody_face():
    """ASCII Woody Allen face"""
    face = f"""
{C.Y}         .--.         {C.RS}
{C.Y}        / .. \\        {C.RS}  {C.D}*adjusts imaginary glasses*{C.RS}
{C.Y}       |  __  |       {C.RS}
{C.Y}       | |  | |       {C.RS}
{C.Y}        \\ \\/ /        {C.RS}
{C.Y}         `--'         {C.RS}
{C.D}      (neurotic gaze) {C.RS}
"""
    print(face)

def quote_box(quote, width=70):
    """Draw a fancy box around the quote"""
    lines = []
    words = quote.split()
    current = ""
    
    for word in words:
        if len(current) + len(word) + 1 <= width - 4:
            current += (" " if current else "") + word
        else:
            lines.append(current)
            current = word
    if current:
        lines.append(current)
    
    # Top border
    print(f"{C.C}╔{'═' * (width - 2)}╗{C.RS}")
    
    # Quote lines
    for line in lines:
        padding = width - 4 - len(line)
        left_pad = padding // 2
        right_pad = padding - left_pad
        print(f"{C.C}║{C.RS}{' ' * left_pad}{C.W}{C.IT}{line}{C.RS}{' ' * right_pad}{C.C}║{C.RS}")
    
    # Bottom border
    print(f"{C.C}╚{'═' * (width - 2)}╝{C.RS}")

def animated_entrance():
    """Fun entrance animation"""
    print(C.CLR)
    time.sleep(0.3)
    
    # Falling text effect
    messages = [
        f"{C.D}Initializing existential dread...{C.RS}",
        f"{C.D}Calibrating neuroses...{C.RS}",
        f"{C.D}Loading Jewish guilt module...{C.RS}",
        f"{C.D}Checking for mortality... [FOUND]{C.RS}",
        f"{C.G}Ready to kvetch.{C.RS}\n",
    ]
    
    for msg in messages:
        print(msg)
        time.sleep(0.4)

def main():
    animated_entrance()
    
    sparkle_line(50)
    print(f"\n{C.BD}{C.Y}☕  A WOODY ALLEN MOMENT  ☕{C.RS}\n")
    
    woody_face()
    
    sparkle_line(50)
    print()
    
    # Pick a quote
    quote = random.choice(QUOTES)
    
    # Dramatic pause
    time.sleep(0.5)
    
    # Print quote with typewriter effect inside box
    quote_box(quote, 70)
    
    print()
    sparkle_line(50)
    
    # Tagline
    taglines = [
        f"{C.D}— Woody Allen, probably, while waiting for a checkup{C.RS}",
        f"{C.D}— Spoken into a dictaphone at 3 AM{C.RS}",
        f"{C.D}— Mumbled to a therapist who stopped listening 20 years ago{C.RS}",
        f"{C.D}— Whispered to a pastrami sandwich{C.RS}",
    ]
    print(f"\n{random.choice(taglines)}")
    print()
    
    # Final existential flutter
    time.sleep(0.3)
    print(f"{C.M}{C.IT}{C.D}         *exists anxiously*{C.RS}")
    print(f"{C.D}         (press Ctrl+C to embrace the void){C.RS}\n")

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print(f"\n\n{C.R}{C.BD}INTERRUPTED! {C.RS}{C.D}Even the void needs a coffee break.{C.RS}\n")