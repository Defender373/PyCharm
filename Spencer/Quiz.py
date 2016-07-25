import operator


def dotProduct(listA, listB):
    '''
    listA: a list of numbers
    listB: a list of numbers of the same length as listA
    '''
    # Your code here

    return sum(map(operator.mul, listA, listB))


def test(a, b):
    return a + b


def dict_interdiff(f, d1, d2):
    '''
    d1, d2: dicts whose keys and values are integers
    Returns a tuple of dictionaries according to the instructions above

    '''
    set1 = set(d1.keys())
    set2 = set(d2.keys())

    return (dict((x, f(d1[x], d2[x])) for x in set1.intersection(set2)),
            dict((x, d1[x] if x in set1 else d2[x]) for x in set1.difference(set2).union(set2.difference(set1))))


d1 = {1: 30, 2: 20, 3: 30, 5: 80}
d2 = {1: 40, 2: 50, 3: 60, 4: 70, 6: 90}

l1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
l2 = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]

print([x * 2 for x in range(50)])
