def average(lst):
    return sum(lst)/len(lst)


def averages_row(mat):
    return [average(x) for x in mat]


def find_min_pos(mat):
    mat_mins = [(min(row), row.index(min(row))) for row in mat]
    min_value = min(mat_mins, key=lambda x: x[0])
    return (mat_mins.index(min_value),
            min_value[1])


def unique(lst):
    ans = []
    el = set()
    for x in lst:
        if x not in el:
            el.add(x)
            ans.append(x)
    return ans
