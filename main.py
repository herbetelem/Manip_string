def countString(string):
    nbCararctere = len(string)
    nbSpace = string.count(" ")
    return nbCararctere - nbSpace


def countIteranceString(string, carac):
    index = 1
    position = "position : "
    for letter in string:
        if letter == carac:
            position = position + str(index) + ", "
        index += 1
    return position[:-2]

def showFromTo(string, start, end):
    result = ""
    while start < end:
        result = result + string[start]
        start += 1
    return result


def returnWithoutSpace1(string):
    return string[1:-1]

def returnWithoutSpace2(string):
    return string.strip()

def returnWithoutSpace3(string):
    return string.lstrip()


def convertVowelAndConso(string):
    result = ""
    for letter in string:
        if letter=='a' or letter =='e' or letter=='i' or letter=='o' or letter=='u' or letter=='y':
            result = result + letter.upper()
        else:
            result = result + letter.lower()
    return result


def invertcarac(string, first, second):
    return string.replace(first, second)