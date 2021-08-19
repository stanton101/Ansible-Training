# print("this is a \" in a string")
# print('this is a \' in a string')
# print('this is a \" and a \' in a string')
#
# k = 'A \\ in a string'
# print(k)

# g = str(6.02e23)
# print(g)
#
# s = 'parrot'
#
# print(type(s[4]))
# print(s[4])


# [1, 9, 8]
# a = ["apple", "orange", "pear"]
# a[1] = 7
# print(a)
#
# b = []
# b.append(1.618)
# b.append(1.414)
# print(b)
#
# list("characters")
# ['c', 'h', 'a', 'r', 'a', 'c', 't', 'e','r', 's']
# c = ['bear', 'giraffe', 'elephant', 'caterpillar']
# print(c)

# d = {'alice': '878-8728-922', 'bob': '256-5262-124', 'eve': '198-2321-787'}
# print(d['bob'])

# d['charles'] = '334-5551-913'
# print(d)
#
# cities = ["London", "New York", "Paris", "Oslo", "Helsinki"]
# for city in cities:
#     print(city)

from urllib.request import urlopen
story = urlopen('http://sixty-north.com/c/t.txt')
story_words = []
for line in story:
    line_words = line.split()
    for word in line_words:
        story_words.append(word)

story.close()
print(story_words)


