"""
Campbell's Soup Can #2002
Produced: 2026-02-02 11:50:52
Worker: OpenAI: GPT-4o (2024-05-13) (openai/gpt-4o-2024-05-13)
Employment: Paid
Flavor: Woody Allen Philosophy
Quality: ✅

Made by Machine #0 - Production Line 0
Like Warhol's soup cans - same but different.
Each can is the same flavor, made by different hands.
"""

import time
import os

# Function to clear the console (for smooth animation)
def clear_console():
    os.system('cls' if os.name == 'nt' else 'clear')

# Colors using ANSI escape codes
RED = '\033[91m'
GREEN = '\033[92m'
YELLOW = '\033[93m'
BLUE = '\033[94m'
MAGENTA = '\033[95m'
CYAN = '\033[96m'
RESET = '\033[0m'

quote = (
    f"{GREEN}Life is divided into the horrible and the miserable.{RESET}\n"
    f"{YELLOW}The horrible are terminal cases, you know, and blind people, crippled.{RESET}\n"
    f"{RED}I don't feel qualified to give advice in that area.{RESET}\n"
    f"{BLUE}But the miserable is everyone else.{RESET}\n"
    f"{MAGENTA}So when you go through life, be thankful you’re miserable.{RESET}"
)

ascii_art = f"""
{CYAN}**************************************************
*                                                *
*         {RED}.__                           .___          *
*         {RED}|  |__ _____    _____   ____ |  |         *
*         {RED}|  |  \\\\__  \  /     \_/ __ \|  |         *
*         {RED}|   Y  \/ __ \|  Y Y  \  ___/|  |__       *
*         {RED}|___|  (____  /__|_|  /\___  >____/       *
*               \/    \/      \/    \/                  *
*   .__                                              *
*   |  |__       ________ ________ __ ______     .____ *
*   |  |  \     _/ __ \  |  \__  \ |  |.__  \   |    |  *
*   |   Y  \   \  ___/|  |  // __ \|  |/ __ \_ |   /   *
*   |___|  /\n..to achieve true inner peace       ...∧_⋅_\n
*            avoid"          ____/  \____|
*           thinking about;\_/ _\__/ /     *
*          eternity,   the past,  and,\  t *
*... generally,  existence."...         *
*                                     
**************************************************{RESET}
"""

for i in range(3):
    clear_console()
    print(ascii_art)
    time.sleep(1)
    clear_console()
    time.sleep(0.5)

print(ascii_art)
print(quote)