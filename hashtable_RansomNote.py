from collections import Counter
from collections import OrderedDict


# def count(ip_list):
#     op_dict = {}
#     for val in ip_list:
#         if 1 <= len(val) <= 5:
#             if val in op_dict.keys():
#                 op_dict[val] += 1
#             else:
#                 op_dict[val] = 1
#         else:
#             exit()
#     return op_dict

def ransom_note(magazine, ransom):
    flag = 0
    # magazine_dict = count(magazine)
    # ransom_dict = count(ransom)
    magazine_dict = OrderedDict(sorted(Counter(magazine).items()))
    ransom_dict = OrderedDict(sorted(Counter(ransom).items()))
    cmp_op = cmp(magazine_dict, ransom_dict)
    if cmp_op != 0:
        for key in ransom_dict:
            if key in magazine_dict.keys():
                if ransom_dict[key] > magazine_dict[key]:
                    flag = 1
                    break
            else:
                flag = 1
                break
    if flag == 0:
        return "Yes"


m, n = map(int, raw_input().strip().split(' '))
if 1 <= m <= 30000 and 1 <= n <= 30000:
    magazine = raw_input().strip().split(' ')
    ransom = raw_input().strip().split(' ')
    answer = ransom_note(magazine, ransom)
    if answer:
        print "Yes"
    else:
        print "No"
