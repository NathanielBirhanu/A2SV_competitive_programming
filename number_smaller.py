n, k = map(int, input().split())
arr1 = list(map(int, input().split()))
arr2 = list(map(int, input().split()))
l = 0
m = 0
ans=[]
while l < len(arr1) and m < len(arr2):
    if arr2[m] < arr1[l]:
        ans.append(arr2[m])
        m += 1
    else:
        ans.append(arr1[l])
        l += 1
ans.extend(arr1[l:])
ans.extend(arr2[m:])
print(*ans)




