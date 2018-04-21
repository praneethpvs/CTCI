class Stack:
    def __init__(self):
        self.items = []

    def isEmpty(self):
        return self.items == []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        return self.items.pop()

    def peek(self):
        return self.items[len(self.items) - 1]

    def size(self):
        return len(self.items)


def is_matched(exp):
    brackets_match = {
        ")": "(",
        "}": "{",
        "]": "[",
        ">": "<"
    }
    track_braces = Stack()
    if len(exp) % 2 != 0 or exp is None:
        return False
    else:
        for val in exp:
            if val in brackets_match.values():
                track_braces.push(val)
            elif val in brackets_match.keys():
                if track_braces.isEmpty():
                    return False
                elif brackets_match[val] != track_braces.peek():
                    return False
                else:
                    track_braces.pop()
            else:
                return False
        else:
            if track_braces.isEmpty():
                return True
            else:
                return False


t = int(raw_input().strip())
for a0 in xrange(t):
    expression = raw_input().strip()
    if is_matched(expression):
        print "YES"
    else:
        print "NO"
