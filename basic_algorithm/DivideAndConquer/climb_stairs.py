def climb(n):
    if n<=2:
       return n
    else:
        return climb(n-1)+climb(n-2)

if __name__ == '__main__':
    print(climb(7))