def negative_number(nums):
    negative = 0
    for i in nums:
        if i < 0:
            negative += 1
    return negative

print(negative_number([0,1,-1,2, -4, -1, -4, -2, 1]))

def positive_number(nums):
    positive = 0
    for i in nums:
        if i >= 0:
            positive += 1
    return positive

print(positive_number([0,1,-1,2, -4, -1, -4, -2, 1]))