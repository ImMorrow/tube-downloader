from gui import GUI, END
from downloader import *
from customtkinter import filedialog as fd
from tkinter.messagebox import askyesnocancel
import _thread, sys, tempfile, base64
from images import ICON


class App:
    def __init__(self):

        ## LOAD ICON ##
        # create temp file
        _, ICON_PATH = tempfile.mkstemp()
        # write icon to temp file
        with open(ICON_PATH, 'wb') as icon_file:
            icon_file.write(base64.b64decode(ICON))
        # save temp file path
        self.icon_path = ICON_PATH

        self.askyesnocancel = askyesnocancel

        # initialize graphics
        self.GUI = GUI(self)

    def clear(self):
        # clear log
        self.GUI.log.configure(state='normal')
        self.GUI.log.delete(1.0, END)
        self.GUI.log.configure(state='disabled')

    def debug(self, message):
        # print message on log
        self.GUI.log.configure(state='normal')
        self.GUI.log.insert(END, message+'\n')
        self.GUI.log.configure(state='disabled')
    
    def select_download_path(self):
        # ask user for download path
        path = fd.askdirectory(title="Select Download Location")
        return path

    def download(self):
        # get path
        path = self.select_download_path()

        # get video link
        url = self.GUI.link.get()

        # get the download type
        _type = self.GUI.download_type.get()

        only_audio = self.GUI.download_audio.get()

        # check if the link is for a list
        is_playlist = 'list' in url

        # download in a new thread
        if is_playlist: _thread.start_new_thread(download_playlist, (self, path, url, _type, only_audio))
        else: _thread.start_new_thread(download, (self, path, url, _type, only_audio))

    def on_close(self):
        # destroy window when closed
        self.GUI.root.destroy()
        sys.exit()

    def run(self):
        self.GUI.loop()


if __name__ == '__main__':
    app = App()
    app.run()