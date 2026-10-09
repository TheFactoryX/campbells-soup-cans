"""
Campbell's Soup Can #5086
Produced: 2026-10-09 20:57:09
Worker: Dots Studio: Dots3-Note Preview (free) (dots-studio/dots-3-note-preview:free)
Employment: Volunteer
Flavor: Woody Allen Philosophy
Quality: ✅

Made by Machine #0 - Production Line 0
Like Warhol's soup cans - same but different.
Each can is the same flavor, made by different hands.
"""



import time
import sys

def main():
    YELLOW = '\033[93m'
    CYAN = '\033[96m'
    RESET = '\033[0m'
    
    quote = "I've spent my entire life searching for the meaning of existence, and all I've found is a suspiciously large number of unanswered questions and a lingering feeling that my hairline is retreating faster than my will to live."
    
    width = 70
    inner = width - 4
    
    words = quote.split()
    lines = []
    current = ''
    for word in words:
        if len(current) + len(word) + 1 <= inner:
            current += word + ' '
        else:
            lines.append(current.strip())
            current = word + ' '
    if current:
        lines.append(current.strip())
    
    border = '+' + '-' * (width - 2) + '+'
    print(YELLOW + border + RESET)
    print(YELLOW + '|' + ' ' * (width - 2) + '|' + RESET)
    
    for line in lines:
        padding = (width - 2 - len(line)) // 2
        sys.stdout.write(YELLOW + '|' + ' ' * padding + CYAN)
        for ch in line:
            sys.stdout.write(ch)
            sys.stdout.flush()
            time.sleep(0.03)
        sys.stdout.write(RESET + ' ' * (width - 2 - len(line) - padding) + YELLOW + '|' + RESET)
        print()
    
    print(YELLOW + '|' + ' ' * (width - 2) + '|' + RESET)
    print(YELLOW + border + RESET)

if __name__ == '__main__':
    main()