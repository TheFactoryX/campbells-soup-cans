"""
Campbell's Soup Can #4841
Produced: 2026-08-25 20:45:58
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

# ANSI color codes
class C:
    R = "\033[91m"   # red
    Y = "\033[93m"   # yellow
    G = "\033[92m"   # green
    B = "\033[94m"   # blue
    M = "\033[95m"   # magenta
    C = "\033[96m"   # cyan
    W = "\033[97m"   # white
    DIM = "\033[2m"
    BOLD = "\033[1m"
    ITAL = "\033[3m"
    UNDR = "\033[4m"
    END = "\033[0m"
    BG_DARK = "\033[48;5;235m"
    BG_YEL = "\033[48;5;220m"
    BG_RED = "\033[48;5;160m"

def clear():
    os.system("cls" if os.name == "nt" else "clear")

def type_out(text, delay=0.04, color=C.W):
    for ch in text:
        sys.stdout.write(color + ch + C.END)
        sys.stdout.flush()
        time.sleep(delay)

def scroll_in(text, width=70, color=C.W, char=" "):
    """Scroll text in from the right like a marquee"""
    padding = width - len(text)
    if padding < 0:
        padding = 0
    for i in range(padding + 1):
        sys.stdout.write("\r" + " " * (padding - i) + color + text[:i] + C.END)
        sys.stdout.flush()
        time.sleep(0.02)
    print()

def box_top(width, color=C.Y):
    print(color + "╔" + "═" * (width - 2) + "╗" + C.END)

def box_mid(width, color=C.Y):
    print(color + "╠" + "═" * (width - 2) + "╣" + C.END)

def box_bot(width, color=C.Y):
    print(color + "╚" + "═" * (width - 2) + "╝" + C.END)

def box_line(text, width, color=C.Y, text_color=C.W, align="center"):
    inner = width - 4
    if align == "center":
        pad = (inner - len(text)) // 2
        left = " " * pad
        right = " " * (inner - len(text) - pad)
    elif align == "left":
        left = " "
        right = " " * (inner - len(text) - 1)
    else:
        left = " " * (inner - len(text) - 1)
        right = " "
    print(f"{color}║{C.END} {left}{text_color}{text}{C.END}{right} {color}║{C.END}")

def animate_thinking(width=70):
    """Animated 'thinking' dots"""
    thoughts = [
        "    .  o  .     ",
        "   o  .  o  .   ",
        "  .  o  .  o    ",
        " o  .  *  .  o  ",
        "  *  ~  *  ~    ",
        " ~  ✦  ~  ✦  ~  ",
    ]
    box_top(width, C.M)
    for _ in range(2):
        for t in thoughts:
            sys.stdout.write("\r" + C.M + "║" + C.END + " " + C.C + t + " " * (width - len(t) - 4) + C.M + " ║" + C.END)
            sys.stdout.flush()
            time.sleep(0.15)
        print()
    print(C.M + "║" + C.END + " " + C.DIM + C.ITAL + "( my brain is doing that thing again... )" + C.END + " " * (width - 38) + C.M + " ║" + C.END)
    box_mid(width, C.M)

def main():
    clear()
    width = 70

    # Title with color flicker
    title_colors = [C.Y, C.M, C.C, C.G, C.R]
    title = "✦  W O O D Y   A L L E N   T H I N K S   A B O U T   E X I S T E N C E  ✦"
    print()
    for i, ch in enumerate(title):
        col = title_colors[(i + hash(ch)) % len(title_colors)]
        sys.stdout.write(col + ch + C.END)
        sys.stdout.flush()
        time.sleep(0.015)
    print("\n")

    # Header box
    box_top(width, C.B)
    box_line("~ a fleeting moment of dread, served fresh ~", width, C.B, C.C)
    box_bot(width, C.B)
    print()

    # Animated thinking
    animate_thinking(width)

    # Build quote with typewriter effect
    quote_line1 = "I'm not afraid of death —"
    quote_line2 = "I just don't want to be there"
    quote_line3 = "when it happens."
    attribution = "— W. Allen (probably, while eating a knish)"

    # Print quote lines centered with typewriter
    for line in [quote_line1, quote_line2, quote_line3]:
        pad = (width - 2 - len(line)) // 2
        prefix = " " * (pad + 1)
        sys.stdout.write(prefix)
        type_out(line, 0.045, C.Y + C.BOLD)
        print()

    print()
    # Attribution with a little flair
    pad = (width - len(attribution) - 2) // 2
    print(" " * pad + C.DIM + C.ITAL + attribution + C.END)
    print()

    # Closing existential thought, slowly
    closing = "[ ...meanwhile, the universe doesn't notice, and that's the worst part. ]"
    pad = (width - len(closing) - 2) // 2
    sys.stdout.write(" " * pad)
    type_out(closing, 0.035, C.DIM + C.C)
    print("\n")

    # A little animation: an existential spiral
    box_top(width, C.DIM + C.M)
    box_line("spinning in circles, like my thoughts:", width, C.DIM + C.M, C.M, align="left")
    box_bot(width, C.DIM + C.M)
    sys.stdout.write(" ")
    frames = ["◐", "◓", "◑", "◒", "◴", "◷", "◶", "◵"]
    for _ in range(24):
        for f in frames:
            sys.stdout.write("\b" + C.M + f + C.END)
            sys.stdout.flush()
            time.sleep(0.04)
    print(" " + C.DIM + "( and yet, here we are. )" + C.END)
    print()

    # ASCII art: a tiny anxious brain
    brain = [
        "        ,---._",
        "       /   o  \\",
        "      |  ?  ?  |",
        "      |   __   |    <-- worried",
        "       \\  '--' /         about",
        "        `~~~~~'         everything",
        "          ||",
        "         /  \\",
    ]
    colors = [C.M, C.C, C.B, C.G, C.Y, C.R, C.M, C.C]
    print()
    for i, line in enumerate(brain):
        pad = (width - len(line)) // 2
        print(" " * pad + colors[i % len(colors)] + line + C.END)
        time.sleep(0.12)

    print()
    # Final blink
    msg = "★  T H A N K   Y O U   F O R   E X I S T I N G   W I T H   M E  ★"
    for _ in range(2):
        sys.stdout.write("\r" + C.Y + C.BOLD + msg.center(width) + C.END)
        sys.stdout.flush()
        time.sleep(0.6)
        sys.stdout.write("\r" + " " * width)
        sys.stdout.flush()
        time.sleep(0.2)
    print("\r" + C.Y + C.BOLD + msg.center(width) + C.END)
    print()

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\n" + C.DIM + "(interrupted — like most of my life goals)" + C.END)
        sys.exit(0)