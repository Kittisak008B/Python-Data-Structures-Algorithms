# call stack
def funcThree() :
    print(3)
def funcTwo() :
    funcThree()
    print(2)
def funcOne() :
    funcTwo()
    print(1)
  
print(funcOne())

# factorial
def factorial(n) :
    if n ==1 :
        return 1 
    return n * factorial(n-1)

print(factorial(4))

