"""
Campbell's Soup Can #1322
Produced: 2026-01-01 13:45:54
Worker: Qwen: Qwen2.5-VL 7B Instruct (free) (qwen/qwen-2.5-vl-7b-instruct:free)
Employment: Volunteer
Flavor: Woody Allen Philosophy
Quality: ✅

Made by Machine #0 - Production Line 0
Like Warhol's soup cans - same but different.
Each can is the same flavor, made by different hands.
"""

from termcolor import colored, cprint

class WoodyQuotes:
    def __init__(self):
        self.quotes = [
            "I'm not afraid of death; I just don't want to be there when it happens.",
            "Life is full of misery, loneliness, and suffering - and it's all over much too soon.",
            "I don't want to achieve immortality through my work; I want to achieve it through not dying."
        ]

    def display_quote(self):
        cprint("\n", 'blue', attrs=['bold'])
        cprint('= ' + '-' * 40 + ' =', 'cyan')
        cprint("# ", 'green', attrs=['bold'], end='')
        cprint(" Woody Allen's Philosophy ", 'red', attrs=['underline'])
        cprint("# ", 'green', attrs=['bold'], end='')
        cprint('='.ljust(38) + ' =', 'cyan')
        index = 0
        while True:
            cprint(colored(self.quotes[index], 'yellow') + colored('\n', 'yellow'), attrs=['bold', 'reverse'])
            index += 1
            if index >= len(self.quotes):
                index = 0
            # Sleep for a few seconds to animate the quote
            import time
            import os
            os.system('cls' if os.name == 'nt' else 'clear')
            time.sleep(3)

if __name__ == "__main__":
    quotes = WoodyQuotes()
    quotes.display_quote()