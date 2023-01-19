def spin_words(sentence):
    # Your code goes here
    new_sentence = []
    words = sentence.split(" ")
    
    for word in words:
        if len(word)<5:
            new_sentence.append(word)
        else:
            new_sentence.append(word[::-1])
    return ' '.join(new_sentence)


def main():
    print(spin_words("God is Amazing"))


main()