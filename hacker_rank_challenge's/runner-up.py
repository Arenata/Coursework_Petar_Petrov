if __name__ == '__main__':
    a = int(input())
    arr = list(map(int, input().split()))
    b = max(arr)
    i=0
    while(i<a):
        if b ==max(arr):
            arr.remove(max(arr))
        i+=1
print(max(arr))


#Made By Petar Petrov