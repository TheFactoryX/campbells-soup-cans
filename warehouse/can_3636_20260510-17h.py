"""
Campbell's Soup Can #3636
Produced: 2026-05-10 17:13:10
Worker: inclusionAI: Ring-2.6-1T (free) (inclusionai/ring-2.6-1t:free)
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
    RESET       = "\033[0m"
    BOLD        = "\033[1m"
    ITALIC      = "\033[3m"
    DIM         = "\033[2m"
    RED         = "\033[91m"
    GREEN       = "\033[92m"
    YELLOW      = "\033[93m"
    BLUE        = "\033[94m"
    MAGENTA     = "\033[95m"
    CYAN        = "\033[96m"
    WHITE       = "\033[97m"
    BG_RED      = "\033[41m"
    BG_BLUE     = "\033[44m"
    BG_MAGENTA  = "\033[45m"

def clear_lines(n=20):
    for _ in range(n):
        sys.stdout.write("\033[2K\r\033[A")
        sys.stdout.flush()

def typewrite(text, color=C.WHITE, delay=0.02, end_newline=True):
    sys.stdout.write(color)
    for ch in text:
        sys.stdout.write(ch)
        sys.stdout.flush()
        time.sleep(delay + random.uniform(-0.005, 0.008))
    sys.stdout.write(C.RESET)
    if end_newline:
        print()

def print_slow(text, color=C.WHITE, delay=0.02):
    sys.stdout.write(color)
    for ch in text:
        sys.stdout.write(ch)
        sys.stdout.flush()
        time.sleep(delay)
    sys.stdout.write(C.RESET)

def sparkle_line(width=60, colors=None):
    if colors is None:
        colors = [C.YELLOW, C.CYAN, C.MAGENTA, C.GREEN, C.RED]
    line = ""
    for i in range(width):
        c1 = random.choice(colors)
        chars = "·•✦✧*☆★░▒▓█"
        c2 = random.choice(chars)
        line += f"{c1}{c2}"
    print(f"{line}{C.RESET}")

def print_wrapped_in_box(text_lines, box_color=C.CYAN, text_color=C.WHITE,
                          accent_color=C.YELLOW, inner_padding=4, animate=True):
    margin = "  "
    max_line_len = max(len(l) for l in text_lines)
    inner_width = max_line_len + inner_padding
    total_width = inner_width + 4

    # Top border
    print(margin, end="")
    if animate:
        typewrite(f"{box_color}", end_newline=False)
        for i in range(total_width):
            sys.stdout.write(f"{accent_color}▓" if i % 3 == 0 else f"{box_color}━")
            sys.stdout.flush()
            time.sleep(0.015)
    else:
        sys.stdout.write(f"{box_color}╔{'═' * total_width}╗\n")
    print(f"{C.RESET}")

    for line in text_lines:
        padded = line.center(inner_width)
        left_wall = "║"
        right_wall = "║"
        if animate:
            print(f"{margin}{box_color}{left_wall}  {text_color}", end="")
            sys.stdout.flush()
            time.sleep(0.02)
        else:
            sys.stdout.write(f"{margin}{box_color}{left_wall}  {text_color}")

        if animate:
            typewrite(padded, color=text_color, delay=0.01, end_newline=False)
        else:
            sys.stdout.write(padded)

        print(f"{box_color}  {left_wall}{C.RESET}")
    # Bottom border
    print(margin, end="")
    if animate:
        typewrite(f"{box_color}", end_newline=False)
        for i in range(total_width):
            sys.stdout.write(f"{accent_color}▓" if i % 3 == 0 else f"{box_color}━")
            sys.stdout.flush()
            time.sleep(0.015)
    else:
        sys.stdout.write(f"{box_color}╚{'═' * total_width}╝")
    print(f"{C.RESET}")


def draw_brain():
    lines = [
        "           {}{}{}".format(C.MAGENTA, "· · ·", C.RESET),
        "        {}{}{}".format(C.MAGENTA, "  ( @ @ )  ", C.RESET),
        "         {}{}{}".format(C.MAGENTA, "\\ ~~~ /", C.RESET),
        "          {}{}{}".format(C.MAGENTA, "| ~~~ |", C.RESET),
        "           {}{}{}".format(C.MAGENTA, "\\ ~~~ /", C.RESET),
        "            {}{}{}".format(C.MAGENTA, "\\___/", C.RESET),
    ]
    for line in lines:
        print(f"  {C.DIM}{line}{C.RESET}")
        time.sleep(0.1)


def draw_lightbulb():
    bulb = [
        f"   {C.YELLOW}▒▒▒▒▒{C.RESET}",
        f"  {C.YELLOW}▒─────▒{C.RESET}",
        f" {C.YELLOW}▒· · ··▒{C.RESET}",
        f"{C.YELLOW}│ WOW! │{C.RESET}",
        f"{C.YELLOW}▒· · ··▒{C.RESET}",
        f"  {C.YELLOW}▒─────▒{C.RESET}",
        f"   {C.YELLOW}▒▒▒▒▒{C.RESET}",
    ]
    for line in bulb:
        print(f"  {line}")
        time.sleep(0.08)


def draw_anxiety_waves():
    waves = [
        f"  {C.DIM}~~~~~~~~~~~~~~·~·~·~·~/~~~~~~~~~~~~~~{C.RESET}",
        f"  {C.DIM}~·~·~·~/~~~~~~~~~~~~~~·~·~·~/~~~~~~~~~~{C.RESET}",
        f"  {C.DIM}~~~~~~~~~/~~~~~~~~·~·~·~/~~~~~~~~~~~~~{C.RESET}",
    ]
    print()
    for w in waves:
        print(w)
        time.sleep(0.08)


def philosophical_existential_doodle():
    print()
    sparkle_line(50)
    time.sleep(0.1)

    sys.stdout.write(f"\n  {C.DIM}")
    print("  ┌──── Why do we exist? ────────────┐")
    print("  │  " + " " * 31 + "│")
    print("  │   " + C.RED + "ERROR 404:" + C.DIM + " Meaning not found." + " " * 12 + "│")
    print(f"  │   {C.DIM}" + " " * 31 + "│")
    print("  │   Have you tried eating?" + " " * 8 + "│")
    print(f"  │   {C.CYAN}> yes{C.DIM}" + " " * 25 + "│")
    print(f"  │   {C.CYAN}> thinking too hard{C.DIM}" + " " * 11 + "│")
    print(f"  │   {C.CYAN}> not dying{C.DIM}" + " " * 20 + "│")
    print(f"  │   {C.CYAN}> therapy??{DIM}" + " " * 20 + "│")
    print("  │   " + C.DIM + "Reconnecting..." + " " * 17 + "│")
    print("  │   " + C.GREEN + "Connected." + C.DIM + " No new updates." + " " * 11 + "│")
    sys.stdout.write(f"  {C.DIM}")
    print("  └───────────────────────────────────────┘")
    print(f"  {C.RESET}")
    time.sleep(0.3)


def existential_nyan_cat_frame():
    """A little animated existential crisis cat"""
    frames = [
        f"  {C.MAGENTA}  ( ͡° ͜ʖ ͡°)  {C.DIM}┬─┬ ノ( ゜-゜ノ){C.RESET}",
        f"  {C.MAGENTA}  ( ◕‿◕ )  {C.DIM}┬─┬ ノ( ゜-゜ノ){C.RESET}",
        f"  {C.MAGENTA}  ( ͡° ͜ʖ ͡°)  {C.DIM}┬─┬ ノ( ゜-゜ノ){C.RESET}",
        f"  {C.MAGENTA}  ( ◕‿◕ )  {C.DIM}┬─┬ ノ( ゜-゜ノ){C.RESET}",
    ]
    print()
    for i, frame in enumerate(frames):
        sys.stdout.write("\r")
        sys.stdout.write(frame)
        sys.stdout.flush()
        time.sleep(0.35)
    print()


def main():
    # Clear terminal if possible
    print("\033c", end="")

    # Opening sparkle
    sparkle_line(60)

    # Title
    title = "WOODY'S PHILOSOPHY CORNER"
    print(f"\n  {C.RED}{C.BOLD}{C.ITALIC}{title.center(58)}{C.RESET}\n")
    time.sleep(0.3)

    # Existential doodle
    philosophical_existential_doodle()
    time.sleep(0.5)

    # Anxiety waves
    draw_anxiety_waves()

    # Little brain
    print(f"\n  {C.DIM}The Overthinker's Thought Process:{C.RESET}\n")
    draw_brain()

    time.sleep(0.4)

    print(f"\n  {C.DIM}Conclusion reached:{C.RESET}")
    print()

    # The BIG QUOTE in a box
    quote_lines = [
        f"{C.ITALIC}I've spent most of my life regretting",
        "the things I haven't done—like skydiving,",
        "learning Italian, or having a meaningful",
        "relationship. But I have never once",
        "regretted staying in bed on a Saturday",
        "afternoon eating a cheese Danish and",
        "wondering if God exists. Probably not.",
        "But the Danish was exceptional.",
        f"{C.RESET}",
    ]

    clean_lines = [
        "I've spent most of my life regretting",
        "the things I haven't done—like skydiving,",
        "learning Italian, or having a meaningful",
        "relationship. But I have never once",
        "regretted staying in bed on a Saturday",
        "afternoon eating a cheese Danish and",
        "wondering if God exists. Probably not.",
        "But the Danish was exceptional.",
    ]

    margin = " " * 8
    print(f"{margin}", end="")
    print(f"{C.CYAN}{'╔' + '═' * 56 + '╗'}")
    print(f"{margin}{C.CYAN}║{'':56}║")
    for i, line in enumerate(clean_lines):
        print(f"{margin}{C.CYAN}║  {C.RESET}{C.WHITE}{C.ITALIC}{line}{C.RESET}{C.CYAN}{'  ' + '║':>{56 - len(line)}}{C.RESET}")
        time.sleep(0.12)
    print(f"{margin}{C.CYAN}║{'':56}║")
    print(f"{margin}{C.CYAN}╚{'═' * 56}╝{C.RESET}")
    time.sleep(0.3)

    # Attribution
    print(f"\n  {C.DIM}   ── attributed to a very anxious man in Manhattan{C.RESET}")

    # Cat moment
    existential_nyan_cat_frame()

    # Closing sparkle
    print()
    sparkle_line(60)

    # Epilogue
    epilogue = f"{C.YELLOW}{C.DIM}  \"I don't want to achieve immortality through my work.{C.RESET}"
    epilogue2 = f"{C.YELLOW}{C.DIM}   I want to achieve it through not dying.{C.RESET}"
    epilogue3 = f"{C.YELLOW}{C.DIM}   ...but also the Danish helps.{C.RESET}"

    print()
    print(f"  {C.GREEN}{'░' * 52}{C.RESET}")
    typewrite(epilogue, delay=0.03, end_newline=True)
    typewrite(epilogue2, delay=0.03, end_newline=True)
    typewrite(epilogue3, delay=0.03, end_newline=True)
    print(f"  {C.GREEN}{'░' * 52}{C.RESET}")

    # Final doodle
    time.sleep(0.5)
    print()
    draw_lightbulb()
    print(f"  {C.DIM}...still no answers. back to the Danish.{C.RESET}\n")


if __name__ == "__main__":
    main()