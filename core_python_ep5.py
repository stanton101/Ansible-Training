import sys
from urllib.request import urlopen


# story = urlopen('http://sixty-north.com/c/t.txt')
# story_words = []
# for line in story:
#     line_words = line.split()
#     for word in line_words:
#         story_words.append(word)
#
# story.close()
# for word in story_words:
#     print(word)
# print(story_words)

def fetch_words(url):
    story = urlopen(url)
    story_words = []
    for line in story:
        line_words = line.decode('utf8').split()
        for word in line_words:
            story_words.append(word)
    story.close()
    return story_words


def print_items(items):
    for item in items:
        print(item)


def main(url):
    words = fetch_words(url)
    print_items(words)


if __name__ == '__main__':
    main(sys.argv[1])



# def even_or_odd(n):
#     if n % 2 == 0:
#         print("even")
#         return
#     print("odd")
#
#
# w = even_or_odd(30)
# w is None
# print(w)


# def nth_root(radicand, n):
#     return radicand ** (1/n)
# print(nth_root(16, 2))
# print(nth_root(27, 3))
# print(nth_root(64, 2))
