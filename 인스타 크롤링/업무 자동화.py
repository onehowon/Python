from tkinter import *
from tkinter.font import Font
do = []

def addscript():
    def add(mode, dos):
        value = "0, 0" if dos == "move" else ""
        setting.quit()
    setting = Tk()
    setting.title("모드 선택")
    setting.config(bg = "white")

    setting.minsize(450,300)
    setting.maxsize(450, 300)

    l1 = Label(text="마우스 움직임").pack(pady=10)
    b1_1 = Button(setting, text="마우스 이동", width=10, height=1, bg ="#D3D3D3", relief = flat, highlightthickness=0, highlightcolor="#D3D3D3").place(x=125, y=60, anchor="s", command=lambda:add(0, "move"))
    b1_2 = Button(setting, text="마우스 클릭", width=10, height=1, bg ="#D3D3D3", relief = flat, highlightthickness=0, highlightcolor="#D3D3D3").place(x=225, y=60, anchor="s", command=lambda:add(0, "click"))
    b1_3 = Button(setting, text="마우스 스크롤", width=10, height=1, bg ="#D3D3D3", relief = flat, highlightthickness=0, highlightcolor="#D3D3D3").palce(x=325, y= 60, anchor="s", command=lambda:add(0, "scroll"))

    l2 = Label(text="키보드 입력")
    b2_1 = Button(setting, text="키보드 키 입력", width=10, height=1, bg ="#D3D3D3", relief = flat, highlightthickness=0,highlightcolor="#D3D3D3").place(x=125, y=110, anchor="s"command=lambda:add(1, "key"))
    b2_2 = Button(setting, text="키보드 문장 입력", width=10, height=1, bg ="#D3D3D3", relief = flat, highlightthickness=0,highlightcolor="#D3D3D3").place(x=225, y=110, anchor="s"command=lambda:add(1, "sente"))
    b2_3 = Button(setting, text="키보드 핫키 입력", width=10, height=1, bg ="#D3D3D3", relief = flat, highlightthickness=0,highlightcolor="#D3D3D3").place(x=325, y=110, anchor="s"command=lambda:add(1, "hotkey"))

    l3 = Label(text = "딜레이")
    b3_1 = Button(setting, text="딜레이 삽입", width=10, height=1, bg ="#D3D3D3", relief = flat, highlightthickness=0)
    setting.mainloop()

window = Tk()
window.title("Macro")
window.config(bg="white")

window.minsize(900, 600)
window.maxsize(900, 600)

add_button = Button(text="스크립트 생성", font=Font(family="맑은 고딕", size=12), width=2, height = 3)
add_button.place(x=450, y=276, anchor="s")

box = Listbox(width = 50, height = 20, bg="#D3D3D3")
box.place(x=450, y=600, anchor="s", relief="flat", highlightthickness=0)

mainloop()