def bai1(arr):
    min = arr[0]
    for i in range (len(arr)):
        if arr[i] < min:
            min = arr[i]
    return min
print (bai1([2,4]))


def bai2(arr):
    min = arr[0]
    sum = 0
    for i in range (len(arr)):
        sum = min + arr[0+1]
    return sum
print(bai2([2,4]))

def bai4(x):
  return x[::-1]
print(bai4("hello world"))
