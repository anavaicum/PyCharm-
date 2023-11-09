def find_str(target, source):
    for i in range(len(target) - len(source) + 1):
        cnt = 0
        j = i
        for idx in range(len(source)):
            if target[j] == source[idx]:
                cnt += 1
            j += 1
        if cnt == len(source):
            return i
    return -1
def find_str_better(target, source):
    for i in range(len(target) - len(source) + 1):
        if target[i:i+len(source)] == source:
            return i
    return -1
def find_str_even_better(target, source):
    position = -1
    j = 0 #index for source
    for i in range(len(target)):
        if target[i] != source[j]:
            j = 0
            position = -1
        if target[i] == source[j]:
            if j == 0:
                position = i
        if j >= len(source) - 1:
            break
        else:
            j += 1
    return position
def find_sum(numbers, sum):
    for i in range(len(numbers) - 1):
       if sum - numbers[i] in numbers:
           return True
    return False
def generate_multiple(number, count):
    multi = [number]
    for i in range(2, count + 1):
        multi.append(number*i)
    return multi
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
def reverse(word):
    vok = 'aeiou'
    vok_in_word = []
    new_word = ''
    for ch in word:
        if ch in vok:
            vok_in_word.append(ch)
    i = 1
    for ch in word:
        if ch not in vok:
            new_word += ch
        else:
            new_word += vok_in_word[-i]
            i += 1
    return new_word
def test_reverse():
    assert reverse('Terminator') == 'Tormaniter'
def test_big_sum():
    assert big_sum('123', '123') == '246'
    assert big_sum('123', '129') == '252'
    assert big_sum('999', '101') == '1100'
def test_generate():
    assert generate_multiple(3, 4) == [3, 6, 9, 12]
    assert generate_multiple(2, 2) == [2, 4]
def test_find_sum():
    assert find_sum([1, 2, 9], 3) == True
    assert find_sum([1, 2, 9], 12) == False
def test_find_str_even_better():
    assert find_str_even_better('string', 'ing') == 3
    assert find_str_even_better('stiring', 'ing') == 4
    assert find_str_even_better('string', 'ffr') == -1
def test_find_str_better():
    assert find_str_better('string', 'ing') == 3
    assert find_str_better('string', 'ffr') == -1
def test_find_str():
    assert find_str('string', 'ing') == 3
    assert find_str('string', 'ffr') == -1
def main():
    pass
test_find_str()
test_find_str_better()
test_find_str_even_better()
test_find_sum()
test_generate()
test_big_sum()
test_reverse()
main()
"""
123
023
a, b = b, a
>>> s = '123'
>>> x = 2
>>> s = '0'*x+s
>>> s
'00123'
>>> 
"""
