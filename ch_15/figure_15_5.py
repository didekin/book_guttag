import random


class Item(object):
    def __init__(self, n, v, w):
        self._name = n
        self._value = v
        self._weight = w

    def get_name(self):
        return self._name

    def get_value(self):
        return self._value

    def get_weight(self):
        return self._weight

    def __str__(self):
        return f'<{self._name}, {self._value}, {self._weight}>'


def max_val(items_to_consider, avail):
    """
    items_to_consider: Those items that nodes higher up in the tree have not yet considered.
    avail: The amount of space still available.
    Returns a tuple of the total value of a solution to the
    0/1 knapsack problem and the items of that solution
    """

    # The search is finished.
    if items_to_consider == [] or avail == 0:
        result = (0, ())
    # Not enough space avaiable for left branch: the inclusion of next item in the pending list.
    elif items_to_consider[0].get_weight() > avail:
        # Explore right branch only RECURSIVELY
        result = max_val(items_to_consider[1:], avail)
    else:
        next_item = items_to_consider[0]
        # Explore left branch RECURSIVELY
        with_val, with_to_take = max_val(items_to_consider[1:],
                                         avail - next_item.get_weight())
        with_val += next_item.get_value()
        with_to_take += (next_item,)
        # Explore right branch RECURSIVELY
        without_val, without_to_take = max_val(items_to_consider[1:], avail)
        # Choose better branch
        if with_val > without_val:
            result = (with_val, with_to_take)
        else:
            result = (without_val, without_to_take)
    return result


def fast_max_val(items_to_consider, avail, memo=None):
    """
    items_to_consider: Those items that nodes higher up in the tree have not yet considered.
    avail: The amount of space still available.
    memo: memoization artifact supplied by recursive calls
    Returns a tuple of the total value of a solution to the
    0/1 knapsack problem and the items of that solution
    """

    if memo is None:
        memo = {}
    # Overlapping subproblems are defined for the same set of items and the same space availability.
    # If the problem is already solved in memo, I extract from there its result.
    if (len(items_to_consider), avail) in memo:
        result = memo[(len(items_to_consider), avail)]
    # Nothing to be done.
    elif items_to_consider == [] or avail == 0:
        result = (0, ())
    # Not enough space avaiable for left branch: the inclusion of next item in the pending list.
    elif items_to_consider[0].get_weight() > avail:
        # Explore right branch only
        result = fast_max_val(items_to_consider[1:], avail, memo)
    else:
        next_item = items_to_consider[0]
        # Explore left branch
        with_val, with_to_take = fast_max_val(items_to_consider[1:],
                                              avail - next_item.get_weight(), memo)
        with_val += next_item.get_value()
        with_to_take += (next_item,)
        # Explore right branch
        without_val, without_to_take = fast_max_val(items_to_consider[1:],
                                                    avail, memo)
        # Choose better branch
        if with_val > without_val:
            result = (with_val, with_to_take)
        else:
            result = (without_val, without_to_take)
    # Once the call to the function returns, I record the result in memo with the actual arguments used.
    # In each level, the length of the list (and the items in it) to be considered is the same in all the nodes.
    memo[(len(items_to_consider), avail)] = result
    return result


def small_test():
    names = ['a', 'b']
    vals = [6, 7]
    weights = [3, 3]
    items = []
    for i in range(len(vals)):
        items.append(Item(names[i], vals[i], weights[i]))
    val, taken = max_val(items, 5)
    for item in taken:
        print(item)
    print('Total value of items taken =', val)


def build_many_items(num_items, maxVal, maxWeight):
    items = []
    for i in range(num_items):
        items.append(Item(str(i),
                          random.randint(1, maxVal),
                          random.randint(1, maxWeight)))
    return items


def big_test(num_items, avail_weight):
    items = build_many_items(num_items, 10, 10)
    val, taken = max_val(items, avail_weight)
    print('Items Taken')
    for item in taken:
        print(item)
    print('Total value of items taken =', val)


# Example usage
small_test()
