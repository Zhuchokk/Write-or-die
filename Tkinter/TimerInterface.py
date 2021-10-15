from tkinter import *
import json
from _thread import start_new_thread
from time import sleep
import keyboard


class Timer:
    def __init__(self, timeout, selected_pakosti, allowable_time, pakosti_func):
        self.root = Tk()
        self.root.geometry('350x150')
        self.root.title(f'Timer: {str(allowable_time) + ":" + "00"}')

        self.timeout = timeout
        self.selected_pakosti = selected_pakosti
        self.allowable_time = allowable_time
        self.local_time = str(allowable_time) + ":" + "00"
        self.timer = True

        self.clock_lbl = Label(self.root, text=self.local_time, font='Arial 30', fg='red')
        self.clock_lbl.grid(row=0, column=0, sticky='NSWE')
        self.clock_start = Button(self.root, text='Продолжить', font='Arial 13', fg='red', command=self._continue)
        self.clock_start.grid(row=1, column=0, sticky='NSWE')
        self.clock_start['state'] = 'disabled'
        self.clock_stop = Button(self.root, text='Стоп', font='Arial 13', fg='green', command=self.stop)
        self.clock_stop.grid(row=1, column=1, sticky='NSWE')
        self.clock_reset = Button(self.root, text='Заново', font='Arial 13', fg='black', command=self.reset)
        self.clock_reset.grid(row=1, column=2, sticky='NSWE')
        start_new_thread(self.countdown, (pakosti_func, ))
        start_new_thread(self.checker, ())
        self.root.protocol('WM_DELETE_WINDOW', quit)
        self.root.mainloop()

    def countdown(self, func):
        while self.local_time != '00:00':
            if self.timer:
                sleep(1)
                tmp = self.local_time.split(':')
                if tmp[1] == '00' and tmp[0] != '00':
                    tmp[1] = '59'
                    tmp[0] = str(int(tmp[0]) - 1)
                    if len(tmp[0]) == 1:
                        tmp[0] = '0' + tmp[0]
                else:
                    tmp[1] = str(int(tmp[1]) - 1)
                    if len(tmp[1]) == 1:
                        tmp[1] = '0' + tmp[1]
                self.local_time = tmp[0] + ':' + tmp[1]
                self.clock_lbl['text'] = self.local_time
                self.root.title('Timer: ' + self.local_time)
        func()
        self.local_time = str(self.timeout) + ':' + '00'
        return self.countdown(func)

    def _continue(self):
        self.timer = True
        self.clock_start['state'] = 'disabled'
        self.clock_stop['state'] = 'normal'

    def stop(self):
        self.timer = False
        self.clock_stop['state'] = 'disabled'
        self.clock_start['state'] = 'normal'

    def reset(self, plug):
        self.timer = False
        self.clock_start['state'] = 'disabled'
        self.clock_stop['state'] = 'normal'
        self.local_time = str(self.allowable_time) + ':' + '00'
        self.timer = True
        print(plug.name)

    def checker(self):
        keyboard.hook(self.reset)
        keyboard.wait()

