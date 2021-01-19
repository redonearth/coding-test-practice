# 알고리즘1: 1부터 n까지의 합을 구하는 알고리즘1
# 입력 n에 따라 덧셈을 n번 수행(반복문)
# 시간 복잡도: O(n)
def sum_all_01(n):
    total = 0
    for num in range(1, n + 1):
        total += num
    return total


print(sum_all_01(100))


# 알고리즘2: 1부터 n까지의 합을 구하는 알고리즘2
# 입력 n이 어떻든 간에, 곱셈/덧셈/나눗셈 하면 됨(반복문 없음)
# 시간 복잡도: O(1)
def sum_all_02(n):
    return int(n * (n + 1) / 2)


print(sum_all_02(100))
