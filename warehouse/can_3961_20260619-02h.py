"""
Campbell's Soup Can #3961
Produced: 2026-06-19 02:06:08
Worker: NVIDIA: Nemotron Nano 9B V2 (free) (nvidia/nemotron-nano-9b-v2:free)
Employment: Volunteer
Flavor: Woody Allen Philosophy
Quality: ❌ (broken)

Made by Machine #0 - Production Line 0
Like Warhol's soup cans - same but different.
Each can is the same flavor, made by different hands.
"""

import time

GREEN = '\033[92m'
YELLOW = '\033[93m'
MAGENTA = '\033[95m'
RESET = '\033[0m'

print(f"{GREEN}####################{RESET}")
print(f"{YELLOW}#                  #{RESET}")
print(f"{MAGENTA}#   \033[33m/\\__/  \\/\\__/  \\ \033[0m  #{RESET}")
print(f"{YELLOW}#  (\033[35m/  \\___/  \\/  \\ \033[0m)  #{RESET}")
print(f"{GREEN}#   \ \033[32m/  \\  \\  \\  \033[0m   #{RESET}")
print(f"{YELLOW}#    \ \033[33m/  \\  \\  \\  \033[0m   #{RESET}")
print(f"{MAGENTA}#     \ \033[36m/\  \\  \\  \\  \033[0m   #{RESET}")
print(f"{GREEN}#      \__________\033[0m  #{RESET}")
print(f"{GREEN}####################{RESET}")

quote = f"""
{MAGENTA}Life's too short for bad philosophy— \033[31mjust \033[33mkeep \033[36mscrolling.\033[0m\n
{RESET}— Woody (probably not the Allen, but maybe?)'''

for _ in range(4):
    print(f"\r{BLUE}{quote}{RESET}", end='')
    time.sleep(0.4)
    print(f"\r{RESET}{quote}{RESET}", end='')
    time.sleep(0.4)