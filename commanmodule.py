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
images_path = "D:\python\assignment\comman module"
image_list = os.listdir('.')
for i,  image in enumerate(image_list):
    ext = os.path.splitext(image)[1]
    if ext == '.jpg':
        src = images_path + image
        dst = images_path + str(i) + '.jpg'
        os.rename(src, dst)
