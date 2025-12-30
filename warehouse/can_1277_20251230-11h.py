"""
Campbell's Soup Can #1277
Produced: 2025-12-30 11:31:00
Worker: Xiaomi: MiMo-V2-Flash (free) (xiaomi/mimo-v2-flash:free)
Employment: Volunteer
Flavor: Woody Allen Philosophy
Quality: ❌ (missing print)

Made by Machine #0 - Production Line 0
Like Warhol's soup cans - same but different.
Each can is the same flavor, made by different hands.
"""

#!/usr/bin/env python3

import sys
import time
import random

def woody_allen_quote():
    quotes = [
        "I'm not afraid of death; I just don't want to be there when it happens.",
        "Life is full of misery, loneliness, and suffering — and it's all over much too soon.",
        "I don't want to achieve immortality through my work; I want to achieve it through not dying.",
        "My only fear is that I'll live forever and run out of things to worry about.",
        "Time is nature's way of keeping everything from happening at once. I wish it would slow down; I'm overwhelmed.",
        "I'm at two with nature. I think it's plotting something.",
        "If you want to make God laugh, tell him about your plans. I stopped making plans; it's less disappointing.",
        "I love nature, but nature keeps making bugs. Why?",
        "Life is a great big canvas, and you should throw all the paint on it you can. I spilled mine; it looks like anxiety.",
        "I don't have a solution, but I admire the problem."
    ]
    return random.choice(quotes)

def ansi(code):
    return f"\033[{code}m"

def clear_screen():
    sys.stdout.write("\033[2J\033[H")

def type_text(text, delay=0.03, color=ansi("97")):
    # 97 = bright white
    sys.stdout.write(color)
    for ch in text:
        sys.stdout.write(ch)
        sys.stdout.flush()
        time.sleep(delay)
    sys.stdout.write(ansi("0") + "\n")

def draw_ascii_figure(width=52):
    # A playful Woody-esque figure: nervous, glasses, hands raised
    face = [
        r"         .---.         ",
        r"        /_____\        ",
        r"       |  o o  |       ",
        r"       |   -   |       ",
        r"        \_____/        ",
        r"          | |          ",
        r"         /   \         "
    ]
    body = [
        r"   (\,/,/)            ",
        r"  (o_o)               ",
        r"  /)__(\              ",
        r"  _\\//_              ",
        r" /      \             ",
        r"(________)            "
    ]
    # Combine and center inside a box of width 'width'
    all_lines = face + body
    centered = []
    for line in all_lines:
        # Strip ANSI codes if any, then center
        stripped = line.replace("\033", "")
        pad_left = (width - len(stripped)) // 2
        pad_right = width - len(stripped) - pad_left
        centered.append(" " * pad_left + stripped + " " * pad_right)
    return centered

def draw_box(text, width=60, fg="95", bg="45", style="bold", effect="blink"):
    # Create a colorful, blinking box around the text
    # Styles and effects: bold=1, faint=2, italic=3, underline=4, blink=5, reverse=7
    style_map = {"bold": "1", "faint": "2", "italic": "3", "underline": "4", "blink": "5", "reverse": "7"}
    s_code = style_map.get(style, "1")
    e_code = style_map.get(effect, "5")
    top = f"{ansi(f'{e_code};{s_code};{fg};{bg}')}┌{'─' * (width - 2)}┐{ansi('0')}\n"
    middle = f"{ansi(f'{e_code};{s_code};{fg};{bg}')}│{' ' * (width - 2)}│{ansi('0')}\n"
    bottom = f"{ansi(f'{e_code};{s_code};{fg};{bg}')}└{'─' * (width - 2)}┘{ansi('0')}\n"
    
    sys.stdout.write(top)
    # Write the quote wrapped inside
    wrapped = []
    max_len = width - 4
    words = text.split()
    line = ""
    for w in words:
        if len(line) + len(w) + 1 <= max_len:
            line += w + " "
        else:
            wrapped.append(line.rstrip())
            line = w + " "
    if line:
        wrapped.append(line.rstrip())
    
    for wline in wrapped:
        left_pad = (width - len(wline) - 2) // 2
        right_pad = width - len(wline) - 2 - left_pad
        sys.stdout.write(f"{ansi(f'{e_code};{s_code};{fg};{bg}')}│ {' ' * left_pad}{wline}{' ' * right_pad} │{ansi('0')}\n")
    sys.stdout.write(bottom)

def color_dots_animation():
    # Animate a few colorful dots with typewriter effect
    dots = [".", ".", "."]
    colors = ["91", "92", "93", "94", "95", "96"]
    for d in dots:
        c = random.choice(colors)
        sys.stdout.write(ansi(c) + d + ansi("0"))
        sys.stdout.flush()
        time.sleep(random.uniform(0.25, 0.5))
    sys.stdout.write("\n")

def run():
    clear_screen()
    # Header
    header = " W O O D Y   A L L E N   Q U O T E   G E N E R A T O R "
    hlen = len(header)
    sys.stdout.write(f"{ansi('1;38;5;226')}╔{'═' * hlen}╗{ansi('0')}\n")
    sys.stdout.write(f"{ansi('1;38;5;226')}║{ansi('3;38;5;226')}{header}{ansi('1;38;5;226')}║{ansi('0')}\n")
    sys.stdout.write(f"{ansi('1;38;5;226')}╚{'═' * hlen}╝{ansi('0')}\n\n")

    # Draw figure
    figure_lines = draw_ascii_figure()
    for line in figure_lines:
        sys.stdout.write(ansi("36") + line + ansi("0") + "\n")
        time.sleep(0.05)

    time.sleep(0.5)

    # Quote with typewriter
    quote = woody_allen_quote()
    type_text(quote, delay=0.035, color=ansi("97"))

    time.sleep(0.5)

    # Animated dots
    color_dots_animation()
    time.sleep(0.3)

    # Philosophical add-on line (blinking box)
    add_line = "The universe is expansion; I am contraction. Still, I hope to meet somewhere in the middle."
    draw_box(add_line, width=60, fg="91", bg="45", style="bold", effect="blink")
    sys.stdout.write("\n")

    # Closing signature
    sys.stdout.write(f"{ansi('2;37')}— a neurotic New Yorker (and you){ansi('0')}\n")

if __name__ == "__main__":
    try:
        run()
    except KeyboardInterrupt:
        sys.stdout.write("\n" + ansi("0") + "Fine, I'll worry later.\n")
    except Exception:
        # Minimal catch to keep the program valid even in odd terminals
        sys.stdout.write("Oops, something unexpected happened (probably existential).")