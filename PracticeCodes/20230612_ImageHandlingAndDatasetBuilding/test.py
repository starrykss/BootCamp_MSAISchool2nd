# zip 간단 실습

a = [1, 2, 3]
b = ["a", "b", "c"]
c = ["#", "$", "!"]

result = zip(a, b, c)
for i in result:
    print(i)

"""
(1, 'a', '#')
(2, 'b', '$')
(3, 'c', '!')
"""

list_temp = list(zip(a, b, c))
print(list_temp)

"""
[(1, 'a', '#'), (2, 'b', '$'), (3, 'c', '!')]
"""
