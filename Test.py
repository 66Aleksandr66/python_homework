def pig_latin(string):
    consonant = (
    'b', 'c', 'd', 'f', 'g', 'h', 'j', 'k', 'l', 'm', 'n', 'p', 'q', 'r', 's', 't', 'v', 'w', 'x', 'y', 'z')
    vowel = ('a', 'e', 'i', 'o', 'u')
    new_string = []

    for word in string.split():
        count = 0
        if word.startswith(vowel):
            word = word + 'ay'
            new_string.append(word)
        elif word.startswith(consonant):
            for i, letter in enumerate(word):
                if letter in consonant:
                    if letter == 'q' and word[i + 1] == 'u':
                        count += 1
                    count += 1
                else:
                    break
                result =  word[count:] + word[:count] + 'ay'
            new_string.append(result)
    return " ".join(new_string)





pig_latin("the quick brown fox")