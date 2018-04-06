# CTCI
def array_left_rotation(a, n, k):
    output = [None] * n
    try:
        if 1 <= n <= 100000 and 1 <= k <= n:
            old_pos = 0
            for i in range(len(a)):
                if i == 0:
                    new_pos = (n + i) % k
                    if new_pos >= len(a):
                        new_pos -= 1
                    output[new_pos] = a[i]
                else:
                    new_pos = (n + i) % k
                    if new_pos <= old_pos:
                        new_pos += k
                    if new_pos >= len(a):
                        new_pos -= len(a)
                    old_pos = new_pos
                    output[new_pos] = a[i]
                i += 1
            return output
    except Exception as e:
        print e


n, k = map(int, raw_input().strip().split(' '))
a = map(int, raw_input().strip().split(' '))
answer = array_left_rotation(a, n, k);
print ' '.join(map(str, answer))
