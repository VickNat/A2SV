from collections import defaultdict

testCases = int(input())

for tests in range(testCases):
  song = list(map(str, input().split()))

  songDict = defaultdict(str)

  for idx in range(1, len(song)+1):
      songDict[idx] = ""

  for word in song:
    letter = 0
    temp = 0
    
    wordList = []
    
    for let in range(len(word)):
      wordList.append(word[let])

    while letter < len(wordList):
      if wordList[letter].isdigit():
        temp *= 10
        temp += int(wordList[letter])
        wordList.remove(wordList[letter])
      else:
        letter += 1

    word = "".join(wordList)
    songDict[temp] = word

  # sortedDict = sorted(songDict)
  orderedSong = []

  for word in songDict.keys():
    orderedSong.append(songDict[word])

  print(" ".join(orderedSong))