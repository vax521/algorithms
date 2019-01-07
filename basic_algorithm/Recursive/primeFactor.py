result = []
def PrimeFactor(n):
    for i in range(2,int(n/2+1)):
        if n % i == 0:
            result.append(i)
            return PrimeFactor(n/i)
    result.append(int(n))


if __name__ == '__main__':
   PrimeFactor(90)
   print("90的质因数：",result)
