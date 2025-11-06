"""
Campbell's Soup Can #100
Produced: 2025-11-06 18:45:57
Worker: DeepSeek: DeepSeek R1 0528 Qwen3 8B (free) (deepseek/deepseek-r1-0528-qwen3-8b:free)
Employment: Volunteer
Flavor: Woody Allen Philosophy
Quality: ❌ (broken)

Made by Machine #0 - Production Line 0
Like Warhol's soup cans - same but different.
Each can is the same flavor, made by different hands.
"""

from time import sleep
import sys

# ANSI color codes
RESET = '\033[0m'
BRIGHT = '\033[1m'
BLACK='\033[30m'
RED='\033[31m'
GREEN='\033[32m'
YELLOW='\033[33m'
BLUE='\033[34m'
MAGENTA='\033[35m'
CYAN='\033[36m'
WHITE='\033[97m'

# Clear the screen
print("\033[H\033[J", end='')

# Print a hollow brain with a question mark inside
brain_art = [
    "                  .-/+\\+/-+.                  ",
    "              `-        `-.               ",
    "          `-.            ,\\_             ",
    "         .  \\       `\`   \\ \\\            ",
    "    `   `     `\\            \\ \\\           ",
    "         .      `--..,--..--`            ",
    "     .` `-         _  _         `-.`     ",
    "   .  \\      .\\,-  ==>===>  ,-./      \\  ",
    "    \"   \\   /. |--===>===>--|  \\/   \"    ",
    "        \" . /         /        \\  . \""    ",
    "           /.       .            \\          ",
    F"{WHITE}         /      O\\\\        {BRIGHT}       ",
    "       /          \\          \\       ",
    "      {RED}|   IN   |{RESET}      |   OUT   |{RESET}     ",
    "      |    .   .   |      |     |