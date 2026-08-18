def count_even_number(nums):
    even_number = 0
    for num in nums:
        if num % 2 == 0:
            even_number += 1
            
    return even_number

print(count_even_number([2,3,4,4,5,6,1]))
