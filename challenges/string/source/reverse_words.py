

def reverse_words(sentence):
    return " ".join(reversed(sentence.split(" ")))


def reverse_letters(word):
    if word == "":
        return word

    return word[-1] + reverse_letters(word[:-1])


def reverse_words_v1(sentence):
    rev_sentence = reverse_letters(sentence)
    words = rev_sentence.split(" ")
    new_sentence = []
    for word in words:
        new_sentence.append(reverse_letters(word))
    return " ".join(new_sentence)


def reverse_words_v2(sentence):
    rev_sentence = reverse_letters(sentence)
    prev = 0
    new_sentence = ""
    for i in range(len(rev_sentence)):
        if rev_sentence[i] == " " or i == len(rev_sentence) - 1:
            end = i
            if i == len(rev_sentence) - 1:
                end = i + 1
            sep = " "
            if new_sentence == "":
                sep = ""
            new_sentence = new_sentence + sep + reverse_letters(rev_sentence[prev:end])
            prev = i + 1
    return new_sentence
