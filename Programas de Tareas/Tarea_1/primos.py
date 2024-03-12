from sys import argv
from math import sqrt
from typing import Generator

class Prime_Num(int):
    def __new__(cls, *, value: int, nth: int):
        num = super().__new__(cls, value)
        num.n = nth
        return  num
    
    def __add__(self, other: int):
        res = super(Prime_Num, self).__add__(other)
        return self.__class__(value=res, nth=self.n)

    def __divmod__(self, value: int) -> tuple[int, int]:
        return super().__divmod__(value)
    
    def __pow__(self, pow):
        return super().__pow__(pow)


def is_Prime(n: int)-> bool:
        '''
            Checks if n is prime.
        '''
        for i in range(2, int(sqrt(n))):
            if n % i == 0:
                return False
        else:
            return True


def nth_Prime(n: int) -> Prime_Num:
        '''
            Finds the nth prime number.
        '''
        num = Prime_Num(value=2, nth=1)
        while True:
            num+=1
            if is_Prime(num):
                num.n+=1
                if num.n == n:
                    return num
    

def find_Primes(a: int, b: int) -> Generator[int, None, int]:
    '''
        Return primes between a and b.
    '''
    for n in range(a+1, b):
        if is_Prime(n):
            yield n       


def main() -> None:
    try: 
        n = argv[1]  
    except IndexError:
        n = input('n>> ')
    finally:
        if n.isdigit() and not n == '1':
            n = int(n)
            p1, p2 = nth_Prime(n), nth_Prime(n+1)
            
            print(f"Your primes are: {p1}->{p2} ; {p1**2}->{p2**2}")
            
            primes = list()
            
            for prime in find_Primes(p1**2, p2**2):
                primes.append(prime)
            
            sumarize = lambda p_list: print("Proof:", *p_list[:4])
            
            print("List:", *primes) if 3<len(primes)<10 else sumarize(primes)


if __name__ == "__main__":             
    main()
