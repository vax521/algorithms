import sys
sys.setrecursionlimit(1000000000)

def partition(seq):
    pi = seq[0]
    lo = [i for i in seq[1:] if i <= pi] 
    hi = [i for i in seq[1:] if i > pi]
    return lo, pi, hi

def quicksort(seq):
    if len(seq)<=1: return seq
    lo,pi,hi = partition(seq)
    print(pi)
    return quicksort(lo)+[pi]+quicksort(hi)

if __name__ == '__main__':
    arr1 = [1,2,3,7,8,9,6,4,3,6,78,7,5,6,87,9,55655,44,4454]
    print(quicksort(arr1))

    
