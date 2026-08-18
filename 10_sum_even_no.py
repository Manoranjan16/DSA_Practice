def sum_even_number(nums):
    even = 0
    for i in nums:
        if i % 2 == 0:
            even += i
    return even
def sum_odd_number(nums):
    odd = 0
    for i in nums:
        if i % 2 != 0:
            odd += i
    return odd
def sum_total_number(nums):
    total = 0
    for i in nums:
        total += i
    return total

nums = [1,2,3,4,5,6]
print(sum_even_number(nums=nums))
print(sum_odd_number(nums=nums))
print(sum_total_number(nums=nums))