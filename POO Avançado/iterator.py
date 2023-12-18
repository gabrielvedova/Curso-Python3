#!/usr/bin/python3

class RGB:
    def __init__(self):
        self.cores = ['red', 'blue', 'green'][::-1]

    def __iter__(self):
        return self

    def __next__(self):
        try:
            return self.cores.pop()
        except IndexError:
            raise StopIteration()


if __name__ == '__main__':

    # sem a função __iter__
    cores = RGB()
    print(next(cores))
    print(next(cores))
    print(next(cores))

    try:
        print(next(cores))
    except StopIteration:
        print('Acabou!')

    # com a função __ter__
    for a in RGB():
        print(a)
