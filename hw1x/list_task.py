def average(lst):
    i = 0
    sum = 0
    while i < len(lst):
        sum += lst[i]
        i += 1
    return sum/len(lst)


def averages_row(mat):
    i = 0
    ans = []
    while i < len(mat):
        ans.append(average(mat[i]))
        i += 1
    return ans


def find_min_pos(mat):
    min_r = 0
    min_c = 0
    i = 0
    while i < len(mat):
        j = 0
        while j < len(mat[i]):
            if mat[i][j] < mat[min_r][min_c]:
                min_r = i
                min_c = j
            j += 1
        i += 1
    return (min_r, min_c)


def unique(lst):
    i = 0
    ans = []
    while i < len(lst):
        j = 0
        f = True
        while j < len(ans):
            if lst[i] == ans[j]:
                f = False
            j += 1
        if f:
            ans.append(lst[i])
        i += 1
    return ans
