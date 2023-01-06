import tkinter
from tkinter import * # tkinter의 모든 함수 가져오기
from tkinter import messagebox, filedialog
import os
from pathlib import Path
import openpyxl
import os.path
from openpyxl.worksheet.table import Table, TableStyleInfo
import tkinter.ttk
import tkinter as tk

def b1():
    global b
    b=1
    print(b)
    put()
def b2():
    global b
    b=2
    print(b)
    put()
def b3():
    global b
    b=3
    print(b)
    put()
def put():
    def close():
        wi.quit()
        wi.destroy()
    def setcell():
        global b
        pinfo_sheet.cell(b, 1).value = 상주성명e.get()
        pinfo_sheet.cell(b, 2).value = 빈소기간e.get()
        pinfo_sheet.cell(b, 3).value = 상조회e.get()
        pinfo_sheet.cell(b, 4).value = 장지e.get()
        pinfo_sheet.cell(b, 5).value = 상차림e.get()
        pinfo_sheet.cell(b, 6).value = 상주e.get()
        info_file.save(info_xl)
        close()
        showpage()

    wi = tk.Tk()  # 창 생성
    wi.geometry("320x250")  # 창의 크기
    wi.title("장례식장 재고관리 프로그램 Ver1.221123")  # 창의 제목
    wi.option_add("*Font", "맑은고딕 12")  # 전체 폰트


    상주성명 = tkinter.Label(wi, text="상주성명", width=10, height=1, relief="solid", background="white")
    상주성명.place(x=20, y=20)
    빈소기간 = tkinter.Label(wi, text="빈소기간", width=10, height=1, relief="solid", background="white")
    빈소기간.place(x=20, y=50)
    상조회 = tkinter.Label(wi, text="상조회", width=10, height=1, relief="solid", background="white")
    상조회.place(x=20, y=80)
    장지 = tkinter.Label(wi, text="장지", width=10, height=1, relief="solid", background="white")
    장지.place(x=20, y=110)
    상차림 = tkinter.Label(wi, text="상차림", width=10, height=1, relief="solid", background="white")
    상차림.place(x=20, y=140)
    상주 = tkinter.Label(wi, text="상주", width=10, height=1, relief="solid", background="white")
    상주.place(x=20, y=170)

    상주성명e = tkinter.Entry(wi)
    상주성명e.place(x=120, y=20)
    빈소기간e = tkinter.Entry(wi)
    빈소기간e.place(x=120, y=50)
    상조회e = tkinter.Entry(wi)
    상조회e.place(x=120, y=80)
    장지e = tkinter.Entry(wi)
    장지e.place(x=120, y=110)
    상차림e = tkinter.Entry(wi)
    상차림e.place(x=120, y=140)
    상주e = tkinter.Entry(wi)
    상주e.place(x=120, y=170)

    입력 = tkinter.Button(wi, text="입력", overrelief="solid", width=10, height=2, repeatdelay=1000, repeatinterval=100,command=setcell)
    입력.place(x=20, y=200)

    취소 = tkinter.Button(wi, text="취소", overrelief="solid", width=10, height=2, repeatdelay=1000, repeatinterval=100,command=close)
    취소.place(x=140, y=200)

    wi.mainloop()
def showpage():
    button1 = tkinter.Button(window, text="입력", overrelief="solid", width=10, repeatdelay=1000, repeatinterval=100,
                             command=b1)
    button1.place(x=20, y=160)

    빈소1 = tkinter.Label(window, text="빈소1", width=30, height=1, relief="solid", background="white")
    빈소1.place(x=20, y=20)
    상주성명1 = tkinter.Label(window, text="상주성명", width=10, height=1, relief="solid", background="white")
    상주성명1.place(x=20, y=40)
    빈소기간1 = tkinter.Label(window, text="빈소기간", width=10, height=1, relief="solid", background="white")
    빈소기간1.place(x=20, y=60)
    상조회1 = tkinter.Label(window, text="상조회", width=10, height=1, relief="solid", background="white")
    상조회1.place(x=20, y=80)
    장지1 = tkinter.Label(window, text="장지", width=10, height=1, relief="solid", background="white")
    장지1.place(x=20, y=100)
    상차림1 = tkinter.Label(window, text="상차림", width=10, height=1, relief="solid", background="white")
    상차림1.place(x=20, y=120)
    상주1 = tkinter.Label(window, text="상주", width=10, height=1, relief="solid", background="white")
    상주1.place(x=20, y=140)

    상주성명11 = tkinter.Label(window, text=pinfo_sheet['A1'].value, width=20, height=1, relief="solid", background="white")
    상주성명11.place(x=100, y=40)
    빈소기간11 = tkinter.Label(window, text=pinfo_sheet['B1'].value, width=20, height=1, relief="solid", background="white")
    빈소기간11.place(x=100, y=60)
    상조회11 = tkinter.Label(window, text=pinfo_sheet['C1'].value, width=20, height=1, relief="solid", background="white")
    상조회11.place(x=100, y=80)
    장지11 = tkinter.Label(window, text=pinfo_sheet['D1'].value, width=20, height=1, relief="solid", background="white")
    장지11.place(x=100, y=100)
    상차림11 = tkinter.Label(window, text=pinfo_sheet['E1'].value, width=20, height=1, relief="solid", background="white")
    상차림11.place(x=100, y=120)
    상주11 = tkinter.Label(window, text=pinfo_sheet['F1'].value, width=20, height=1, relief="solid", background="white")
    상주11.place(x=100, y=140)

    # ---------

    button2 = tkinter.Button(window, text="입력", overrelief="solid", width=10, repeatdelay=1000, repeatinterval=100,
                             command=b2)
    button2.place(x=20 + 400, y=160)

    빈소2 = tkinter.Label(window, text="빈소2", width=30, height=1, relief="solid", background="white")
    빈소2.place(x=20 + 400, y=20)
    상주성명2 = tkinter.Label(window, text="상주성명", width=10, height=1, relief="solid", background="white")
    상주성명2.place(x=20 + 400, y=40)
    빈소기간2 = tkinter.Label(window, text="빈소기간", width=10, height=1, relief="solid", background="white")
    빈소기간2.place(x=20 + 400, y=60)
    상조회2 = tkinter.Label(window, text="상조회", width=10, height=1, relief="solid", background="white")
    상조회2.place(x=20 + 400, y=80)
    장지2 = tkinter.Label(window, text="장지", width=10, height=1, relief="solid", background="white")
    장지2.place(x=20 + 400, y=100)
    상차림2 = tkinter.Label(window, text="상차림", width=10, height=1, relief="solid", background="white")
    상차림2.place(x=20 + 400, y=120)
    상주2 = tkinter.Label(window, text="상주", width=10, height=1, relief="solid", background="white")
    상주2.place(x=20 + 400, y=140)

    상주성명22 = tkinter.Label(window, text=pinfo_sheet['A2'].value, width=20, height=1, relief="solid", background="white")
    상주성명22.place(x=100 + 400, y=40)
    빈소기간22 = tkinter.Label(window, text=pinfo_sheet['B2'].value, width=20, height=1, relief="solid", background="white")
    빈소기간22.place(x=100 + 400, y=60)
    상조회22 = tkinter.Label(window, text=pinfo_sheet['C2'].value, width=20, height=1, relief="solid", background="white")
    상조회22.place(x=100 + 400, y=80)
    장지22 = tkinter.Label(window, text=pinfo_sheet['D2'].value, width=20, height=1, relief="solid", background="white")
    장지22.place(x=100 + 400, y=100)
    상차림22 = tkinter.Label(window, text=pinfo_sheet['E2'].value, width=20, height=1, relief="solid", background="white")
    상차림22.place(x=100 + 400, y=120)
    상주22 = tkinter.Label(window, text=pinfo_sheet['F2'].value, width=20, height=1, relief="solid", background="white")
    상주22.place(x=100 + 400, y=140)

    # --------

    button3 = tkinter.Button(window, text="입력", overrelief="solid", width=10, repeatdelay=1000, repeatinterval=100,
                             command=b3)
    button3.place(x=20 + 800, y=160)

    빈소3 = tkinter.Label(window, text="빈소3", width=30, height=1, relief="solid", background="white")
    빈소3.place(x=20 + 800, y=20)
    상주성명3 = tkinter.Label(window, text="상주성명", width=10, height=1, relief="solid", background="white")
    상주성명3.place(x=20 + 800, y=40)
    빈소기간3 = tkinter.Label(window, text="빈소기간", width=10, height=1, relief="solid", background="white")
    빈소기간3.place(x=20 + 800, y=60)
    상조회3 = tkinter.Label(window, text="상조회", width=10, height=1, relief="solid", background="white")
    상조회3.place(x=20 + 800, y=80)
    장지3 = tkinter.Label(window, text="장지", width=10, height=1, relief="solid", background="white")
    장지3.place(x=20 + 800, y=100)
    상차림3 = tkinter.Label(window, text="상차림", width=10, height=1, relief="solid", background="white")
    상차림3.place(x=20 + 800, y=120)
    상주3 = tkinter.Label(window, text="상주", width=10, height=1, relief="solid", background="white")
    상주3.place(x=20 + 800, y=140)

    상주성명33 = tkinter.Label(window, text=pinfo_sheet['A3'].value, width=20, height=1, relief="solid", background="white")
    상주성명33.place(x=100 + 800, y=40)
    빈소기간33 = tkinter.Label(window, text=pinfo_sheet['B3'].value, width=20, height=1, relief="solid", background="white")
    빈소기간33.place(x=100 + 800, y=60)
    상조회33 = tkinter.Label(window, text=pinfo_sheet['C3'].value, width=20, height=1, relief="solid", background="white")
    상조회33.place(x=100 + 800, y=80)
    장지33 = tkinter.Label(window, text=pinfo_sheet['D3'].value, width=20, height=1, relief="solid", background="white")
    장지33.place(x=100 + 800, y=100)
    상차림33 = tkinter.Label(window, text=pinfo_sheet['E3'].value, width=20, height=1, relief="solid", background="white")
    상차림33.place(x=100 + 800, y=120)
    상주33 = tkinter.Label(window, text=pinfo_sheet['F3'].value, width=20, height=1, relief="solid", background="white")
    상주33.place(x=100 + 800, y=140)
if __name__ == "__main__":
    home = 'xl/전체물품리스트_세트저장용.xlsx'
    info_xl='xl/personal.xlsx'

    og_file= openpyxl.load_workbook(home, data_only=True) #초기 시트 위치 저장(값으로)
    info_file=openpyxl.load_workbook(info_xl,data_only=True) #개인정보, 빈소별 물품정보 저장 공간(값으)

    info_sheets=[info_file['빈소1'],info_file['빈소2'],info_file['빈소3'],info_file['빈소5'],info_file['빈소6'],info_file['특101'],info_file['특102'],info_file['특201'],info_file['특202']]
    og_sheets=[og_file['식당판매'], og_file['매점판매'], og_file['장의용품'], og_file['상복'], og_file['기타']]
    set_sheet=og_file['세트']
    pinfo_sheet=info_file['개인정보'] #개인정보 출력용

    global temp_sheet #2
    global temp_sheet2 #2
    global room #2

    global b #1

    window = tk.Tk() # 창 생성
    window.geometry("1200x720") # 창의 크기
    window.title("장례식장 재고관리 프로그램 Ver1.221123") # 창의 제목
    window.option_add("*Font", "맑은고딕 12") # 전체 폰트

    button1 = tkinter.Button(window, text="입력",overrelief="solid", width=10, repeatdelay=1000, repeatinterval=100, command=b1)
    button1.place(x=20, y=160)

    빈소1 = tkinter.Label(window, text="빈소1", width=30, height=1, relief="solid",background="white")
    빈소1.place(x=20, y=20)
    상주성명1 = tkinter.Label(window, text="상주성명", width=10, height=1, relief="solid",background="white")
    상주성명1.place(x=20,y=40)
    빈소기간1 = tkinter.Label(window, text="빈소기간", width=10, height=1, relief="solid",background="white")
    빈소기간1.place(x=20, y=60)
    상조회1 = tkinter.Label(window, text="상조회", width=10, height=1, relief="solid",background="white")
    상조회1.place(x=20, y=80)
    장지1 = tkinter.Label(window, text="장지", width=10, height=1, relief="solid",background="white")
    장지1.place(x=20, y=100)
    상차림1 = tkinter.Label(window, text="상차림", width=10, height=1, relief="solid",background="white")
    상차림1.place(x=20, y=120)
    상주1 = tkinter.Label(window, text="상주", width=10, height=1, relief="solid",background="white")
    상주1.place(x=20, y=140)

    상주성명11 = tkinter.Label(window, text=pinfo_sheet['A1'].value, width=20, height=1, relief="solid",background="white")
    상주성명11.place(x=100, y=40)
    빈소기간11 = tkinter.Label(window, text=pinfo_sheet['B1'].value, width=20, height=1, relief="solid",background="white")
    빈소기간11.place(x=100, y=60)
    상조회11 = tkinter.Label(window, text=pinfo_sheet['C1'].value, width=20, height=1, relief="solid",background="white")
    상조회11.place(x=100, y=80)
    장지11 = tkinter.Label(window, text=pinfo_sheet['D1'].value, width=20, height=1, relief="solid",background="white")
    장지11.place(x=100, y=100)
    상차림11 = tkinter.Label(window, text=pinfo_sheet['E1'].value, width=20, height=1, relief="solid",background="white")
    상차림11.place(x=100, y=120)
    상주11 = tkinter.Label(window, text=pinfo_sheet['F1'].value, width=20, height=1, relief="solid",background="white")
    상주11.place(x=100, y=140)

    #---------

    button2 = tkinter.Button(window, text="입력", overrelief="solid", width=10, repeatdelay=1000, repeatinterval=100, command=b2)
    button2.place(x=20+400, y=160)

    빈소2 = tkinter.Label(window, text="빈소2", width=30, height=1, relief="solid", background="white")
    빈소2.place(x=20+400, y=20)
    상주성명2 = tkinter.Label(window, text="상주성명", width=10, height=1, relief="solid", background="white")
    상주성명2.place(x=20+400, y=40)
    빈소기간2 = tkinter.Label(window, text="빈소기간", width=10, height=1, relief="solid", background="white")
    빈소기간2.place(x=20+400, y=60)
    상조회2 = tkinter.Label(window, text="상조회", width=10, height=1, relief="solid", background="white")
    상조회2.place(x=20+400, y=80)
    장지2 = tkinter.Label(window, text="장지", width=10, height=1, relief="solid", background="white")
    장지2.place(x=20+400, y=100)
    상차림2 = tkinter.Label(window, text="상차림", width=10, height=1, relief="solid", background="white")
    상차림2.place(x=20+400, y=120)
    상주2 = tkinter.Label(window, text="상주", width=10, height=1, relief="solid", background="white")
    상주2.place(x=20+400, y=140)

    상주성명22 = tkinter.Label(window, text=pinfo_sheet['A2'].value, width=20, height=1, relief="solid", background="white")
    상주성명22.place(x=100+400, y=40)
    빈소기간22 = tkinter.Label(window, text=pinfo_sheet['B2'].value, width=20, height=1, relief="solid", background="white")
    빈소기간22.place(x=100+400, y=60)
    상조회22 = tkinter.Label(window, text=pinfo_sheet['C2'].value, width=20, height=1, relief="solid", background="white")
    상조회22.place(x=100+400, y=80)
    장지22 = tkinter.Label(window, text=pinfo_sheet['D2'].value, width=20, height=1, relief="solid", background="white")
    장지22.place(x=100+400, y=100)
    상차림22 = tkinter.Label(window, text=pinfo_sheet['E2'].value, width=20, height=1, relief="solid", background="white")
    상차림22.place(x=100+400, y=120)
    상주22 = tkinter.Label(window, text=pinfo_sheet['F2'].value, width=20, height=1, relief="solid", background="white")
    상주22.place(x=100+400, y=140)

    #--------

    button3 = tkinter.Button(window, text="입력", overrelief="solid", width=10, repeatdelay=1000, repeatinterval=100, command=b3)
    button3.place(x=20 + 800, y=160)

    빈소3 = tkinter.Label(window, text="빈소3", width=30, height=1, relief="solid", background="white")
    빈소3.place(x=20 + 800, y=20)
    상주성명3 = tkinter.Label(window, text="상주성명", width=10, height=1, relief="solid", background="white")
    상주성명3.place(x=20 + 800, y=40)
    빈소기간3 = tkinter.Label(window, text="빈소기간", width=10, height=1, relief="solid", background="white")
    빈소기간3.place(x=20 + 800, y=60)
    상조회3 = tkinter.Label(window, text="상조회", width=10, height=1, relief="solid", background="white")
    상조회3.place(x=20 + 800, y=80)
    장지3 = tkinter.Label(window, text="장지", width=10, height=1, relief="solid", background="white")
    장지3.place(x=20 + 800, y=100)
    상차림3 = tkinter.Label(window, text="상차림", width=10, height=1, relief="solid", background="white")
    상차림3.place(x=20 + 800, y=120)
    상주3 = tkinter.Label(window, text="상주", width=10, height=1, relief="solid", background="white")
    상주3.place(x=20 + 800, y=140)

    상주성명33 = tkinter.Label(window, text=pinfo_sheet['A3'].value, width=20, height=1, relief="solid", background="white")
    상주성명33.place(x=100 + 800, y=40)
    빈소기간33 = tkinter.Label(window, text=pinfo_sheet['B3'].value, width=20, height=1, relief="solid", background="white")
    빈소기간33.place(x=100 + 800, y=60)
    상조회33 = tkinter.Label(window, text=pinfo_sheet['C3'].value, width=20, height=1, relief="solid", background="white")
    상조회33.place(x=100 + 800, y=80)
    장지33 = tkinter.Label(window, text=pinfo_sheet['D3'].value, width=20, height=1, relief="solid", background="white")
    장지33.place(x=100 + 800, y=100)
    상차림33 = tkinter.Label(window, text=pinfo_sheet['E3'].value, width=20, height=1, relief="solid", background="white")
    상차림33.place(x=100 + 800, y=120)
    상주33 = tkinter.Label(window, text=pinfo_sheet['F3'].value, width=20, height=1, relief="solid", background="white")
    상주33.place(x=100 + 800, y=140)

    window.mainloop()