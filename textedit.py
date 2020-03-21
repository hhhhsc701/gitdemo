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


#频率最高的6个单词及其频率
def plot(l):
    x = []
    y = []
    for i in range(6):
        x.append(l[i][0])
        y.append(l[i][1])
    return x,y
    
#画出柱状图
def draw_picture():
    root2 = Toplevel(root)
    root2.title('关键词')
    f1 = Figure(figsize=(5, 4), dpi=100)
    f_plot = f1.add_subplot(111)
    x, y = plot(get_f(list_1))  
    f_plot.bar(x, y)
    for i,j in zip(x,y):
        f_plot.text(i,j,'%.0f'%j,ha='center',va='bottom')
    canvs = FigureCanvasTkAgg(f1, master=root2)
    canvs.draw()
    canvs.get_tk_widget().pack(side=TOP, fill=BOTH, expand=1)


#添加超链接
def click():
    root4 = Toplevel(root)
    root4.geometry('300x200')
    root4.title('')
    Label(root4,text='请点击以下链接').pack()
    l1 = Label(root4,text='https://translate.google.cn/')
    l1.pack(pady=10)
    l1.bind('<ButtonPress-1>',lambda x:webbrowser.open('https://translate.google.cn/'))
    l2 = Label(root4,text='http://fanyi.youdao.com/')
    l2.pack(pady=10)
    l2.bind('<ButtonPress-1>',lambda x:webbrowser.open('http://fanyi.youdao.com/'))
    l3 = Label(root4,text='https://fanyi.baidu.com/')
    l3.pack(pady=10)
    l3.bind('<ButtonPress-1>',lambda x:webbrowser.open('https://fanyi.baidu.com/'))

##########################################################################################
#读取文档
path = filedialog.askopenfilename(initialdir = "/",title = "选择文件",filetypes = (("txt files","*.txt"),("all files","*.*")))
f = open(path).read()
#文本中的所有单词
list_ = get_content(path)
#文本中去除了停用词后剩余单词
list_1 = remove_stop(list_)
#将文章显示出来
text1 = ScrolledText(root,width=50, height=25,font=('Times New Roman', 13))
text1.place(x=0)
text1.insert(END,f)
#添加按钮
Button(root,text='单词个数',command=lambda :total_number()).place(x=500,y=25)
Button(root,text='词频统计',command=lambda :print_f()).place(x=500,y=125)
Button(root, text='关键词图表 ', command=lambda :draw_picture()).place(x=500,y=225)
Button(root,text='翻译网站',command=lambda :click()).place(x=500,y=325)
Button(root,text='退出',command=lambda :root.destroy()).place(x=500,y=425)
root.mainloop()