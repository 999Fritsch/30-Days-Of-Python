from math import sqrt

def find_euclidian_distance(p, q):
    first = p[0] - q[0]
    first = first ** 2

    second = p[1] - q[1]
    second **= 2

    return sqrt(first + second)

if __name__ == "__main__":
    print(find_euclidian_distance((2,3), (10,8)))