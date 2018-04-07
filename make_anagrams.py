def number_needed(a, b):
    dd_a = [0] * 26
    dd_b = [0] * 26
    deletions = 0
    for char in a:
        dd_a[ord(char) - ord('a')] = dd_a[ord(char) - ord('a')] + 1

    for char in b:
        dd_b[ord(char) - ord('a')] = dd_b[ord(char) - ord('a')] + 1

    for i in range(26):
        deletions += abs(int(dd_a[i] - dd_b[i]))
        i += 1
    return deletions


if __name__ == "__main__":
    a = raw_input("Enter string 1: ").strip()
    b = raw_input("Enter string 2: ").strip()
    print "Number of characters to be deleted to make the two strings anagrams: {}".format(number_needed(a, b))
