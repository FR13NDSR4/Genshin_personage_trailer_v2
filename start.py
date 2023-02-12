from customtkinter import *
from customtkinter import CTkButton
from Mondstat import *
from Li_Yue import *
from Inazuma import *
from Sumeru import *

set_appearance_mode("dark")
set_default_color_theme("blue")
window = CTk()
window.geometry("500x500")
window.title("Genshin Trailer")
frame_1 = CTkFrame(master=window)
frame_1.pack(pady=1, padx=10, fill="both", expand=True)
autor_label = CTkLabel(master=frame_1, text="Author: https://github.com/FR13NDSR4", font=("arial", 15))
autor_label.place(x=200, y=460)


main_label = CTkLabel(master=frame_1, text="Choose region of personage: ", font=("arial", 25))
main_label.place(x=75, y=20)


def clear():
    all_widgets = window.place_slaves()
    for ca in all_widgets:
        ca.destroy()
    start()


clear_label = CTkButton(master=frame_1, text="Home", command=clear)
clear_label.place(x=9, y=460)


def start():
    mondstat_button = CTkButton(master=frame_1, text="Mondstat", command=mond)
    mondstat_button.place(x=150, y=200)
    li_yue_button = CTkButton(master=frame_1, text="Li Yue", fg_color="brown", command=li_yue)
    li_yue_button.place(x=150, y=240)
    inazuma_button = CTkButton(master=frame_1, text="Inazuma", fg_color="purple", command=inazuma)
    inazuma_button.place(x=150, y=280)
    sumeru_button = CTkButton(master=frame_1, text="Sumeru", fg_color="green", command=sumeru)
    sumeru_button.place(x=150, y=320)


def mond():
    Fishl_button = CTkButton(master=frame_1, text="Fishl", command=mondstat1)
    Fishl_button.place(x=150, y=200)
    Mona_button = CTkButton(master=frame_1, text="Mona", command=mondstat2)
    Mona_button.place(x=150, y=240)
    Venti_button = CTkButton(master=frame_1, text="Venti", command=mondstat3)
    Venti_button.place(x=150, y=280)
    Klee_button = CTkButton(master=frame_1, text="Klee", command=mondstat4)
    Klee_button.place(x=150, y=320)


def li_yue():
    Cici_button = CTkButton(master=frame_1, text="Cici", command=li_yue1, fg_color="brown")
    Cici_button.place(x=150, y=200)
    Xiao_button = CTkButton(master=frame_1, text="Xiao", command=li_yue2, fg_color="brown")
    Xiao_button.place(x=150, y=240)
    HuTao_button = CTkButton(master=frame_1, text="Venti", command=li_yue3, fg_color="brown")
    HuTao_button.place(x=150, y=280)
    Zhongli_button = CTkButton(master=frame_1, text="Klee", command=li_yue4, fg_color="brown")
    Zhongli_button.place(x=150, y=320)


def inazuma():
    Kazuha_button = CTkButton(master=frame_1, text="Kazuha", command=inazuma1, fg_color="purple")
    Kazuha_button.place(x=150, y=200)
    Raiden_button = CTkButton(master=frame_1, text="Raiden", command=inazuma2, fg_color="purple")
    Raiden_button.place(x=150, y=240)
    Balladeer_button = CTkButton(master=frame_1, text="Baladeer", command=inazuma3, fg_color="purple")
    Balladeer_button.place(x=150, y=280)
    Sara_button = CTkButton(master=frame_1, text="Sara", command=inazuma4, fg_color="purple")
    Sara_button.place(x=150, y=320)


def sumeru():
    Tignari_button = CTkButton(master=frame_1, text="Tignari", command=sumeru1, fg_color="green")
    Tignari_button.place(x=150, y=200)
    Nahida_button = CTkButton(master=frame_1, text="Nahida", command=sumeru2, fg_color="green")
    Nahida_button.place(x=150, y=240)
    Syno_button = CTkButton(master=frame_1, text="Syno", command=sumeru3, fg_color="green")
    Syno_button.place(x=150, y=280)
    Dori_button = CTkButton(master=frame_1, text="Dori", command=sumeru4, fg_color="green")
    Dori_button.place(x=150, y=320)


if __name__ == "__main__":
    start()

window.mainloop()
