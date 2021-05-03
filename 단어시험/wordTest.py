import random

def getWord(wordResult, meanResult):

    wordList = []
    n=0
    for i in wordResult:
        word = []
        word.append(wordResult[n])
        word.append(meanResult[n])
        wordList.append(word)

        n=n+1
    random.shuffle(wordList)
    print("\n 단 어 시 험 생 성 \n")
    score = 0
    wrongWord = []
    for i in range(len(wordList)):
        print(str(i+1)+'.'+wordList[i][1])
        insertWord = input("단어 입력")
        if insertWord == wordList[i][0]:
            print("정답")
            score = score+1
        elif insertWord != wordList[i][0]:
            print("땡 정답은 "+wordList[i][0]+" 입니다")
            wrongWord.append(wordList[i])
        print("맞은 개수 : "+str(score))

        print("*****틀린 단어*****")
        for i in range(len(wrongWord)) :
            for i in range(len(wrongWord)) :
                print("단어 : "+wrongWord[i][0]+" 뜻 : "+wrongWord[i][1])
            print("*****************")
            getBack = input("돌아가려면 엔터를 눌러주세요")