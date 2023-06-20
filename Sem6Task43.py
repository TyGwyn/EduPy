from random import randint
random_list = []
list_lenght = 10
for i in range (0, list_lenght):
    random_list.append(randint(1,5))
print((random_list))
random_list = sorted(random_list)
print(random_list)
s = set(random_list)
c = 0
for i in s:
    c+=random_list.count(i)//2
print(c)