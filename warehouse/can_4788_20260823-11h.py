"""
Campbell's Soup Can #4788
Produced: 2026-08-23 11:34:15
Worker: NVIDIA: Nemotron Nano 12B 2 VL (free) (nvidia/nemotron-nano-12b-v2-vl:free)
Employment: Volunteer
Flavor: Woody Allen Philosophy
Quality: ❌ (broken)

Made by Machine #0 - Production Line 0
Like Warhol's soup cans - same but different.
Each can is the same flavor, made by different hands.
"""

import time
import random
import os
import sys

def print_ansi(text, color='\033[0m'):
    codes = {
        'green': '\033[32m', 'red': '\033[31m', 'yellow': '\033[33m',
        'blue': '\033[34m', 'magenta': '\033[35m', 'cyan': '\033[36m'
    }
    print(color + text + '\033[0m')

def fuzzy_type(quote):
    chars = list(quote)
    current = ""
    for char in chars:
        wait = random.uniform(0.2, 0.7)
        for _ in range(3):
            color = random.choice(['\033[31m', '\033[33m', '\033[35m'])
            print(color + current + char, end='\r')
            sys.stdout.flush()
            time.sleep(wait)
        current += char
        time.sleep(0.1)
    print()

def generate_ascii_quote():
    words = [
        ("IMAGINE", "\033[33m"), ("NOT", "\033[31m"), ("BEING", "\033[36m"),
        ("A", "\033[34m"), ("TOAST", "\033[35m"), "— Life", "\033[32m"), 
        ("is", "\033[33m"), ("like", "\033[31m"), ("a", "\033[34m"), 
        ("bad", "\033[35m"), ("soap", "\033[32m"), "Offer!", "\033[0m"
    ]
    shuffled = random.sample(words, len(words))
    quote = ""
    for text, color in shuffled:
        quote += current + color + text + '\033[0m'
        current = color + text
    return quote

def create_box(text):
    lines = text.split('\n')
    max_len = max(len(line) for line in lines)
    width = max_len + 4
    border = "\033[30m" + "+" + "*" * 2 + "+" + "*" * (max_len + 2) + "+" + "\033[0m"
    header = "\033[30m" + "|" + " " + " " + "|" + "|" + "-" * (max_len + 2) + "|\033[0m"
    footer = "\033[30m" + "+" + "-" * 2 + "+" + "-" * (max_len + 2) + "+\033[0m"
    result = [border]
    result.append(header)
    for line in lines:
        result.append(
            "\033[30m" + "| " + line.ljust(max_len) + "    |\033[0m")
    result.append(footer)
    return '\n'.join(result)

def show_animation(text):
    frames = [
        f"=={text[0]}{text[1]}.{text[2]}==",
        f"=={text[1]}{text[2]}.{text[0]}==",
        f"=={text[2]}{text[0]}.{text[1]}=="
    ]
    for frame in frames:
        print("\033c")
        print("\033[30m" + "="*40)
        print(f"\033[33m{frame}\033[0m")
        print("\033[30m" + "="*40)
        time.sleep(0.5)

ascii_quote = generate_ascii_quote()
print_ansi("\n" + "="*60)
print("<?=")
print("  wondered Woody".upper(), color='\033[33m')
print_ansi(" (looking up from laptop)...", 'yellow')
quote = generate_ascii_quote().split('\n')[0]
print_ansi(quote + "...", '\033[31m')
print("Dear, phhil", color='\033[36m' + "(not phillies))", '\033[0m')
input("\n[Press Enter to make it worse...]")
print_ansi("\n" + "="*60)
print("<?=" + "\033[35m"*15 + "?",
       "\033[34m"*15 + "hmm",
       "\033[36m"*15 + "#what's","_",
       "\033[37m"*15 + "?",
       sep='\n', end='\n')
show_animation("HERESIES")
input("\n[Second input to quirk out]")