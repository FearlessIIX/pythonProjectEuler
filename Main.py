import math


def main():
    euler12()


# Euler 12
def euler12():
    current_tri = 1
    tri_factor = 2
    tri_div_size = 0

    while tri_div_size < 500:

        tri_div_size = fdc(current_tri) * 2
        if tri_div_size >= 500:
            break
        current_tri += tri_factor
        tri_factor += 1

    print(current_tri)


def fdc(num):
    div_count = 0
    for div in range(1, int(math.sqrt(num) + 1)):
        if num % div == 0:
            div_count += 1
    return div_count


if __name__ == "__main__":
    main()
