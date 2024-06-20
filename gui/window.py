from tkinter import *
from tkinter import messagebox
from Explorer import Explorer

if __name__=="__main__":
    root = Tk()
    root.geometry('600x400')
    root.maxsize(600, 400)
    root.minsize(600, 400)
    root.title('Программный классификатор')
    root.config(bg='#052561')

    SelectButton = Button(text="Выберите программу", command=Explorer.open_explorer)
    SelectButton.place(x=160, y=100)

    InfoButton = Button(text="О приложении", command=lambda : messagebox.showinfo(title="О приложении", message="Программный код прогоняется через "
                                                                                                                "классификатор, результатом чего является вывод о том,"
                                                                                                                "на каком ЯП написан входной код."))
    InfoButton.place(x=310, y=100)

    ClassifierButton = Button(text="Классифицировать", width=33, background="lightgreen")
    ClassifierButton.place(x=161, y=140)

    root.mainloop()