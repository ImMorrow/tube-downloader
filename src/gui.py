from customtkinter import *
from customtkinter import filedialog as fd


class GUI:
    def __init__(self, app):

        self.app = app

        # create root object 'window'
        self.root = CTk()
        # set window properties
        self.root.title("uTube Downloader")
        self.root.geometry("512x512")
        self.root.resizable(False,False)

        # change icon
        self.root.iconbitmap(self.app.icon_path) # hardcoded icon

        self.root.protocol('WM_DELETE_WINDOW', self.app.on_close)

        self.load()
    
    def load(self):

        self.label = CTkLabel(self.root, text="Tube Downloader", font=("Arial", 28)).pack(pady=5)

        self.frame = CTkFrame(self.root, height=512, width=512)

        self.frame.grid_propagate(False)

        CTkLabel(self.frame, text="Video / Playlist Link Here:", font=("Arial", 25)).grid(column=0, row=0, pady=20, padx=20, sticky="w")

        self.link = CTkEntry(self.frame, placeholder_text="Enter url here", font=("Arial", 15))
        self.link.grid(column=0, row=1, ipadx=100, padx=20, sticky='w')


        CTkButton(self.frame, text="Download", width=20, command=self.app.download).grid(column=0, row=1, pady=20, sticky="e", padx=20)

        CTkLabel(self.frame, text="Download As Type:", font=("Arial", 20)).grid(column=0, row=2, padx=20, sticky='w')
        self.download_type = CTkComboBox(self.frame, values=['mp4','mp3', 'wav'], state='readonly')
        self.download_type.set('mp4')
        self.download_type.grid(column=0, row=2, sticky='e', padx=20)

        self.download_audio = CTkCheckBox(self.frame, text="Audio Only", onvalue=True, offvalue=False)
        self.download_audio.grid(column=0, row=3, padx=20, sticky='w')


        self.log = CTkTextbox(self.frame, width=430, height=160, state='disabled')

        self.log.grid(column=0, row=4, padx=20, pady=15, sticky='nw')

        CTkButton(self.frame, text='clear', command=self.app.clear).grid(column=0, row=5, sticky='s')

        self.frame.pack(fill='both', padx=20, pady=20)

    
    def loop(self):
        self.root.mainloop()
