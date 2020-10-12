'''
Your function should take in a single parameter (a string `word`)
Your function should return a count of how many occurences of ***"th"*** occur within `word`. Case matters.
Your function must utilize recursion. It cannot contain any loops.
'''


def count_th(word):

    # TBC
    word_len = len(word)

    # Base Case
    if word_len == 0:
        return 0
    # else 1st two letters is "th"
    elif word[:2] == 'th':
        return 1 + count_th(word[2:])
    else:
        return count_th(word[1:])


if __name__ == "__main__":

    word = "thabcthefthghith"

    print(
        f"There are {count_th(word)} TH in this word")
