#ques 1
import datetime as dt
x = dt.datetime.now()
print("today day is",x.strftime("%A"))

#ques2
import webbrowser
youtube=input("enter your search:")
webbrowser.open_new_tab('https://www.youtube.com/=%s'%youtube)

#ques3
import os
path="D:\python\assignment\comman module"
filename=listdir('.')
for name in filename:
        src = path + image
        dst = path + str(i) + '.jpg'
        os.rename(src, dst)

