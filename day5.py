# Comparing Nested Dictionaries
def compare_nested_dicts(d1, d2):
    if type(d1) != type(d2):
        return False

    if isinstance(d1, dict):
        if set(d1.keys()) != set(d2.keys()):
            return False
        for key in d1:
            if not compare_nested_dicts(d1[key], d2[key]):
                return False
        return True

    # For non-dict values
    return d1 == d2

# Test Case 1: Simple equal dictionaries
d1 = {'a': 1, 'b': 2}
d2 = {'a': 1, 'b': 2}
print(compare_nested_dicts(d1, d2))   # True

# Test Case 2: Simple unequal dictionaries
d3 = {'a': 1, 'b': 3}
print(compare_nested_dicts(d1, d3))   # False

# Test Case 3: Nested equal
d4 = {'a': 1, 'b': {'x': 10, 'y': 20}}
d5 = {'a': 1, 'b': {'x': 10, 'y': 20}}
print(compare_nested_dicts(d4, d5))   # True

# Test Case 4: Nested unequal
d6 = {'a': 1, 'b': {'x': 10, 'y': 21}}
print(compare_nested_dicts(d4, d6))   # False

# Test Case 5: Different structure
d7 = {'a': 1, 'b': {'x': 10}}
print(compare_nested_dicts(d4, d7))   # False
