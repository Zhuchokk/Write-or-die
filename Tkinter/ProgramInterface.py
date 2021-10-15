from tkinter import *
import json
import os


class TkinterInterface:
    def __init__(self, pakosti, start_func):
        with open(os.path.abspath('data.json'), 'r') as f:
            self.data = json.load(f)
        print(os.path.abspath('data.json'))
        self.pakosti = pakosti
        self.start_func = start_func
        self.root = Tk()
        self.spin_var1 = IntVar()
        self.spin_var2 = IntVar()
        self.spin_var1.set(self.data['allowable_time'])
        self.spin_var2.set(self.data['timeout'])

        self.root.geometry('700x400')
        self.root.title(self.data['title'])
        self.heading_lbl = Label(self.root, text=self.data['title'], fg='red', font='Arial 25')
        self.heading_lbl.grid(row=0, column=0, sticky='NSWE')
        self.time_lbl = Label(self.root, text='Допустимое время бездействия(в минутах):', font='Arial 13')
        self.time_lbl.grid(row=1, column=0)
        self.time_spinbox = Spinbox(self.root, from_=1, to=600, width=7, textvariable=self.spin_var1)
        self.time_spinbox.grid(row=1, column=1)
        self.time_lbl = Label(self.root, text='Таймаут между пакостями(в минутах):', font='Arial 13')
        self.time_lbl.grid(row=2, column=0)
        self.pakosti_time_spinbox = Spinbox(self.root, from_=1, to=600, width=7, textvariable=self.spin_var2)
        self.pakosti_time_spinbox.grid(row=2, column=1)
        self.pakosti_lbl = Label(self.root, text='Пакости, которые будет использовать программа:', font='Arial 13')
        self.pakosti_lbl.grid(row=3, column=0)
        self.pakosti_checkbuttons = []
        ln = len(self.pakosti)
        self.pakosti_states = [BooleanVar() for _ in range(ln)]
        for i in range(ln):
            self.pakosti_states[i].set(pakosti[i] in self.data['selected_pakosti'])
            self.pakosti_checkbuttons.append(Checkbutton(self.root, text=pakosti[i], var=self.pakosti_states[i]))
            self.pakosti_checkbuttons[i].grid(row=i + 3, column=1)

        save_but = Button(self.root, text='Сохранить изменения', font='Arial 11', command=self.save_pakosti)
        save_but.grid(row=ln + 4, column=0, sticky='NSWE')
        start_but = Button(self.root, text='Старт!', font='Arial 11', fg='red', command=self.start_func)
        start_but.grid(row=ln + 4, column=1, sticky='NSWE')
        self.root.mainloop()

    def save_pakosti(self):
        self.data['selected_pakosti'] = []
        for i in range(len(self.pakosti_checkbuttons)):
            if self.pakosti_states[i].get():
                self.data['selected_pakosti'].append(self.pakosti_checkbuttons[i]["text"])
        self.data['allowable_time'] = int(self.time_spinbox.get())
        self.data['timeout'] = int(self.pakosti_time_spinbox.get())
        print(self.data)
        with open(os.path.abspath('data.json'), 'w') as f:
            json.dump(self.data, f)
