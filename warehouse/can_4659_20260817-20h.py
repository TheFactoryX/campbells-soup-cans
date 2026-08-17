"""
Campbell's Soup Can #4659
Produced: 2026-08-17 20:43:51
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
RESET = '\033[0m'
BOLD = '\033[1m'
DIM = '\033[2m'
ITALIC = '\033[3m'
UNDERLINE = '\033[4m'
BLINK = '\033[5m'

# Colors
RED = '\033[91m'
GREEN = '\033[92m'
YELLOW = '\033[93m'
BLUE = '\033[94m'
MAGENTA = '\033[95m'
CYAN = '\033[96m'
WHITE = '\033[97m'
GRAY = '\033[90m'

# Background colors
BG_BLACK = '\033[40m'
BG_RED = '\033[41m'
BG_GREEN = '\033[42m'
BG_YELLOW = '\033[43m'
BG_BLUE = '\033[44m'
BG_MAGENTA = '\033[45m'
BG_CYAN = '\033[46m'
BG_WHITE = '\033[47m'

# Woody Allen quotes (original, in his style)
WOODY_QUOTES = [
    "I took a speed-reading course and read 'War and Peace' in twenty minutes. It involves Russia.",
    "I don't want to achieve immortality through my work. I want to achieve it through not dying.",
    "The only time my wife and I had a simultaneous orgasm was when the judge signed the divorce papers.",
    "I'm not afraid of death. I just don't want to be there when it happens.",
    "Life is full of misery, loneliness, and suffering - and it's all over much too soon.",
    "I have bad reflexes. I was once run over by a car being pushed by two guys.",
    "I'm astounded by people who want to 'know' the universe when it's hard enough to find your way around Chinatown.",
    "Money is better than poverty, if only for financial reasons.",
    "I failed to make the chess team because of my height. I'm too short to reach the board.",
    "There is no question that there is an unseen world. The problem is, how far is it from midtown and how late is it open?",
    "I don't believe in an afterlife, although I am bringing a change of underwear.",
    "The food here is terrible, and such small portions!",
    "I can't listen to too much Wagner. I start getting the urge to conquer Poland.",
    "If you want to make God laugh, tell him about your plans.",
    "I'm at two with nature. I have a place in the country where the deer and the antelope play... and I shoot them.",
    "I don't know the question, but sex is definitely the answer.",
    "My one regret in life is that I'm not someone else.",
    "I'm such a good lover because I practice a lot on my own.",
    "The lion and the lamb shall lie down together, but the lamb won't get much sleep.",
    "I have a very pessimistic view of life. You should know this about me if we're going to go out.",
]

def clear_screen():
    print('\033[2J\033[H', end='')

def hide_cursor():
    print('\033[?25l', end='')

def show_cursor():
    print('\033[?25h', end='')

def typewriter(text, delay=0.02, color=WHITE):
    for char in text:
        print(f'{color}{char}{RESET}', end='', flush=True)
        time.sleep(delay)
    print()

def fade_in(text, color=WHITE, steps=10):
    for i in range(steps + 1):
        intensity = i / steps
        # Simulate fade by printing with increasing brightness
        r = int(255 * intensity)
        g = int(255 * intensity)
        b = int(255 * intensity)
        print(f'\033[38;2;{r};{g};{b}m{text}\033[0m', end='\r')
        time.sleep(0.03)
    print()

def rainbow_text(text):
    colors = [RED, YELLOW, GREEN, CYAN, BLUE, MAGENTA]
    result = ''
    for i, char in enumerate(text):
        if char != ' ':
            result += f'{colors[i % len(colors)]}{char}'
        else:
            result += ' '
    return result + RESET

def draw_box(text_lines, border_color=CYAN, title=None):
    max_len = max(len(line.replace('\033[0m', '').replace('\033[91m', '').replace('\033[92m', '').replace('\033[93m', '').replace('\033[94m', '').replace('\033[95m', '').replace('\033[96m', '').replace('\033[97m', '').replace('\033[1m', '').replace('\033[3m', '')) for line in text_lines)
    
    # Clean length calculation
    def clean_len(s):
        import re
        return len(re.sub(r'\033\[[0-9;]*m', '', s))
    
    max_len = max(clean_len(line) for line in text_lines)
    if title:
        max_len = max(max_len, clean_len(title) + 4)
    
    width = max_len + 4
    
    top = f'{border_color}╔{"═" * width}╗{RESET}'
    bottom = f'{border_color}╚{"═" * width}╝{RESET}'
    
    print(top)
    
    if title:
        title_line = f' {title} '
        padding = width - clean_len(title_line)
        left_pad = padding // 2
        right_pad = padding - left_pad
        print(f'{border_color}║{RESET}{" " * left_pad}{BOLD}{YELLOW}{title}{RESET}{" " * right_pad}{border_color}║{RESET}')
        print(f'{border_color}╠{"═" * width}╣{RESET}')
    
    for line in text_lines:
        clean_line = line
        padding = width - clean_len(clean_line)
        print(f'{border_color}║{RESET} {line}{" " * padding}{border_color}║{RESET}')
    
    print(bottom)

def woody_face():
    return f"""
{CYAN}      ╭─────────────╮{RESET}
{CYAN}      │  {WHITE}@   @{CYAN}   │{RESET}   {YELLOW}"*adjusts glasses nervously*"{RESET}
{CYAN}      │  {WHITE}  ^  {CYAN}   │{RESET}
{CYAN}      │  {MAGENTA}\\___/{CYAN}   │{RESET}   {GREEN}"Why is there something{RESET}
{CYAN}      ╰─────────────╯{RESET}   {GREEN}rather than nothing?{RESET}
                    {GREEN}And why the waitress{RESET}
                    {GREEN}never gets my order right?"{RESET}
"""

def animate_entrance():
    frames = [
        f"""
{GRAY}         .--.         {RESET}
{GRAY}        / .. \\        {RESET}
{GRAY}       |      |       {RESET}
{GRAY}       \\ __ /        {RESET}
        """,
        f"""
{CYAN}         .--.         {RESET}
{CYAN}        / .. \\        {RESET}
{CYAN}       |      |       {RESET}
{CYAN}       \\ __ /        {RESET}
        """,
        f"""
{YELLOW}         .--.         {RESET}
{YELLOW}        / @@ \\        {RESET}
{YELLOW}       |  ^^  |       {RESET}
{YELLOW}       \\ __ /        {RESET}
        """,
        f"""
{GREEN}         .--.         {RESET}
{GREEN}        / @@ \\        {RESET}
{GREEN}       |  ^^  |       {RESET}
{GREEN}       \\__/  \\       {RESET}
        """,
    ]
    
    for frame in frames:
        clear_screen()
        print(frame)
        time.sleep(0.2)

def sparkle_animation(duration=1.5):
    sparkles = ['✦', '✧', '★', '☆', '✨', '⋆', '✰', '✵']
    end_time = time.time() + duration
    while time.time() < end_time:
        x = random.randint(5, 70)
        y = random.randint(2, 15)
        sparkle = random.choice(sparkles)
        color = random.choice([RED, YELLOW, GREEN, CYAN, BLUE, MAGENTA])
        print(f'\033[{y};{x}H{color}{sparkle}{RESET}', end='', flush=True)
        time.sleep(0.05)
        print(f'\033[{y};{x}H ', end='', flush=True)

def main():
    hide_cursor()
    clear_screen()
    
    # Pick a random quote
    quote = random.choice(WOODY_QUOTES)
    
    # Animate entrance
    animate_entrance()
    
    # Show Woody face
    clear_screen()
    print(woody_face())
    time.sleep(1.5)
    
    # Type out the quote in a nice box
    clear_screen()
    
    # Word wrap the quote
    words = quote.split()
    lines = []
    current_line = ""
    max_width = 55
    
    for word in words:
        test_line = current_line + (" " if current_line else "") + word
        if len(test_line) <= max_width:
            current_line = test_line
        else:
            lines.append(current_line)
            current_line = word
    if current_line:
        lines.append(current_line)
    
    # Color each line differently
    colored_lines = []
    colors = [CYAN, YELLOW, GREEN, MAGENTA, BLUE]
    for i, line in enumerate(lines):
        colored_lines.append(f'{colors[i % len(colors)]}{ITALIC}{line}{RESET}')
    
    draw_box(colored_lines, border_color=MAGENTA, title=f'{BOLD}WOODY ALLEN WISDOM{RESET}')
    
    print()
    
    # Typewriter signature
    time.sleep(0.5)
    typewriter(f'{GRAY}— Woody Allen (probably){RESET}', delay=0.03, color=GRAY)
    print()
    
    # Final sparkle
    sparkle_animation(1)
    
    # Final message
    print(f'\n{DIM}Press Enter to face the void...{RESET}')
    input()
    
    show_cursor()
    clear_screen()
    print(f'{YELLOW}Thanks for reading. I\'d stay longer but I have a therapy appointment.{RESET}\n')

if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        show_cursor()
        clear_screen()
        print(f'\n{RED}Interrupted. Typical. Even my programs have abandonment issues.{RESET}\n')
    except Exception as e:
        show_cursor()
        print(f'\n{RED}Error: {e}{RESET}')
        print(f'{GRAY}See? Even the universe conspires against me.{RESET}\n')