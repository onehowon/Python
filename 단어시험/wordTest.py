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
    print("\n �� �� �� �� �� �� \n")
    score = 0
    wrongWord = []
    for i in range(len(wordList)):
        print(str(i+1)+'.'+wordList[i][1])
        insertWord = input("�ܾ� �Է�")
        if insertWord == wordList[i][0]:
            print("����")
            score = score+1
        elif insertWord != wordList[i][0]:
            print("�� ������ "+wordList[i][0]+" �Դϴ�")
            wrongWord.append(wordList[i])
        print("���� ���� : "+str(score))

        print("*****Ʋ�� �ܾ�*****")
        for i in range(len(wrongWord)) :
            for i in range(len(wrongWord)) :
                print("�ܾ� : "+wrongWord[i][0]+" �� : "+wrongWord[i][1])
            print("*****************")
            getBack = input("���ư����� ���͸� �����ּ���")