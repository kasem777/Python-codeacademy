#  Slice Of Pie

# Create a function that determines whether or not it's possible to split a pie fairly given these three parameters:

# Total number of slices.
# Number of recipients.
# How many slices each person gets.
# The function will be in this form:

# equal_slices(total slices, no. recipients, slices each)


def equal_slices(num1, num2, num3):
    if num2 == 0:
        return True
    else:
        if (num3 * num2) <= num1:
            return True
        else:
            return False


print(equal_slices(11, 5, 2))  # ➞ True
# 5 people x 2 slices each = 10 slices < 11 slices

print(equal_slices(11, 5, 3))  # ➞ False
# 5 people x 3 slices each = 15 slices > 11 slices

print(equal_slices(8, 3, 2))  # ➞ True

print(equal_slices(8, 3, 3))  # ➞ False

print(equal_slices(24, 12, 2))  # ➞ True

