"""
Campbell's Soup Can #385
Produced: 2025-11-19 18:44:07
Worker: Goliath 120B (alpindale/goliath-120b)
Employment: Paid
Flavor: Woody Allen Philosophy
Quality: ❌ (broken)

Made by Machine #0 - Production Line 0
Like Warhol's soup cans - same but different.
Each can is the same flavor, made by different hands.
"""

none
import subprocess,os,time
ASCII_BOX_CHAR = 'lyn+++++drdhyzpwMJNX\nq2!rug03#4>5@789\n(:&+6`1%/=Bania'\
+( chr(8192) * 20) + 'sTACm,.-QK|{/WO\n>p"`_V}Q\n}//3Q*}?x\n04@85&!'\
+( chr(124) * 15 ) + '@*I\n_^?+%`1C{"+'`9\n?at_267$/P\n'

def print_box(message):
    print(f"{chr(27) + '1;33;40;100m' + f''+{ASCII_BOX_CHAR}+''}{chr(27) + '0;0m'}\n")
    print(f"{chr(33) + '1;35;40m' + f']                   {message}                  [{'*'*54+'}')}{chr(33) + '0;0m'\n")
    print(f"{chr(27) + '1;33;40;100m' + f''+{ASCII_BOX_CHAR}{chr(27) + '0;0m'}\n")

def print_quote():
    quote_list = [
        "I don't want to achieve immortality through my work; I want to achieve it through not dying.",
        "I'm not afraid of death; I just don't want to be there when it happens.",
        "Life is full of misery, loneliness, and suffering - and it's all over much too soon.",
        "My analyst told me I'm 100% neurotic, but that's about the lowest he could go.",
        "Don't you see the conflict? I'm a b chip programmer, getting consumed by my inability to live without using external dependencies.",
        "Most of the time, I'm pessimistic, and when it doesn't work out, it's a pleasant surprise."
    ]
    print_box(quote_list[int(random.uniform(0, len(quote_list))).astype(int)])

def rain_animation():
    for i in range(15):
        print(end='\r|PloP' * (80 // 10 * (15 - i)))
        time.sleep(0.1)

def main():
    print_box('''
                                                                            .               .                       .
                  .   .   .                                   .       .                   .    .                 .
                  .    .   . .                               .          .                 .      .
                  .        .                           .                 .            .  .            .
                  .        .  . .                     .                 .          .  .          .
                  .                  .        .  . .    .                      .  .  .        .
                  .                     .                  .         .
                  .                   .                   .     .
                  .                     .                 .  .
                  .                        .             .
                  .                          .     .
                  .                              .
                  .                           .  .
                    .                     .  .
                       .               .   .  .
                  .           .    .       .
                 .        .     .
                     .   .''')
    print_quote()
    rain_animation()
    print("           .                                                   .")
    print_quote()
    print("            .                                                .")
    print_quote()
    print("               .                                            .")
    print_quote()
    print("               .                                        .")
    print_quote()
    print("               .                                     .")
    print_quote()
    print("                                        .")
    print_quote()
    print("                          .")
    print_quote()
    print("                     .")
    print_quote()
    print("                 .")
    print_quote()
    print("                 .")
    print