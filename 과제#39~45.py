#과제39
def result(n):
    nums = [i for i in range(n + 1) if i == 0 or i % 2 != 0]
    print(nums)

a = int(input("양수 입력: "))
result(a)

#과제40
def result(n):
    if n % 3 == 0 and n != 0:
        print(n)

a = int(input("숫자 입력: "))
result(a)

#과제41
def result(nums):
    return max(nums), min(nums)

scores = list(map(int, input("숫자 4개 입력: ").split()))
maximum, minimum = result(scores)

print("최댓값:", maximum)
print("최솟값:", minimum)

#과제42
def result(n):
    nums = [i for i in range(n + 1) if i == 0 or i % 2 != 0]
    print(nums)

a = int(input("양수 입력: "))


#과제43
def factorial(n):
    result = 1
    for i in range(1,n+1):
        result *= i
    return result

a = int(input("0이상 정수 입력: "))
print(f"{a}! = {factorial(a)}")

#과제44
def result(i, j):
    nums = [x * y for x in range(2, i+1) for y in range(2, j+1) if x * y >= 30]
    return sum(nums)

i, j = map(int, input("2이상 9이하 양수 2개 입력: ").split())
print("i와 j의 곱이 30 이상인 경우의 총합 =", result(i, j))

#과제45
def result(a):
    return sum(a)   

a = [1, 2, 3, 4, 5]
print("총합 =", result(a))