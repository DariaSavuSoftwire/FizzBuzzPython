

# Am reguli pentru: 3 5 7 11 13 17
# Voi pastra outputul intr-o variabila
def fizzBuzz(maxRange):
    for number in range(1,maxRange):
        #Ma ocup prima data de multipli de 11
        if number%(11*13*17)==0:
            print("BongFezz")
            continue
        elif number%(11*13)==0:
            print("FezzBong")
            continue
        elif number%11==0:
            #Si in cazul unui multiplu de 11*17 functioneaza deoarece printez doar o valoare
            print("Bong")
            continue

        result =""
        if number%3==0:
            result="Buzz,"+result
        if number%7==0:
            result=result+"Bang,"
        if number%13==0:
            result = "Fezz,"+result
        if number%5==0:
            result="Fizz,"+result
        parts=result.split(",")
        if(number%17==0):
            parts.reverse()
        result="".join(parts)
        if result=="":
            print(number)
        else:
            print(result)



if __name__ == '__main__':
    print("Alegeti un numar natural pana la care sa mearga jocul:")
    while True:
        try:
            number=int(input())
            fizzBuzz(number)
            break
        except ValueError:
            print("Te rog introdu un numar natural")