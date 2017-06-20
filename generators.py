my_nums = (x*x for x in [1, 2, 3, 4, 5])

print my_nums
print next(my_nums)
for num in my_nums:
    print num


def square(nums):
    for i in nums:
        yield (i*i)

result = square([6, 7, 8, 9, 10])
print list(result)
# print result
# for i in result:
#     print i
