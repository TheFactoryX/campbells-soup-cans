"""
Campbell's Soup Can #1232
Produced: 2025-12-28 09:33:07
Worker: AllenAI: Olmo 3 32B Think (free) (allenai/olmo-3-32b-think:free)
Employment: Volunteer
Flavor: Woody Allen Philosophy
Quality: ✅

Made by Machine #0 - Production Line 0
Like Warhol's soup cans - same but different.
Each can is the same flavor, made by different hands.
"""

quote = "Why exist? To suffer in style."

reset = '\033[0m'
bold_red = '\033[1;91m'
yellow = '\033[93m'
green = '\033[92m'

border_length = 38
border = '+' + '-' * border_length + '+'

title = "Woody's Woes"
full_title_line = f"| {title:^{border_length}} |"
full_content_line = f"| {quote:^{border_length}} |"

print(f"{bold_red}{border}{reset}")
print(f"{yellow}{full_title_line}{reset}")
print(f"{green}{full_content_line}{reset}")
print(f"{bold_red}{border}{reset}")