def myLineEditor():
    list = ArrayList()
    while True:
        command = input("[메뉴선택] i-입력, d-삭제, r-변경, p-출력, l-파일읽기, s-저장, q-종료=> ")

        if command == 'i':
            pos = int(input(" 입력행 번호: "))
            str = input(" 입력행 내용: ")
            list.insert(pos,str)
        elif command == "d":
            pos = int(input(" 삭제행 번호: "))
            list.delete(pos)
        elif command == 'r':
            pos = int(input(" 변경행 번호: "))
            str = input(" 변경행 내용: ")
            list.replace(pos,str)