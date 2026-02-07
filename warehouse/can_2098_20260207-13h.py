"""
Campbell's Soup Can #2098
Produced: 2026-02-07 13:54:07
Worker: Arcee AI: Trinity Mini (free) (arcee-ai/trinity-mini:free)
Employment: Volunteer
Flavor: Woody Allen Philosophy
Quality: ❌ (broken)

Made by Machine #0 - Production Line 0
Like Warhol's soup cans - same but different.
Each can is the same flavor, made by different hands.
"""

#!/usr/bin/env python3
"""
Woody Allen's Existential Comedy Show
"""
import sys

def main():
    # Woody Allen's signature quote
    quote = """
    I'm not afraid of death; I just don't want to be there when it happens.
    Life is full of misery, loneliness, and suffering - and it's all over much too soon.
    I don't want to achieve immortality through my work; I want to achieve it through not dying.
    """
    
    # Create colorful ASCII art box with Woody's face
    box = f"""
    {'\033[1;35m' + ' ' * 30 + 'W O O D Y   A L L E N' + ' ' * 30 + '\033[0m'}
    {'\033[1;33m' + ' ' * 30 + 'THE EXISTENTIAL COMEDY SHOW' + ' ' * 30 + '\033[0m'}
    {'\033[1;36m' + ' ' * 30 + '╔' + '═' * 60 + '╗' + ' ' * 30 + '\033[0m'}
    {'\033[1;36m' + ' ' * 30 + '║' + ' ' * 58 + '║' + ' ' * 30 + '\033[0m'}
    {'\033[1;36m' + ' ' * 30 + '║' + '\033[1;31m' + '  😎  ' + '\033[1;36m' + '  ' + '\033[1;32m' + '  😐  ' + '\033[1;36m' + '  ' + '\033[1;34m' + '  😵  ' + '\033[1;36m' + '  ' + '\033[1;35m' + '  😴  ' + '\033[1;36m' + '  ' + '\033[1;33m' + '  😴  ' + '\033[1;36m' + '  ' + '\033[1;34m' + '  😵  ' + '\033[1;36m' + '  ' + '\033[1;32m' + '  😐  ' + '\033[1;36m' + '  ' + '\033[1;31m' + '  😎  ' + '\033[1;36m' + '  ' + '\033[1;35m' + '  ' + '\033[0m'}
    {'\033[1;36m' + ' ' * 30 + '║' + ' ' * 58 + '║' + ' ' * 30 + '\033[0m'}
    {'\033[1;36m' + ' ' * 30 + '╚' + '═' * 60 + '╝' + ' ' * 30 + '\033[0m'}
    """
    
    # Print the colorful box
    print(box)
    
    # Print the quote with alternating colors
    for line in quote.splitlines():
        if line.strip():
            print(f"\033[1;37m{line}\033[0m")

if __name__ == "__main__":
    main()