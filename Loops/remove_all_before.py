# Remove all before:

# Not all of the elements are important. What you need to do here is to remove
# from the list all of the elements before the given one.

# example
# For the illustration we have a list [3, 4, 5] and we need to remove
# all elements that go before 3 - which is 1 and 2.
# We have two edge cases here: (1) if a cutting element cannot be found,
# then the list shoudn't be changed. (2) if the list is empty, then it should remain empty.

# Input: List and the border element.
# Output: Iterable (tuple, list, iterator ...).


def remove_all_before(items, border):
    # if border not in items:
    #     return items
    # else:
    #     x = items.index(border)
    #     return items[x:]
    # ======================================
    if border in items:
        x = items.index(border)
        return items[x:]
    else:
        return items


# =======================================
# try:
#     x = items.index(border)
#     return items[x:]
# except:
#     return items

# These "asserts" are used for self-checking and not for an auto-testing
print(remove_all_before([1, 1, 2, 2, 3, 3], 2))  # == [2, 2, 3, 3]
print(remove_all_before([1, 2, 3, 4, 5], 3))  # == [3, 4, 5]
print(remove_all_before([1, 1, 2, 4, 2, 3, 4], 2))  # == [2, 4, 2, 3, 4]
print(remove_all_before([1, 1, 5, 6, 7], 2))  # == [1, 1, 5, 6, 7]
print(remove_all_before([], 0)) == []
print(
    remove_all_before([7, 7, 7, 7, 7, 7, 7, 7, 7], 7)
)  # == [7, 7, 7, 7, 7, 7, 7, 7, 7]
