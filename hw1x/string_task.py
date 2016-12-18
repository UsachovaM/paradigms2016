def make_plural(s):
    if s.endswith('s') or s.endswith('sh') or s.endswith('o'):
        return s + 'es'
    elif s.endswith('y'):
        return s[:-1] + 'ies'
    else:
        return s + 's'


def get_hash_tag(s):
    i = s.find('{')
    j = s.find('}')
    if i != -1 and i < j:
        return s[i + 1:j]
    else:
        return s


def tokenize(s):
    ans = []
    while s != '':
        if s[0] == ' ':
            if len(s) == 1:
                ans.append('')
            if len(s) >= 2 and s[1] == ' ':
                ans.append('')
            s = s[1:]
        else:
            i = s.find(' ')
            temp = s[:i]
            s = s[i:]
            if temp.find('<') != -1 and temp.find('>') == -1:
                temp = temp[:temp.find('<')] + temp[temp.find('<') + 1:]
                temp = temp + s[:s.find('>')]
                s = s[s.find('>'):]
                if s.find(' ') != -1:
                    temp = temp + s[1:s.find(' ')]
                    s = s[s.find(' '):]
                else:
                    temp = temp + s[1:]
            ans.append(temp)
    return ans
