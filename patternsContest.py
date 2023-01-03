size = int(input())

words = []

for inp in range(size):
    temp = input()
    words.append(temp)

answer = []

for length in range(len(words[0])):
    setPatterns = []

    for index in range(size):
        if words[index][length] == "?":
            continue
        elif words[index][length].isalpha():
            setPatterns.append(words[index][length])

    pattern = set(setPatterns)

    if len(pattern) == 0:
        answer.append("a")
    elif len(pattern) == 1:
        answer.append(setPatterns[0])
    elif len(pattern) > 1:
        answer.append("?")

print("".join(answer))
