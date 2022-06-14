#Decimal to Binary Converter

def converttobinary():
    Num = int(input('Enter Decimal Number:'))
    print('Converting Decimal to Binary')
    print('Binary Number:')
    return bin(Num).replace("0b","")


print('\n')
def binarytodecimal():
    B2D = int(input('Enter Binary Number:'))
    print('Converting Binary to Decimal')
    print('Decimal Number:')
    Convert = str(B2D)
    converted_n = int(Convert,2)
    print(converted_n)


# Driver code
if __name__ == '__main__':
    print(converttobinary())
    print(binarytodecimal())
