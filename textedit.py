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


#将停用词表转换为列表
def stop_word():
	file=open(r'E:\文档\大作业\英文停用词表.txt').readlines()
	stop_list=[i.replace(' \n','') for i in file]
	return stop_list

#去除停用词
def remove_stop(seg_list):
    new_list=[]
    stop_list=stop_word()
    for word in seg_list:
        if word not in stop_list:
            new_list.append(word)
    return new_list