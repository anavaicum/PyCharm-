def big_sum(a, b):
    s = 0
    t = 0
    p = 1
    for i in range(len(a) - 1, -1, -1):
        sum = int(a[i]) + int(b[i]) + t
        # if sum > 9:
        #     t = 1
        # else:
        #     t = 0
        t = 1 if sum > 9 else 0
        s = p*(sum % 10) + s
        p *= 10
    if t == 1:
        s = p + s
    return str(s)

def test_big_sum():
    assert big_sum('123', '123') == '246'
    assert big_sum('123', '129') == '252'
    assert big_sum('999', '101') == '1100'

test_big_sum()