def make_plural(s):
    if s.endswith(('s', 'sh', 'o')):
        return s + 'es'
    elif s.endswith('y'):
        return s[:-1] + 'ies'
    else:
        return s + 's'


def get_hash_tag(s):
    substr = s[s.find('{'):]
    if '{' in s and substr.find('}') > 1:
        return substr[1: substr.find('}')]
    else:
        return s


def tokenize(s):
    ans = []
    temp = ''
    flag = False
    for char in s:
        if char == '<':
            flag = True
        elif char == '>':
            flag = False
        elif char == ' ' and not flag:
            ans.append(temp)
            temp = ''
        else:
            temp += char
    ans.append(temp)
    return ans
