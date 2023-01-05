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

def put():
    wi = tk.Tk()  # 창 생성
    wi.geometry("400x200")  # 창의 크기
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
    상주성명e.place(x=150, y=20)
    wi.mainloop()

if __name__ == "__main__":
    home = 'xl/전체물품리스트_세트저장용.xlsx'
    info_xl='xl/personal.xlsx'

    og_file= openpyxl.load_workbook(home, data_only=True) #초기 시트 위치 저장(값으로)
    info_file=openpyxl.load_workbook(info_xl,data_only=True) #개인정보, 빈소별 물품정보 저장 공간(값으)

    info_sheets=[info_file['빈소1'],info_file['빈소2'],info_file['빈소3'],info_file['빈소5'],info_file['빈소6'],info_file['특101'],info_file['특102'],info_file['특201'],info_file['특202']]
    og_sheets=[og_file['식당판매'], og_file['매점판매'], og_file['장의용품'], og_file['상복'], og_file['기타']]
    set_sheet=og_file['세트']
    pinfo_sheet=info_file['개인정보'] #개인정보 출력용

    global temp_sheet
    global temp_sheet2
    global room

    window = tk.Tk() # 창 생성
    window.geometry("1200x720") # 창의 크기
    window.title("장례식장 재고관리 프로그램 Ver1.221123") # 창의 제목
    window.option_add("*Font", "맑은고딕 12") # 전체 폰트

    button1 = tkinter.Button(window, text="입력",overrelief="solid", width=10, repeatdelay=1000, repeatinterval=100, command=put)
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

    상주성명11 = tkinter.Label(window, text=pinfo_sheet['B1'].value, width=20, height=1, relief="solid",background="white")
    상주성명11.place(x=100, y=40)
    빈소기간11 = tkinter.Label(window, text=pinfo_sheet['D1'].value, width=20, height=1, relief="solid",background="white")
    빈소기간11.place(x=100, y=60)
    상조회11 = tkinter.Label(window, text=pinfo_sheet['E1'].value, width=20, height=1, relief="solid",background="white")
    상조회11.place(x=100, y=80)
    장지11 = tkinter.Label(window, text=pinfo_sheet['F1'].value, width=20, height=1, relief="solid",background="white")
    장지11.place(x=100, y=100)
    상차림11 = tkinter.Label(window, text=pinfo_sheet['G1'].value, width=20, height=1, relief="solid",background="white")
    상차림11.place(x=100, y=120)
    상주11 = tkinter.Label(window, text=pinfo_sheet['H1'].value, width=20, height=1, relief="solid",background="white")
    상주11.place(x=100, y=140)

    #---------

    button2 = tkinter.Button(window, text="입력", overrelief="solid", width=10, repeatdelay=1000, repeatinterval=100, command=put)
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

    상주성명22 = tkinter.Label(window, text=pinfo_sheet['B2'].value, width=20, height=1, relief="solid", background="white")
    상주성명22.place(x=100+400, y=40)
    빈소기간22 = tkinter.Label(window, text=pinfo_sheet['D2'].value, width=20, height=1, relief="solid", background="white")
    빈소기간22.place(x=100+400, y=60)
    상조회22 = tkinter.Label(window, text=pinfo_sheet['E2'].value, width=20, height=1, relief="solid", background="white")
    상조회22.place(x=100+400, y=80)
    장지22 = tkinter.Label(window, text=pinfo_sheet['F2'].value, width=20, height=1, relief="solid", background="white")
    장지22.place(x=100+400, y=100)
    상차림22 = tkinter.Label(window, text=pinfo_sheet['G2'].value, width=20, height=1, relief="solid", background="white")
    상차림22.place(x=100+400, y=120)
    상주22 = tkinter.Label(window, text=pinfo_sheet['H2'].value, width=20, height=1, relief="solid", background="white")
    상주22.place(x=100+400, y=140)

    #--------

    button3 = tkinter.Button(window, text="입력", overrelief="solid", width=10, repeatdelay=1000, repeatinterval=100, command=put)
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

    상주성명33 = tkinter.Label(window, text=pinfo_sheet['B3'].value, width=20, height=1, relief="solid", background="white")
    상주성명33.place(x=100 + 800, y=40)
    빈소기간33 = tkinter.Label(window, text=pinfo_sheet['D3'].value, width=20, height=1, relief="solid", background="white")
    빈소기간33.place(x=100 + 800, y=60)
    상조회33 = tkinter.Label(window, text=pinfo_sheet['E3'].value, width=20, height=1, relief="solid", background="white")
    상조회33.place(x=100 + 800, y=80)
    장지33 = tkinter.Label(window, text=pinfo_sheet['F3'].value, width=20, height=1, relief="solid", background="white")
    장지33.place(x=100 + 800, y=100)
    상차림33 = tkinter.Label(window, text=pinfo_sheet['G3'].value, width=20, height=1, relief="solid", background="white")
    상차림33.place(x=100 + 800, y=120)
    상주33 = tkinter.Label(window, text=pinfo_sheet['H3'].value, width=20, height=1, relief="solid", background="white")
    상주33.place(x=100 + 800, y=140)

    window.mainloop()