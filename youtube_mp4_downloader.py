import tkinter as tk
from pytube import YouTube
from tkinter import ttk
from tkinter import messagebox


def array(url):

    yt = YouTube(url)
    video = yt.streams.filter(progressive=True,file_extension='mp4').all()
    a=0
    for v in video:

        v=str(v).replace("\"","")
        options=v.split(" ")
        array1.append(options[3]+" "+options[4])
        download_array.append(options[1])

    add_combo(array1)


def add_combo(array):
    combo['values']=array


def download_video():

    if text1.get() !="" and path.get() !="":

        messagebox.showinfo("","Please waiting a moment")

        choice_index = array1.index(combo.get())

        itagg = str(download_array[choice_index]).split("=")

        slash = "\ \\"
        slash=slash.replace(" ", "")

        file_path=str(path.get()).replace("\\", slash)

        yt = YouTube(text1.get())
        video = yt.streams.get_by_itag(itagg[1])
        video.download(file_path)

    else:
        messagebox.showinfo("Warning", "Please fill in all fields")


array1 = []
download_array=[]

window = tk.Tk()
window.title("Youtube Video Downloader")
window.geometry("600x350")

mycolor = '#%02x%02x%02x' % (229, 229, 229)
window.configure(background=mycolor)

labelurl = tk.Label(window, text="Please enter url").place(x=20, y=30)

labelinfo=tk.Label(window,text="Choose the quality").place(x=20,y=110)

labelpath=tk.Label(window,text="File Path").place(x=20,y=170)

path=tk.Entry(window,width=45)
path.place(x=170, y=170)

text1 = tk.Entry(window,width=45)
text1.place(x=170, y=30)

buton = tk.Button(window, text="Get quality options",height=1, command=lambda:array(text1.get()))
buton.place(x=170, y=70)

url=text1.get()

butond=tk.Button(window,text="Download video",command=download_video)
butond.place(x=170, y=210)

combo = ttk.Combobox(window,width=42)
combo.place(x=170, y=110)

window.mainloop()










