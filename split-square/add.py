"""Produce new square adding two inputs squares.

Two simple squares can be added::

    >>> s1 = 0
    >>> s2 = 1

    >>> add(s1, s2)
    1

A simple square and a split square can be added::

    >>> s1 = 0
    >>> s2 = [1, 0, 1, 0]

    >>> add(s1, s2)
    [1, 0, 1, 0]

Two split squares can be added::

    >>> s1 = [0, 0, 0, 1]
    >>> s2 = [0, 1, 0, 1]

    >>> add(s1, s2)
    [0, 1, 0, 1]

Nested squares can be added::

    >>> s1 = [0, [1, 1, 1, [0, 0, 0, 0]], [0, 0, 0, 0], 1]
    >>> s2 = [1, [1, 0, 1, [0, 0, 1, 1]], [1, 0, 1, 0], 1]

    >>> add(s1, s2)
    [1, [1, 1, 1, [0, 0, 1, 1]], [1, 0, 1, 0], 1]

Unevenly-nested squares can be added::

    >>> s1 = [0, [1, 1, 1, 0           ], [0, 0, 0, 0], 1]
    >>> s2 = [1, [1, 0, 1, [0, 0, 1, 1]], [1, 0, 1, 0], 1]

    >>> add(s1, s2)
    [1, [1, 1, 1, [0, 0, 1, 1]], [1, 0, 1, 0], 1]

    >>> s1 = [0, [1, 1, 1, 1                      ], [0, 0, 0, 0], 1]
    >>> s2 = [1, [1, 0, 1, [0, [0, 0, 0, 0], 1, 1]], [1, 0, 1, 0], 1]

    >>> add(s1, s2)
    [1, [1, 1, 1, [1, [1, 1, 1, 1], 1, 1]], [1, 0, 1, 0], 1]
"""


def add(s1, s2):
    """Produce new split square adding two input squares."""
    # create a solution_list
    # check each position in s1 list for its value, check each position in s2 list for its value
    # if value is a number add the numbers together if sum =2 then push 0 to solution_list else push sum
    # if value is an list push a new list to solution_list and recurse through the list
    def binary_add(n1, n2):
        sum = n1 + n2
        if sum == 2:
            return 1
        else:
            return sum

    def even_structure(num, structure_len):
        new_list = []
        while structure_len > 0:
            new_list.append(num)
            structure_len -= 1
        return new_list

    # if both s1 and s2 are int return binary_add of s1+s2
    if isinstance(s1, int) and isinstance(s2, int):
        return binary_add(s1, s2)

    # if the structures of s1 and s2 are different even the structures and recurse
    if isinstance(s1, int) or isinstance(s2, int):
        if isinstance(s1, list):
            s2 = even_structure(s2, len(s1))
            return add(s1, s2)
        if isinstance(s2, list):
            s1 = even_structure(s1, len(s2))
            return add(s1, s2)

    # current idx structures should be even, begin loop to create solution
    # even structures as needed.
    solution = []
    max_len = max(len(s1), len(s2))
    for idx in range(max_len):
        el1 = s1[idx] if idx < len(s1) else 0
        el2 = s2[idx] if idx < len(s2) else 0
        if isinstance(el1, list) or isinstance(el2, list):
            if not isinstance(el1, list):
                el1 = even_structure(el1, len(el2))
            if not isinstance(el2, list):
                el2 = even_structure(el2, len(el1))
            solution.append(add(el1, el2))
        else:
            solution.append(binary_add(el1, el2))

    return solution


if __name__ == "__main__":
    import doctest
    if doctest.testmod().failed == 0:
        print("***ALL TESTS PASS; YOU'RE A RECURSION WIZARD!")
