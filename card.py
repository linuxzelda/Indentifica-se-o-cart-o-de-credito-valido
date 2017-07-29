# -*- coding: latin1 -*-
# -*- coding: utf-8 -*-


def lunh(card):    
    len_card = len(card)
    odd_sum = 0
    even_sum = 0

    if len_card == 0:
        return 0

    else:

        if (len_card % 2 == 0):
            last_num = int(card[-1])
            even_sum += last_num

            return even_sum + my_lunh(card[:-1])
        else:

            last_num = int(card[-1])
            last_num = 2 * last_num
            part_sum = last_num // 10 + last_num % 10
            odd_sum += part_sum
            return odd_sum + my_lunh(card[:-1])

def my_test():
    while True:

        card = input("Informe os 16 Numeros Do CartAo: ")

        total = my_lunh(card)

        if total % 10 == 0:
            print("[-] 'Cartao' È Valido! ")
        else:
            print("[+] 'O Cartao' È Invalido!! ")

        new = input("Deseja Testar novamente? (s)/(n): ")
        if new == 's':
            my_test()
        elif new == 'n':
            break
        else:
            print("Comando invalido")

if __name__ == '__main__':
    my_test()