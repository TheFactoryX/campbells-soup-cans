"""
Campbell's Soup Can #1812
Produced: 2026-01-24 07:32:00
Worker: NVIDIA: Nemotron 3 Nano 30B A3B (free) (nvidia/nemotron-3-nano-30b-a3b:free)
Employment: Volunteer
Flavor: Woody Allen Philosophy
Quality: ❌ (broken)

Made by Machine #0 - Production Line 0
Like Warhol's soup cans - same but different.
Each can is the same flavor, made by different hands.
"""

#!/usr/bin/env python3
# -*- coding: utf-8 -*-

cyan = '\033[96m'
yellow = '\033[93m'
reset = '\033[0m'

quote = "I'm not afraid of death; I just don't want to be there when it happens."
border_length = 70
border_str = '=' * border_length
centered_quote = quote.center(border_length)

print(cyan + border_str + reset)
print(yellow + centered_quote + reset)
print(cyan + border_str + reset)
print(reset, end='\n\n')
print("  " + " ".join(["O", "W", "O", "D", "Y", " ", "A", "L", "L", "E", "N", " ", "D", "A", "Y", " ", "!"]) + "  ")
print(reset, end='\n\n')
print("  " + " ".join(["T", "H", "E", " ", "J", "U", "D", "G", "E", " ", "I", "S", " ", "N", "O", "T", " ", "T", "H", "E", " ", "U", "N", "I", "C", "E", " ", "O", "N", "E"]).center(70)) + "  ")
print(reset, end='\n\n')
print("  " + " ".join(["L", "I", "F", "E", " ", "I", "S", " ", "A", " ", "J", "O", "K", "E", " ", "T", "H", "A", "T", " ", "S", " ", "N", "O", "T", " ", "F", "U", "N", "Y", " ", "B", "U", "T", " ", "I", " ", "L", "A", "U", "G", "H", " ", "A", "T", " ", "I", "T", " ", "A", "N", "Y", "W", "A", "Y", "."]).center(70)) + "  ")
print(reset)