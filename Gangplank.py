from tkinter import *



win = Tk() # 창 생성
win.geometry("1600x900")
win.title("리스트")
win.option_add("*Font", "맑은고딕 13")
win.resizable(False, False)

# 1호 리스트박스 정의


일호=Listbox(selectmode='single', height=0)
entry1 = Entry(width=20)
일호.insert(0,'상주성명')
일호.insert(1,'안치일시')
일호.insert(2,'입관일시')
일호.insert(3,'발인일시')
일호.insert(4,'상조회')
일호.insert(5,'장지')
일호.insert(6,'상차림')
일호.insert(7,'상주')
entry1.pack()
일호.pack()


일호일=Listbox(selectmode='single', height=8)
일호일.pack()
일호일.place(x=300, y=110)

def change():

    일호일.insert(일호.curselection(),entry1.get())
    일호일.insert(일호.curselection(),entry1.get())
    일호일.insert(일호.curselection(),entry1.get())
    일호일.insert(일호.curselection(),entry1.get())
    일호일.insert(일호.curselection(),entry1.get())
    일호일.insert(일호.curselection(),entry1.get())
    일호일.insert(일호.curselection(),entry1.get())
    일호일.insert(일호.curselection(),entry1.get())



# 1호입력 버튼 정의


일호입력 =Button(text='입력', padx=5, pady=5, command=change)
일호입력.pack()


# 1호 위치 정의

일호.place(x=40,y=110)
entry1.place(x=40,y=70)
일호입력.place(x=210,y=70)



# 2호 리스트박스 정의

이호=Listbox(win,selectmode='extended', height=0)
text2=Text(width=20, height=1.5)
이호.insert(0,'상주성명')
이호.insert(1,'안치일시')
이호.insert(2,'입관일시')
이호.insert(3,'발인일시')
이호.insert(4,'상조회')
이호.insert(5,'장지')
이호.insert(6,'상차림')
이호.insert(7,'상주')
text2.pack()
이호.pack()



# 2호입력 버튼 정의

이호입력 =Button(win, text='입력', padx=5, pady=5)
이호입력.pack

# 2호 위치 정의

이호.place(x=540,y=110)
text2.place(x=540,y=70)
이호입력.place(x=710,y=70)



#3호 리스트박스 정의

삼호=Listbox(win,selectmode='extended', height=0)
text3=Text(width=20, height=1.5)
삼호.insert(0,'상주성명')
삼호.insert(1,'안치일시')
삼호.insert(2,'입관일시')
삼호.insert(3,'발인일시')
삼호.insert(4,'상조회')
삼호.insert(5,'장지')
삼호.insert(6,'상차림')
삼호.insert(7,'상주')
text3.pack()
삼호.pack()



# 3호입력 버튼 정의

삼호입력 =Button(win, text='입력', padx=5, pady=5)
삼호입력.pack

# 3호 위치 정의

삼호.place(x=1040,y=110)
text3.place(x=1040,y=70)
삼호입력.place(x=1210,y=70)


# 5호 리스트박스 정의

오호=Listbox(win,selectmode='extended', height=0)
text5=Text(width=20, height=1.5)
오호.insert(0,'상주성명')
오호.insert(1,'안치일시')
오호.insert(2,'입관일시')
오호.insert(3,'발인일시')
오호.insert(4,'상조회')
오호.insert(5,'장지')
오호.insert(6,'상차림')
오호.insert(7,'상주')
text5.pack()
오호.pack()

# 5호입력 버튼 정의

오호입력 =Button(win, text='입력', padx=5, pady=5)
오호입력.pack


# 5호 위치 정의

오호.place(x=40,y=360)
text5.place(x=40,y=320)
오호입력.place(x=210,y=320)


# 6호 리스트박스 정의


육호=Listbox(win,selectmode='extended', height=0)
text6=Text(width=20, height=1.5)
육호.insert(0,'상주성명')
육호.insert(1,'안치일시')
육호.insert(2,'입관일시')
육호.insert(3,'발인일시')
육호.insert(4,'상조회')
육호.insert(5,'장지')
육호.insert(6,'상차림')
육호.insert(7,'상주')
text6.pack()
육호.pack()


# 6호입력 버튼 정의

육호입력 =Button(win, text='입력', padx=5, pady=5)
육호입력.pack


# 6호 위치 정의

육호.place(x=540,y=360)
text6.place(x=540,y=320)
육호입력.place(x=710,y=320)


# 특101호 리스트박스 정의

특백일호=Listbox(win,selectmode='extended', height=0)
text7=Text(width=20, height=1.5)
특백일호.insert(0,'상주성명')
특백일호.insert(1,'안치일시')
특백일호.insert(2,'입관일시')
특백일호.insert(3,'발인일시')
특백일호.insert(4,'상조회')
특백일호.insert(5,'장지')
특백일호.insert(6,'상차림')
특백일호.insert(7,'상주')
text7.pack()
특백일호.pack()


# 특101호입력 버튼 정의

특백일호입력 =Button(win, text='입력', padx=5, pady=5)
특백일호입력.pack


# 특101호 위치 정의

특백일호.place(x=1040,y=360)
text7.place(x=1040,y=320)
특백일호입력.place(x=1210,y=320)


# 특102호 리스트박스 정의

특백이호=Listbox(win,selectmode='extended', height=0)
text8=Text(width=20, height=1.5)
특백이호.insert(0,'상주성명')
특백이호.insert(1,'안치일시')
특백이호.insert(2,'입관일시')
특백이호.insert(3,'발인일시')
특백이호.insert(4,'상조회')
특백이호.insert(5,'장지')
특백이호.insert(6,'상차림')
특백이호.insert(7,'상주')
text8.pack()
특백이호.pack()


# 특102호입력 버튼 정의

특백이호입력 =Button(win, text='입력', padx=5, pady=5)
특백이호입력.pack


# 특102호 위치 정의

특백이호.place(x=40,y=610)
text8.place(x=40,y=570)
특백이호입력.place(x=210,y=570)


# 특201호 리스트박스 정의

특이백일호=Listbox(win,selectmode='extended', height=0)
text9=Text(width=20, height=1.5)
특이백일호.insert(0,'상주성명')
특이백일호.insert(1,'안치일시')
특이백일호.insert(2,'입관일시')
특이백일호.insert(3,'발인일시')
특이백일호.insert(4,'상조회')
특이백일호.insert(5,'장지')
특이백일호.insert(6,'상차림')
특이백일호.insert(7,'상주')
text9.pack()
특이백일호.pack()



# 특201호입력 버튼 정의

특이백일호입력 =Button(win, text='입력', padx=5, pady=5)
특이백일호입력.pack

# 특201호 위치 정의

특이백일호.place(x=540,y=610)
text9.place(x=540,y=570)
특이백일호입력.place(x=710,y=570)



# 특202호 리스트박스 정의

특이백이호=Listbox(win,selectmode='extended', height=0)
text10=Text(width=20, height=1.5)
특이백이호.insert(0,'상주성명')
특이백이호.insert(1,'안치일시')
특이백이호.insert(2,'입관일시')
특이백이호.insert(3,'발인일시')
특이백이호.insert(4,'상조회')
특이백이호.insert(5,'장지')
특이백이호.insert(6,'상차림')
특이백이호.insert(7,'상주')
text10.pack()
특이백이호.pack()



# 특202호입력 버튼 정의

특이백이호입력 =Button(win, text='입력', padx=5, pady=5)
특이백이호입력.pack

# 특202호 위치 정의

특이백이호.place(x=1040,y=110)
text10.place(x=1040,y=70)
특이백이호입력.place(x=1210,y=70)

win.mainloop()