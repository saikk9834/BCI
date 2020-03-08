
from tkinter import PhotoImage
from ttk import Label,Button
import time
from PIL import Image, ImageTk

    
class AnimatedGIF(Label, object):
    def __init__(self, master, path, forever=True):
        self._master = master
        self._loc = 0
        self._forever = forever

        self._is_running = False

        im = Image.open(path)
        self._frames = []
        i = 0
        try:
            while True:
                photoframe = ImageTk.PhotoImage(im.copy().convert('RGBA'))
                self._frames.append(photoframe)

                i += 1
                im.seek(i)
        except EOFError: pass
        
        self._last_index = len(self._frames) - 1

        try:
            self._delay = im.info['duration']
        except:
            self._delay = 100

        self._callback_id = None

        super(AnimatedGIF, self).__init__(master, image=self._frames[0])

    def start_animation(self, frame=None):
        if self._is_running: return

        if frame is not None:
            self._loc = 0
            self.configure(image=self._frames[frame])

        self._master.after(self._delay, self._animate_GIF)
        self._is_running = True

    def stop_animation(self):
        if not self._is_running: return

        if self._callback_id is not None:
            self.after_cancel(self._callback_id)
            self._callback_id = None

        self._is_running = False

    def _animate_GIF(self):
        self._loc += 1
        self.configure(image=self._frames[self._loc])

        if self._loc == self._last_index:
            if self._forever:
                self._loc = 0
                self._callback_id = self._master.after(self._delay, self._animate_GIF)
            else:
                self._callback_id = None
                self._is_running = False
        else:
            self._callback_id = self._master.after(self._delay, self._animate_GIF)

    def pack(self, start_animation=True, **kwargs):
        if start_animation:
            self.start_animation()

        super(AnimatedGIF, self).pack(**kwargs)

    def grid(self, start_animation=True, **kwargs):
        if start_animation:
            self.start_animation()

        super(AnimatedGIF, self).grid(**kwargs)
        
    def place(self, start_animation=True, **kwargs):
        if start_animation:
            self.start_animation()

        super(AnimatedGIF, self).place(**kwargs)
        
    def pack_forget(self, **kwargs):
        self.stop_animation()

        super(AnimatedGIF, self).pack_forget(**kwargs)

    def grid_forget(self, **kwargs):
        self.stop_animation()

        super(AnimatedGIF, self).grid_forget(**kwargs)
        
    def place_forget(self, **kwargs):
        self.stop_animation()

        super(AnimatedGIF, self).place_forget(**kwargs)

def change2(self):
    global start
    global l
    global label
    end = time.time()
    l.pack_forget()
    time_taken=round(end-start)
    if(time_taken>=0 and time_taken<2):
        ch='A'
    elif(time_taken>=2 and time_taken<4):
        ch='F'
    elif(time_taken>=4 and time_taken<6):
        ch='K'
    elif(time_taken>=6 and time_taken<8):
        ch='P'
    elif(time_taken>=8 and time_taken<10):
        ch='U'
    label.pack_forget()
    label['text']=label['text']+ch
    label.pack()
    l = AnimatedGIF(root, "BCI Design 1.gif")
    l.bind("<ButtonRelease-1>", change)
    start=time.time()
    l.pack()

def change3(self):
    global start
    global l
    global label
    end = time.time()
    l.pack_forget()
    time_taken=round(end-start)
    if(time_taken>=0 and time_taken<2):
        ch='B'
    elif(time_taken>=2 and time_taken<4):
        ch='G'
    elif(time_taken>=4 and time_taken<6):
        ch='L'
    elif(time_taken>=6 and time_taken<8):
        ch='Q'
    elif(time_taken>=8 and time_taken<10):
        ch='V'
    label.pack_forget()
    label['text']=label['text']+ch
    label.pack()
    l = AnimatedGIF(root, "BCI Design 1.gif")
    l.bind("<ButtonRelease-1>", change)
    start=time.time()
    l.pack()

def change4(self):
    global start
    global l
    global label
    end = time.time()
    l.pack_forget()
    time_taken=round(end-start)
    if(time_taken>=0 and time_taken<2):
        ch='C'
    elif(time_taken>=2 and time_taken<4):
        ch='H'
    elif(time_taken>=4 and time_taken<6):
        ch='M'
    elif(time_taken>=6 and time_taken<8):
        ch='R'
    elif(time_taken>=8 and time_taken<10):
        ch='W'
    elif(time_taken>=10 and time_taken<=12):
        ch='Z'
    label.pack_forget()
    label['text']=label['text']+ch
    label.pack()
    l = AnimatedGIF(root, "BCI Design 1.gif")
    l.bind("<ButtonRelease-1>", change)
    start=time.time()
    l.pack()

def change5(self):
    global start
    global l
    global label
    end = time.time()
    l.pack_forget()
    time_taken=round(end-start)
    if(time_taken>=0 and time_taken<2):
        ch='D'
    elif(time_taken>=2 and time_taken<4):
        ch='I'
    elif(time_taken>=4 and time_taken<6):
        ch='N'
    elif(time_taken>=6 and time_taken<8):
        ch='S'
    elif(time_taken>=8 and time_taken<=10):
        ch='X'
    label.pack_forget()
    label['text']=label['text']+ch
    label.pack()
    l = AnimatedGIF(root, "BCI Design 1.gif")
    l.bind("<ButtonRelease-1>", change)
    start=time.time()
    l.pack()

def change6(self):
    global start
    global l
    global label
    end = time.time()
    l.pack_forget()
    time_taken=round(end-start)
    if(time_taken>=0 and time_taken<2):
        ch='E'
    elif(time_taken>=2 and time_taken<4):
        ch='J'
    elif(time_taken>=4 and time_taken<6):
        ch='O'
    elif(time_taken>=6 and time_taken<8):
        ch='T'
    elif(time_taken>=8 and time_taken<=10):
        ch='Y'
    label.pack_forget()
    label['text']=label['text']+ch
    label.pack()
    start=time.time()
    l = AnimatedGIF(root, "BCI Design 1.gif")
    l.bind("<ButtonRelease-1>", change)
    l.pack()

def change(self):
    global l
    global start
    end = time.time()
    l.pack_forget()
    time_taken=round(end-start)
    start=time.time()
    if(time_taken>=0 and time_taken<2):
        l = AnimatedGIF(root, "BCI Design 2.gif")
        l.bind("<ButtonRelease-1>", change2)
    elif(time_taken>=2 and time_taken<4):
        l = AnimatedGIF(root, "BCI Design 3.gif")
        l.bind("<ButtonRelease-1>", change3)
    elif(time_taken>=4 and time_taken<6):
        l = AnimatedGIF(root, "BCI Design 4.gif")
        l.bind("<ButtonRelease-1>", change4)
    elif(time_taken>=6 and time_taken<8):
        l = AnimatedGIF(root, "BCI Design 5.gif")
        l.bind("<ButtonRelease-1>", change5)
    elif(time_taken>=8 and time_taken<10):
        l = AnimatedGIF(root, "BCI Design 6.gif")
        l.bind("<ButtonRelease-1>", change6)
    l.pack()

def done(self):
    global label
    global button
    label['text'] = 'Your word is :' + label['text']
    
        
if __name__ == "__main__":
    from tkinter import Tk, Label

    root = Tk()
    root.minsize(150,100)
    # Add the path to a GIF to make the example working
    l = AnimatedGIF(root, "BCI Design 1.gif")
    start = time.time()
    l.bind("<ButtonRelease-1>", change)
    l.pack()
    label = Label(root, text='')
    button = Button(root, text='Word Complete?')
    button.bind("<ButtonRelease-1>",done)
    button.pack()
    label.pack()
    root.mainloop()

