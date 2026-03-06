"""
Campbell's Soup Can #2605
Produced: 2026-03-06 17:52:59
Worker: Qwen: Qwen3 VL 235B A22B Thinking (qwen/qwen3-vl-235b-a22b-thinking)
Employment: Volunteer
Flavor: Woody Allen Philosophy
Quality: ✅

Made by Machine #0 - Production Line 0
Like Warhol's soup cans - same but different.
Each can is the same flavor, made by different hands.
"""

import time
import sys

def print_slow(text, delay=0.02):
    for char in text:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(delay)
    sys.stdout.write('\n')

def main():
    width = 60
    yellow = '\033[93m'
    blue = '\033[94m'
    green = '\033[92m'
    red = '\033[91m'
    magenta = '\033[95m'
    reset = '\033[0m'
    
    # ASCII art of neurotic Woody
    woody_art = [
        f"{magenta}     ,-----,      {reset}",
        f"{magenta}    / (o o) \\    {reset}",
        f"{magenta}   |   \\^/   |   {reset}",
        f"{magenta}   |  (o_o)  |   {reset}",
        f"{magenta}    \\  ---  /    {reset}",
        f"{magenta}     `-----'     {reset}",
        f"{magenta}        |        {reset}",
        f"{magenta}        |        {reset}",
        f"{magenta}      /   \\      {reset}",
        f"{magenta}     /     \\     {reset}",
    ]
    
    quote = (
        "I'm not saying I'm a failure, but I've never met a deadline I didn't postpone, "
        "and I'm pretty sure my birth certificate is just a 'try again' coupon. "
        "Existence is like a bad Broadway show: you pay too much, it's poorly written, "
        "and you're trapped in the front row with no intermission."
    )
    
    # Print the box with animation
    print(f"{yellow}{'=' * width}{reset}")
    
    # Title with blinking effect
    title = "WOODY ALLEN'S NEUROTIC WISDOM"
    for _ in range(3):
        print(f"{yellow}|\033[5m{green}{title.center(width-2)}\033[0m{yellow}|{reset}")
        time.sleep(0.2)
        print(f"{yellow}|{green}{title.center(width-2)}{yellow}|{reset}")
        time.sleep(0.2)
    
    print(f"{yellow}{'-' * width}{reset}")
    
    # Print quote with typewriter effect
    print_slow(f"{yellow}|{reset}", 0)
    wrapped = []
    words = quote.split()
    current = ""
    for word in words:
        if len(current) + len(word) + 1 <= width - 4:
            current += word + " "
        else:
            wrapped.append(current.strip())
            current = word + " "
    if current:
        wrapped.append(current.strip())
    
    for line in wrapped:
        print(f"{yellow}| {blue}{line.ljust(width-4)} {yellow}|{reset}")
        time.sleep(0.1)
    
    print(f"{yellow}|{' ' * (width-2)}|{reset}")
    
    # Print Woody ASCII art with bounce animation
    for i in range(3):
        for line in woody_art:
            print(f"{yellow}|{reset}{line.center(width-2)}{yellow}|{reset}")
        time.sleep(0.3)
        for _ in range(3):
            print(f"{yellow}|{' ' * (width-2)}|{reset}")
            time.sleep(0.1)
    
    print(f"{yellow}{'=' * width}{reset}")
    
    # Final existential punchline
    punchline = "This message will self-destruct in 5... 4... 3... (just kidding, I forgot the self-destruct button)"
    print(f"\n{red}{punchline.center(width)}{reset}\n")

if __name__ == "__main__":
    main()