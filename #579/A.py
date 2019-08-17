def query(permutation: list, n: int) -> bool:
    if n == 1:
        return True

    i = permutation.index(1)
    right = permutation[i:] + permutation[:i]
    left = permutation[i - n::-1] + permutation[:i - n:-1]

    if right[1] == 2:
        for index in range(2, n):
            if right[index] != right[index - 1] + 1:
                return False
        return True
    elif left[1] == 2:
        for index in range(2, n):
            if left[index] != left[index - 1] + 1:
                return False
        return True
    else:
        return False


if __name__ == '__main__':
    q = int(input())
    for i in range(q):
        n = int(input())
        permutation = [int(item) for item in input().split()]
        if query(permutation, n):
            print('YES')
        else:
            print('NO')
