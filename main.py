
def fizzBuzz():
    results=list(map(lambda number:int(number%5==0)*'Fizz'+int(number%3==0)*'Buzz' or number,range(1,101)))
    print(results)

if __name__ == '__main__':
    fizzBuzz()