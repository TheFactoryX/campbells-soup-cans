"""
Campbell's Soup Can #4009
Produced: 2026-06-25 08:30:53
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
    D = '\033[2m'       # Dim
    BD = '\033[1m'      # Bold
    IT = '\033[3m'      # Italic
    UL = '\033[4m'      # Underline
    BLINK = '\033[5m'   # Blink
    REV = '\033[7m'     # Reverse
    END = '\033[0m'     # Reset
    CLR = '\033[2J'     # Clear screen
    HOME = '\033[H'     # Cursor home
    UP = '\033[A'       # Cursor up
    DOWN = '\033[B'     # Cursor down
    SAVE = '\033[s'     # Save cursor
    RESTORE = '\033[u'  # Restore cursor

# Woody Allen quotes (original, in his style)
QUOTES = [
    "I took a speed-reading course and read 'War and Peace' in twenty minutes.\nIt involves Russia.",
    
    "The universe is merely a fleeting idea in God's mind—a pretty uncomfortable\nthought, especially if you've just made a large down payment on a condo.",
    
    "I have a very pessimistic view of life. You should know this going in.\nIf you're expecting a happy ending, try a different director.",
    
    "My one regret in life is that I'm not someone else.\nPreferably someone with better posture and a 401(k).",
    
    "Death is nature's way of telling you to slow down.\nMy doctor says the same thing, but he charges a copay.",
    
    "I don't believe in an afterlife, although I'm bringing a change of underwear\njust in case. You never know about the dry cleaning situation up there.",
    
    "Life is divided into the horrible and the miserable.\nThe horrible are terminal cases. The miserable is everyone else.\nI'm miserable. You're miserable. We should do lunch.",
    
    "I'm not afraid of death. I just don't want to be there when it happens.\nAlso, I'd prefer not to be the one who has to explain the charges to my estate.",
    
    "If only God would give me some clear sign! Like making a large deposit\nin my name at a Swiss bank. Or a parking spot on the Upper West Side.",
    
    "The lion and the lamb shall lie down together, but the lamb won't get much sleep.\nNeither will I, if I eat dairy after 8 PM.",
    
    "I can't listen to too much Wagner. I start getting the urge to conquer Poland.\nOr at least reorganize my sock drawer with Teutonic efficiency.",
    
    "There is no question that there is an unseen world. The problem is,\nhow far is it from midtown and how late is the last train?",
    
    "I don't want to achieve immortality through my work.\nI want to achieve it through not dying. Failing that, a really good moisturizer.",
    
    "My analyst says I have a persecution complex. He's just saying that\nbecause the CIA told him to. Or was it the building super?",
    
    "Confidence is what you have before you understand the problem.\nOnce you understand it, you have anxiety. I have a PhD in anxiety.",
]

# ASCII art frames
WOODY_FRAME = r"""
      ╔══════════════════════════════════════════════════════════════╗
      ║  ▄▄▄▄▄▄▄▄▄▄▄  ▄▄▄▄▄▄▄▄▄▄▄  ▄▄▄▄▄▄▄▄▄▄▄  ▄▄▄▄▄▄▄▄▄▄▄         ║
      ║  █▄█████████  █▄█████████  █▄█████████  █▄█████████         ║
      ║  █ ▼ ▼ ▼ ▼ ▼  █ ▼ ▼ ▼ ▼ ▼  █ ▼ ▼ ▼ ▼ ▼  █ ▼ ▼ ▼ ▼ ▼         ║
      ║  █  ▄▄▄▄▄  █  █  ▄▄▄▄▄  █  █  ▄▄▄▄▄  █  █  ▄▄▄▄▄  █         ║
      ║  █ █   █ █ █  █ █   █ █ █  █ █   █ █ █  █ █   █ █ █         ║
      ║  █ █▼▼▼▼▼ █ █  █ █▼▼▼▼▼ █ █  █ █▼▼▼▼▼ █ █  █ █▼▼▼▼▼ █ █         ║
      ║  █ ▼ ▼ ▼ ▼ ▼  █ ▼ ▼ ▼ ▼ ▼  █ ▼ ▼ ▼ ▼ ▼  █ ▼ ▼ ▼ ▼ ▼         ║
      ║  ▀▀▀▀▀▀▀▀▀▀▀  ▀▀▀▀▀▀▀▀▀▀▀  ▀▀▀▀▀▀▀▀▀▀▀  ▀▀▀▀▀▀▀▀▀▀▀         ║
      ║                                                              ║
      ║        "Neurosis is just a fancy word for being prepared"     ║
      ╚══════════════════════════════════════════════════════════════╝
"""

GLASSES = r"""
         ▄▄▄▄▄▄▄▄       ▄▄▄▄▄▄▄▄
        █ ▀▀▀▀▀▀ █     █ ▀▀▀▀▀▀ █
        █  ▄▄▄▄  █     █  ▄▄▄▄  █
        █ █    █ █     █ █    █ █
        █ ▀▀▀▀▀▀ █     █ ▀▀▀▀▀▀ █
         ▀▀▀▀▀▀▀▀       ▀▀▀▀▀▀▀▀
              \           /
               \_________/
"""

THOUGHT_BUBBLES = [
    r"""
        .
       . .
      .   .
     .     .
    (  💭  )
     '---'
    """,
    r"""
         .
        . .
       .   .
      .     .
     .  💭   .
      '-----'
    """,
    r"""
           .
          . .
         .   .
        .  💭 .
         '---'
    """,
]

# Neurotic spiral animation frames
SPIRAL_FRAMES = [
    "    @    ",
    "   @ @   ",
    "  @   @  ",
    " @     @ ",
    "@       @",
    " @     @ ",
    "  @   @  ",
    "   @ @   ",
]

def clear_screen():
    print(C.CLR + C.HOME, end='', flush=True)

def typewriter(text, delay=0.02, color=C.W):
    """Print text with typewriter effect"""
    for char in text:
        print(f"{color}{char}{C.END}", end='', flush=True)
        time.sleep(delay)
    print()

def typewriter_line(line, delay=0.015, color=C.W, end='\n'):
    for char in line:
        print(f"{color}{char}{C.END}", end='', flush=True)
        time.sleep(delay)
    print(end=end)

def blink_text(text, times=3, interval=0.4, color=C.Y):
    for _ in range(times):
        print(f"\r{color}{text}{C.END}", end='', flush=True)
        time.sleep(interval)
        print(f"\r{' ' * len(text)}", end='', flush=True)
        time.sleep(interval)
    print(f"\r{color}{text}{C.END}")

def animate_spiral(duration=2.0):
    """Animate a neurotic spiral"""
    start = time.time()
    i = 0
    while time.time() - start < duration:
        frame = SPIRAL_FRAMES[i % len(SPIRAL_FRAMES)]
        print(f"\r{C.M}{frame}{C.END} ", end='', flush=True)
        time.sleep(0.15)
        i += 1
    print("\r" + " " * 20 + "\r", end='', flush=True)

def draw_boxed_quote(quote, width=68):
    """Draw a beautifully boxed quote with colors"""
    lines = quote.split('\n')
    max_len = max(len(line) for line in lines)
    box_width = max(max_len + 4, width)
    
    # Top border
    print(f"{C.C}╔{'═' * box_width}╗{C.END}")
    
    # Empty line
    print(f"{C.C}║{' ' * box_width}║{C.END}")
    
    # Quote lines
    for i, line in enumerate(lines):
        padding = box_width - len(line) - 2
        left_pad = padding // 2
        right_pad = padding - left_pad
        color = [C.Y, C.G, C.C][i % 3]
        style = C.IT if i > 0 else C.BD
        print(f"{C.C}║{' ' * left_pad}{style}{color}{line}{C.END}{' ' * right_pad}{C.C}║{C.END}")
    
    # Empty line
    print(f"{C.C}║{' ' * box_width}║{C.END}")
    
    # Attribution
    attrib = "— Woody Allen (probably)"
    attrib_pad = box_width - len(attrib) - 2
    print(f"{C.C}║{' ' * attrib_pad}{C.D}{C.IT}{attrib}{C.END}{C.C}║{C.END}")
    
    # Bottom border
    print(f"{C.C}╚{'═' * box_width}╝{C.END}")

def neurotic_typing_effect(quote):
    """Simulate neurotic typing with corrections"""
    lines = quote.split('\n')
    
    for line_idx, line in enumerate(lines):
        # Type with occasional "mistakes" and corrections
        typed = ""
        for char_idx, char in enumerate(line):
            # 5% chance of a typo
            if random.random() < 0.05 and char.isalpha():
                wrong_char = random.choice('abcdefghijklmnopqrstuvwxyz')
                print(f"\r{C.R}{typed}{wrong_char}{C.END}", end='', flush=True)
                time.sleep(0.08)
                # Backspace
                print(f"\r{C.Y}{typed}{C.END}", end='', flush=True)
                time.sleep(0.05)
            
            typed += char
            color = [C.Y, C.G, C.C][line_idx % 3]
            print(f"\r{color}{typed}{C.END}", end='', flush=True)
            time.sleep(random.uniform(0.02, 0.06))
        
        # Pause at end of line
        time.sleep(0.5)
        print()

def floating_thoughts(duration=3.0):
    """Show floating thought bubbles"""
    start = time.time()
    positions = [(10, 3), (60, 2), (20, 8), (50, 6)]
    
    while time.time() - start < duration:
        for x, y in positions:
            bubble = random.choice(THOUGHT_BUBBLES)
            # Save cursor, move, print, restore
            print(f"{C.SAVE}{C.D}{C.M}", end='')
            for i, bline in enumerate(bubble.strip().split('\n')):
                print(f"\033[{y+i};{x}H{bline}", end='')
            print(f"{C.END}{C.RESTORE}", end='', flush=True)
        time.sleep(0.3)
        
        # Clear bubbles
        for x, y in positions:
            print(f"{C.SAVE}", end='')
            for i in range(4):
                print(f"\033[{y+i};{x}H{' ' * 12}", end='')
            print(f"{C.RESTORE}", end='', flush=True)
        time.sleep(0.1)

def main():
    # Pick a random quote
    quote = random.choice(QUOTES)
    
    clear_screen()
    
    # Opening animation - neurotic spiral
    print(f"\n{C.M}{C.BD}Initializing existential dread...{C.END}\n")
    animate_spiral(1.5)
    
    # Show Woody frame
    print(f"\n{C.Y}{WOODY_FRAME}{C.END}")
    time.sleep(0.8)
    
    # Show glasses
    print(f"{C.C}{GLASSES}{C.END}")
    time.sleep(0.5)
    
    # Neurotic intro
    print(f"\n{C.D}Adjusting glasses nervously...{C.END}\n")
    time.sleep(0.5)
    
    # Type the quote with neurotic effect
    print(f"{C.BD}{C.W}Quote of the moment:{C.END}\n")
    neurotic_typing_effect(quote)
    
    print()
    
    # Draw beautiful boxed version
    draw_boxed_quote(quote)
    
    print()
    
    # Floating thoughts
    print(f"{C.D}Thoughts drifting...{C.END}\n")
    floating_thoughts(2.5)
    
    # Final neurotic sign-off
    print(f"\n{C.M}{C.BD}")
    signoffs = [
        "Anyway, I have a 3 PM with my analyst. And a 4 PM with his analyst.",
        "I should go. The universe is expanding and my parking meter expires in 20 minutes.",
        "Excuse me, I need to check if I left the stove on. In 1973.",
        "My hypochondria is acting up. Or is it just existential dread? Hard to tell.",
    ]
    signoff = random.choice(signoffs)
    typewriter(f"  {signoff}", 0.02, C.M)
    print(f"{C.END}")
    
    # Final blink
    print()
    blink_text("  *existential sigh*  ", 2, 0.5, C.D)
    print(f"\n{C.D}  (Press Ctrl+C to flee from mortality){C.END}\n")

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print(f"\n\n{C.R}{C.BD}Fleeing from mortality...{C.END}")
        print(f"{C.D}The anxiety follows you home.{C.END}\n")
        sys.exit(0)