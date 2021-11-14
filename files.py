import itertools
#https://stackoverflow.com/questions/42876366/check-if-a-string-defines-a-color
#from matplotlib.colors import is_color_like
colors=["red", "blue", "green", "black", "yellow"]

def Data_Report(path):
    input_file = open(path, "r")
    lines = input_file.readlines()

    #1
    print("number of lines in the file: " + str(len(lines)))

    #2
    count = 0
    for line in lines:
        count += len(line.split())
    print("number of words in the file: " + str(count))

    #3
    print("number of unique words in the file: " + str(len(set(itertools.chain.from_iterable(map(str.split, lines))))))

    #4
    print("average sentence length: " + str(count / len(lines)))

    max = 0
    for line in lines:
        if max < len(line.split()):
             max = len(line.split())
    print("maximum sentence length: " + str(max))

    #6
    res = []
    resMax = []
    maxWithoutK = 0
    for line in lines:
        for word in line.split():
            if "k" not in word:
                res.append(word)
            else:
                if maxWithoutK < len(res):
                    maxWithoutK = len(res)
                    resMax = res
                res = []
    if maxWithoutK < len(res):
        maxWithoutK = len(res)
        resMax = res
    print("the longest word sequence in a text that does not contain the letter k: " + str(resMax))

    #8
    d = dict()
    for line in lines:
        for word in line.split():
            if word in colors:
                if word in d:
                    d[word] = d[word] + 1
                else:
                    d[word] = 1
    print("color names in the text and the number of occurrences:")
    for key in list(d.keys()):
        print(key, ":", d[key])


Data_Report("D:\\user\\Pictures\\הדר סמינר\\תכנות כיתה ו\python\\files py\\txt.txt")





    



