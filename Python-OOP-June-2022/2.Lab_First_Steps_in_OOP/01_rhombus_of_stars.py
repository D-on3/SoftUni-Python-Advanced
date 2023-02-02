def get_line(i, n, char='*'):
    spaces_count = n - 1 - i
    stars_count = i + 1
    return ' ' * spaces_count + (f'{char} ' * stars_count).strip()


def print_rhombus(n):
    for i in range(n):
        print(get_line(i, n,'*'))
    for i in range(n-2, -1, -1):
        print(get_line(i, n))


n = int(input())
print_rhombus(n)
