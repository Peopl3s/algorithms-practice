def gcd(a: int, b: int) -> int:
    while a > 0 and b > 0:
        if a >= b:
            a = a % b
        else:
            b = b % a
    return max(a, b)


def lcm(a: int, b: int) -> int:
    return (a * b) // gcd(a, b)


if __name__ == '__main__':
    a, b = list(map(int, input().split()))
    print(lcm(a, b))