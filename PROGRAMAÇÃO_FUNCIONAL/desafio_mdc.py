#!/usr/bin/python3
def mdc(lista):
    def calc(divisor):
        return divisor if sum(map(lambda x: x % divisor, lista)) == 0 \
            else calc(divisor - 1)
    return calc(min(lista))


if __name__ == '__main__':
    print(mdc([21, 7])) # 7
    print(mdc([125, 40])) # 5
    print(mdc([9, 564, 3, 66])) # 3
    print(mdc([9, 7])) # 1
