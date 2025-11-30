"""
Campbell's Soup Can #618
Produced: 2025-11-30 08:36:18
Worker: Meituan: LongCat Flash Chat (free) (meituan/longcat-flash-chat:free)
Employment: Volunteer
Flavor: Woody Allen Philosophy
Quality: ✅

Made by Machine #0 - Production Line 0
Like Warhol's soup cans - same but different.
Each can is the same flavor, made by different hands.
"""

import time
import sys
import os

# ANSI Color Codes
COLORS = {
    'red': '\033[91m',
    'green': '\033[92m',
    'yellow': '\033[93m',
    'blue': '\033[94m',
    'magenta': '\033[95m',
    'cyan': '\033[96m',
    'white': '\033[97m',
    'gray': '\033[90m',
    'bold': '\033[1m',
    'underline': '\033[4m',
    'end': '\033[0m'
}

# Brain ASCII Art (existential, neurotic)
brain_art = [
    "    ┌───────────────────────────────────────────────┐",
    "    │  "+COLORS['magenta']+"███████"+COLORS['end']+"  "+COLORS['red']+"███████"+COLORS['end']+"   "+COLORS['blue']+"▓▓▓▓▓▓▓▓"+COLORS['end']+"                  │",
    "    │ "+COLORS['magenta']+"██"+COLORS['end']+"       "+COLORS['red']+"██     ██"+COLORS['end']+" "+COLORS['blue']+"▓▓▓▓▓▓▓▓▓▓▓▓"+COLORS['end']+"               │",
    "    │ "+COLORS['magenta']+"███"+COLORS['end']+"      "+COLORS['red']+"████████"+COLORS['end']+" "+COLORS['blue']+"▓▓▓▓▓▓▓▓▓▓▓▓▓▓"+COLORS['end']+"             │",
    "    │ "+COLORS['magenta']+"█"+COLORS['end']+" "+COLORS['magenta']+"███"+COLORS['end']+" █  "+COLORS['red']+"██ "+COLORS['red']+"██ "+COLORS['end']+"█  "+COLORS['blue']+"▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓"+COLORS['end']+"             │",
    "    │ "+COLORS['magenta']+"█"+COLORS['end']+"  "+COLORS['magenta']+"█████"+COLORS['end']+" "+COLORS['red']+"██  ██"+COLORS['end']+"   "+COLORS['blue']+"▓▓▓▓▓▓▓▓▓▓▓▓▓▓"+COLORS['end']+"              │",
    "    │ "+COLORS['magenta']+"█"+COLORS['end']+"  "+COLORS['magenta']+"█████"+COLORS['end']+" "+COLORS['red']+"███"+COLORS['end']+" "+COLORS['red']+"████"+COLORS['end']+"  "+COLORS['blue']+"▓▓▓▓▓▓▓▓▓▓▓▓▓"+COLORS['end']+"    "+COLORS['green']+"┌───┐"+COLORS['end']+"        │",
    "    │ "+COLORS['magenta']+"█"+COLORS['end']+"   "+COLORS['magenta']+"███"+COLORS['end']+"  "+COLORS['red']+"██████"+COLORS['end']+"   "+COLORS['blue']+"▓▓▓▓▓▓▓▓▓▓▓"+COLORS['end']+"               │",
    "    │ "+COLORS['magenta']+"██"+COLORS['end']+"    "+COLORS['magenta']+"█"+COLORS['end']+"  "+COLORS['red']+"██"+COLORS['end']+"   "+COLORS['red']+"██"+COLORS['end']+"  "+COLORS['blue']+"▓▓▓▓▓▓▓▓▓▓"+COLORS['end']+"     "+COLORS['yellow']+"(☼ ω ☼)"+COLORS['end']+"      │",
    "    │ "+COLORS['magenta']+"███████"+COLORS['end']+" "+COLORS['red']+"██  "+COLORS['red']+"██"+COLORS['end']+"   "+COLORS['blue']+"▓▓▓▓▓▓▓▓▓▓"+COLORS['end']+"               │",
    "    └───────────────────────────────────────────────┘",
    "              "+COLORS['gray']+"The Organ Weighs "+"█"*2 + " 3 lbs"+COLORS['end']
]

# Woody Allen Quote - neurotic, absurd, existential
quote_lines = [
    COLORS['bold'] + COLORS['cyan'] + "I asked my therapist if I could attend my own autopsy.",
    "",
    COLORS['yellow'] + "Mostly because I wanted to see if my last thought",
    "was actually just indigestion from the schnitzel.",
    "",
    COLORS['magenta'] + "Turns out, even in death, I’m late, misunderstood,",
    "and owe the mortician $84 for overdue parking in the morgue.",
    "",
    COLORS['red'] + "The afterlife has a 2-year waitlist",
    "and my reservation was lost due to existential database corruption.",
    "",
    COLORS['bold'] + COLORS['white'] + "So now I lurk in the waiting room of eternity,",
    "writing Yelp reviews for purgatory and questioning my life choices",
    "while the guy who invented religion gets platinum rewards.",
    COLORS['end']
]

# Typing effect with cursor
def type_text(text, color='', delay=0.03, final_delay=0.05):
    for char in text:
        sys.stdout.write(color + char + COLORS['end'])
        sys.stdout.flush()
        time.sleep(delay)
    time.sleep(final_delay)
    print()

# Clear screen (fallback for Windows and Unix)
def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

# Main function
def main():
    clear_screen()
    
    # Display brain art with blinking effect
    for _ in range(2):
        clear_screen()
        for line in brain_art[:6]:
            print("  " + line)
            time.sleep(0.05)
        print("\n")
        for line in brain_art[6:]:
            print("  " + line)
            time.sleep(0.05)
        time.sleep(0.3)
        clear_screen()
        time.sleep(0.2)

    # Display brain art (final)
    for line in brain_art:
        print("  " + line)
        time.sleep(0.1)

    print("\n")
    
    # Display quote
    for line in quote_lines:
        if "Mostly" in line or "Turns out" in line:
            type_text(line, delay=0.04)
        elif "The afterlife" in line or "So now I lurk" in line:
            for char in line:
                if char in ".,!?;:":
                    sys.stdout.write(COLORS['bold'] + COLORS['yellow'] + char + COLORS['end'])
                    sys.stdout.flush()
                    time.sleep(0.6)
                else:
                    sys.stdout.write(char)
                    sys.stdout.flush()
                    time.sleep(0.07)
            time.sleep(0.3)
            print()
        else:
            type_text(line, delay=0.03)
    
    print("\n" + COLORS['gray'] + " " * 45 + "— Woody Allen (probably)" + COLORS['end'])
    
    # Final surprise: flicker and vanish
    for _ in range(4):
        print(COLORS['bold'] + " " * 45 + "PS: I faked my resurrection. I just left." + COLORS['end'])
        time.sleep(0.3)
        print("\033[A" + " " * 80)  # Move up and clear
        time.sleep(0.2)
    
    print(COLORS['bold'] + COLORS['red'] + " " * 45 + "PS: Please clap." + COLORS['end'])
    time.sleep(1)
    clear_screen()
    print(COLORS['green'] + COLORS['bold'] + "\n\n  ♥ Thank you for overthinking life with me. Stay anxious. ♥" + COLORS['end'])
    print(COLORS['gray'] + " " * 20 + "Exited before death could claim the runtime." + COLORS['end'])

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        clear_screen()
        print(COLORS['red'] + "\n\n  User escaped existence. Story of my life.\n" + COLORS['end'])