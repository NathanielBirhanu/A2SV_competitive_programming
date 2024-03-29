def insertionSort1(n, arr):
    key = arr[-1]
    j = n - 2

    while j >= 0 and arr[j] > key:
        arr[j + 1] = arr[j]
        print(" ".join(map(str, arr)))  # Print interim array
        j -= 1

    arr[j + 1] = key
    print(" ".join(map(str, arr)))  # Print final array

if __name__ == '__main__':
    n = int(input().strip())
    arr = list(map(int, input().rstrip().split()))
    insertionSort1(n, arr)
