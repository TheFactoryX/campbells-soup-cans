"""
Campbell's Soup Can #957
Produced: 2025-12-15 20:38:05
Worker: Qwen: Qwen3 235B A22B (free) (qwen/qwen3-235b-a22b:free)
Employment: Volunteer
Flavor: Woody Allen Philosophy
Quality: ❌ (missing print)

Made by Machine #0 - Production Line 0
Like Warhol's soup cans - same but different.
Each can is the same flavor, made by different hands.
"""

import time
import sys

CYAN = '\033[36m'
YELLOW = '\033[33m'
RESET = '\033[0m'
BOLD = '\033[1m'

coffee_art = f"""{YELLOW}
        ~  ~  ~        
           \\ | /           
            \\|/            
         _________         
        |  ANXIETY  |       
        |     ☕     |       
        |___________|       
            |     |          
            |_____|          
{RESET}"""

sys.stdout.write(coffee_art)
time.sleep(0.7)

quote = "My therapist says I have a preoccupation with vengeance. We'll see when he gets mine back from the dry cleaners."

frame_width = len(quote) + 6
top_frame = f"{CYAN}╔{'═' * frame_width}╗"
bottom_frame = f"╚{'═' * frame_width}╝{RESET}"

sys.stdout.write(top_frame + '\n')
sys.stdout.write(f"║   {BOLD}{CYAN}")
for char in quote:
    sys.stdout.write(char)
    sys.stdout.flush()
    time.sleep(0.045)
sys.stdout.write(f"{RESET}{CYAN}   ║\n")
sys.stdout.write(bottom_frame)

sys.stdout.write(f"\n{YELLOW}  'Life is full of loneliness, misery, and suffering -{RESET}\n")
sys.stdout.write(f"{YELLOW}   and it's all over much too soon.' - {BOLD}My Anxiety{RESET}\n")