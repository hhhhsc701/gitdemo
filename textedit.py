#文本编辑器
import re
import webbrowser
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.figure import Figure
from tkinter import *
from tkinter import filedialog
from tkinter.scrolledtext import ScrolledText
import tkinter.messagebox as tm

#创建界面
root = Tk()
root.geometry('600x500')
root.title('文本编辑器')

#去标点并转换小写,除去单词间的空格并以列表形式输出
def get_content(path):  
    punctuation='!"#$%&\'()*+,-./:;<=>?@[\\]^_`{|}~…'
    re_punctuation = "[{}]+".format(punctuation)
    with open(path,'r',encoding='gbk',errors='ignore')as f:
        content=''
        for l in f:
            l.strip()
            content += l
        line = re.sub(re_punctuation,"",content.lower())
        return line.split()