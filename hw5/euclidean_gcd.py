from __future__ import print_function  # Python 2


def euclidean_gcd(start_a, start_b):
    print("\n================================================\n")

    a, b = (start_a, start_b) if start_a > start_b else (start_b, start_a)

    while b > 0:
        # Intermediate gcd reductions
        print(r"gcd({a}, {b}) = gcd({b}, ${a}\bmod{b}$) = gcd({b}, {amodb})"
              .format(a=a, b=b, amodb=a % b), end=' & ')

        # Tableau form
        print("{a} = {q} * {b} + {r}".format(a=a, q=a // b, b=b, r=a % b), end=r' \\'+'\n')
        a, b = b, a % b
    print("gcd({a}, {b}) = {a}".format(a=a, b=b))
    print("\ngcd({a}, {b}) = {result}".format(a=start_a, b=start_b, result=a))


def main():
    euclidean_gcd(44, 180)
    euclidean_gcd(340, 178)
    euclidean_gcd(2 ** 32 - 1, 2 ** 0 - 1)


if __name__ == '__main__':
    main()
