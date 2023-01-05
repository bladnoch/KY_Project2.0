import tkinter
from tkinter import * # tkinter의 모든 함수 가져오기
from tkinter import messagebox, filedialog, Label
import os
from pathlib import Path
import openpyxl
import os.path
from openpyxl.worksheet.table import Table, TableStyleInfo
import tkinter.ttk
import tkinter as tk

#def time():

#def ID_a():

def close():
    win.quit()
    win.destroy()


win = Tk() # 창 생성
win.geometry("1600x900") # 창의 크기
win.title("장례식장 재고관리 프로그램 Ver1.221123") # 창의 제목
win.option_add("*Font", "맑은고딕 13") # 전체 폰트
#win.resizable(False, False) #윈도우 사이즈 조절 불가
tab_bt=tkinter.ttk.Notebook(win, width=300, height=630)


# 1호 레이블 정의

일호상주성명_lab = Label(win)
일호상주성명_lab.config(text = "상주성명",width=10, relief="solid")
일호안치일시_lab = Label(win)
일호안치일시_lab.config(text = "안치일시",width=10, relief="solid")
일호입관일시_lab = Label(win)
일호입관일시_lab.config(text = "입관일시", width=10, relief="solid")
일호발인일자_lab = Label(win)
일호발인일자_lab.config(text = "발인일자", width=10, relief="solid")
일호상조회_lab = Label(win)
일호상조회_lab.config(text = "상조회", width=10, relief="solid")
일호장지_lab = Label(win)
일호장지_lab.config(text = "장지", width=10, relief="solid")
일호상차림_lab = Label(win)
일호상차림_lab.config(text = "상차림", width=10, relief="solid")
일호상주_lab: Label = Label(win)
일호상주_lab.config(text = "상주", width=10, relief="solid")

# 1호 레이블 위치정의

일호상주성명_lab.place(x=20,y=40)
일호안치일시_lab.place(x=20,y=70)
일호입관일시_lab.place(x=20,y=100)
일호발인일자_lab.place(x=20,y=130)
일호상조회_lab.place(x=20,y=160)
일호장지_lab.place(x=20,y=190)
일호상차림_lab.place(x=20,y=220)
일호상주_lab.place(x=20,y=250)


#1호 엔트리 정의

일호상주성명 = Entry(win)
일호상주성명.config(width=10,relief="solid",borderwidth=2)
일호안치일시 = Entry(win)
일호안치일시.config(width=10,relief="solid",borderwidth=2)
일호입관일시 = Entry(win)
일호입관일시.config(width=10,relief="solid",borderwidth=2)
일호발인일자 = Entry(win)
일호발인일자.config(width=10,relief="solid",borderwidth=2)
일호상조회 = Entry(win)
일호상조회.config(width=10,relief="solid",borderwidth=2)
일호장지 = Entry(win)
일호장지.config(width=10,relief="solid",borderwidth=2)
일호상차림 = Entry(win)
일호상차림.config(width=10,relief="solid",borderwidth=2)
일호상주 = Entry(win)
일호상주.config(width=10,relief="solid",borderwidth=2)

#1호 엔트리 위치정의

일호상주성명.place(x=115,y=40)
일호안치일시.place(x=115,y=70)
일호입관일시.place(x=115,y=100)
일호발인일자.place(x=115,y=130)
일호상조회.place(x=115,y=160)
일호장지.place(x=115,y=190)
일호상차림.place(x=115,y=220)
일호상주.place(x=115,y=250)




# 2호 레이블 정의

이호상주성명_lab = Label(win)
이호상주성명_lab.config(text = "상주성명",width=10, relief="solid")
이호안치일시_lab = Label(win)
이호안치일시_lab.config(text = "안치일시",width=10, relief="solid")
이호입관일시_lab = Label(win)
이호입관일시_lab.config(text = "입관일시", width=10, relief="solid")
이호발인일자_lab = Label(win)
이호발인일자_lab.config(text = "발인일자", width=10, relief="solid")
이호상조회_lab = Label(win)
이호상조회_lab.config(text = "상조회", width=10, relief="solid")
이호장지_lab = Label(win)
이호장지_lab.config(text = "장지", width=10, relief="solid")
이호상차림_lab = Label(win)
이호상차림_lab.config(text = "상차림", width=10, relief="solid")
이호상주_lab: Label = Label(win)
이호상주_lab.config(text = "상주", width=10, relief="solid")

# 2호 레이블 위치정의

이호상주성명_lab.place(x=500,y=40)
이호안치일시_lab.place(x=500,y=70)
이호입관일시_lab.place(x=500,y=100)
이호발인일자_lab.place(x=500,y=130)
이호상조회_lab.place(x=500,y=160)
이호장지_lab.place(x=500,y=190)
이호상차림_lab.place(x=500,y=220)
이호상주_lab.place(x=500,y=250)

#2호 엔트리 정의

이호상주성명 = Entry(win)
이호상주성명.config(width=10,relief="solid",borderwidth=2)
이호안치일시 = Entry(win)
이호안치일시.config(width=10,relief="solid",borderwidth=2)
이호입관일시 = Entry(win)
이호입관일시.config(width=10,relief="solid",borderwidth=2)
이호발인일자 = Entry(win)
이호발인일자.config(width=10,relief="solid",borderwidth=2)
이호상조회 = Entry(win)
이호상조회.config(width=10,relief="solid",borderwidth=2)
이호장지 = Entry(win)
이호장지.config(width=10,relief="solid",borderwidth=2)
이호상차림 = Entry(win)
이호상차림.config(width=10,relief="solid",borderwidth=2)
이호상주 = Entry(win)
이호상주.config(width=10,relief="solid",borderwidth=2)

#2호 엔트리 위치정의

이호상주성명.place(x=595,y=40)
이호안치일시.place(x=595,y=70)
이호입관일시.place(x=595,y=100)
이호발인일자.place(x=595,y=130)
이호상조회.place(x=595,y=160)
이호장지.place(x=595,y=190)
이호상차림.place(x=595,y=220)
이호상주.place(x=595,y=250)


# 3호 레이블 정의

삼호상주성명_lab = Label(win)
삼호상주성명_lab.config(text = "상주성명",width=10, relief="solid")
삼호안치일시_lab = Label(win)
삼호안치일시_lab.config(text = "안치일시",width=10, relief="solid")
삼호입관일시_lab = Label(win)
삼호입관일시_lab.config(text = "입관일시", width=10, relief="solid")
삼호발인일자_lab = Label(win)
삼호발인일자_lab.config(text = "발인일자", width=10, relief="solid")
삼호상조회_lab = Label(win)
삼호상조회_lab.config(text = "상조회", width=10, relief="solid")
삼호장지_lab = Label(win)
삼호장지_lab.config(text = "장지", width=10, relief="solid")
삼호상차림_lab = Label(win)
삼호상차림_lab.config(text = "상차림", width=10, relief="solid")
삼호상주_lab: Label = Label(win)
삼호상주_lab.config(text = "상주", width=10, relief="solid")

# 3호 레이블 위치정의

삼호상주성명_lab.place(x=980,y=40)
삼호안치일시_lab.place(x=980,y=70)
삼호입관일시_lab.place(x=980,y=100)
삼호발인일자_lab.place(x=980,y=130)
삼호상조회_lab.place(x=980,y=160)
삼호장지_lab.place(x=980,y=190)
삼호상차림_lab.place(x=980,y=220)
삼호상주_lab.place(x=980,y=250)

#3호 엔트리 정의

삼호상주성명 = Entry(win)
삼호상주성명.config(width=10,relief="solid",borderwidth=2)
삼호안치일시 = Entry(win)
삼호안치일시.config(width=10,relief="solid",borderwidth=2)
삼호입관일시 = Entry(win)
삼호입관일시.config(width=10,relief="solid",borderwidth=2)
삼호발인일자 = Entry(win)
삼호발인일자.config(width=10,relief="solid",borderwidth=2)
삼호상조회 = Entry(win)
삼호상조회.config(width=10,relief="solid",borderwidth=2)
삼호장지 = Entry(win)
삼호장지.config(width=10,relief="solid",borderwidth=2)
삼호상차림 = Entry(win)
삼호상차림.config(width=10,relief="solid",borderwidth=2)
삼호상주 = Entry(win)
삼호상주.config(width=10,relief="solid",borderwidth=2)

#3호 엔트리 위치정의

삼호상주성명.place(x=1075,y=40)
삼호안치일시.place(x=1075,y=70)
삼호입관일시.place(x=1075,y=100)
삼호발인일자.place(x=1075,y=130)
삼호상조회.place(x=1075,y=160)
삼호장지.place(x=1075,y=190)
삼호상차림.place(x=1075,y=220)
삼호상주.place(x=1075,y=250)



win.mainloop()