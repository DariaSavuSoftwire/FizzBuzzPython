
def fizzBuzz():
    for number in range(1,100):
        result=''
        if number%5==0:
            result+="Fizz"
        if number%3==0:
            result+="Buzz"
        print(number if result=='' else result)

if __name__ == '__main__':
    fizzBuzz()