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


#计算单词数量
def total_number():
    root1 = Toplevel(root)
    root1.geometry('300x200')
    root1.title('')
    num = '单词总数量为：'+str(len(list_))
    Label(root1,text=num).pack(pady=70)

#统计单词频率并输出
def get_f(words):
    tf_dic={}
    for w in words:
        tf_dic[w]=tf_dic.get(w,0)+1
    l = sorted(tf_dic.items(),key=lambda x:x[1],reverse=True)
    return l

#输出单词的频率并添加查询功能
def print_f():
    root3 = Toplevel(root)
    root3.geometry('400x300')
    root3.title('词频')
    text2 = ScrolledText(root3,width=30, height=20)
    text2.place(x=0)
    Label(root3,text='请输入你要查找的单词：').place(x=250)
    Label(root3,text='该单词的词频是：').place(x=250,y=80)
    E = Entry(root3,width=15)
    E.place(x=250,y=25)
    l = get_f(list_)
    l1 = [[],[]]
    a = -20
    for i in l:
        a += 20
        s = list(i)
        k = s[0]+':'+str(s[1])+'\n'
        text2.insert(END,k)
        l1[0].append(s[0])
        l1[1].append(s[1])
    def find():
        word = E.get()
        if word in l1[0]:
            Label(root3,text=str(l1[1][l1[0].index(word)])).place(x=350,y=80)
        else:
            tm.showerror(title='错误', message='未找到该单词')
            root3.destroy()
            print_f()
    Button(root3,text='查询',command=lambda :find()).place(x=285,y=50)