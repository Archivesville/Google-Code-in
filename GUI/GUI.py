import tkinter as tk
import webbrowser
import os
import subprocess


def open_github():
    webbrowser.open(url="https://github.com/")

def open_spotify():
    subprocess.call("/Applications/Spotify.app") 

def open_youtube():
    webbrowser.open("https://www.youtube.com/feed/trending")  

def main():
    gui=tk.Tk()
    gui.geometry('500x50')
    gui.title('Python automate')
    button_1=tk.Button(text='Open Github',command=open_github)
    button_1.place(x=0,y=0)
    button_2=tk.Button(text='Open Spotify',command=open_spotify)
    button_2.place(x=150,y=0)
    button_3=tk.Button(text='Open Youtube',command=open_youtube)
    button_3.place(x=300,y=0)
    gui.mainloop()

if __name__=="__main__":
    main()
