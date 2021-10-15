from Tkinter.ProgramInterface import *
from Tkinter.TimerInterface import *
from Pakosti.PCFunctions import *
import json
from os import path


def create_timer():
    global timer
    with open(path.abspath('data.json'), 'r') as f:
        data = json.load(f)
    timer = Timer(data['timeout'], data['selected_pakosti'], data['allowable_time'], lambda: pakosti.create_pacost(data['selected_pakosti']))


pakosti = Pakosti()
interface = TkinterInterface(pakosti.list_pakosti, create_timer)
