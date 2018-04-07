# CTCI


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


def array_right_rotation(a, n):
    k = len(a)
    try:
        if 1 <= k <= 100000 and 1 <= n <= k:
            s = (n % k) * -1
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
    k_times = int(raw_input("Enter the no.of rotations to be performed: "))
    print("For left rotation enter   --> 1")
    print("For right rotation enter  --> 2")
    try:
        left_right = int(raw_input("Do you want to perform left rotation or right rotation: ").strip())
        if left_right not in [1, 2]:
            raise TypeError
        else:
            print "input list: {}".format(list_a)
            if left_right == 1:
                answer = array_left_rotation(list_a, k_times)
                op_list = ' '.join(map(str, answer))
                print "List after performing {} left rotations : {}".format(k_times, op_list)
            if left_right == 2:
                answer = array_right_rotation(list_a, k_times)
                op_list = ' '.join(map(str, answer))
                print "List after performing {} right rotations : {}".format(k_times, op_list)
    except TypeError as err:
        print err
    except Exception as e:
        print e
