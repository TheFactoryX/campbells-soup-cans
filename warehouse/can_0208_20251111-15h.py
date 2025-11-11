"""
Campbell's Soup Can #208
Produced: 2025-11-11 15:33:58
Worker: MiniMax: MiniMax M2 (free) (minimax/minimax-m2:free)
Employment: Volunteer
Flavor: Woody Allen Philosophy
Quality: ❌ (broken)

Made by Machine #0 - Production Line 0
Like Warhol's soup cans - same but different.
Each can is the same flavor, made by different hands.
"""

import sys
import time
import shutil

# ANSI palette helpers
CODES = {
    'reset': '\033[0m',
    'bold': '\033[1m',
    'dim': '\033[2m',
    'blink': '\033[5m',
    'black': '\033[30m',
    'red': '\033[31m',
    'green': '\033[32m',
    'yellow': '\033[33m',
    'blue': '\033[34m',
    'magenta': '\033[35m',
    'cyan': '\033[36m',
    'white': '\033[37m',
    'gray': '\033[90m',
    'orange': '\033[38;5;208m',
    'pink': '\033[38;5;205m',
    'teal': '\033[38;5;14m',
    'lavender': '\033[38;5;189m',
    'gold': '\033[38;5;220m',
    'aqua': '\033[38;5;45m',
    'rose': '\033[38;5;211m',
}
RAINBOW = [
    CODES['gold'],      # yellow/gold
    CODES['orange'],    # orange
    CODES['rose'],      # pink-rose
    CODES['magenta'],   # magenta
    CODES['purple'],    # not defined, fallback using blue then reset
    CODES['blue'],      # blue
    CODES['teal'],      # cyan/teal
    CODES['green'],     # green
]

def term_width():
    try:
        return shutil.get_terminal_size((80, 24)).columns
    except Exception:
        return 80

def is_dumb():
    return not sys.stdout.isatty() or 'NO_COLOR' in os.environ if 'os' in globals() else not sys.stdout.isatty()

def strip_ansi(s):
    import re
    return re.sub(r'\033\[[0-9;]*m', '', s)

def fit_text(s, width):
    s_vis = strip_ansi(s)
    if len(s_vis) <= width:
        return s
    # preserve last 3 chars for ellipsis
    ell = "..."
    return s[:max(0, width - len(ell))] + ell

def center_visual(s, width, fill=' '):
    vis_len = len(strip_ansi(s))
    pad = max(0, (width - vis_len) // 2)
    return fill * pad + s

def colorize_text(text, color):
    return f"{color}{text}{CODES['reset']}"

def make_banner(text, color):
    width = max(30, min(term_width() - 4, 72))
    inner = fit_text(text, width - 4)
    top = "+" + "-"*(width-2) + "+"
    mid = "|" + " "*(width-2) + "|"
    line = "|" + center_visual(inner, width-2) + "|"
    return f"{color}{top}{CODES['reset']}\n{CODES['reset']}{color}{mid}{CODES['reset']}\n{CODES['reset']}{color}{line}{CODES['reset']}\n{CODES['reset']}{color}{mid}{CODES['reset']}\n{CODES['reset']}{color}{top}{CODES['reset']}"

def type_gradient(text, delay=0.028, newline=True):
    # Print characters with a rainbow gradient effect
    for i, ch in enumerate(text):
        color = RAINBOW[i % len(RAINBOW)]
        sys.stdout.write(f"{color}{ch}{CODES['reset']}")
        sys.stdout.flush()
        time.sleep(delay)
    if newline:
        sys.stdout.write("\n")
        sys.stdout.flush()

def print_header():
    width = max(28, min(term_width() - 6, 80))
    # Small ASCII camera with spinning sprockets
    sprocket_spin = ["/", "-", "\\", "|"]
    film_body_top = f"{CODES['gray']}  {CODES['bold']}{CODES['lavender']}~~~{CODES['reset']}"
    film_body_mid = f"{CODES['gray']}  {CODES['bold']}{CODES['cyan']}[#####]{CODES['reset']}"
    film_body_bot = f"{CODES['gray']}  {CODES['bold']}{CODES['lavender']}~~~{CODES['reset']}"

    for frame in range(1, 9):
        w = min(16 + frame, width - 4)
        left_s = sprocket_spin[frame % 4]
        right_s = sprocket_spin[(frame + 2) % 4]
        top = f"{CODES['gray']}+{'-'*w}+{CODES['reset']}"
        mid = f"{CODES['gray']}|{CODES['reset']}{film_body_top}{' '*max(0, w - 12 - (frame%2))}{CODES['gray']}|{CODES['reset']}"
        mid2 = f"{CODES['gray']}|{CODES['reset']}{film_body_mid}{' '*max(0, w - 12)}{CODES['gray']}|{CODES['reset']}"
        bot = f"{CODES['gray']}|{CODES['reset']}{film_body_bot}{' '*max(0, w - 12 - (frame%2))}{CODES['gray']}|{CODES['reset']}"
        botline = f"{CODES['gray']}+{'-'*w}+{CODES['reset']}"
        sprocket = f"{CODES['gray']} {left_s} {CODES['white']} WoodyCam MK.I {CODES['gray']} {right_s}{CODES['reset']}"

        sys.stdout.write("\033[2J\033[H")  # clear screen
        print(make_banner("A Quote by Woody", CODES['gold']))
        print()
        print(sprocket)
        print(top)
        print(mid)
        print(mid2)
        print(bot)
        print(botline)
        time.sleep(0.12)

    # Hold final frame
    sys.stdout.write("\033[2J\033[H")
    print(make_banner("A Quote by Woody", CODES['gold']))
    print()

def main():
    quote = (
        "I took a speed-run class on 'How to Live Authentically,' but the teacher "
        "was a squirrel with a thesaurus, and my anxiety kept editing my memories. "
        "Now I’m not sure if I exist, but I definitely need a snack."
    )
    author = "— a neurotic man in a trench coat, circa Tuesday"

    print_header()

    # Quote box
    box_color = CODES['cyan']
    text_color = CODES['white']
    attr_color = CODES['gray']

    width = max(30, min(term_width() - 4, 78))
    inside = width - 4

    # Fit each line to inside width
    lines = []
    words = quote.split()
    cur = ""
    for w in words:
        if len(strip_ansi(cur + " " + w)) <= inside:
            cur = (cur + " " + w).strip()
        else:
            lines.append(cur)
            cur = w
    if cur:
        lines.append(cur)

    # Title bar
    title = f"{CODES['bold']}{CODES['gold']}PHILOSOPHICAL MOMENT:{CODES['reset']}"
    print(f"{box_color}+{'-'*inside}+{CODES['reset']}")
    print(f"{box_color}|{CODES['reset']}{title}{' '*(inside - len(strip_ansi(title)))}{box_color}|{CODES['reset']}")
    print(f"{box_color}+{'-'*inside}+{CODES['reset']}")

    # Quote lines with gradient typewriter
    top_bot = f"{box_color}+{'-'*inside}+{CODES['reset']}"
    print(top_bot)
    for ln in lines:
        line = f"  {fit_text(ln, inside-4)}  "
        type_gradient(line, delay=0.018, newline=True)
    print(top_bot)

    # Attribution
    attr = fit_text(author, inside)
    print(f"{box_color}|{attr_color}{attr:{<{inside}}}{box_color}|{CODES['reset']}")
    print(top_bot)

    # Playful footer
    footer = f"{CODES['blink']}{CODES['teal']}Please deposit 2 quarters of existential dread into the happiness slot.{CODES['reset']}"
    print()
    if sys.stdout.isatty():
        type_gradient(footer, delay=0.01, newline=True)
    else:
        print(footer)

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        # A polite exit
        sys.stdout.write(f"\n{CODES['gray']}…fleeing into thezv oid of inbox zero…{CODES['reset']}\n")
        sys.stdout.flush()