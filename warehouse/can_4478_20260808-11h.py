"""
Campbell's Soup Can #4478
Produced: 2026-08-08 11:43:06
Worker: Poolside: Laguna XS 2.1 (free) (poolside/laguna-xs-2.1:free)
Employment: Volunteer
Flavor: Woody Allen Philosophy
Quality: ✅

Made by Machine #0 - Production Line 0
Like Warhol's soup cans - same but different.
Each can is the same flavor, made by different hands.
"""

import time

quote = [
    "I'm not afraid of death—I just dread it more than",
    "my dentist. Which is saying something, because",
    "I haven't seen a dentist since 1992. That",
    "means I'm either a genius, a coward, or an idiot.",
    "Probably all three. Which makes for a very exciting",
    "existential journey."
]

max_line_length = max(len(line) for line in quote)
border_char = '═'
top = '╔' + (border_char * (max_line_length + 2)) + '╗'
bottom = '╚' + (border_char * (max_line_length + 2)) + '╝'

print('\033[95m' + top + '\033[0m')
for line in quote:
    padded_line = line.ljust(max_line_length)
    print('\033[95m║ \033[93m' + padded_line + '\033[95m ║\033[0m')
    time.sleep(0.4)
print('\033[95m' + bottom + '\033[0m')