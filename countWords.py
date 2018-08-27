def count(words):
    print(str((len(words) - len(words.replace(" ", "")))+1))


count("This is a test sentence")