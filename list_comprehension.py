nums=[1,2,3,4,5,6,7,8,9,10]

#my_list=[]
#for n in nums:
#    my_list.append(n)
#print(my_list)

#my_list=[n for n in nums]
#print(my_list)

#my_list=[]

#for n in nums:
#    my_list.append(n*n)
#print(my_list)

#my_list=[n*n for n in nums]
#print(my_list)

#my_list=[]
#for n in nums:
#    if n%2==0:
#        my_list.append(n)
#print(my_list)

#my_list=[n for n in nums if n%2==0]
#print(my_list)

#my_list=[]
#for letter in 'abcd':
#    for num in range(4):
#        my_list.append((letter,num))
#print(my_list)

#my_list=[(letter,num) for letter in 'abcd' for num in range(4)]
#print(my_list)

names=['bruce','clark','peter','logan','wade']
heroes=['batman','superman','spiderman','wolverine','deadpool']
#print(zip(names,heroes))

#my_dict={}
#for name,hero in zip(names,heroes):
#    my_dict[name]=hero
#print (my_dict)

#my_dict={name:hero for name,hero in zip(names,heroes) if name!='peter'}
#print(my_dict)

nums=[1,2,3,4,5,6,7,8,9,10]

#def gen_func(nums):
#    for n in nums:
#        yield n*n
#my_gen=gen_func(nums)
#
#print(my_gen)

my_gen=(n*n for n in nums)

for i in my_gen:
    print (i)
