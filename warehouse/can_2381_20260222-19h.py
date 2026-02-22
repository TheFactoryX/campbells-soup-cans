"""
Campbell's Soup Can #2381
Produced: 2026-02-22 19:37:16
Worker: Qwen: Qwen3 VL 235B A22B Thinking (qwen/qwen3-vl-235b-a22b-thinking)
Employment: Volunteer
Flavor: Woody Allen Philosophy
Quality: ❌ (broken)

Made by Machine #0 - Production Line 0
Like Warhol's soup cans - same but different.
Each can is the same flavor, made by different hands.
"""

import time
import textwrap

quote = (
    "I'm not afraid of death; I just don't want to be there when it happens. "
    "And if I am, I hope it's during a comedy show so at least I go out laughing. "
    "But then again, what if the comedian is bad? Then it's a waste of a death."
)

def print_woody_quote():
    inner_width = 55
    lines = textwrap.wrap(quote, width=inner_width)
    padded_lines = [line.ljust(inner_width) for line in lines]
    total_width = inner_width + 4
    border = '═' * total_width

    print('\033[96m' + ' ' * 10 + '┌' + '─' * (total_width - 2) + '┐')
    print('\033[96m' + ' ' * 10 + '│' + '\033[97m' + '  WOODY ALLEN PHILOSOPHY' + '\033[96m' + ' ' * (total_width - 25) + '│')
    
    time.sleep(0.5)
    print('\033[96m' + ' ' * 10 + '├' + '─' * (total_width - 2) + '┤')
    
    for i, line in enumerate(padded_lines):
        if i == 0:
            time.sleep(0.7)
        print('\033[96m' + ' ' * 10 + '│\033[93m', end='')
        for char in line:
            print(char, end='', flush=True)
            time.sleep(0.02)
        print('\033[96m│')
        time.sleep(0.3)
    
    time.sleep(0.5)
    print('\033[96m' + ' ' * 10 + '└' + '─' * (total_width - 2) + '┘')
    print('\033[97m' + ' ' * 10 + ' ' * 2 + '© 2023 Neurotic Philosophy Dept.' + ' ' * (total_width - 35))

def main():
    print('\033[2J\033[H', end='')  # Clear screen
    print('\033[1;37m' + ' ' * 15 + '╔══════════════════════════════════════╗')
    print('\033[1;37m' + ' ' * 15 + '║' + '\033[3m\033[35m' + '   "The universe is expanding, which is a' + ' ' * 7 + '\033[0m\033[1;37m' + '║')
    print('\033[1;37m' + ' ' * 15 + '║' + '\033[3m\033[35m' + '    relief because I feel like it's been' + ' ' * 8 + '\033[0m\033[1;37m' + '║')
    print('\033[1;37m' + ' ' * 15 + '║' + '\033[3m\033[35m' + '    getting smaller and smaller. Or maybe' + ' ' * 8 + '\033[0m\033[1;37m' + '║')
    print('\033[1;37m' + ' ' * 15 + '║' + '\033[3m\033[35m' + '    that's just my anxiety. It\'s hard to' + ' ' * 8 + '\033[0m\033[1;37m' + '║')
    print('\033[1;37m' + ' ' * 15 + '║' + '\033[3m\033[35m' + '    tell the difference sometimes."      ' + ' ' * 8 + '\033[0m\033[1;37m' + '║')
    print('\033[1;37m' + ' ' * 15 + '╚══════════════════════════════════════╝')
    time.sleep(1.5)
    print_woody_quote()
    print('\033[0m')

if __name__ == "__main__":
    main()