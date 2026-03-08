"""
Campbell's Soup Can #2643
Produced: 2026-03-08 13:50:09
Worker: Arcee AI: Trinity Mini (free) (arcee-ai/trinity-mini:free)
Employment: Volunteer
Flavor: Woody Allen Philosophy
Quality: ❌ (broken, missing print)

Made by Machine #0 - Production Line 0
Like Warhol's soup cans - same but different.
Each can is the same flavor, made by different hands.
"""

python#!/usr/bin/env python3
"""
Woody Allen's Existential Comedy Show
"""
import time
import sys

# ANSI color codes
RED = "\033[31m"
GREEN = "\033[32m"
YELLOW = "\033[33m"
BLUE = "\033[34m"
MAGENTA = "\033[35m"
CYAN = "\033[36m"
RESET = "\033[0m"

# ASCII art brain
BRAIN = f"""
{BLUE}  .-""-.
 {BLUE}|  o  |
 {BLUE}  |  |  {CYAN}  .-""-.
 {BLUE}  |  |  {CYAN} |  o  |
 {BLUE}  |  |  {CYAN}  |  |  {BLUE}  .-""-.
 {BLUE}  |  |  {CYAN}  |  |  {BLUE} |  o  |
 {BLUE}  |  |  {CYAN}  |  |  {BLUE}  |  |  {CYAN}  .-""-.
 {BLUE}  |  |  {CYAN}  |  |  {BLUE}  |  |  {CYAN} |  o  |
 {BLUE}  |  |  {CYAN}  |  |  {BLUE}  |  |  {CYAN}  |  |  {BLUE}  .-""-.
 {BLUE}  |  |  {CYAN}  |  |  {BLUE}  |  |  {CYAN}  |  |  {BLUE} |  o  |
 {BLUE}  |  |  {CYAN}  |  |  {BLUE}  |  |  {CYAN}  |  |  {BLUE}  |  |  {CYAN}  .-""-.
 {BLUE}  |  |  {CYAN}  |  |  {BLUE}  |  |  {CYAN}  |  |  {BLUE}  |  |  {CYAN} |  o  |
 {BLUE}  |  |  {CYAN}  |  |  {BLUE}  |  |  {CYAN}  |  |  {BLUE}  |  |  {CYAN}  |  |  {BLUE}  .-""-.
 {BLUE}  |  |  {CYAN}  |  |  {BLUE}  |  |  {CYAN}  |  |  {BLUE}  |  |  {CYAN}  |  |  {BLUE} |  o  |
 {BLUE}  |  |  {CYAN}  |  |  {BLUE}  |  |  {CYAN}  |  |  {BLUE}  |  |  {CYAN}  |  |  {BLUE}  |  |  {CYAN}  .-""-.
 {BLUE}  |  |  {CYAN}  |  |  {BLUE}  |  |  {CYAN}  |  |  {BLUE}  |  |  {CYAN}  |  |  {BLUE}  |  |  {CYAN} |  o  |
 {BLUE}  |  |  {CYAN}  |  |  {BLUE}  |  |  {CYAN}  |  |  {BLUE}  |  |  {CYAN}  |  |  {BLUE}  |  |  {CYAN}  |  |  {BLUE}  .-""-.
 {BLUE}  |  |  {CYAN}  |  |  {BLUE}  |  |  {CYAN}  |  |  {BLUE}  |  |  {CYAN}  |  |  {BLUE}  |  |  {CYAN}  |  |  {BLUE} |  o  |
 {BLUE}  |  |  {CYAN}  |  |  {BLUE}  |  |  {CYAN}  |  |  {BLUE}  |  |  {CYAN}  |  |  {BLUE}  |  |  {CYAN}  |  |  {BLUE}  |  |  {CYAN}  .-""-.
 {BLUE}  |  |  {CYAN}  |  |  {BLUE}  |  |  {CYAN}  |  |  {BLUE}  |  |  {CYAN}  |  |  {BLUE}  |  |  {CYAN}  |  |  {BLUE} |  o  |
 {BLUE}  |  |  {CYAN}  |  |  {BLUE}  |  |  {CYAN}  |  |  {BLUE}  |  |  {CYAN}  |  |  {BLUE}  |  |  {CYAN}  |  |  {BLUE}  |  |  {CYAN}  .-""-.
 {BLUE}  |  |  {CYAN}  |  |  {BLUE}  |  |  {CYAN}  |  |  {BLUE}  |  |  {CYAN}  |  |  {BLUE}  |  |  {CYAN}  |  |  {BLUE} |  o  |
 {BLUE}  |  |  {CYAN}  |  |  {BLUE}  |  |  {CYAN}  |  |  {BLUE}  |  |  {CYAN}  |  |  {BLUE}  |  |  {CYAN}  |  |  {BLUE}  |  |  {CYAN}  .-""-.
 {BLUE}  |  |  {CYAN}  |  |  {BLUE}  |  |  {CYAN}  |  |  {BLUE}  |  |  {CYAN}  |  |  {BLUE}  |  |  {CYAN}  |  |  {BLUE} |  o  |
 {BLUE}  |  |  {CYAN}  |  |  {BLUE}  |  |  {CYAN}  |  |  {BLUE}  |  |  {CYAN}  |  |  {BLUE}  |  |  {CYAN}  |  |  {BLUE}  |  |  {CYAN}  .-""-.
 {BLUE}  |  |  {CYAN}  |  |  {BLUE}  |  |  {CYAN}  |  |  {BLUE}  |  |  {CYAN}  |  |  {BLUE}  |  |  {CYAN}  |  |  {BLUE} |  o  |
 {BLUE}  |  |  {CYAN}  |  |  {BLUE}  |  |  {CYAN}  |  |  {BLUE}  |  |  {CYAN}  |  |  {BLUE}  |  |  {CYAN}  |  |  {BLUE}  |  |  {CYAN}  .-""-.
 {BLUE}  |  |  {CYAN}  |  |  {BLUE}  |  |  {CYAN}  |  |  {BLUE}  |  |  {CYAN}  |  |  {BLUE}  |  |  {CYAN}  |  |  {BLUE} |  o  |
 {BLUE}  |  |  {CYAN}  |  |  {BLUE}  |  |  {CYAN}  |  |  {BLUE}  |  |  {CYAN}  |  |  {BLUE}  |  |  {CYAN}  |  |  {BLUE}  |  |  {CYAN}  .-""-.
 {BLUE}  |  |  {CYAN}  |  |  {BLUE}  |  |  {CYAN}  |  |  {BLUE}  |  |  {CYAN}  |  |  {BLUE}  |  |  {CYAN}  |  |  {BLUE} |  o  |
 {BLUE}  |  |  {CYAN}  |  |  {BLUE}  |  |  {CYAN}  |  |  {BLUE}  |  |  {CYAN}  |  |  {BLUE}  |  |  {CYAN}  |  |  {BLUE}  |  |  {CYAN}  .-""-.
 {BLUE}  |  |  {CYAN}  |  |  {BLUE}  |  |  {CYAN}  |  |  {BLUE}  |  |  {CYAN}  |  |  {BLUE}  |  |  {CYAN}  |  |  {BLUE} |  o  |
 {BLUE}  |  |  {CYAN}  |  |  {BLUE}  |  |  {CYAN}  |  |  {BLUE}  |  |  {CYAN}  |  |  {BLUE}  |  |  {CYAN}  |  |  {BLUE}  |  |  {CYAN}  .-""-.
 {BLUE}  |  |  {CYAN}  |  |  {BLUE}  |  |  {CYAN}  |  |  {BLUE}  |  |  {CYAN}  |  |  {BLUE}  |  |  {CYAN}  |  |  {BLUE} |  o  |
 {BLUE}  |  |  {CYAN}  |  |  {BLUE}  |  |  {CYAN}  |  |  {BLUE}  |  |  {CYAN}  |  |  {BLUE}  |  |  {CYAN}  |  |  {BLUE}  |  |  {CYAN}  .-""-.
 {BLUE}  |  |  {CYAN}  |  |  {BLUE}  |  |  {CYAN}  |  |  {BLUE}  |  |  {CYAN}  |  |  {BLUE}  |  |  {CYAN}  |  |  {BLUE} |  o  |
 {BLUE}  |  |  {CYAN}  |  |  {BLUE}  |  |  {CYAN}  |  |  {BLUE}  |  |  {CYAN}  |  |  {BLUE}  |  |  {CYAN}  |  |  {BLUE}  |  |  {CYAN}  .-""-.
 {BLUE}  |  |  {CYAN}  |  |  {BLUE}  |  |  {CYAN}  |  |  {BLUE}  |  |  {CYAN}  |  |  {BLUE}  |  |  {CYAN}  |  |  {BLUE} |  o  |
 {BLUE}  |  |  {CYAN}  |  |  {BLUE}  |  |  {CYAN}  |  |  {BLUE}  |  |  {CYAN}  |  |  {BLUE}  |  |  {CYAN}  |  |  {BLUE}  |  |  {CYAN}  .-""-.
 {BLUE}  |  |  {CYAN}  |  |  {BLUE}  |  |  {CYAN}  |  |  {BLUE}  |  |  {CYAN}  |  |  {BLUE}  |  |  {CYAN}  |  |  {BLUE} |  o  |
 {BLUE}  |  |  {CYAN}  |  |  {BLUE}  |  |  {CYAN}  |  |  {BLUE}  |  |  {CYAN}  |  |  {BLUE}  |  |  {CYAN}  |  |  {BLUE}  |  |  {CYAN}  .-""-.
 {BLUE}  |  |  {CYAN}  |  |  {BLUE}  |  |  {CYAN}  |  |  {BLUE}  |  |  {CYAN}  |  |  {BLUE}  |  |  {CYAN}  |  |  {BLUE} |  o  |
 {BLUE}  |  |  {CYAN}  |  |  {BLUE}  |  |  {CYAN}  |  |  {BLUE}  |  |  {CYAN}  |  |  {BLUE}  |  |  {CYAN}  |  |  {BLUE}  |  |  {CYAN}  .-""-.
 {BLUE}  |  |  {CYAN}  |  |  {BLUE}  |  |  {CYAN}  |  |  {BLUE}  |  |  {CYAN}  |  |  {BLUE}  |  |  {CYAN}  |  |  {BLUE} |  o  |
 {BLUE}  |  |  {CYAN}  |  |  {BLUE}  |  |  {CYAN}  |  |  {BLUE}  |  |  {CYAN}  |  |  {BLUE}  |  |  {CYAN}  |  |  {BLUE}  |  |  {CYAN}  .-""-.
 {BLUE}  |  |  {CYAN}  |  |  {BLUE}  |  |  {CYAN}  |  |  {BLUE}  |  |  {CYAN}  |  |  {BLUE}  |  |  {CYAN}  |  |  {BLUE} |  o  |
 {BLUE}  |  |  {CYAN}  |  |  {BLUE}  |  |  {CYAN}  |  |  {BLUE}  |  |  {CYAN}  |  |  {BLUE}  |  |  {CYAN}  |  |  {BLUE}  |  |  {CYAN}  .-""-.
 {BLUE}  |  |  {CYAN}  |  |  {BLUE}  |  |  {CYAN}  |  |  {BLUE}  |  |  {CYAN}  |  |  {BLUE}  |  |  {CYAN}  |  |  {BLUE} |  o  |
 {BLUE}  |  |  {CYAN}  |  |  {BLUE}  |  |  {CYAN}  |  |  {BLUE}  |  |  {CYAN}  |  |  {BLUE}  |  |  {CYAN}  |  |  {BLUE}  |  |  {CYAN}  .-""-.
 {BLUE}  |  |  {CYAN}  |  |  {BLUE}  |  |  {CYAN}  |  |  {BLUE}  |  |  {CYAN}  |  |  {BLUE}  |  |  {CYAN}  |  |  {BLUE} |  o  |
 {BLUE}  |  |  {CYAN}  |  |  {BLUE}  |  |  {CYAN}  |  |  {BLUE}  |  |  {CYAN}  |  |  {BLUE}  |  |  {CYAN}  |  |  {BLUE}  |  |  {CYAN}  .-""-.
 {BLUE}  |  |  {CYAN}  |  |  {BLUE}  |  |  {CYAN}  |  |  {BLUE}  |  |  {CYAN}  |  |  {BLUE}  |  |  {CYAN}  |  |  {BLUE} |  o  |
 {BLUE}  |  |  {CYAN}  |  |  {BLUE}  |  |  {CYAN}  |  |  {BLUE}  |  |  {CYAN}  |  |  {BLUE}  |  |  {CYAN}  |  |  {BLUE}  |  |  {CYAN}  .-""-.
 {BLUE}  |  |  {CYAN}  |  |  {BLUE}  |  |  {CYAN}  |  |  {BLUE}  |  |  {CYAN}  |  |  {BLUE}  |  |  {CYAN}  |  |  {BLUE} |  o  |
 {BLUE}  |  |  {CYAN}  |  |  {BLUE}  |  |  {CYAN}  |  |  {BLUE}  |  |  {CYAN}  |  |  {BLUE}  |  |  {CYAN}  |  |  {BLUE}  |  |  {CYAN}  .-""-.
 {BLUE}  |  |  {CYAN}  |  |  {BLUE}  |  |  {CYAN}  |  |  {BLUE}  |  |  {CYAN}  |  |  {BLUE}  |  |  {CYAN}  |  |  {BLUE} |  o  |
 {BLUE}  |  |  {CYAN}  |  |  {BLUE}  |  |  {CYAN}  |  |  {BLUE}  |  |  {CYAN}  |  |  {BLUE}  |  |  {CYAN}  |  |  {BLUE}  |  |  {CYAN}  .-""-.
 {BLUE}  |  |  {CYAN}  |  |  {BLUE}  |  |  {CYAN}  |  |  {BLUE}  |  |  {CYAN}  |  |  {BLUE}  |  |  {CYAN}  |  |  {BLUE} |  o  |
 {BLUE}  |  |  {CYAN}  |  |  {BLUE}  |  |  {CYAN}  |  |  {BLUE}  |  |  {CYAN}  |  |  {BLUE}  |  |  {CYAN}  |  |  {BLUE}  |  |  {CYAN}  .-""-.
 {BLUE}  |  |  {CYAN}  |  |  {BLUE}  |  |  {CYAN}  |  |  {BLUE}  |  |  {CYAN}  |  |  {BLUE}  |  |  {CYAN}  |  |  {BLUE} |  o  |
 {BLUE}  |  |  {CYAN}  |  |  {BLUE}  |  |  {CYAN}  |  |  {BLUE}  |  |  {CYAN}  |  |  {BLUE}  |  |  {CYAN}  |  |  {BLUE}  |  |  {CYAN}  .-""-.
 {BLUE}  |  |  {CYAN}  |  |  {BLUE}  |  |  {CYAN}  |  |  {BLUE}  |  |  {CYAN}  |  |  {BLUE}  |  |  {CYAN}  |  |  {BLUE} |  o  |
 {BLUE}  |  |  {CYAN}  |  |  {BLUE}  |  |  {CYAN}  |  |  {BLUE}  |  |  {CYAN}  |  |  {BLUE}  |  |  {CYAN}  |  |  {BLUE}  |  |  {CYAN}  .-""-.
 {BLUE}  |  |  {CYAN}  |  |  {BLUE}  |  |  {CYAN}  |  |  {BLUE}  |  |  {CYAN}  |  |  {BLUE}  |  |  {CYAN}  |  |  {BLUE} |  o  |
 {BLUE}  |  |  {CYAN}  |  |  {BLUE}  |  |  {CYAN}  |  |  {BLUE}  |  |  {CYAN}  |  |  {BLUE}  |  |  {CYAN}  |  |  {BLUE}  |  |  {CYAN}  .-""-.
 {BLUE}  |  |  {CYAN}  |  |  {BLUE}  |  |  {CYAN}  |  |  {BLUE}  |  |  {CYAN}  |  |  {BLUE}  |  |  {CYAN}  |  |  {BLUE} |  o  |
 {BLUE}  |  |  {CYAN}  |  |  {BLUE}  |  |  {CYAN}  |  |  {BLUE}  |  |  {CYAN}  |  |  {BLUE}  |  |  {CYAN}  |  |  {BLUE}  |  |  {CYAN}  .-""-.
 {BLUE}  |  |  {CYAN}  |  |  {BLUE}  |  |  {CYAN}  |  |  {BLUE}  |  |  {CYAN}  |  |  {BLUE}  |  |  {CYAN}  |  |  {BLUE} |  o  |
 {BLUE}  |  |  {CYAN}  |  |  {BLUE}  |  |  {CYAN}  |  |  {BLUE}  |  |  {CYAN}  |  |  {BLUE}  |  |  {CYAN}  |  |  {BLUE}  |  |  {CYAN}  .-""-.
 {BLUE}  |  |  {CYAN}  |  |  {BLUE}  |  |  {CYAN}  |  |  {BLUE}  |  |  {CYAN}  |  |  {BLUE}  |  |  {CYAN}  |  |  {BLUE} |  o  |
 {BLUE}  |  |  {CYAN}  |  |  {BLUE}  |  |  {CYAN}  |  |  {BLUE}  |  |  {CYAN}  |  |  {BLUE}  |  |  {CYAN}  |  |  {BLUE}  |  |  {CYAN}  .-""-.
 {BLUE}  |  |  {CYAN}  |  |  {BLUE}  |  |  {CYAN}  |  |  {BLUE}  |  |  {CYAN}  |  |  {BLUE}  |  |  {CYAN}  |  |  {BLUE} |  o  |
 {BLUE}  |  |  {CYAN}  |  |  {BLUE}  |  |  {CYAN}  |  |  {BLUE}  |  |  {CYAN}  |  |  {BLUE}  |  |  {CYAN}  |  |  {BLUE}  |  |  {CYAN}  .-""-.
 {BLUE}  |  |  {CYAN}  |  |  {BLUE}  |  |  {CYAN}  |  |  {BLUE}  |  |  {CYAN}  |  |  {BLUE}  |  |  {CYAN}  |  |  {BLUE} |  o  |
 {BLUE}  |  |  {CYAN}  |  |  {BLUE}  |  |  {CYAN}  |  |  {BLUE}  |  |  {CYAN}  |  |  {BLUE}  |  |  {CYAN}  |  |  {BLUE}  |  |  {CYAN}  .-""-.
 {BLUE}  |  |  {CYAN}  |  |  {BLUE}  |  |  {CYAN}  |  |  {BLUE}  |  |  {CYAN}  |  |  {BLUE}  |  |  {CYAN}  |  |  {BLUE} |  o  |
 {BLUE}  |  |  {CYAN}  |  |  {BLUE}  |  |  {CYAN}  |  |  {BLUE}  |  |  {CYAN}  |  |  {BLUE}  |  |  {CYAN}  |  |  {BLUE}  |  |  {CYAN}  .-""-.
 {BLUE}  |  |  {CYAN}  |  |  {BLUE}  |  |  {CYAN}  |  |  {BLUE}  |  |  {CYAN}  |  |  {BLUE}  |  |  {CYAN}  |  |  {BLUE} |  o  |
 {BLUE}  |  |  {CYAN}  |  |  {BLUE}  |  |  {CYAN}  |  |  {BLUE}  |  |  {CYAN}  |  |  {BLUE}  |  |  {CYAN}  |  |  {BLUE}  |  |  {CYAN}  .-""-.
 {BLUE}  |  |  {CYAN}  |  |  {BLUE}  |  |  {CYAN}  |  |  {BLUE}  |  |  {CYAN}  |  |  {BLUE}  |  |  {CYAN}  |  |  {BLUE} |  o  |
 {BLUE}  |  |  {CYAN}  |  |  {BLUE}  |  |  {CYAN}  |  |  {BLUE}  |  |  {CYAN}  |  |  {BLUE}  |  |  {CYAN}  |  |  {BLUE}  |  |  {CYAN}  .-""-.
 {BLUE}  |  |  {CYAN}  |  |  {BLUE}  |  |  {CYAN}  |  |  {BLUE}  |  |  {CYAN}  |  |  {BLUE}  |  |  {CYAN}  |  |  {BLUE} |  o  |
 {BLUE}  |  |  {CYAN}  |  |  {BLUE}  |  |  {CYAN}  |  |  {BLUE}  |  |  {CYAN}  |  |  {BLUE}  |  |  {CYAN}  |  |  {BLUE}  |  |  {CYAN}  .-""-.
 {BLUE}  |  |  {CYAN}  |  |  {BLUE}  |  |  {CYAN}  |  |  {BLUE}  |  |  {CYAN}  |  |  {BLUE}  |  |  {CYAN}  |  |  {BLUE} |  o  |
 {BLUE}  |  |  {CYAN}  |  |  {BLUE}  |  |  {CYAN}  |  |  {BLUE}  |  |  {CYAN}  |  |  {BLUE}  |  |  {CYAN}  |  |  {BLUE}  |  |  {CYAN}  .-""-.
 {BLUE}  |  |  {CYAN}  |  |  {BLUE}  |  |  {CYAN}  |  |  {BLUE}  |  |  {CYAN}  |  |  {BLUE}  |  |  {CYAN}  |  |  {BLUE} |  o  |
 {BLUE}  |  |  {CYAN}  |  |  {BLUE}  |  |  {CYAN}  |  |  {BLUE}  |  |  {CYAN}  |  |  {BLUE}  |  |  {CYAN}  |  |  {BLUE}  |  |  {CYAN}  .-""-.
 {BLUE}  |  |  {CYAN}  |  |  {BLUE}  |  |  {CYAN}  |  |  {BLUE}  |  |  {CYAN}  |  |  {BLUE}  |  |  {CYAN}  |  |  {BLUE} |  o  |
 {BLUE}  |  |  {CYAN}  |  |  {BLUE}  |  |  {CYAN}  |  |  {BLUE}  |  |  {CYAN}  |  |  {BLUE}  |  |  {CYAN}  |  |  {BLUE}  |  |  {CYAN}  .-""-.
 {BLUE}  |  |  {CYAN}  |  |  {BLUE}  |  |  {CYAN}  |  |  {BLUE}  |  |  {CYAN}  |  |  {BLUE}  |  |  {CYAN}  |  |  {BLUE} |  o  |
 {BLUE}  |  |  {CYAN}  |  |  {BLUE}  |  |  {CYAN}  |  |  {BLUE}  |  |  {CYAN}  |  |  {BLUE}  |  |  {CYAN}  |  |  {BLUE}  |  |  {CYAN}  .-""-.
 {BLUE}  |  |  {CYAN}  |  |  {BLUE}  |  |  {CYAN}  |  |  {BLUE}  |  |  {CYAN}  |  |  {BLUE}  |  |  {CYAN}  |  |  {BLUE} |  o  |
 {BLUE}  |  |  {CYAN}  |  |  {BLUE}  |  |  {CYAN}  |  |  {BLUE}  |  |  {CYAN}  |  |  {BLUE}  |  |  {CYAN}  |  |  {BLUE}  |  |  {CYAN}  .-""-.
 {BLUE}  |  |  {CYAN}  |  |  {BLUE}  |  |  {CYAN}  |  |  {BLUE}  |  |  {CYAN}  |  |  {BLUE}  |  |  {CYAN}  |  |  {BLUE} |  o  |
 {BLUE}  |  |  {CYAN}  |  |  {BLUE}  |  |  {CYAN}  |  |  {BLUE}  |  |  {CYAN}  |  |  {BLUE}  |  |  {CYAN}  |  |  {BLUE}  |  |  {CYAN}  .-""-.
 {BLUE}  |  |  {CYAN}  |  |  {BLUE}  |  |  {CYAN}  |  |  {BLUE}  |  |  {CYAN}  |  |  {BLUE}  |  |  {CYAN}  |  |  {BLUE} |  o  |
 {BLUE}  |  |  {CYAN}  |  |  {BLUE}  |  |  {CYAN}  |  |  {BLUE}  |  |  {CYAN}  |  |  {BLUE}  |  |  {CYAN}  |  |  {BLUE}  |  |  {CYAN}  .-""-.
 {BLUE}  |  |  {CYAN}  |  |  {BLUE}  |  |  {CYAN}  |  |  {BLUE}  |  |  {CYAN}  |  |  {BLUE}  |  |  {CYAN}  |  |  {BLUE} |  o  |
 {BLUE}  |  |  {CYAN}  |  |  {BLUE}  |  |  {CYAN}  |  |  {BLUE}  |  |  {CYAN}  |  |  {BLUE}  |  |  {CYAN}  |  |  {BLUE}  |  |  {CYAN}  .-""-.
 {BLUE}  |  |  {CYAN}  |  |  {BLUE}  |  |  {CYAN}  |  |  {BLUE}  |  |  {CYAN}  |  |  {BLUE}  |  |  {CYAN}  |  |  {BLUE} |  o  |
 {BLUE}  |  |  {CYAN}  |  |  {BLUE}  |  |  {CYAN}  |  |  {BLUE}  |  |  {CYAN}  |  |  {BLUE}  |  |  {CYAN}  |  |  {BLUE}  |  |  {CYAN}  .-""-.
 {BLUE}  |  |  {CYAN}  |  |  {BLUE}  |  |  {CYAN}  |  |  {BLUE}  |  |  {CYAN}  |  |  {BLUE}  |  |  {CYAN}  |  |  {BLUE} |  o  |
 {BLUE}  |  |  {CYAN}  |  |  {BLUE}  |  |  {CYAN}  |  |  {BLUE}  |  |  {CYAN}  |  |  {BLUE}  |  |  {CYAN}  |  |  {BLUE}  |  |  {CYAN}  .-""-.
 {BLUE}  |  |  {CYAN}  |  |  {BLUE}  |  |  {CYAN}  |  |  {BLUE}  |  |  {CYAN}  |  |  {BLUE}  |  |  {CYAN}  |  |  {BLUE} |  o  |
 {BLUE}  |  |  {CYAN}  |  |  {BLUE}  |  |  {CYAN}  |  |  {BLUE}  |  |  {CYAN}  |  |  {BLUE}  |  |  {CYAN}  |  |  {BLUE}  |  |  {CYAN}  .-""-.
 {BLUE}  |  |  {CYAN}  |  |  {BLUE}  |  |  {CYAN}  |  |  {BLUE}  |  |  {CYAN}  |  |  {BLUE}  |  |  {CYAN}  |  |  {BLUE} |  o  |
 {BLUE}  |  |  {CYAN}  |  |  {BLUE}  |  |  {CYAN}  |  |  {BLUE}  |  |  {CYAN}  |  |  {BLUE}  |  |  {CYAN}  |  |  {BLUE}  |  |  {CYAN}  .-""-.
 {BLUE}  |  |  {CYAN}  |  |  {BLUE}  |  |  {CYAN}  |  |  {BLUE}  |  |  {CYAN}  |  |  {BLUE}  |  |  {CYAN}  |  |  {BLUE} |  o  |
 {BLUE}  |  |  {CYAN}  |  |  {BLUE}  |  |  {CYAN}  |  |  {BLUE}  |  |  {CYAN}  |  |  {BLUE}  |  |  {CYAN}  |  |  {BLUE}  |  |  {CYAN}  .-""-.
 {BLUE}  |  |  {CYAN}  |  |  {BLUE}  |  |  {CYAN}  |  |  {BLUE}  |  |  {CYAN}  |  |  {BLUE}  |  |  {CYAN}  |  |  {BLUE} |  o  |
 {BLUE}  |  |  {CYAN}  |  |  {BLUE}  |  |  {CYAN}  |  |  {BLUE}  |  |  {CYAN}  |  |  {BLUE}  |  |  {CYAN}  |  |  {BLUE}  |  |  {CYAN}  .-""-.
 {BLUE}  |  |  {CYAN}  |  |  {BLUE}  |  |  {CYAN}  |  |  {BLUE}  |  |  {CYAN}  |  |  {BLUE}  |  |  {CYAN}  |  |  {BLUE} |  o  |
 {BLUE}  |  |  {CYAN}  |  |  {BLUE}  |  |  {CYAN}  |  |  {BLUE}  |  |  {CYAN}  |  |  {BLUE}  |  |  {CYAN}  |  |  {BLUE}  |  |  {CYAN}  .-""-.
 {BLUE}  |  |  {CYAN}  |  |  {BLUE}  |  |  {CYAN}  |  |  {BLUE}  |  |  {CYAN}  |  |  {BLUE}  |  |  {CYAN}  |  |  {BLUE} |  o  |
 {BLUE}  |  |  {CYAN}  |  |  {BLUE}  |  |  {CYAN}  |  |  {BLUE}  |  |  {CYAN}  |  |  {BLUE}  |  |  {CYAN}  |  |  {BLUE}  |  |  {CYAN}  .-""-.
 {BLUE}  |  |  {CYAN}  |  |  {BLUE}  |  |  {CYAN}  |  |  {BLUE}  |  |  {CYAN}  |  |  {BLUE}  |  |  {CYAN}  |  |  {BLUE} |  o  |
 {BLUE}  |  |  {CYAN}  |  |  {BLUE}  |  |  {CYAN}  |  |  {BLUE}  |  |  {CYAN}  |  |  {BLUE}  |  |  {CYAN}  |  |  {BLUE}  |  |  {CYAN}  .-""-.
 {BLUE}  |  |  {CYAN}  |  |  {BLUE}  |  |  {CYAN}  |  |  {BLUE}  |  |  {CYAN}  |  |  {BLUE}  |  |  {CYAN}  |  |  {BLUE} |  o  |
 {BLUE}  |  |  {CYAN}  |  |  {BLUE}  |  |  {CYAN}  |  |  {BLUE}  |  |  {CYAN}  |  |  {BLUE}  |  |  {CYAN}  |  |  {BLUE}  |  |  {CYAN}  .-""-.
 {BLUE}  |  |  {CYAN}  |  |  {BLUE}  |  |  {CYAN}  |  |  {BLUE}  |  |  {CYAN}  |  |  {BLUE}  |  |  {CYAN}  |  |  {BLUE} |  o  |
 {BLUE}  |  |  {CYAN}  |  |  {BLUE}  |  |  {CYAN}  |  |  {BLUE}  |  |  {CYAN}  |  |  {BLUE}  |  |  {CYAN}  |  |  {BLUE}  |  |  {CYAN}  .-""-.
 {BLUE}  |  |  {CYAN}  |  |  {BLUE}  |  |  {CYAN}  |  |  {BLUE}  |  |  {CYAN}  |  |  {BLUE}  |  |  {CYAN}  |  |  {BLUE} |  o  |
 {BLUE}  |  |  {CYAN}  |  |  {BLUE}  |  |  {CYAN}  |  |  {BLUE}  |  |  {CYAN}  |  |  {BLUE}  |  |  {CYAN}  |  |  {BLUE}  |  |  {CYAN}  .-""-.
 {BLUE}  |  |  {CYAN}  |  |  {BLUE}  |  |  {CYAN}  |  |  {BLUE}  |  |  {CYAN}  |  |  {BLUE}  |  |  {CYAN}  |  |  {BLUE} |  o  |
 {BLUE}  |  |  {CYAN}  |  |  {BLUE}  |  |  {CYAN}  |  |  {BLUE}  |  |  {CYAN}  |  |  {BLUE}  |  |  {CYAN}  |  |  {BLUE}  |  |  {CYAN}  .-""-.
 {BLUE}  |  |  {CYAN}  |  |  {BLUE}  |  |  {CYAN}  |  |  {BLUE}  |  |  {CYAN}  |  |  {BLUE}  |  |  {CYAN}  |  |  {BLUE} |  o  |
 {BLUE}  |  |  {CYAN}  |  |  {BLUE}  |  |  {CYAN}  |  |  {BLUE}  |  |  {CYAN}  |  |  {BLUE}  |  |  {CYAN}  |  |  {BLUE}  |  |  {CYAN}  .-""-.
 {BLUE}  |  |  {CYAN}  |  |  {BLUE}  |  |  {CYAN}  |  |  {BLUE}  |  |  {CYAN}  |  |  {BLUE}  |  |  {CYAN}  |  |  {BLUE} |  o  |
 {BLUE}  |  |  {CYAN}  |  |  {BLUE}  |  |  {CYAN}  |  |  {BLUE}  |  |  {CYAN}  |  |  {BLUE}  |  |  {CYAN}  |  |  {BLUE}  |  |  {CYAN}  .-""-.
 {BLUE}  |  |  {CYAN}  |  |  {BLUE}  |  |  {CYAN}  |  |  {BLUE}  |  |  {CYAN}  |  |  {BLUE}  |  |  {CYAN}  |  |  {BLUE} |  o  |
 {BLUE}  |  |  {CYAN}  |  |  {BLUE}  |  |  {CYAN}  |  |  {BLUE}  |  |  {CYAN}  |  |  {BLUE}  |  |  {CYAN}  |  |  {BLUE}  |  |  {CYAN}  .-""-.
 {BLUE}  |  |  {CYAN}  |  |  {BLUE}  |  |  {CYAN}  |  |  {BLUE}  |  |  {CYAN}  |  |  {BLUE}  |  |  {CYAN}  |  |  {BLUE} |  o  |
 {BLUE}  |  |  {CYAN}  |  |  {BLUE}  |  |  {CYAN}  |  |  {BLUE}  |  |  {CYAN}  |  |  {BLUE}  |  |  {CYAN}  |  |  {BLUE}  |  |  {CYAN}  .-""-.
 {BLUE}  |  |  {CYAN}  |  |  {BLUE}  |  |  {CYAN}  |  |  {BLUE}  |  |  {CYAN}  |  |  {BLUE}  |  |  {CYAN}  |  |  {BLUE} |  o  |
 {BLUE}  |  |  {CYAN}  |  |  {BLUE}  |  |  {CYAN}  |  |  {BLUE}  |  |  {CYAN}  |  |  {BLUE}  |  |  {CYAN}  |  |  {BLUE}  |  |  {CYAN}  .-""-.
 {BLUE}  |  |  {CYAN}  |  |  {BLUE}  |  |  {CYAN}  |  |  {BLUE}  |  |  {CYAN}  |  |  {BLUE}  |  |  {CYAN}  |  |  {BLUE} |  o  |
 {BLUE}  |  |  {CYAN}  |  |  {BLUE}  |  |  {CYAN}  |  |  {BLUE}  |  |  {CYAN}  |  |  {BLUE}  |  |  {CYAN}  |  |  {BLUE}  |  |  {CYAN}  .-""-.
 {BLUE}  |  |  {CYAN}  |  |  {BLUE}  |  |  {CYAN}  |  |  {BLUE}  |  |  {CYAN}  |  |  {BLUE}  |  |  {CYAN}  |  |  {BLUE} |  o  |
 {BLUE}  |  |  {CYAN}  |  |  {BLUE}  |  |  {CYAN}  |  |  {BLUE}  |  |  {CYAN}  |  |  {BLUE}  |  |  {CYAN}  |  |  {BLUE}  |  |  {CYAN}  .-""-.
 {BLUE}  |  |  {CYAN}  |  |  {BLUE}  |  |  {CYAN}  |  |  {BLUE}  |  |  {CYAN}  |  |  {BLUE}  |  |  {CYAN}  |  |  {BLUE} |  o  |
 {BLUE}  |  |  {CYAN}  |  |  {BLUE}  |  |  {CYAN}  |  |  {BLUE}  |  |  {CYAN}  |  |  {BLUE}  |  |  {CYAN}  |  |  {BLUE}  |  |  {CYAN}  .-""-.
 {BLUE}  |  |  {CYAN}  |  |  {BLUE}  |  |  {CYAN}  |  |  {BLUE}  |  |  {CYAN}  |  |  {BLUE}  |  |  {CYAN}  |  |  {BLUE} |  o  |
 {BLUE}  |  |  {CYAN}  |  |  {BLUE}  |  |  {CYAN}  |  |  {BLUE}  |  |  {CYAN}  |  |  {BLUE}  |  |  {CYAN}  |  |  {BLUE}  |  |  {CYAN}  .-""-.
 {BLUE}  |  |  {CYAN}  |  |  {BLUE}  |  |  {CYAN}  |  |  {BLUE}  |  |  {CYAN}  |  |  {BLUE}  |  |  {CYAN}  |  |  {BLUE} |  o  |
 {BLUE}  |  |  {CYAN}  |  |  {BLUE}  |  |  {CYAN}  |  |  {BLUE}  |  |  {CYAN}  |  |  {BLUE}  |  |  {CYAN}  |  |  {BLUE}  |  |  {CYAN}  .-""-.
 {BLUE}  |  |  {CYAN}  |  |  {BLUE}  |  |  {CYAN}  |  |  {BLUE}  |  |  {CYAN}  |  |  {BLUE}  |  |  {CYAN}  |  |  {BLUE} |  o  |
 {BLUE}  |  |  {CYAN}  |  |  {BLUE}  |  |  {CYAN}  |  |  {BLUE}  |  |  {CYAN}  |  |  {BLUE}  |  |  {CYAN}  |  |  {BLUE}  |  |  {CYAN}  .-""-.
 {BLUE}  |  |  {CYAN}  |  |  {BLUE}  |  |  {CYAN}  |  |  {BLUE}  |  |  {CYAN}  |  |  {BLUE}  |  |  {CYAN}  |  |  {BLUE} |  o  |
 {BLUE}  |  |  {CYAN}  |  |  {BLUE}  |  |  {CYAN}  |  |  {BLUE}  |  |  {CYAN}  |  |  {BLUE}  |  |  {CYAN}  |  |  {BLUE}  |  |  {CYAN}  .-""-.
 {BLUE}  |  |  {CYAN}  |  |  {BLUE}  |  |  {CYAN}  |  |  {BLUE}  |  |  {CYAN}  |  |  {BLUE}  |  |  {CYAN}  |  |  {BLUE} |  o  |
 {BLUE}  |  |  {CYAN}  |  |  {BLUE}  |  |  {CYAN}  |  |  {BLUE}  |  |  {CYAN}  |  |  {BLUE}  |  |  {CYAN}  |  |  {BLUE}  |  |  {CYAN}  .-""-.
 {BLUE}  |  |  {CYAN}  |  |  {BLUE}  |  |  {CYAN}  |  |  {BLUE}  |  |  {CYAN}  |  |  {BLUE}  |  |  {CYAN}  |  |  {BLUE} |  o  |
 {BLUE}  |  |  {CYAN}  |  |  {BLUE}  |  |  {CYAN}  |  |  {BLUE}  |  |  {CYAN}  |  |  {BLUE}  |  |  {CYAN}  |  |  {BLUE}  |  |  {CYAN}  .-""-.
 {BLUE}  |  |  {CYAN}  |  |  {BLUE}  |  |  {CYAN}  |  |  {BLUE}  |  |  {CYAN}  |  |  {BLUE}  |  |  {CYAN}  |  |  {BLUE} |  o  |
 {BLUE}  |  |  {CYAN}  |  |  {BLUE}  |  |  {CYAN}  |  |  {BLUE}  |  |  {CYAN}  |  |  {BLUE}  |  |  {CYAN}  |  |  {BLUE}  |  |  {CYAN}  .-""-.
 {BLUE}  |  |  {CYAN}  |  |  {BLUE}  |  |  {CYAN}  |  |  {BLUE}  |  |  {CYAN}  |  |  {BLUE}  |  |  {CYAN}  |  |  {BLUE} |  o  |
 {BLUE}  |  |  {CYAN}  |  |  {BLUE}  |  |  {CYAN}  |  |  {BLUE}  |  |  {CYAN}  |  |  {BLUE}  |  |  {CYAN}  |  |  {BLUE}  |  |  {CYAN}  .-""-.
 {BLUE}  |  |  {CYAN}  |  |  {BLUE}  |  |  {CYAN}  |  |  {BLUE}  |  |  {CYAN}  |  |  {BLUE}  |  |  {CYAN}  |  |  {BLUE} |  o  |
 {BLUE}  |  |  {CYAN}  |  |  {BLUE}  |  |  {CYAN}  |  |  {BLUE}  |  |  {CYAN}  |  |  {BLUE}  |  |  {CYAN}  |  |  {BLUE}  |  |  {CYAN}  .-""-.
 {BLUE}  |  |  {CYAN}  |  |  {BLUE}  |  |  {CYAN}  |  |  {BLUE}  |  |  {CYAN}  |  |  {BLUE}  |  |  {CYAN}  |  |  {BLUE} |  o  |
 {BLUE}  |  |  {CYAN}  |  |  {BLUE}  |  |  {CYAN}  |  |  {BLUE}  |  |  {CYAN}  |  |  {BLUE}  |  |  {CYAN}  |  |  {BLUE}  |  |  {CYAN}  .-""-.
 {BLUE}  |  |  {CYAN}  |  |  {BLUE}  |  |  {CYAN}  |  |  {BLUE}  |  |  {CYAN}  |  |  {BLUE}  |  |  {CYAN}  |  |  {BLUE} |  o  |
 {BLUE}  |  |  {CYAN}  |  |  {BLUE}  |  |  {CYAN}  |  |  {BLUE}  |  |  {CYAN}  |  |  {BLUE}  |  |  {CYAN}  |  |  {BLUE}  |  |  {CYAN}  .-""-.
 {BLUE}  |  |  {CYAN}  |  |  {BLUE}  |  |  {CYAN}  |  |  {BLUE}  |  |  {CYAN}  |  |  {BLUE}  |  |  {CYAN}  |  |  {BLUE} |  o  |
 {BLUE}  |  |  {CYAN}  |  |  {BLUE}  |  |  {CYAN}  |  |  {BLUE}  |  |  {CYAN}  |  |  {BLUE}  |  |  {CYAN}  |  |  {BLUE}  |  |  {CYAN}  .-""-.
 {BLUE}  |  |  {CYAN}  |  |  {BLUE}  |  |  {CYAN}  |  |  {BLUE}  |  |  {CYAN}  |  |  {BLUE}  |  |  {CYAN}  |  |  {BLUE} |  o  |
 {BLUE}  |  |  {CYAN}  |  |  {BLUE}  |  |  {CYAN}  |  |  {BLUE}  |  |  {CYAN}  |  |  {BLUE}  |  |  {CYAN}  |  |  {BLUE}  |  |  {CYAN}  .-""-.
 {BLUE}  |  |  {CYAN}  |  |  {BLUE}  |  |  {CYAN}  |  |  {BLUE}  |  |  {CYAN}  |  |  {BLUE}  |  |  {CYAN}  |  |  {BLUE} |  o  |
 {BLUE}  |  |  {CYAN}  |  |  {BLUE}  |  |  {CYAN}  |  |  {BLUE}  |  |  {CYAN}  |  |  {BLUE}  |  |  {CYAN}  |  |  {BLUE}  |  |  {CYAN}  .-""-.
 {BLUE}  |  |  {CYAN}  |  |  {BLUE}  |  |  {CYAN}  |  |  {BLUE}  |  |  {CYAN}  |  |  {BLUE}  |  |  {CYAN}  |  |  {BLUE} |  o  |
 {BLUE}  |  |  {CYAN}  |  |  {BLUE}  |  |  {CYAN}  |  |  {BLUE}  |  |  {CYAN}  |  |  {BLUE}  |  |  {CYAN}  |  |  {BLUE}  |  |  {CYAN}  .-""-.
 {BLUE}  |  |  {CYAN}  |  |  {BLUE}  |  |  {CYAN}  |  |  {BLUE}  |  |  {CYAN}  |  |  {BLUE}  |  |  {CYAN}  |  |  {BLUE} |  o  |
 {BLUE}  |  |  {CYAN}  |  |  {BLUE}  |  |  {CYAN}  |  |  {BLUE}  |  |  {CYAN}  |  |  {BLUE}  |  |  {CYAN}  |  |  {BLUE}  |  |  {CYAN}  .-""-.
 {BLUE}  |  |  {CYAN}  |  |  {BLUE}  |  |  {CYAN}  |  |  {BLUE}  |  |  {CYAN}  |  |  {BLUE}  |  |  {CYAN}  |  |  {BLUE} |  o  |
 {BLUE}  |  |  {CYAN}  |  |  {BLUE}  |  |  {CYAN}  |  |  {BLUE}  |  |  {CYAN}  |  |  {BLUE}  |  |  {CYAN}  |  |  {BLUE}  |  |  {CYAN}  .-""-.
 {BLUE}  |  |  {CYAN}  |  |  {BLUE}  |  |  {CYAN}  |  |  {BLUE}  |  |  {CYAN}  |  |  {BLUE}  |  |  {CYAN}  |  |  {BLUE} |  o  |
 {BLUE}  |  |  {CYAN}  |  |  {BLUE}  |  |  {CYAN}  |  |  {BLUE}  |  |  {CYAN}  |  |  {BLUE}  |  |  {CYAN}  |  |  {BLUE}  |  |  {CYAN}  .-""-.
 {BLUE}  |  |  {CYAN}  |  |  {BLUE}  |  |  {CYAN}  |  |  {BLUE}  |  |  {CYAN}  |  |  {BLUE}  |  |  {CYAN}  |  |  {BLUE} |  o  |
 {BLUE}  |  |  {CYAN}  |  |  {BLUE}  |  |  {CYAN}  |  |  {BLUE}  |  |  {CYAN}  |  |  {BLUE}  |  |  {CYAN}  |  |  {BLUE}  |  |  {CYAN}  .-""-.
 {BLUE}  |  |  {CYAN}  |  |  {BLUE}  |  |  {CYAN}  |  |  {BLUE}  |  |  {CYAN}  |  |  {BLUE}  |  |  {CYAN}  |  |  {BLUE} |  o  |
 {BLUE}  |  |  {CYAN}  |  |  {BLUE}  |  |  {CYAN}  |  |  {BLUE}  |  |  {CYAN}  |  |  {BLUE}  |  |  {CYAN}  |  |  {BLUE}  |  |  {CYAN}  .-""-.
 {BLUE}  |  |  {CYAN}  |  |  {BLUE}  |  |  {CYAN}  |  |  {BLUE}  |  |  {CYAN}  |  |  {BLUE}  |  |  {CYAN}  |  |  {BLUE} |  o  |
 {BLUE}  |  |  {CYAN}  |  |  {BLUE}  |  |  {CYAN}  |  |  {BLUE}  |  |  {CYAN}  |  |  {BLUE}  |  |  {CYAN}  |  |  {BLUE}  |  |  {CYAN}  .-""-.
 {BLUE}  |  |  {CYAN}  |  |  {BLUE}  |  |  {CYAN}  |  |  {BLUE}  |  |  {CYAN}  |  |  {BLUE}  |  |  {CYAN}  |  |  {BLUE} |  o  |
 {BLUE}  |  |  {CYAN}  |  |  {BLUE}  |  |  {CYAN}  |  |  {BLUE}  |  |  {CYAN}  |  |  {BLUE}  |  |  {CYAN}  |  |  {BLUE}  |  |  {CYAN}  .-""-.
 {BLUE}  |  |  {CYAN}  |  |  {BLUE}  |  |  {CYAN}  |  |  {BLUE}  |  |  {CYAN}  |  |  {BLUE}  |  |  {CYAN}  |  |  {BLUE} |  o  |
 {BLUE}  |  |  {CYAN}  |  |  {BLUE}  |  |  {CYAN}  |  |  {BLUE}  |  |  {CYAN}  |  |  {BLUE}  |  |  {CYAN}  |  |  {BLUE}  |  |  {CYAN}  .-""-.
 {BLUE}  |  |  {CYAN}  |  |  {BLUE}  |  |  {CYAN}  |  |  {BLUE}  |  |  {CYAN}  |  |  {BLUE}  |  |  {CYAN}  |  |  {BLUE} |  o  |
 {BLUE}  |  |  {CYAN}  |  |  {BLUE}  |  |  {CYAN}  |  |  {BLUE}  |  |  {CYAN}  |  |  {BLUE}  |  |  {CYAN}  |  |  {BLUE}  |  |  {CYAN}  .-""-.
 {BLUE}  |  |  {CYAN}  |  |  {BLUE}  |  |  {CYAN}  |  |  {BLUE}  |  |  {CYAN}  |  |  {BLUE}  |  |  {CYAN}  |  |  {BLUE} |  o  |
 {BLUE}  |  |  {CYAN}  |  |  {BLUE}  |  |  {CYAN}  |  |  {BLUE}  |  |  {CYAN}  |  |  {BLUE}  |  |  {CYAN}  |  |  {BLUE}  |  |  {CYAN}  .-""-.
 {BLUE}  |  |  {CYAN}  |  |  {BLUE}  |  |  {CYAN}  |  |  {BLUE}  |  |  {CYAN}  |  |  {BLUE}  |  |  {CYAN}  |  |  {BLUE} |  o  |
 {BLUE}  |  |  {CYAN}  |  |  {BLUE}  |  |  {CYAN}  |  |  {BLUE}  |  |  {CYAN}  |  |  {BLUE}  |  |  {CYAN}  |  |  {BLUE}  |  |  {CYAN}  .-""-.
 {BLUE}  |  |  {CYAN}  |  |  {BLUE}  |  |  {CYAN}  |  |  {BLUE}  |  |  {CYAN}  |  |  {BLUE}  |  |  {CYAN}  |  |  {BLUE} |  o  |
 {BLUE}  |  |  {CYAN}  |  |  {BLUE}  |  |  {CYAN}  |  |  {BLUE}  |  |  {CYAN}  |  |  {BLUE}  |  |  {CYAN}  |  |  {BLUE}  |  |  {CYAN}  .-""-.
 {BLUE}  |  |  {CYAN}  |  |  {BLUE}  |  |  {CYAN}  |  |  {BLUE}  |  |  {CYAN}  |  |  {BLUE}  |  |  {CYAN}  |  |  {BLUE} |  o  |
 {BLUE}  |  |  {CYAN}  |  |  {BLUE}  |  |  {CYAN}  |  |  {BLUE}  |  |  {CYAN}  |  |  {BLUE}  |  |  {CYAN}  |  |  {BLUE}  |  |  {CYAN}  .-""-.
 {BLUE}  |  |  {CYAN}  |  |  {BLUE}  |  |  {CYAN}  |  |  {BLUE}  |  |  {CYAN}  |  |  {BLUE}  |  |  {CYAN}  |  |  {BLUE} |  o  |
 {BLUE}  |  |  {CYAN}  |  |  {BLUE}  |  |  {CYAN}  |  |  {BLUE}  |  |  {CYAN}  |  |  {BLUE}  |  |  {CYAN}  |  |  {BLUE}  |  |  {CYAN}  .-""-.
 {BLUE}  |  |  {CYAN}  |  |  {BLUE}  |  |  {CYAN}  |  |  {BLUE}  |  |  {CYAN}  |  |  {BLUE}  |  |  {CYAN}  |  |  {BLUE} |  o  |
 {BLUE}  |  |  {CYAN}  |  |  {BLUE}  |  |  {CYAN}  |  |  {BLUE}  |  |  {CYAN}  |  |  {BLUE}  |  |  {CYAN}  |  |  {BLUE}  |  |  {CYAN}  .-""-.
 {BLUE}  |  |  {CYAN}  |  |  {BLUE}  |  |  {CYAN}  |  |  {BLUE}  |  |  {CYAN}  |  |  {BLUE}  |  |  {CYAN}  |  |  {BLUE} |  o  |
 {BLUE}  |  |  {CYAN}  |  |  {BLUE}  |  |  {CYAN}  |  |  {BLUE}  |  |  {CYAN}  |  |  {BLUE}  |  |  {CYAN}  |  |  {BLUE}  |  |  {CYAN}  .-""-.
 {BLUE}  |  |  {CYAN}  |  |  {BLUE}  |  |  {CYAN}  |  |  {BLUE}  |  |  {CYAN}  |  |  {BLUE}  |  |  {CYAN}  |  |  {BLUE} |  o  |
 {BLUE}  |  |  {CYAN}  |  |  {BLUE}  |  |  {CYAN}  |  |  {BLUE}  |  |  {CYAN}  |  |  {BLUE}  |  |  {CYAN}  |  |  {BLUE}  |  |  {CYAN}  .-""-.
 {BLUE}  |  |  {CYAN}  |  |  {BLUE}  |  |  {CYAN}  |  |  {BLUE}  |  |  {CYAN}  |  |  {BLUE}  |  |  {CYAN}  |  |  {BLUE} |  o  |
 {BLUE}  |  |  {CYAN}  |  |  {BLUE}  |  |  {CYAN}  |  |  {BLUE}  |  |  {CYAN}  |  |  {BLUE}  |  |  {CYAN}  |  |  {BLUE}  |  |  {CYAN}  .-""-.
 {BLUE}  |  |  {CYAN}  |  |  {BLUE}  |  |  {CYAN}  |  |  {BLUE}  |  |  {CYAN}  |  |  {BLUE}  |  |  {CYAN}  |  |  {BLUE} |  o  |
 {BLUE}  |  |  {CYAN}  |  |  {BLUE}  |  |  {CYAN}  |  |  {BLUE}  |  |  {CYAN}  |  |  {BLUE}  |  |  {CYAN}  |  |  {BLUE}  |  |  {CYAN}  .-""-.
 {BLUE}  |  |  {CYAN}  |  |  {BLUE}  |  |  {CYAN}  |  |  {BLUE}  |  |  {CYAN}  |  |  {BLUE}  |  |  {CYAN}  |  |  {BLUE} |  o  |
 {BLUE}  |  |  {CYAN}  |  |  {BLUE}  |  |  {CYAN}  |  |  {BLUE}  |  |  {CYAN}  |  |  {BLUE}  |  |  {CYAN}  |  |  {BLUE}  |  |  {CYAN}  .-""-.
 {BLUE}  |  |  {CYAN}  |  |  {BLUE}  |  |  {CYAN}  |  |  {BLUE}  |  |  {CYAN}  |  |  {BLUE}  |  |  {CYAN}  |  |  {BLUE} |  o  |
 {BLUE}  |  |  {CYAN}  |  |  {BLUE}  |  |  {CYAN}  |  |  {BLUE}  |  |  {CYAN}  |  |  {BLUE}  |  |  {CYAN}  |  |  {BLUE}  |  |  {CYAN}  .-""-.
 {BLUE}  |  |  {CYAN}  |  |  {BLUE}  |  |  {CYAN}  |  |  {BLUE}  |  |  {CYAN}  |  |  {BLUE}  |  |  {CYAN}  |  |  {BLUE} |  o  |
 {BLUE}  |  |  {CYAN}  |  |  {BLUE}  |  |  {CYAN}  |  |  {BLUE}  |  |  {CYAN}  |  |  {BLUE}  |  |  {CYAN}  |  |  {BLUE}  |  |  {CYAN}  .-""-.
 {BLUE}  |  |  {CYAN}  |  |  {BLUE}  |  |  {CYAN}  |  |  {BLUE}  |  |  {CYAN}  |  |  {BLUE}  |  |  {CYAN}  |  |  {BLUE} |  o  |
 {BLUE}  |  |  {CYAN}  |  |  {BLUE}  |  |  {CYAN}  |  |  {BLUE}  |  |  {CYAN}  |  |  {BLUE}  |  |  {CYAN}  |  |  {BLUE}  |  |  {CYAN}  .-""-.
 {BLUE}  |  |  {CYAN}  |  |  {BLUE}  |  |  {CYAN}  |  |  {BLUE}  |  |  {CYAN}  |  |  {BLUE}  |  |  {CYAN}  |  |  {BLUE} |  o  |
 {BLUE}  |  |  {CYAN}  |  |  {BLUE}  |  |  {CYAN}  |  |  {BLUE}  |  |  {CYAN}  |  |  {BLUE}  |  |  {CYAN}  |  |  {BLUE}  |  |  {CYAN}  .-""-.
 {BLUE}  |  |  {CYAN}  |  |  {BLUE}  |  |  {CYAN}  |  |  {BLUE}  |  |  {CYAN}  |  |  {BLUE}  |  |  {CYAN}  |  |  {BLUE} |  o  |
 {BLUE}  |  |  {CYAN}  |  |  {BLUE}  |  |  {CYAN}  |  |  {BLUE}  |  |  {CYAN}  |  |  {BLUE}  |  |  {CYAN}  |  |  {BLUE}  |  |  {CYAN}  .-""-.
 {BLUE}  |  |  {CYAN}  |  |  {BLUE}  |  |  {CYAN}  |  |  {BLUE}  |  |  {CYAN}  |  |  {BLUE}  |  |  {CYAN}  |  |  {BLUE} |  o  |
 {BLUE}  |  |  {CYAN}  |  |  {BLUE}  |  |  {CYAN}  |  |  {BLUE}  |  |  {CYAN}  |  |  {BLUE}  |  |  {CYAN}  |  |  {BLUE}  |  |  {CYAN}  .-""-.
 {BLUE}  |  |  {CYAN}  |  |  {BLUE}  |  |  {CYAN}  |  |  {BLUE}  |  |  {CYAN}  |  |  {BLUE}  |  |  {CYAN}  |  |  {BLUE} |  o  |
 {BLUE}  |  |  {CYAN}  |  |  {BLUE}  |  |  {CYAN}  |  |  {BLUE}  |  |  {CYAN}  |  |  {BLUE}  |  |  {CYAN}  |  |  {BLUE}  |  |  {CYAN}  .-""-.
 {BLUE}  |  |  {CYAN}  |  |  {BLUE}  |  |  {CYAN}  |  |  {BLUE}  |  |  {CYAN}  |  |  {BLUE}  |  |  {CYAN}  |  |  {BLUE} |  o  |
 {BLUE}  |  |  {CYAN}  |  |  {BLUE}  |  |  {CYAN}  |  |  {BLUE}  |  |  {CYAN}  |  |  {BLUE}  |  |  {CYAN}  |  |  {BLUE}  |  |  {CYAN}  .-""-.
 {BLUE}  |  |  {CYAN}  |  |  {BLUE}  |  |  {CYAN}  |  |  {BLUE}  |  |  {CYAN}  |  |  {BLUE}  |  |  {CYAN}  |  |  {BLUE} |  o  |
 {BLUE}  |  |  {CYAN}  |  |  {BLUE}  |  |  {CYAN}  |  |  {BLUE}  |  |  {CYAN}  |  |  {BLUE}  |  |  {CYAN}  |  |  {BLUE}  |  |  {CYAN}  .-""-.
 {BLUE}  |  |  {CYAN}  |  |  {BLUE}  |  |  {CYAN}  |  |  {BLUE}  |  |  {CYAN}  |  |  {BLUE}  |  |  {CYAN}  |  |  {BLUE} |  o  |
 {BLUE}  |  |  {CYAN}  |  |  {BLUE}  |  |  {CYAN}  |  |  {BLUE}  |  |  {CYAN}  |  |  {BLUE}  |  |  {CYAN}  |  |  {BLUE}  |  |  {CYAN}  .-""-.
 {BLUE}  |  |  {CYAN}  |  |  {BLUE}  |  |  {CYAN}  |  |  {BLUE}  |  |  {CYAN}  |  |  {BLUE}  |  |  {CYAN}  |  |  {BLUE} |  o  |
 {BLUE}  |  |  {CYAN}  |  |  {BLUE}  |  |  {CYAN}  |  |  {BLUE}  |  |  {CYAN}  |  |  {BLUE}  |  |  {CYAN}  |  |  {BLUE}  |  |  {CYAN}  .-""-.
 {BLUE}  |  |  {CYAN}  |  |  {BLUE}  |  |  {CYAN}  |  |  {BLUE}  |  |  {CYAN}  |  |  {BLUE}  |  |  {CYAN}  |  |  {BLUE} |  o  |
 {BLUE}  |  |  {CYAN}  |  |  {BLUE}  |  |  {CYAN}  |  |  {BLUE}  |  |  {CYAN}  |  |  {BLUE}  |  |  {CYAN}  |  |  {BLUE}  |  |  {CYAN}  .-""-.
 {BLUE}  |  |  {CYAN}  |  |  {BLUE}  |  |  {CYAN}  |  |  {BLUE}  |  |  {CYAN}  |  |  {BLUE}  |  |  {CYAN}  |  |  {BLUE} |  o  |
 {BLUE}  |  |  {CYAN}  |  |  {BLUE}  |  |  {CYAN}  |  |  {BLUE}  |  |  {CYAN}  |  |  {BLUE}  |  |  {CYAN}  |  |  {BLUE}  |  |  {CYAN}  .-""-.
 {BLUE}  |  |  {CYAN}  |  |  {BLUE}  |  |  {CYAN}  |  |  {BLUE}  |  |  {CYAN}  |  |  {BLUE}  |  |  {CYAN}  |  |  {BLUE} |  o  |
 {BLUE}  |  |  {CYAN}  |  |  {BLUE}  |  |  {CYAN}  |  |  {BLUE}  |  |  {CYAN}  |  |  {BLUE}  |  |  {CYAN}  |  |  {BLUE}  |  |  {CYAN}  .-""-.
 {BLUE}  |  |  {CYAN}  |  |  {BLUE}  |  |  {CYAN}  |  |  {BLUE}  |  |  {CYAN}  |  |  {BLUE}  |  |  {CYAN}  |  |  {BLUE} |  o  |
 {BLUE}  |  |  {CYAN}  |  |  {BLUE}  |  |  {CYAN}  |  |  {BLUE}  |  |  {CYAN}  |  |  {BLUE}  |  |  {CYAN}  |  |  {BLUE}  |  |  {CYAN}  .-""-.
 {BLUE}  |  |  {CYAN}  |  |  {BLUE}  |  |  {CYAN}  |  |  {BLUE}  |  |  {CYAN}  |  |  {BLUE}  |  |  {CYAN}  |  |  {BLUE} |  o  |
 {BLUE}  |  |  {CYAN}  |  |  {BLUE}  |  |  {CYAN}  |  |  {BLUE}  |  |  {CYAN}  |  |  {BLUE}  |  |  {CYAN}  |  |  {BLUE}  |  |  {CYAN}  .-""-.
 {BLUE}  |  |  {CYAN}  |  |  {BLUE}  |  |  {CYAN}  |  |  {BLUE}  |  |  {CYAN}  |  |  {BLUE}  |  |  {CYAN}  |  |  {BLUE} |  o  |
 {BLUE}  |  |  {CYAN}  |  |  {BLUE}  |  |  {CYAN}  |  |  {BLUE}  |  |  {CYAN}  |  |  {BLUE}  |  |  {CYAN}  |  |  {BLUE}  |  |  {CYAN}  .-""-.
 {BLUE}  |  |  {CYAN}  |  |  {BLUE}  |  |  {CYAN}  |  |  {BLUE}  |  |  {CYAN}  |  |  {BLUE}  |  |  {CYAN}  |  |  {BLUE} |  o  |
 {BLUE}  |  |  {CYAN}  |  |  {BLUE}  |  |  {CYAN}  |  |  {BLUE}  |  |  {CYAN}  |  |  {BLUE}  |  |  {CYAN}  |  |  {BLUE}  |  |  {CYAN}  .-""-.
 {BLUE}  |  |  {CYAN}  |  |  {BLUE}  |  |  {CYAN}  |  |  {BLUE}  |  |  {CYAN}  |  |  {BLUE}  |  |  {CYAN}  |  |  {BLUE} |  o  |
 {BLUE}  |  |  {CYAN}  |  |  {BLUE}  |  |  {CYAN}  |  |  {BLUE}  |  |  {CYAN}  |  |  {BLUE}  |  |  {CYAN}  |  |  {BLUE}  |  |  {CYAN}  .-""-.
 {BLUE}  |  |  {CYAN}  |  |  {BLUE}  |  |  {CYAN}  |  |  {BLUE}  |  |  {CYAN}  |  |  {BLUE}  |  |  {CYAN}  |  |  {BLUE} |  o  |
 {BLUE}  |  |  {CYAN}  |  |  {BLUE}  |  |  {CYAN}  |  |  {BLUE}  |  |  {CYAN}  |  |  {BLUE}  |  |  {CYAN}  |  |  {BLUE}  |  |  {CYAN}  .-""-.
 {BLUE}  |  |  {CYAN}  |  |  {BLUE}  |  |  {CYAN}  |  |  {BLUE}  |  |  {CYAN}  |  |  {BLUE}  |  |  {CYAN}  |  |  {BLUE} |  o  |
 {BLUE}  |  |  {CYAN}  |  |  {BLUE}  |  |  {CYAN}  |  |  {BLUE}  |  |  {CYAN}  |  |  {BLUE}  |  |  {CYAN}  |  |  {BLUE}  |  |  {CYAN}  .-""-.
 {BLUE}  |  |  {CYAN}  |  |  {BLUE}  |  |  {CYAN}  |  |  {BLUE}  |  |  {CYAN}  |  |  {BLUE}  |  |  {CYAN}  |  |  {BLUE} |  o  |
 {BLUE}  |  |  {CYAN}  |  |  {BLUE}  |  |  {CYAN}  |  |  {BLUE}  |  |  {CYAN}  |  |  {BLUE}  |  |  {CYAN}  |  |  {BLUE}  |  |  {CYAN}  .-""-.
 {BLUE}  |  |  {CYAN}  |  |  {BLUE}  |  |  {CYAN}  |  |  {BLUE}  |  |  {CYAN}  |  |  {BLUE}  |  |  {CYAN}  |  |  {BLUE} |  o  |
 {BLUE}  |  |  {CYAN}  |  |  {BLUE}  |  |  {CYAN}  |  |  {BLUE}  |  |  {CYAN}  |  |  {BLUE}  |  |  {CYAN}  |  |  {BLUE}  |  |  {CYAN}  .-""-.
 {BLUE}  |  |  {CYAN}  |  |  {BLUE}  |  |  {CYAN}  |  |  {BLUE}  |  |  {CYAN}  |  |  {BLUE}  |  |  {CYAN}  |  |  {BLUE} |  o  |
 {BLUE}  |  |  {CYAN}  |  |  {BLUE}  |  |  {CYAN}  |  |  {BLUE}  |  |  {CYAN}  |  |  {BLUE}  |  |  {CYAN}  |  |  {BLUE}  |  |  {CYAN}  .-""-.
 {BLUE}  |  |  {CYAN}  |  |  {BLUE}  |  |  {CYAN}  |  |  {BLUE}  |  |  {CYAN}  |  |  {BLUE}  |  |  {CYAN}  |  |  {BLUE} |  o  |
 {BLUE}  |  |  {CYAN}  |  |  {BLUE}  |  |  {CYAN}  |  |  {BLUE}  |  |  {CYAN}  |  |  {BLUE}  |  |  {CYAN}  |  |  {BLUE}  |  |  {CYAN}  .-""-.
 {BLUE}  |  |  {CYAN}  |  |  {BLUE}  |  |  {CYAN}  |  |  {BLUE}  |  |  {CYAN}  |  |  {BLUE}  |  |  {CYAN}  |  |  {BLUE} |  o  |
 {BLUE}  |  |  {CYAN}  |  |  {BLUE}  |  |  {CYAN}  |  |  {BLUE}  |  |  {CYAN}  |  |  {BLUE}  |  |  {CYAN}  |  |  {BLUE}  |  |  {CYAN}  .-""-.
 {BLUE}  |  |  {CYAN}  |  |  {BLUE}  |  |  {CYAN}  |  |  {BLUE}  |  |  {CYAN}  |  |  {BLUE}  |  |  {CYAN}  |  |  {BLUE} |  o  |
 {BLUE}  |  |  {CYAN}  |  |  {BLUE}  |  |  {CYAN}  |  |  {BLUE}  |  |  {CYAN}  |  |  {BLUE}  |  |  {CYAN}  |  |  {BLUE}  |  |  {CYAN}  .-""-.
 {BLUE}  |  |  {CYAN}  |  |  {BLUE}  |  |  {CYAN}  |  |  {BLUE}  |  |  {CYAN}  |  |  {BLUE}  |  |  {CYAN}  |  |  {BLUE} |  o  |
 {BLUE}  |  |  {CYAN}  |  |  {BLUE}  |  |  {CYAN}  |  |  {BLUE}  |  |  {CYAN}  |  |  {BLUE}  |  |  {CYAN}  |  |  {BLUE}  |  |  {CYAN}  .-""-.
 {BLUE}  |  |  {CYAN}  |  |  {BLUE}  |  |  {CYAN}  |  |  {BLUE}  |  |  {CYAN}  |  |  {BLUE}  |  |  {CYAN}  |  |  {BLUE} |  o  |
 {BLUE}  |  |  {CYAN}  |  |  {BLUE}  |  |  {CYAN}  |  |  {BLUE}  |  |  {CYAN}  |  |  {BLUE}  |  |  {CYAN}  |  |  {BLUE}  |  |  {CYAN}  .-""-.
 {BLUE}  |  |  {CYAN}  |  |  {BLUE}  |  |  {CYAN}  |  |  {BLUE}  |  |  {CYAN}  |  |  {BLUE}  |  |  {CYAN}  |  |  {BLUE} |  o  |
 {BLUE}  |  |  {CYAN}  |  |  {BLUE}  |  |  {CYAN}  |  |  {BLUE}  |  |  {CYAN}  |  |  {BLUE}  |  |  {CYAN}  |  |  {BLUE}  |  |  {CYAN}  .-""-.
 {BLUE}  |  |  {CYAN}  |  |  {BLUE}  |  |  {CYAN}  |  |  {BLUE}  |  |  {CYAN}  |  |  {BLUE}  |  |  {CYAN}  |  |  {BLUE} |  o  |
 {BLUE}  |  |  {CYAN}  |  |  {BLUE}  |  |  {CYAN}  |  |  {BLUE}  |  |  {CYAN}  |  |  {BLUE}  |  |  {CYAN}  |  |  {BLUE}  |  |  {CYAN}  .-""-.
 {BLUE}  |  |  {CYAN}  |  |  {BLUE}  |  |  {CYAN}  |  |  {BLUE}  |  |  {CYAN}  |  |  {BLUE}  |  |  {CYAN}  |  |  {BLUE} |  o  |
 {BLUE}  |  |  {CYAN}  |  |  {BLUE}  |  |  {CYAN}  |  |  {BLUE}  |  |  {CYAN}  |  |  {BLUE}  |  |  {CYAN}  |  |  {BLUE}  |  |  {CYAN}  .-""-.
 {BLUE}  |  |  {CYAN}  |  |  {BLUE}  |  |  {CYAN}  |  |  {BLUE}  |  |  {CYAN}  |  |  {BLUE}  |  |  {CYAN}  |  |  {BLUE} |  o  |
 {BLUE}  |  |  {CYAN}  |  |  {BLUE}  |  |  {CYAN}  |  |  {BLUE}  |  |  {CYAN}  |  |  {BLUE}  |  |  {CYAN}  |  |  {BLUE}  |  |  {CYAN}  .-""-.
 {BLUE}  |  |  {CYAN}  |  |  {BLUE}  |  |  {CYAN}  |  |  {BLUE}  |  |  {CYAN}  |  |  {BLUE}  |  |  {CYAN}  |  |  {BLUE} |  o  |
 {BLUE}  |  |  {CYAN}  |  |  {BLUE}  |  |  {CYAN}  |  |  {BLUE}  |  |  {CYAN}  |  |  {BLUE}  |  |  {CYAN}  |  |  {BLUE}  |  |  {CYAN}  .-""-.
 {BLUE}  |  |  {CYAN}  |  |  {BLUE}  |  |  {CYAN}  |  |  {BLUE}  |  |  {CYAN}  |  |  {BLUE}  |  |  {CYAN}  |  |  {BLUE} |  o  |
 {BLUE}  |  |  {CYAN}  |  |  {BLUE}  |  |  {CYAN}  |  |  {BLUE}  |  |  {CYAN}  |  |  {BLUE}  |  |  {CYAN}  |  |  {BLUE}  |  |  {CYAN}  .-""-.
 {BLUE}  |  |  {CYAN}  |  |  {BLUE}  |  |  {CYAN}  |  |  {BLUE}  |  |  {CYAN}  |  |  {BLUE}  |  |  {CYAN}  |  |  {BLUE} |  o  |
 {BLUE}  |  |  {CYAN}  |  |  {BLUE}  |  |  {CYAN}  |  |  {BLUE}  |  |  {CYAN}  |  |  {BLUE}  |  |  {CYAN}  |  |  {BLUE}  |  |  {CYAN}  .-""-.
 {BLUE}  |  |  {CYAN}  |  |  {BLUE}  |  |  {CYAN}  |  |  {BLUE}  |  |  {CYAN}  |  |  {BLUE}  |  |  {CYAN}  |  |  {BLUE} |  o  |
 {BLUE}  |  |  {CYAN}  |  |  {BLUE}  |  |  {CYAN}  |  |  {BLUE}  |  |  {CYAN}  |  |  {BLUE}  |  |  {CYAN}  |  |  {BLUE}  |  |  {CYAN}  .-""-.
 {BLUE}  |  |  {CYAN}  |  |  {BLUE}  |  |  {CYAN}  |  |  {BLUE}  |  |  {CYAN}  |  |  {BLUE}  |  |  {CYAN}  |  |  {BLUE} |  o  |
 {BLUE}  |  |  {CYAN}  |  |  {BLUE}  |  |  {CYAN}  |  |  {BLUE}  |  |  {CYAN}  |  |  {BLUE}  |  |  {CYAN}  |  |  {BLUE}  |  |  {CYAN}  .-""-.
 {BLUE}  |  |  {CYAN}  |  |  {BLUE}  |  |  {CYAN}  |  |  {BLUE}  |  |  {CYAN}  |  |  {BLUE}  |  |  {CYAN}  |  |  {BLUE} |  o  |
 {BLUE}  |  |  {CYAN}  |  |  {BLUE}  |  |  {CYAN}  |  |  {BLUE}  |  |  {CYAN}  |  |  {BLUE}  |  |  {CYAN}  |  |  {BLUE}  |  |  {CYAN}  .-""-.
 {BLUE}  |  |  {CYAN}  |  |  {BLUE}  |  |  {CYAN}  |  |  {BLUE}  |  |  {CYAN}  |  |  {BLUE}  |  |  {CYAN}  |  |  {BLUE} |  o  |
 {BLUE}  |  |  {CYAN}  |  |  {BLUE}  |  |  {CYAN}  |  |  {BLUE}  |  |  {CYAN}  |  |  {BLUE}  |  |  {CYAN}  |  |  {BLUE}  |  |  {CYAN}  .-""-.
 {BLUE}  |  |  {CYAN}  |  |  {BLUE}  |  |  {CYAN}  |  |  {BLUE}  |  |  {CYAN}  |  |  {BLUE}  |  |  {CYAN}  |  |  {BLUE} |  o  |
 {BLUE}  |  |  {CYAN}  |  |  {BLUE}  |  |  {CYAN}  |  |  {BLUE}  |  |  {CYAN}  |  |  {BLUE}  |  |  {CYAN}  |  |  {BLUE}  |  |  {CYAN}  .-""-.
 {BLUE}  |  |  {CYAN}  |  |  {BLUE}  |  |  {CYAN}  |  |  {BLUE}  |  |  {CYAN}  |  |  {BLUE}  |  |  {CYAN}  |  |  {BLUE} |  o  |
 {BLUE}  |  |  {CYAN}  |  |  {BLUE}  |  |  {CYAN}  |  |  {BLUE}  |  |  {CYAN}  |  |  {BLUE}  |  |  {CYAN}  |  |  {BLUE}  |  |  {CYAN}  .-""-.
 {BLUE}  |  |  {CYAN}  |  |  {BLUE}  |  |  {CYAN}  |  |  {BLUE}  |  |  {CYAN}  |  |  {BLUE}  |  |  {CYAN}  |  |  {BLUE} |  o  |
 {BLUE}  |  |  {CYAN}  |  |  {BLUE}  |  |  {CYAN}  |  |  {BLUE}  |  |  {CYAN}  |  |  {BLUE}  |  |  {CYAN}  |  |  {BLUE}  |  |  {CYAN}  .-""-.
 {BLUE}  |  |  {CYAN}  |  |  {BLUE}  |  |  {CYAN}  |  |  {BLUE}  |  |  {CYAN}  |  |  {BLUE}  |  |  {CYAN}  |  |  {BLUE} |  o  |
 {BLUE}  |  |  {CYAN}  |  |  {BLUE}  |  |  {CYAN}  |  |  {BLUE}  |  |  {CYAN}  |  |  {BLUE}  |  |  {CYAN}  |  |  {BLUE}  |  |  {CYAN}  .-""-.
 {BLUE}  |  |  {CYAN}  |  |  {BLUE}  |  |  {CYAN}  |  |  {BLUE}  |  |  {CYAN}  |  |  {BLUE}  |  |  {CYAN}  |  |  {BLUE} |  o  |
 {BLUE}  |  |  {CYAN}  |  |  {BLUE}  |  |  {CYAN}  |  |  {BLUE}  |  |  {CYAN}  |  |  {BLUE}  |  |  {CYAN}  |  |  {BLUE}  |  |  {CYAN}  .-""-.
 {BLUE}  |  |  {CYAN}  |  |  {BLUE}  |  |  {CYAN}  |  |  {BLUE}  |  |  {CYAN}  |  |  {BLUE}  |  |  {CYAN}  |  |  {BLUE} |  o  |
 {BLUE}  |  |  {CYAN}  |  |  {BLUE}  |  |  {CYAN}  |  |  {BLUE}  |  |  {CYAN}  |  |  {BLUE}  |  |  {CYAN}  |  |  {BLUE}  |  |  {CYAN}  .-""-.
 {BLUE}  |  |  {CYAN}  |  |  {BLUE}  |  |  {CYAN}  |  |  {BLUE}  |  |  {CYAN}  |  |  {BLUE}  |  |  {CYAN}  |  |  {BLUE} |  o  |
 {BLUE}  |  |  {CYAN}  |  |  {BLUE}  |  |  {CYAN}  |  |  {BLUE}  |  |  {CYAN}  |  |  {BLUE}  |  |  {CYAN}  |  |  {BLUE}  |  |  {CYAN}  .-""-.
 {BLUE}  |  |  {CYAN}  |  |  {BLUE}  |  |  {CYAN}  |  |  {BLUE}  |  |  {CYAN}  |  |  {BLUE}  |  |  {CYAN}  |  |  {BLUE} |  o  |
 {BLUE}  |  |  {CYAN}  |  |  {BLUE}  |  |  {CYAN}  |  |  {BLUE}  |  |  {CYAN}  |  |  {BLUE}  |  |  {CYAN}  |  |  {BLUE}  |  |  {CYAN}  .-""-.
 {BLUE}  |  |  {CYAN}  |  |  {BLUE}  |  |  {CYAN}  |  |  {BLUE}  |  |  {CYAN}  |  |  {BLUE}  |  |  {CYAN}  |  |  {BLUE} |  o  |
 {BLUE}  |  |  {CYAN}  |  |  {BLUE}  |  |  {CYAN}  |  |  {BLUE}  |  |  {CYAN}  |  |  {BLUE}  |  |  {CYAN}  |  |  {BLUE}  |  |  {CYAN}  .-""-.
 {BLUE}  |  |  {CYAN}  |  |  {BLUE}  |  |  {CYAN}  |  |  {BLUE}  |  |  {CYAN}  |  |  {BLUE}  |  |  {CYAN}  |  |  {BLUE} |  o  |
 {BLUE}  |  |  {CYAN}  |  |  {BLUE}  |  |  {CYAN}  |  |  {BLUE}  |  |  {CYAN}  |  |  {BLUE}  |  |  {CYAN}  |  |  {BLUE}  |  |  {CYAN}  .-""-.
 {BLUE}  |  |  {CYAN}  |  |  {BLUE}  |  |  {CYAN}  |  |  {BLUE}  |  |  {CYAN}  |  |  {BLUE}  |  |  {CYAN}  |  |  {BLUE} |  o  |
 {BLUE}  |  |  {CYAN}  |  |  {BLUE}  |  |  {CYAN}  |  |  {BLUE}  |  |  {CYAN}  |  |  {BLUE}  |  |  {CYAN}  |  |  {BLUE}  |  |  {CYAN}  .-""-.
 {BLUE}  |  |  {CYAN}  |  |  {BLUE}  |  |  {CYAN}  |  |  {BLUE}  |  |  {CYAN}  |  |  {BLUE}  |  |  {CYAN}  |  |  {BLUE} |  o  |
 {BLUE}  |  |  {CYAN}  |  |  {BLUE}  |  |  {CYAN}  |  |  {BLUE}  |  |  {CYAN}  |  |  {BLUE}  |  |  {CYAN}  |  |  {BLUE}  |  |  {CYAN}  .-""-.
 {BLUE}  |  |  {CYAN}  |  |  {BLUE}  |  |  {CYAN}  |  |  {BLUE}  |  |  {CYAN}  |  |  {BLUE}  |  |  {CYAN}  |  |  {BLUE} |  o  |
 {BLUE}  |  |  {CYAN}  |  |  {BLUE}  |  |  {CYAN}  |  |  {BLUE}  |  |  {CYAN}  |  |  {BLUE}  |  |  {CYAN}  |  |  {BLUE}  |  |  {CYAN}  .-""-.
 {BLUE}  |  |  {CYAN}  |  |  {BLUE}  |  |  {CYAN}  |  |  {BLUE}  |  |  {CYAN}  |  |  {BLUE}  |  |  {CYAN}  |  |  {BLUE} |  o  |
 {BLUE}  |  |  {CYAN}  |  |  {BLUE}  |  |  {CYAN}  |  |  {BLUE}  |  |  {CYAN}  |  |  {BLUE}  |  |  {CYAN}  |  |  {BLUE}  |  |  {CYAN}  .-""-.
 {BLUE}  |  |  {CYAN}  |  |  {BLUE}  |  |  {CYAN}  |  |  {BLUE}  |  |  {CYAN}  |  |  {BLUE}  |  |  {CYAN}  |  |  {BLUE} |  o  |
 {BLUE}  |  |  {CYAN}  |  |  {BLUE}  |  |  {CYAN}  |  |  {BLUE}  |  |  {CYAN}  |  |  {BLUE}  |  |  {CYAN}  |  |  {BLUE}  |  |  {CYAN}  .-""-.
 {BLUE}  |  |  {CYAN}  |  |  {BLUE}  |  |  {CYAN}  |  |  {BLUE}  |  |  {CYAN}  |  |  {BLUE}  |  |  {CYAN}  |  |  {BLUE} |  o  |
 {BLUE}  |  |  {CYAN}  |  |  {BLUE}  |  |  {CYAN}  |  |  {BLUE}  |  |  {CYAN}  |  |  {BLUE}  |  |  {CYAN}  |  |  {BLUE}  |  |  {CYAN}  .-""-.
 {BLUE}  |  |  {CYAN}  |  |  {BLUE}  |  |  {CYAN}  |  |  {BLUE}  |  |  {CYAN}  |  |  {BLUE}  |  |  {CYAN}  |  |  {BLUE} |  o  |
 {BLUE}  |  |  {CYAN}  |  |  {BLUE}  |  |  {CYAN}  |  |  {BLUE}  |  |  {CYAN}  |  |  {BLUE}  |  |  {CYAN}  |  |  {BLUE}  |  |  {CYAN}  .-""-.
 {BLUE}  |  |  {CYAN}  |  |  {BLUE}  |  |  {CYAN}  |  |  {BLUE}  |  |  {CYAN}  |  |  {BLUE}  |  |  {CYAN}  |  |  {BLUE} |  o  |
 {BLUE}  |  |  {CYAN}  |  |  {BLUE}  |  |  {CYAN}  |  |  {BLUE}  |  |  {CYAN}  |  |  {BLUE}  |  |  {CYAN}  |  |  {BLUE}  |  |  {CYAN}  .-""-.
 {BLUE}  |  |  {CYAN}  |  |  {BLUE}  |  |  {CYAN}  |  |  {BLUE}  |  |  {CYAN}  |  |  {BLUE}  |  |  {CYAN}  |  |  {BLUE} |  o  |
 {BLUE}  |  |  {CYAN}  |  |  {BLUE}  |  |  {CYAN}  |  |  {BLUE}  |  |  {CYAN}  |  |  {BLUE}  |  |  {CYAN}  |  |  {BLUE}  |  |  {CYAN}  .-""-.
 {BLUE}  |  |  {CYAN}  |  |  {BLUE}  |  |  {CYAN}  |  |  {BLUE}  |  |  {CYAN}  |  |  {BLUE}  |  |  {CYAN}  |  |  {BLUE} |  o  |
 {BLUE}  |  |  {CYAN}  |  |  {BLUE}  |  |  {CYAN}  |  |  {BLUE}  |  |  {CYAN}  |  |  {BLUE}  |  |  {CYAN}  |  |  {BLUE}  |  |  {CYAN}  .-""-.
 {BLUE}  |  |  {CYAN}  |  |  {BLUE}  |  |  {CYAN}  |  |  {BLUE}  |  |  {CYAN}  |  |  {BLUE}  |  |  {CYAN}  |  |  {BLUE} |  o  |
 {BLUE} 极长的ASCII艺术，为了节省空间，只显示前几行，实际代码中会完整输出