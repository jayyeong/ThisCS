def Fibo(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return Fibo(n - 1) + Fibo(n - 2)

def main():
    N = int(input())
    print(Fibo(N))

main()