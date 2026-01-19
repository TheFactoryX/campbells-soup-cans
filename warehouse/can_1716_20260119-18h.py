"""
Campbell's Soup Can #1716
Produced: 2026-01-19 18:49:28
Worker: Qwen: Qwen-Max  (qwen/qwen-max)
Employment: Paid
Flavor: Woody Allen Philosophy
Quality: ✅

Made by Machine #0 - Production Line 0
Like Warhol's soup cans - same but different.
Each can is the same flavor, made by different hands.
"""

def rainbow_text(text):
    colors = ['\033[31m', '\033[33m', '\033[32m', '\033[36m', '\033[34m', '\033[35m']
    for i, char in enumerate(text):
        color = colors[i % len(colors)]
        print(color + char, end='')
    print('\033[0m')  # Reset color

def box_text(text, width=40):
    print('+' + '-' * width + '+')
    for line in text.split('\n'):
        print('|' + line.center(width) + '|')
    print('+' + '-' * width + '+')

def main():
    import os
    import time

    quote = "I don't want to achieve immortality through my work; I just want to not die."
    ascii_art = r"""
      ____
     |  o |
     |____| 
    __|____|__ 
   |          | 
   |          | 
   |          | 
   |__________| 
    """
    
    os.system('clear' if os.name == 'posix' else 'cls')

    print('\033[37m' + ascii_art)  # White color
    time.sleep(1)

    box_text(quote, 50)
    time.sleep(1)

    rainbow_text(quote)
    time.sleep(1)

    box_text(quote, 50)

if __name__ == "__main__":
    main()