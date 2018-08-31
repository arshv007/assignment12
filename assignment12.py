#Ques1
import datetime as dt
x = dt.date.today()
print(x.strftime("%A"))

#Ques2
import webbrowser
webbrowser.open("https://www.youtube.com/watch?v=hEgO047GxaQ")


#Ques3

import os,sys
folder = r'C:\Users\ARSH\Desktop\python git\assignment12\files'
for file in os.listdir(folder):
    infile = os.path.join(folder,file)
    if not os.path.isfile(infile):
        continue
    oldbase = os.path.splitext(file)
    newname = infile.replace('.txt', '.jpg')
    output = os.rename(infile, newname)
