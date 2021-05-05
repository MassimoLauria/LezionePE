
def ifib(n):
    if n<=0:
        return 0
    elif n==1:
        return 1
    
    old, cur = 0,1
    for i in range(2,n+1):
        old , cur = cur, cur+old
    return cur


def rfib(n):
    if n<=0:
        return 0
    elif n==1:
        return 1
    
    return rfib(n-1)+rfib(n-2)



if __name__ == '__main__':
    print("Eseguito direttamente nel sorgente fib.py")
    print("Eseguo fib iterativo per n=100: ", end='')
    print(ifib(100))
    print("Eseguo fib ricorsivo per n=20: ", end='')
    print(rfib(20))
    
