

def list_words_by_count(filename):
    with open(filename, "r") as file:
        lst = file.read().split()
        count_words = {}
        for item in lst:
            count_words[item] = str(get_word_count(lst, item.lower()))
        return count_words


def print_top(filename, n):
    count_words = list_words_by_count(filename)
    count_words = dict(sorted(count_words.items(), key=lambda item: int(item[1]), reverse=True))
    index = 0
    for key in count_words.keys():
        if index == n:
            return
        index += 1
        print(key + " " + count_words[key])


def get_word_count(lst, word):
    count = 0
    for item in lst:
        if item.lower() == word:
            count += 1
            lst.remove(item)
    return count


def main():
    filename = "test.txt"
    print_top(filename, 17)


if __name__ == '__main__':
    main()
