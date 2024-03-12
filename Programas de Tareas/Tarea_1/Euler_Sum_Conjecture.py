from math import pow

'''
Este programa busca refutar la conjetura de la suma de Euler, 
que propone que para n y k mayores a 1, si la suma de n-esimos 
enteros positivos elevatos a la k llega a ser un entero positivo 
a la k, entonces n es mayor o igual a k.
Se realizará la demostración mediante el cálculo de un contra 
ejemplo para algún k menor a 6, dónde para un n menor a k se 
cumple la igualdad.
''' 


def main() -> None:
    
    def euler(first_call:bool, k=1, n=1) -> None:
        '''Get all the possible combinations of numbers
        
        between 1 and 'max'.
        '''
        i = n-1
        if n == 1:
            if len(p_ints) > 1:
                for _ in range(p_ints[n], max+1):
                    check_Euler(k, p_ints)
                    p_ints[0]+=1
            return
        elif first_call:
            euler(first_call=True, k=k, n=i)
            p_ints.append(1)
            p_ints[:i] = [p_ints[i]] * i
            
        for _ in range(max): 
            euler(first_call=False, k=k, n=i)
            p_ints[i]+=1
            p_ints[:i] = [p_ints[i]] * i
    
    def disproof(k=4):
        check_Euler(k=k, p_ints=[95800, 217519, 414560])
    
    global counter_ex
    counter_ex = list()
    disproof()
    
    if _k := get_int('Enter exponent k to find other counter example>> '):
        max = 5
        p_ints = [1,]
        euler(first_call=True, k=_k, n=_k-1)


def check_Euler(k: int, p_ints:list) -> None:
        '''Tests for the given exponent k if the coonjecture
        
        stands with the n<k numbers in the 'p_ints' list.
        '''
        sum_ints = sum(map(lambda a_n:pow(a_n,k), p_ints))
        result = pow(sum_ints, (1/k))
        if int(result) == round(result, 10):
            counter_ex.append({f'Exponent: {k}':f'{p_ints} -> {int(result)}'})
        print(p_ints, result)

      
def get_int(prompt: str) -> int:
        n = input(prompt)
        if n.isdigit():
            return int(n)


if __name__ == "__main__":
    main()
    [print(example) for example in counter_ex]