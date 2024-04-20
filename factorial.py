#We are about to write a function that calculates the factorial of a number

def factorial(n):
    if n==0:
        return 1
    else:
        return n*factorial(n-1)

print("Digite um número natural\n")


N=int(input())

print(f'O fatorial de {N} é {factorial(N)}')
