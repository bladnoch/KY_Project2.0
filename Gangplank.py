from tkinter import *
from openpyxl import *

wb = Workbook()
ws = wb.active
ws.title = '개인정보'
wb.save('개인정보.xlsx')
wb.close()

win = Tk() # 창 생성
win.geometry("1600x900")
win.title("리스트")
win.option_add("*Font", "맑은고딕 13")
win.resizable(False, False)

def change():
    일호일.insert(일호.curselection(),일호상주성명.get())
def change1() :
    일호일.insert(일호.curselection(),일호빈소기간.get())
def change2() :
    일호일.insert(일호.curselection(),일호상조회.get())
def change3() :
    일호일.insert(일호.curselection(),일호장지.get())
def change4() :
    일호일.insert(일호.curselection(),일호상차림.get())
def change5() :
    일호일.insert(일호.curselection(),일호상주.get())

def change6():
    이호일.insert(이호.curselection(),이호상주성명.get())
def change7() :
    이호일.insert(이호.curselection(),이호빈소기간.get())
def change8() :
    이호일.insert(이호.curselection(),이호상조회.get())
def change9() :
    이호일.insert(이호.curselection(),이호장지.get())
def change10() :
    이호일.insert(이호.curselection(),이호상차림.get())
def change11() :
    이호일.insert(이호.curselection(),이호상주.get())

def change12():
    삼호일.insert(삼호.curselection(),삼호상주성명.get())
def change13() :
    삼호일.insert(삼호.curselection(),삼호빈소기간.get())
def change14() :
    삼호일.insert(삼호.curselection(),삼호상조회.get())
def change15() :
    삼호일.insert(삼호.curselection(),삼호장지.get())
def change16() :
    삼호일.insert(삼호.curselection(),삼호상차림.get())
def change17() :
    삼호일.insert(삼호.curselection(),삼호상주.get())

def change18():
    오호일.insert(오호.curselection(),오호상주성명.get())
def change19() :
    오호일.insert(오호.curselection(),오호빈소기간.get())
def change20() :
    오호일.insert(오호.curselection(),오호상조회.get())
def change21() :
    오호일.insert(오호.curselection(),오호장지.get())
def change22() :
    오호일.insert(오호.curselection(),오호상차림.get())
def change23() :
    오호일.insert(오호.curselection(),오호상주.get())

def change24():
    육호일.insert(육호.curselection(),육호상주성명.get())
def change25() :
    육호일.insert(육호.curselection(),육호빈소기간.get())
def change26() :
    육호일.insert(육호.curselection(),육호상조회.get())
def change27() :
    육호일.insert(육호.curselection(),육호장지.get())
def change28() :
    육호일.insert(육호.curselection(),육호상차림.get())
def change29() :
    육호일.insert(육호.curselection(),육호상주.get())

def change30():
    특백일호일.insert(특백일호.curselection(),특백일호상주성명.get())
def change31() :
    특백일호일.insert(특백일호.curselection(),특백일호빈소기간.get())
def change32() :
    특백일호일.insert(특백일호.curselection(),특백일호상조회.get())
def change33() :
    특백일호일.insert(특백일호.curselection(),특백일호장지.get())
def change34() :
    특백일호일.insert(특백일호.curselection(),특백일호상차림.get())
def change35() :
    특백일호일.insert(특백일호.curselection(),특백일호상주.get())

def change36():
    특백이호일.insert(특백이호.curselection(),특백이호상주성명.get())
def change37() :
    특백이호일.insert(특백이호.curselection(),특백이호빈소기간.get())
def change38() :
    특백이호일.insert(특백이호.curselection(),특백이호상조회.get())
def change39() :
    특백이호일.insert(특백이호.curselection(),특백이호장지.get())
def change40() :
    특백이호일.insert(특백이호.curselection(),특백이호상차림.get())
def change41() :
    특백이호일.insert(특백이호.curselection(),특백이호상주.get())

def change42():
    특이백일호일.insert(특이백일호.curselection(),특이백일호상주성명.get())
def change43() :
    특이백일호일.insert(특이백일호.curselection(),특이백일호빈소기간.get())
def change44() :
    특이백일호일.insert(특이백일호.curselection(),특이백일호상조회.get())
def change45() :
    특이백일호일.insert(특이백일호.curselection(),특이백일호장지.get())
def change46() :
    특이백일호일.insert(특이백일호.curselection(),특이백일호상차림.get())
def change47() :
    특이백일호일.insert(특이백일호.curselection(),특이백일호상주.get())

def change48():
    특이백이호일.insert(특이백이호.curselection(),특이백이호상주성명.get())
def change49() :
    특이백이호일.insert(특이백이호.curselection(),특이백이호빈소기간.get())
def change50() :
    특이백이호일.insert(특이백이호.curselection(),특이백이호상조회.get())
def change51() :
    특이백이호일.insert(특이백이호.curselection(),특이백이호장지.get())
def change52() :
    특이백이호일.insert(특이백이호.curselection(),특이백이호상차림.get())
def change53() :
    특이백이호일.insert(특이백이호.curselection(),특이백이호상주.get())

# 1호 리스트박스 정의


일호=Listbox(selectmode='single', width=10, height=13)

일호상주성명 = Entry(width=15)
일호빈소기간 = Entry(width=15)
일호상조회 = Entry(width=15)
일호장지 = Entry(width=15)
일호상차림 = Entry(width=15)
일호상주 = Entry(width=15)

일호.insert(0,'')
일호.insert(1,' 상주성명')
일호.insert(2,'')
일호.insert(3,' 빈소기간')
일호.insert(4,'')
일호.insert(5,'   상조회')
일호.insert(6,'')
일호.insert(7,'    장지')
일호.insert(8,'')
일호.insert(9,'   상차림')
일호.insert(10,'')
일호.insert(11,'    상주')
일호.insert(12,'')
일호상주성명.pack()
일호빈소기간.pack()
일호상조회.pack()
일호장지.pack()
일호상차림.pack()
일호상주.pack()
일호.pack()


일호일=Listbox(selectmode='single', height=6)
일호일.pack()
일호일.place(x=325, y=125)





# 1호입력 버튼 정의


일호상주성명입력 =Button(text='입력', padx=1, pady=1, command=change)
일호상주성명입력.pack()
일호빈소기간입력 =Button(text='입력', padx=1, pady=1, command=change1)
일호빈소기간입력.pack()
일호상조회입력 =Button(text='입력', padx=1, pady=1, command=change2)
일호상조회입력.pack()
일호장지입력 =Button(text='입력', padx=1, pady=1, command=change3)
일호장지입력.pack()
일호상차림입력 =Button(text='입력', padx=1, pady=1, command=change4)
일호상차림입력.pack()
일호상주입력 =Button(text='입력', padx=1, pady=1, command=change5)
일호상주입력.pack()


# 1호 위치 정의

일호.place(x=40,y=60)
일호상주성명.place(x=135,y=80)
일호빈소기간.place(x=135,y=115)
일호상조회.place(x=135,y=150)
일호장지.place(x=135,y=185)
일호상차림.place(x=135,y=220)
일호상주.place(x=135,y=255)
일호상주성명입력.place(x=265,y=75)
일호빈소기간입력.place(x=265,y=110)
일호상조회입력.place(x=265,y=145)
일호장지입력.place(x=265,y=180)
일호상차림입력.place(x=265,y=215)
일호상주입력.place(x=265,y=250)


# 2호 리스트박스 정의


이호=Listbox(selectmode='single', width=10, height=13)

이호상주성명 = Entry(width=15)
이호빈소기간 = Entry(width=15)
이호상조회 = Entry(width=15)
이호장지 = Entry(width=15)
이호상차림 = Entry(width=15)
이호상주 = Entry(width=15)

이호.insert(0,'')
이호.insert(1,' 상주성명')
이호.insert(2,'')
이호.insert(3,' 빈소기간')
이호.insert(4,'')
이호.insert(5,'   상조회')
이호.insert(6,'')
이호.insert(7,'    장지')
이호.insert(8,'')
이호.insert(9,'   상차림')
이호.insert(10,'')
이호.insert(11,'    상주')
이호.insert(12,'')
이호상주성명.pack()
이호빈소기간.pack()
이호상조회.pack()
이호장지.pack()
이호상차림.pack()
이호상주.pack()
이호.pack()


이호일=Listbox(selectmode='single', height=6)
이호일.pack()
이호일.place(x=825, y=125)





# 2호 입력 버튼 정의


이호상주성명입력 =Button(text='입력', padx=1, pady=1, command=change6)
이호상주성명입력.pack()
이호빈소기간입력 =Button(text='입력', padx=1, pady=1, command=change7)
이호빈소기간입력.pack()
이호상조회입력 =Button(text='입력', padx=1, pady=1, command=change8)
이호상조회입력.pack()
이호장지입력 =Button(text='입력', padx=1, pady=1, command=change9)
이호장지입력.pack()
이호상차림입력 =Button(text='입력', padx=1, pady=1, command=change10)
이호상차림입력.pack()
이호상주입력 =Button(text='입력', padx=1, pady=1, command=change11)
이호상주입력.pack()


# 2호 위치 정의

이호.place(x=540,y=60)
이호상주성명.place(x=635,y=80)
이호빈소기간.place(x=635,y=115)
이호상조회.place(x=635,y=150)
이호장지.place(x=635,y=185)
이호상차림.place(x=635,y=220)
이호상주.place(x=635,y=255)
이호상주성명입력.place(x=765,y=75)
이호빈소기간입력.place(x=765,y=110)
이호상조회입력.place(x=765,y=145)
이호장지입력.place(x=765,y=180)
이호상차림입력.place(x=765,y=215)
이호상주입력.place(x=765,y=250)

# 3호 리스트박스 정의


삼호=Listbox(selectmode='single', width=10, height=13)

삼호상주성명 = Entry(width=15)
삼호빈소기간 = Entry(width=15)
삼호상조회 = Entry(width=15)
삼호장지 = Entry(width=15)
삼호상차림 = Entry(width=15)
삼호상주 = Entry(width=15)

삼호.insert(0,'')
삼호.insert(1,' 상주성명')
삼호.insert(2,'')
삼호.insert(3,' 빈소기간')
삼호.insert(4,'')
삼호.insert(5,'   상조회')
삼호.insert(6,'')
삼호.insert(7,'    장지')
삼호.insert(8,'')
삼호.insert(9,'   상차림')
삼호.insert(10,'')
삼호.insert(11,'    상주')
삼호.insert(12,'')
삼호상주성명.pack()
삼호빈소기간.pack()
삼호상조회.pack()
삼호장지.pack()
삼호상차림.pack()
삼호상주.pack()
삼호.pack()


삼호일=Listbox(selectmode='single', height=6)
삼호일.pack()
삼호일.place(x=1325, y=125)





# 3호 입력 버튼 정의


삼호상주성명입력 =Button(text='입력', padx=1, pady=1, command=change12)
삼호상주성명입력.pack()
삼호빈소기간입력 =Button(text='입력', padx=1, pady=1, command=change13)
삼호빈소기간입력.pack()
삼호상조회입력 =Button(text='입력', padx=1, pady=1, command=change14)
삼호상조회입력.pack()
삼호장지입력 =Button(text='입력', padx=1, pady=1, command=change15)
삼호장지입력.pack()
삼호상차림입력 =Button(text='입력', padx=1, pady=1, command=change16)
삼호상차림입력.pack()
삼호상주입력 =Button(text='입력', padx=1, pady=1, command=change17)
삼호상주입력.pack()


# 3호 위치 정의

삼호.place(x=1040,y=60)
삼호상주성명.place(x=1135,y=80)
삼호빈소기간.place(x=1135,y=115)
삼호상조회.place(x=1135,y=150)
삼호장지.place(x=1135,y=185)
삼호상차림.place(x=1135,y=220)
삼호상주.place(x=1135,y=255)
삼호상주성명입력.place(x=1265,y=75)
삼호빈소기간입력.place(x=1265,y=110)
삼호상조회입력.place(x=1265,y=145)
삼호장지입력.place(x=1265,y=180)
삼호상차림입력.place(x=1265,y=215)
삼호상주입력.place(x=1265,y=250)


# 5호 리스트박스 정의


오호=Listbox(selectmode='single', width=10, height=13)

오호상주성명 = Entry(width=15)
오호빈소기간 = Entry(width=15)
오호상조회 = Entry(width=15)
오호장지 = Entry(width=15)
오호상차림 = Entry(width=15)
오호상주 = Entry(width=15)

오호.insert(0,'')
오호.insert(1,' 상주성명')
오호.insert(2,'')
오호.insert(3,' 빈소기간')
오호.insert(4,'')
오호.insert(5,'   상조회')
오호.insert(6,'')
오호.insert(7,'    장지')
오호.insert(8,'')
오호.insert(9,'   상차림')
오호.insert(10,'')
오호.insert(11,'    상주')
오호.insert(12,'')
오호상주성명.pack()
오호빈소기간.pack()
오호상조회.pack()
오호장지.pack()
오호상차림.pack()
오호상주.pack()
오호.pack()


오호일=Listbox(selectmode='single', height=6)
오호일.pack()
오호일.place(x=325, y=385)



# 5호입력 버튼 정의


오호상주성명입력 =Button(text='입력', padx=1, pady=1, command=change18)
오호상주성명입력.pack()
오호빈소기간입력 =Button(text='입력', padx=1, pady=1, command=change19)
오호빈소기간입력.pack()
오호상조회입력 =Button(text='입력', padx=1, pady=1, command=change20)
오호상조회입력.pack()
오호장지입력 =Button(text='입력', padx=1, pady=1, command=change21)
오호장지입력.pack()
오호상차림입력 =Button(text='입력', padx=1, pady=1, command=change22)
오호상차림입력.pack()
오호상주입력 =Button(text='입력', padx=1, pady=1, command=change23)
오호상주입력.pack()


# 5호 위치 정의

오호.place(x=40,y=320)
오호상주성명.place(x=135,y=340)
오호빈소기간.place(x=135,y=375)
오호상조회.place(x=135,y=410)
오호장지.place(x=135,y=445)
오호상차림.place(x=135,y=480)
오호상주.place(x=135,y=515)
오호상주성명입력.place(x=265,y=335)
오호빈소기간입력.place(x=265,y=370)
오호상조회입력.place(x=265,y=405)
오호장지입력.place(x=265,y=440)
오호상차림입력.place(x=265,y=475)
오호상주입력.place(x=265,y=510)


# 6호 리스트박스 정의


육호=Listbox(selectmode='single', width=10, height=13)

육호상주성명 = Entry(width=15)
육호빈소기간 = Entry(width=15)
육호상조회 = Entry(width=15)
육호장지 = Entry(width=15)
육호상차림 = Entry(width=15)
육호상주 = Entry(width=15)

육호.insert(0,'')
육호.insert(1,' 상주성명')
육호.insert(2,'')
육호.insert(3,' 빈소기간')
육호.insert(4,'')
육호.insert(5,'   상조회')
육호.insert(6,'')
육호.insert(7,'    장지')
육호.insert(8,'')
육호.insert(9,'   상차림')
육호.insert(10,'')
육호.insert(11,'    상주')
육호.insert(12,'')
육호상주성명.pack()
육호빈소기간.pack()
육호상조회.pack()
육호장지.pack()
육호상차림.pack()
육호상주.pack()
육호.pack()


육호일=Listbox(selectmode='single', height=6)
육호일.pack()
육호일.place(x=825, y=385)



# 6호입력 버튼 정의


육호상주성명입력 =Button(text='입력', padx=1, pady=1, command=change24)
육호상주성명입력.pack()
육호빈소기간입력 =Button(text='입력', padx=1, pady=1, command=change25)
육호빈소기간입력.pack()
육호상조회입력 =Button(text='입력', padx=1, pady=1, command=change26)
육호상조회입력.pack()
육호장지입력 =Button(text='입력', padx=1, pady=1, command=change27)
육호장지입력.pack()
육호상차림입력 =Button(text='입력', padx=1, pady=1, command=change28)
육호상차림입력.pack()
육호상주입력 =Button(text='입력', padx=1, pady=1, command=change29)
육호상주입력.pack()


# 6호 위치 정의

육호.place(x=540,y=320)
육호상주성명.place(x=635,y=340)
육호빈소기간.place(x=635,y=375)
육호상조회.place(x=635,y=410)
육호장지.place(x=635,y=445)
육호상차림.place(x=635,y=480)
육호상주.place(x=635,y=515)
육호상주성명입력.place(x=765,y=335)
육호빈소기간입력.place(x=765,y=370)
육호상조회입력.place(x=765,y=405)
육호장지입력.place(x=765,y=440)
육호상차림입력.place(x=765,y=475)
육호상주입력.place(x=765,y=510)



# 특101호 리스트박스 정의


특백일호=Listbox(selectmode='single', width=10, height=13)

특백일호상주성명 = Entry(width=15)
특백일호빈소기간 = Entry(width=15)
특백일호상조회 = Entry(width=15)
특백일호장지 = Entry(width=15)
특백일호상차림 = Entry(width=15)
특백일호상주 = Entry(width=15)

특백일호.insert(0,'')
특백일호.insert(1,' 상주성명')
특백일호.insert(2,'')
특백일호.insert(3,' 빈소기간')
특백일호.insert(4,'')
특백일호.insert(5,'   상조회')
특백일호.insert(6,'')
특백일호.insert(7,'    장지')
특백일호.insert(8,'')
특백일호.insert(9,'   상차림')
특백일호.insert(10,'')
특백일호.insert(11,'    상주')
특백일호.insert(12,'')
특백일호상주성명.pack()
특백일호빈소기간.pack()
특백일호상조회.pack()
특백일호장지.pack()
특백일호상차림.pack()
특백일호상주.pack()
특백일호.pack()


특백일호일=Listbox(selectmode='single', height=6)
특백일호일.pack()
특백일호일.place(x=1325, y=385)



# 특101호입력 버튼 정의


특백일호상주성명입력 =Button(text='입력', padx=1, pady=1, command=change30)
특백일호상주성명입력.pack()
특백일호빈소기간입력 =Button(text='입력', padx=1, pady=1, command=change31)
특백일호빈소기간입력.pack()
특백일호상조회입력 =Button(text='입력', padx=1, pady=1, command=change32)
특백일호상조회입력.pack()
특백일호장지입력 =Button(text='입력', padx=1, pady=1, command=change33)
특백일호장지입력.pack()
특백일호상차림입력 =Button(text='입력', padx=1, pady=1, command=change34)
특백일호상차림입력.pack()
특백일호상주입력 =Button(text='입력', padx=1, pady=1, command=change35)
특백일호상주입력.pack()


# 특101호 위치 정의

특백일호.place(x=1040,y=320)
특백일호상주성명.place(x=1135,y=340)
특백일호빈소기간.place(x=1135,y=375)
특백일호상조회.place(x=1135,y=410)
특백일호장지.place(x=1135,y=445)
특백일호상차림.place(x=1135,y=480)
특백일호상주.place(x=1135,y=515)
특백일호상주성명입력.place(x=1265,y=335)
특백일호빈소기간입력.place(x=1265,y=370)
특백일호상조회입력.place(x=1265,y=405)
특백일호장지입력.place(x=1265,y=440)
특백일호상차림입력.place(x=1265,y=475)
특백일호상주입력.place(x=1265,y=510)




# 특102호 리스트박스 정의


특백이호=Listbox(selectmode='single', width=10, height=13)

특백이호상주성명 = Entry(width=15)
특백이호빈소기간 = Entry(width=15)
특백이호상조회 = Entry(width=15)
특백이호장지 = Entry(width=15)
특백이호상차림 = Entry(width=15)
특백이호상주 = Entry(width=15)

특백이호.insert(0,'')
특백이호.insert(1,' 상주성명')
특백이호.insert(2,'')
특백이호.insert(3,' 빈소기간')
특백이호.insert(4,'')
특백이호.insert(5,'   상조회')
특백이호.insert(6,'')
특백이호.insert(7,'    장지')
특백이호.insert(8,'')
특백이호.insert(9,'   상차림')
특백이호.insert(10,'')
특백이호.insert(11,'    상주')
특백이호.insert(12,'')
특백이호상주성명.pack()
특백이호빈소기간.pack()
특백이호상조회.pack()
특백이호장지.pack()
특백이호상차림.pack()
특백이호상주.pack()
특백이호.pack()


특백이호일=Listbox(selectmode='single', height=6)
특백이호일.pack()
특백이호일.place(x=325, y=645)





# 특102호입력 버튼 정의


특백이호상주성명입력 =Button(text='입력', padx=1, pady=1, command=change36)
특백이호상주성명입력.pack()
특백이호빈소기간입력 =Button(text='입력', padx=1, pady=1, command=change37)
특백이호빈소기간입력.pack()
특백이호상조회입력 =Button(text='입력', padx=1, pady=1, command=change38)
특백이호상조회입력.pack()
특백이호장지입력 =Button(text='입력', padx=1, pady=1, command=change39)
특백이호장지입력.pack()
특백이호상차림입력 =Button(text='입력', padx=1, pady=1, command=change40)
특백이호상차림입력.pack()
특백이호상주입력 =Button(text='입력', padx=1, pady=1, command=change41)
특백이호상주입력.pack()


# 특102호 위치 정의

특백이호.place(x=40,y=580)
특백이호상주성명.place(x=135,y=600)
특백이호빈소기간.place(x=135,y=635)
특백이호상조회.place(x=135,y=670)
특백이호장지.place(x=135,y=705)
특백이호상차림.place(x=135,y=740)
특백이호상주.place(x=135,y=775)
특백이호상주성명입력.place(x=265,y=595)
특백이호빈소기간입력.place(x=265,y=630)
특백이호상조회입력.place(x=265,y=665)
특백이호장지입력.place(x=265,y=700)
특백이호상차림입력.place(x=265,y=735)
특백이호상주입력.place(x=265,y=770)



# 특201호 리스트박스 정의


특이백일호=Listbox(selectmode='single', width=10, height=13)

특이백일호상주성명 = Entry(width=15)
특이백일호빈소기간 = Entry(width=15)
특이백일호상조회 = Entry(width=15)
특이백일호장지 = Entry(width=15)
특이백일호상차림 = Entry(width=15)
특이백일호상주 = Entry(width=15)

특이백일호.insert(0,'')
특이백일호.insert(1,' 상주성명')
특이백일호.insert(2,'')
특이백일호.insert(3,' 빈소기간')
특이백일호.insert(4,'')
특이백일호.insert(5,'   상조회')
특이백일호.insert(6,'')
특이백일호.insert(7,'    장지')
특이백일호.insert(8,'')
특이백일호.insert(9,'   상차림')
특이백일호.insert(10,'')
특이백일호.insert(11,'    상주')
특이백일호.insert(12,'')
특이백일호상주성명.pack()
특이백일호빈소기간.pack()
특이백일호상조회.pack()
특이백일호장지.pack()
특이백일호상차림.pack()
특이백일호상주.pack()
특이백일호.pack()


특이백일호일=Listbox(selectmode='single', height=6)
특이백일호일.pack()
특이백일호일.place(x=825, y=645)





# 특201호입력 버튼 정의


특이백일호상주성명입력 =Button(text='입력', padx=1, pady=1, command=change42)
특이백일호상주성명입력.pack()
특이백일호빈소기간입력 =Button(text='입력', padx=1, pady=1, command=change43)
특이백일호빈소기간입력.pack()
특이백일호상조회입력 =Button(text='입력', padx=1, pady=1, command=change44)
특이백일호상조회입력.pack()
특이백일호장지입력 =Button(text='입력', padx=1, pady=1, command=change45)
특이백일호장지입력.pack()
특이백일호상차림입력 =Button(text='입력', padx=1, pady=1, command=change46)
특이백일호상차림입력.pack()
특이백일호상주입력 =Button(text='입력', padx=1, pady=1, command=change47)
특이백일호상주입력.pack()


# 특201호 위치 정의

특이백일호.place(x=540,y=580)
특이백일호상주성명.place(x=635,y=600)
특이백일호빈소기간.place(x=635,y=635)
특이백일호상조회.place(x=635,y=670)
특이백일호장지.place(x=635,y=705)
특이백일호상차림.place(x=635,y=740)
특이백일호상주.place(x=635,y=775)
특이백일호상주성명입력.place(x=765,y=595)
특이백일호빈소기간입력.place(x=765,y=630)
특이백일호상조회입력.place(x=765,y=665)
특이백일호장지입력.place(x=765,y=700)
특이백일호상차림입력.place(x=765,y=735)
특이백일호상주입력.place(x=765,y=770)

# 특202호 리스트박스 정의


특이백이호=Listbox(selectmode='single', width=10, height=13)

특이백이호상주성명 = Entry(width=15)
특이백이호빈소기간 = Entry(width=15)
특이백이호상조회 = Entry(width=15)
특이백이호장지 = Entry(width=15)
특이백이호상차림 = Entry(width=15)
특이백이호상주 = Entry(width=15)

특이백이호.insert(0,'')
특이백이호.insert(1,' 상주성명')
특이백이호.insert(2,'')
특이백이호.insert(3,' 빈소기간')
특이백이호.insert(4,'')
특이백이호.insert(5,'   상조회')
특이백이호.insert(6,'')
특이백이호.insert(7,'    장지')
특이백이호.insert(8,'')
특이백이호.insert(9,'   상차림')
특이백이호.insert(10,'')
특이백이호.insert(11,'    상주')
특이백이호.insert(12,'')
특이백이호상주성명.pack()
특이백이호빈소기간.pack()
특이백이호상조회.pack()
특이백이호장지.pack()
특이백이호상차림.pack()
특이백이호상주.pack()
특이백이호.pack()


특이백이호일=Listbox(selectmode='single', height=6)
특이백이호일.pack()
특이백이호일.place(x=1325, y=645)





# 특202호입력 버튼 정의


특이백이호상주성명입력 =Button(text='입력', padx=1, pady=1, command=change48)
특이백이호상주성명입력.pack()
특이백이호빈소기간입력 =Button(text='입력', padx=1, pady=1, command=change49)
특이백이호빈소기간입력.pack()
특이백이호상조회입력 =Button(text='입력', padx=1, pady=1, command=change50)
특이백이호상조회입력.pack()
특이백이호장지입력 =Button(text='입력', padx=1, pady=1, command=change51)
특이백이호장지입력.pack()
특이백이호상차림입력 =Button(text='입력', padx=1, pady=1, command=change52)
특이백이호상차림입력.pack()
특이백이호상주입력 =Button(text='입력', padx=1, pady=1, command=change53)
특이백이호상주입력.pack()


# 특202호 위치 정의

특이백이호.place(x=1040,y=580)
특이백이호상주성명.place(x=1135,y=600)
특이백이호빈소기간.place(x=1135,y=635)
특이백이호상조회.place(x=1135,y=670)
특이백이호장지.place(x=1135,y=705)
특이백이호상차림.place(x=1135,y=740)
특이백이호상주.place(x=1135,y=775)
특이백이호상주성명입력.place(x=1265,y=595)
특이백이호빈소기간입력.place(x=1265,y=630)
특이백이호상조회입력.place(x=1265,y=665)
특이백이호장지입력.place(x=1265,y=700)
특이백이호상차림입력.place(x=1265,y=735)
특이백이호상주입력.place(x=1265,y=770)


win.mainloop()