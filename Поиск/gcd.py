def gcd(a: int, b: int) -> int:
    while a > 0 and b > 0:
        if a >= b:
            a = a % b
        else:
            b = b % a
    return max(a, b)


def gcd_recursive(a: int, b: int) -> int:
    if a == 0 or b == 0:
        return max(a, b)
    return gcd_recursive(b, a % b)


if __name__ == '__main__':
    a, b = list(map(int, input().split()))
    print(gcd(a, b))
    print(gcd_recursive(a, b))