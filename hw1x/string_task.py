def make_plural(s):
    if s.endswith(('s', 'sh', 'o')):
        return s + 'es'
    elif s.endswith('y'):
        return s[:-1] + 'ies'
    else:
        return s + 's'


def get_hash_tag(s):
    first_bkt = s.find('{')
    substr = s[first_bkt:]
    if '{' in s and substr.find('}') > 1:
        return s[s.find('{') + 1: substr.find('}') + s.find('{')]
    else:
        return s


def tokenize(s):
    ans = []
    temp = ''
    flag = [0, 0]
    for char in s:
        if flag[0] == 0:
            if char == '<':
                if flag[1] == 0:
                    flag[0] = 1
                else:
                    flag[1] = 0
            elif char == '>':
                flag[1] = 1
            elif char == ' ':
                ans.append(temp)
                temp = ''
            else:
                temp += char
        else:
            if char == '>':
                flag[0] = 0
            else:
                temp += char
    ans.append(temp)
    return ans
