def print_row(size, star_count):
    for row in range(size - star_count):
        print(" ", end="")
    for row in range(1, star_count):
        print("*", end=" ")
    print("*")


def print_rhombus(n: int):
    for i in range(1, n + 1):
        print_row(n, i)
    for i in range(n - 1, 0, -1):
        print_row(n, i)


n = int(input())
print_rhombus(n)