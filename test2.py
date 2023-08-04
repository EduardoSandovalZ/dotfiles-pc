#cada multiplo de 3 imprimos fizz
#cada multiplo de 5 imprimimos buzz
#cada que sea multiplo de 3 y 5 imprimimos fizzbuzz

def fizzbuzz():
    for i in range (1,101):
        if i % 3 == 0 and i % 5 == 0:
            print('fizzbuzz')
        elif i % 3 == 0 :
            print('fizz')
        elif i % 5 == 0:
            print('buzz')
        else:
            print(i)



fizzbuzz()
