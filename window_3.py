from tkinter import *
from unicodedata import name
from PIL import Image , ImageTk
from pygame import mixer
from tkinter import filedialog
import os
import time
import shutil
import window_4 as mw4


def main_win3():
    root = Tk()
    root.geometry("880x420")
    root.title("Eternal Music")
    root.configure(background="#000000")

    width = root.winfo_screenwidth()
    height = root.winfo_screenheight()
    print(f"{width}x{height}")

    '''def img_changer():
        playlist.configure(img=img1)
        time.sleep(3)
        playlist.configure(img=img2)
        time.sleep(3)
        playlist.configure(img=img3)'''

    def play_song(event):
        music_name=playlist.get(ACTIVE)
        mixer.music.load(playlist.get(ACTIVE))
        mixer.music.play()


    global paused
    paused =False
    def pause_unpause():
        global paused
        if paused == True :
            mixer.music.unpause()
            paused=False
            playbtn['image'] = play

        else:
            mixer.music.pause()
            paused=True    
            playbtn['image']= pause
    


    global current
    current=0
    def next_song():
        next_song = playlist.curselection()
        next_song =next_song[0] + 1
        song = playlist.get(next_song)
        song =f"C:\\Users\\ASUS\\Music\\{song}"
        mixer.music.load(song)  
        mixer.music.play()
        playlist.selection_clear(0,END)
        playlist.activate(next_song)
        playlist.selection_set(next_song,last=None)


    def previous_song():
        next_song = playlist.curselection()
        next_song =next_song[0] - 1
        song = playlist.get(next_song)
        song =f"C:\\Users\\ASUS\\Music\\{song}"
        mixer.music.load(song)
        mixer.music.play()
        playlist.selection_clear(0,END)
        playlist.activate(next_song)
        playlist.selection_set(next_song,last=None)


    def open_folder():
        path = "C:\\Users\\ASUS\\Music"
        os.chdir(path)
        songs = os.listdir(path)
        for song in songs:
            if song.endswith(".mp3"):
                playlist.insert(END,song)


    def load_music():
        playlist.delete(0,END)
        path = filedialog.askdirectory()
        if path :
            os.chdir(path)
            songs = os.listdir(path)
            for song in songs:
                if song.endswith(".mp3"):
                    playlist.insert(END,song)

        playlist.update()

    def move_to_win4(event):
        mw4.main_win4()
    


    def add_song():
        song=filedialog.askopenfilename(initialdir="C:\\Users\\ASUS\\Music",title="chhoos a song",filetypes=(("mp3 Files","*.mp3"),))
        song =song.replace('C:\\Users\\ASUS\\Music\\', " ")
        playlist.insert(END,song)
        source= str(playlist.get(END))
        destination="C:\\Users\\ASUS\\Videos"
        shutil.copy(source,destination)

      

    def create_folder():
        os.chdir("C:\\Users\\ASUS\\Videos")
        os.mkdir("pratik")



    mixer.init()

    pause=Image.open("C:\\Users\\PRANALI PATIL\\Documents\\Music_Player\\play.png")
    pause = pause.resize((80,80),Image.ANTIALIAS)
    pause = ImageTk.PhotoImage(pause)

    head=Image.open("C:\\Users\\PRANALI PATIL\\Documents\\Music_Player\\top.png")
    head = head.resize((1530,65),Image.ANTIALIAS)
    head= ImageTk.PhotoImage(head)
    headname=Label(root,image=head,bd=0)
    headname.place(x=2,y=1)

    frame_img = Frame(root, relief=SUNKEN, height=500, width=900)
    frame_img.place(x=18,y=84)
    frame_img.config(background="#627296")

    
    root.mainloop()
    

