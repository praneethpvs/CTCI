# CTCI
from pprint import pprint


class UndefinedArrayLength(Exception):
    def __init__(self, ipstr):
        self.ipstr = ipstr


class UndefinedRotationNo(Exception):
    def __init__(self, ipstr):
        self.ipstr = ipstr


def array_left_rotation(a, n):
    k = len(a)
    try:
        if 1 <= k <= 100000 and 1 <= n <= k:
            s = n % k
            shifted_array = a[s:] + a[:s]
            return shifted_array
        elif k < 1 or k > 100000:
            raise UndefinedArrayLength("Length of array not in mentioned limits.")
        elif n < 1 or n > k:
            raise UndefinedRotationNo("Number of rotation times is not within the specified limit.")
    except UndefinedArrayLength as err:
        print err.ipstr
    except UndefinedRotationNo as err:
        print err.ipstr


if __name__ == "__main__":
    list_a = map(int, raw_input("Enter list elements separated by space in a single line: ").strip().split(' '))
    k_times = int(raw_input("Enter the no.of left rotations to be performed: "))
    try:
        print "input list: {}".format(list_a)
        answer = array_left_rotation(list_a, k_times)
        op_list = ' '.join(map(str, answer))
        print "List after performing {} left rotations : {}".format(k_times, op_list)
    except Exception as e:
        print e
