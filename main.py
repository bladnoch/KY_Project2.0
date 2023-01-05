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

    button1 = tkinter.Button(window, text="입력",overrelief="solid", width=10, repeatdelay=1000, repeatinterval=100)
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
    상주1 = tkinter.Label(window, text="상주성명", width=10, height=1, relief="solid",background="white")
    상주1.place(x=20, y=140)

    상주성명1 = tkinter.Label(window, text=pinfo_sheet['A2'].value, width=20, height=1, relief="solid",background="white")
    상주성명1.place(x=100, y=40)
    빈소기간1 = tkinter.Label(window, text=" ", width=20, height=1, relief="solid",background="white")
    빈소기간1.place(x=100, y=60)
    상조회1 = tkinter.Label(window, text=" ", width=20, height=1, relief="solid",background="white")
    상조회1.place(x=100, y=80)
    장지1 = tkinter.Label(window, text=" ", width=20, height=1, relief="solid",background="white")
    장지1.place(x=100, y=100)
    상차림1 = tkinter.Label(window, text=" ", width=20, height=1, relief="solid",background="white")
    상차림1.place(x=100, y=120)
    상주1 = tkinter.Label(window, text=" ", width=20, height=1, relief="solid",background="white")
    상주1.place(x=100, y=140)

    #---------

    button2 = tkinter.Button(window, text="입력", overrelief="solid", width=10, repeatdelay=1000, repeatinterval=100)
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
    상주2 = tkinter.Label(window, text="상주성명", width=10, height=1, relief="solid", background="white")
    상주2.place(x=20+400, y=140)

    상주성명2 = tkinter.Label(window, text=" ", width=20, height=1, relief="solid", background="white")
    상주성명2.place(x=100+400, y=40)
    빈소기간2 = tkinter.Label(window, text=" ", width=20, height=1, relief="solid", background="white")
    빈소기간2.place(x=100+400, y=60)
    상조회2 = tkinter.Label(window, text=" ", width=20, height=1, relief="solid", background="white")
    상조회2.place(x=100+400, y=80)
    장지2 = tkinter.Label(window, text=" ", width=20, height=1, relief="solid", background="white")
    장지2.place(x=100+400, y=100)
    상차림2 = tkinter.Label(window, text=" ", width=20, height=1, relief="solid", background="white")
    상차림2.place(x=100+400, y=120)
    상주2 = tkinter.Label(window, text=" ", width=20, height=1, relief="solid", background="white")
    상주2.place(x=100+400, y=140)

    #--------

    button3 = tkinter.Button(window, text="입력", overrelief="solid", width=10, repeatdelay=1000, repeatinterval=100)
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
    상주3 = tkinter.Label(window, text="상주성명", width=10, height=1, relief="solid", background="white")
    상주3.place(x=20 + 800, y=140)

    상주성명3 = tkinter.Label(window, text=" ", width=20, height=1, relief="solid", background="white")
    상주성명3.place(x=100 + 800, y=40)
    빈소기간3 = tkinter.Label(window, text=" ", width=20, height=1, relief="solid", background="white")
    빈소기간3.place(x=100 + 800, y=60)
    상조회3 = tkinter.Label(window, text=" ", width=20, height=1, relief="solid", background="white")
    상조회3.place(x=100 + 800, y=80)
    장지3 = tkinter.Label(window, text=" ", width=20, height=1, relief="solid", background="white")
    장지3.place(x=100 + 800, y=100)
    상차림3 = tkinter.Label(window, text=" ", width=20, height=1, relief="solid", background="white")
    상차림3.place(x=100 + 800, y=120)
    상주3 = tkinter.Label(window, text=" ", width=20, height=1, relief="solid", background="white")
    상주3.place(x=100 + 800, y=140)

    window.mainloop()