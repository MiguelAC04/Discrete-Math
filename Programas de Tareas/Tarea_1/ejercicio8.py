from math import pow

def main() -> None:
    a = 95_800
    b = 217_519
    c = 414_560
    d = 422_481

    res_1 = pow(a, 4) + pow(b,4) + pow(c,4)
    res_2 = pow(d,4)

    if res_1 == res_2:
        print("Equal:")
    else:
        print("Different:")
    
    print(f'\t{res_1}\n\t{res_2}')


main()