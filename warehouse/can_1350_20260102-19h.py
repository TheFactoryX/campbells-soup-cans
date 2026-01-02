"""
Campbell's Soup Can #1350
Produced: 2026-01-02 19:25:03
Worker: Qwen: Qwen2.5-VL 7B Instruct (free) (qwen/qwen-2.5-vl-7b-instruct:free)
Employment: Volunteer
Flavor: Woody Allen Philosophy
Quality: ✅

Made by Machine #0 - Production Line 0
Like Warhol's soup cans - same but different.
Each can is the same flavor, made by different hands.
"""

import time
import string

def print_quote():
    quote = "I'm not afraid of dying; I just don't want to be there when my life is over."
    print("\033[47;1;30m" + '-' * 30 + "\033[0m")
    print("\033[47;30;35m" + "      .-'                     .-'      " + "\033[0m")
    print("\033[47;30;35m" + "   .-'     '\"                '    '-.'    \033[0m")
    print("\033[47;30;35m" + "  .-'                    '\"              '-.' \033[0m")
    print("\033[47;1;82m" + string.center(quote, 30, " ") + "\033[0m")
    print("\033[47;30;35m" + "    '-.                      '            '-." + "\033[0m")
    print("\033[47;30;35m" + "      '                        '        '    " + "\033[0m")
    print("\033[47;1;30m" + '_' * 30 + "\033[0m")

print_quote()
time.sleep(2)  # delay for 2 seconds before exiting