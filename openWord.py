from openpyxl import load_workbook
import wordTest
import getWord

getWord.getWord()
load_wb = load_workbook('./wordList.xlsx', data_only = True)
load_ws = load_wb['wordList']

words = []
mean = []

eng =load_ws ['A']
kor = load_ws['B']

for cell in eng:

    words.append(cell.value)
for cell in kor:
    mean.append(cell.value)

page = 0
end = len(words)

div = 20

wordResult = [words[i*div:(i+1)*div] for i in range((end+div-1)//div)]
meanResult = [mean[i*div:(i+1)*div] for i in range((end+div-1)//div)]

n=0
print('page '+str(page+1)+'/'+str(len(wordResult)))
for i in wordResult[page]:
    print(str(n+1)+'. '+i+"  "+meanResult[0][n])
    n=n+1
n=0

while True:
    print('\n(1) 이전 (2) 다음 (3) 원하는 페이지 이동 (4) 현재 단어 시험보기 (5) 단어장 종료\n')
    selectMenu = int(input("메뉴입력 : "))

    if selectMenu==1:
        if page==0:
            print("\n첫번째 페이지입니다.\n")
        else:
            page =page-1
            print('page '+str(page+1)+'/'+str(len(wordResult)))
            for i in wordResult[page]:
                print(str(n+1)+'. '+i+"  "+meanResult[int(page)][n])
                n=n+1
            n=0
    elif selectMenu ==2:
        if page==(len(wordResult))-1:
            print("\n맨 마지막 장입니다.\n")
        else:
            page=page+1
            print('page '+str(page+1)+'/'+str(len(wordResult)))
            for i in wordResult[page]:
                print(str(n+1)+'. '+i+"  "+meanResult[int(page)][n])
                n=n+1
            n=0
    elif selectMenu ==3:
            pageNum=int(input("원하는 페이지 입력 = "))
            if pageNum > len(wordResult) or pageNum-1 < 0 :
                print("잘못 입력하셨습니다")
            else:
                page = pageNum-1
                print('page '+str(page+1)+'/'+str(len(wordResult)))
                for i in wordResult[page]:
                    print(str(n+1)+'. '+i+"  "+meanResult[int(page)][n])
                    n=n+1
                n=0
    elif selectMenu ==4:
        wordTest.getWord(wordResult[page], meanResult[page])
        print('page '+str(page+1)+'/'+str(len(wordResult)))
        for i in wordResult[page]:
            print(str(n+1)+'. '+i+" "+meanResult[int(page)][n])
            n=n+1
        n=0
    elif selectMenu ==5:
        break
                