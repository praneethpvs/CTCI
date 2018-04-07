def count(ip_list):
    op_dict = {}
    for val in ip_list:
        if val in op_dict.keys():
            op_dict[val] += 1
        else:
            op_dict[val] = 1
    return op_dict


def ransom_note(magazine, ransom):
    flag = 0
    magazine_dict = count(magazine)
    ransom_dict = count(ransom)
    for key in ransom_dict:
        if key in magazine_dict.keys():
            ransom_dict[key] -= magazine_dict[key]
    ransom_values = list(ransom_dict.values())
    ransom_values = sorted(ransom_values, key=ransom_values.index, reverse=True)
    for val in ransom_values:
        if val > 0:
            flag = 1
            break

    if flag == 0:
        return "Yes"


m, n = map(int, raw_input().strip().split(' '))
if 1 <= m <= 30000 and 1 <= n <= 30000:
    magazine = raw_input().strip().split(' ')
    ransom = raw_input().strip().split(' ')
    for word in magazine:
        if not 1 <= len(word) <= 5:
            exit()
    for word in ransom:
        if not 1 <= len(word) <= 5:
            exit()
    answer = ransom_note(magazine, ransom)
    if (answer):
        print "Yes"
    else:
        print "No"
