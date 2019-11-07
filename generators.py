# # def square_numbers(nums):
# #
# #     for i in nums:
# #       yield(i*i)
#
#
# #for generators comprehension
# my_nums=(x*x for x in [1,2,3,4,5])
#
# print(list(my_nums))

#fibonacci numbers


def genfibon(n):
    a=0
    b=1


    for i in range(n):
        nextnumber=a+b
        yield nextnumber
        a=b
        b=nextnumber

for num in genfibon(10):
    print(num)
