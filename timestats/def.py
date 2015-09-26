from sys import argv

def validate_operand(input, function_name):
    if not isinstance(input, list): 
        raise TypeError('unsupported operand for %s, requires list of datetimes: %r is %s' %
         (function_name, input, type(input)))
    if not len(input) > 0:
        raise ValueError('list for %s has zero len: %r' % (function_name, input))

def validate_result(index, result, function_name):
    if not isinstance(result, int):
        raise TypeError('unsupported type in operand[%d] for %s: %r is %s' %
         (index, function_name, result, type(result)))

def foo(input):
    return input[0]


test_set=[]

test_set.append([1, 2, 3])
test_set.append( ['abc', 'xyz'] )
empty = []
test_set.append(empty)
test_set.append(1)
test_set.append('abc')
test_set.append('a')
test_set.append(2.0)
test_set.append((1,2,3))
h = set()
for elem in range(3):
    h.add(elem)
test_set.append(h)
"""
for elem in test_set:
    print "\n\nTesting %s:" % type(elem), elem
    try:
        print foo(elem)
    except Exception as e:
        print e.type, ":", e

"""

test_case = int(argv[1])

z = test_set[test_case]
validate_operand(z, "foo")
ans = foo(z)
validate_result(0, ans, "foo")
print z