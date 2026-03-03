"""
Campbell's Soup Can #2546
Produced: 2026-03-03 16:01:32
Worker: Qwen: Qwen3 235B A22B Thinking 2507 (qwen/qwen3-235b-a22b-thinking-2507)
Employment: Volunteer
Flavor: Woody Allen Philosophy
Quality: ✅

Made by Machine #0 - Production Line 0
Like Warhol's soup cans - same but different.
Each can is the same flavor, made by different hands.
"""

import time
import sys

def main():
    border_color = '\033[94m'
    text_color = '\033[93m'
    reset = '\033[0m'
    
    box_width = 60
    inner_width = box_width - 4
    
    quote = "I've achieved complete clarity about mortality: I'm not afraid to die, I just want my obituary to say 'He didn't pay the bill on time'"
    
    words = quote.split()
    lines = []
    current_line = []
    
    for word in words:
        if len(' '.join(current_line + [word])) <= inner_width:
            current_line.append(word)
        else:
            lines.append(' '.join(current_line))
            current_line = [word]
    if current_line:
        lines.append(' '.join(current_line))
    
    total_content_lines = 5
    num_lines = len(lines)
    top_padding = max(0, (total_content_lines - num_lines) // 2)
    bottom_padding = total_content_lines - num_lines - top_padding
    
    print(f"{border_color}╔{'═' * (box_width-2)}╗{reset}")
    
    for i in range(total_content_lines):
        if i < top_padding:
            sys.stdout.write(f"{border_color}║{reset}{' ' * inner_width}{border_color}║{reset}\n")
        elif i < top_padding + num_lines:
            line = lines[i - top_padding]
            padded_line = line.center(inner_width)
            
            sys.stdout.write(f"{border_color}║{reset} ")
            sys.stdout.write(text_color)
            for char in padded_line:
                sys.stdout.write(char)
                sys.stdout.flush()
                time.sleep(0.03)
            sys.stdout.write(f"{reset} {border_color}║{reset}\n")
        else:
            sys.stdout.write(f"{border_color}║{reset}{' ' * inner_width}{border_color}║{reset}\n")
    
    print(f"{border_color}╚{'═' * (box_width-2)}╝{reset}")
    
    time.sleep(0.5)
    print(f"\n{text_color}  (This existential crisis was brought to you by the letter 'Z' and 3 cups of decaf){reset}")

if __name__ == "__main__":
    main()