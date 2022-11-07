import tkinter as tk
import tkinter.font
import tkinter.ttk as ttk
from tkinter import Text, filedialog, messagebox
from typing_extensions import IntVar

import tools
import controller

width = 300
height = 300

class MainMenu():
    def __init__(self):
        self.topMenu = TopMenu(root)
        self.frame = ttk.Frame(root)
        self.frame.grid(row=1, column=0, sticky="nsew")
        self.frames = [self.topMenu.frame, self.frame]

    def places(self):
        self.topMenu.places()

        ITP = ImgToPdf()
        CPDF = ConcatPdf()

        # 各種ウィジェットの作成
        button_change = button_default(self.frame, text="画像pdf変換", command=self.change_to_imgToPdf)
        butoon_change_concatPdf = button_default(self.frame, text="pdf結合", command=CPDF.change_concatPdf)

        # 各種ウィジェットの設置
        button_change.pack()
        butoon_change_concatPdf.pack()
    
    def change(self):
        self.places()
        [frame.tkraise() for frame in self.frames]

    def change_to_imgToPdf(self):
        [frame.destroy() for frame in self.frames]
        ITP = ImgToPdf()
        ITP.change()


class ImgToPdf:
    def __init__(self):
        self.filenames = []
        # アプリフレームの作成と設置
        self.frame_imgToPdf = ttk.Frame(root)
        self.frame_imgToPdf.grid(row=1, column=0, sticky="nsew")

        self.top_menu = TopMenu(root)

        self.frames = [self.frame_imgToPdf, self.top_menu.frame]
    
    def places(self):
        # back image
        
        self.top_menu.places()

        label1_frame_imgToPdf = ttk.Label(self.frame_imgToPdf, text="画像pdf変換")
        button_get_folder_path = button_default(self.frame_imgToPdf, text="フォルダで一括選択", command=self.get_folderpath)
        button_get_img_path = button_default(self.frame_imgToPdf, text="画像またはzipファイルを選択", command=self.get_imgpath)
        self.img_label = ttk.Label(self.frame_imgToPdf, text="0個の画像を選択")
        
        label1_frame_imgToPdf.pack()
        button_get_folder_path.pack()
        button_get_img_path.pack()

        self.img_label.pack()

        self.pdf_name_enrty = tk.Entry(self.frame_imgToPdf)
        self.pdf_name_enrty.insert(tk.END,'pdfの名前を入力')
        self.pdf_name_enrty.pack()

        button_change_pdf_frame_imgToPdf = button_default(self.frame_imgToPdf, text="pdfに変換", command=self.change_pdf)
        button_change_pdf_frame_imgToPdf.pack()

        self.convert_log = tk.Text(self.frame_imgToPdf, height=5)
        self.convert_log.configure(state='disable')
        self.convert_log.pack()

        self.pgb = ttk.Progressbar(self.frame_imgToPdf,orient="horizontal",value=0,maximum=100,length=200,mode='determinate')
        self.pgb.pack()

    def change(self):
        self.places()
        [name.tkraise() for name in self.frames]

    def get_imgpath(self):
        filenames_tmp = filedialog.askopenfilenames(filetypes = [("","*")])
        if(len(filenames_tmp)==1 and filenames_tmp[0].split('.')[1]=="zip"):
            self.filenames = controller.pdfMaker.getFileNameFromZip(filenames_tmp[0])
        else:
            self.filenames = filenames_tmp
        self.img_label["text"] = str(len(self.filenames))+"個の画像を選択"

    def get_folderpath(self):
        folder_name = filedialog.askdirectory()
        if(len(folder_name)==0):
            write_log(self.convert_log, "フォルダを選択して下さい")
            return 0
        self.filenames = controller.pdfMaker.getFileNameFromFolder(folder_name)
        self.img_label["text"] = str(len(self.filenames))+"個の画像を選択"
        if(len(self.filenames)==0):
            write_log(self.convert_log, folder_name+"には画像はありませんでした")

    def clear_imgpath(self):
        self.filenames = []
        self.img_label["text"] = str(len(self.filenames))+"個の画像を選択"
    
    def change_pdf(self):
        if(self.pdf_name_enrty.get()=="" or len(self.filenames)==0):
            write_log(self.convert_log, "pdfの名前と変換する画像を設定して下さい")
            return 0
        pdf_name = self.pdf_name_enrty.get() + ".pdf"
        pdf_folder = filedialog.askdirectory() + "/"
        self.pgb.configure(value=0)

        for i in tools.imgToPdf.ImgToPdf(self.filenames, pdf_folder, pdf_name):
            self.pgb.configure(value= int(i*100/len(self.filenames)))
            self.pgb.update()
        self.pgb.configure(value= 100)
        self.pgb.update()

        self.clear_imgpath()

        self.convert_log.configure(state='normal')
        self.convert_log.insert(tk.END, "made "+pdf_name+"\n  "+"for  "+pdf_folder+"\n")
        self.convert_log.configure(state='disable')

class ConcatPdf:
    def __init__(self):
        self.filenames = []
        # アプリフレームの作成と設置
        self.frame_concatPdf = ttk.Frame(root)
        self.frame_concatPdf.grid(row=0, column=0, sticky="nsew")

        self.back_img = tk.PhotoImage(file='./imgs/back.png')
        self.back_img = self.back_img.subsample(10,10)

    def places(self):
        back_button = ttk.Button(self.frame_concatPdf, image=self.back_img, command=change_main)
        
        label1_frame_concatPdf = ttk.Label(self.frame_concatPdf, text="pdf結合")
        button_get_pdf_path = button_default(self.frame_concatPdf, text="pdfを選択", command=self.get_pdfpath)
        self.pdf_label = ttk.Label(self.frame_concatPdf, text="0個のpdfを選択")
        
        back_button.pack(side="left", anchor="nw")

        label1_frame_concatPdf.pack()
        button_get_pdf_path.pack()

        self.pdf_label.pack()

        self.pdf_name_enrty = tk.Entry(self.frame_concatPdf)
        self.pdf_name_enrty.insert(tk.END,'出力pdfの名前を入力')
        self.pdf_name_enrty.pack()

        button_change_pdf_frame_concatPdf = button_default(self.frame_concatPdf, text="結合", command=self.change_pdf)
        button_change_pdf_frame_concatPdf.pack()

        self.convert_log = tk.Text(self.frame_concatPdf, height=10)
        self.convert_log.configure(state='disable')
        self.convert_log.pack()
        
    def change_concatPdf(self):
        self.clear_pdfpath()
        self.frame_concatPdf.tkraise()

    def get_pdfpath(self):
        self.filenames = filedialog.askopenfilenames(filetypes = [("","*")])
        self.pdf_label["text"] = str(len(self.filenames))+"個のpdfを選択"

    def clear_pdfpath(self):
        self.filenames = []
        self.pdf_label["text"] = str(len(self.filenames))+"個のpdfを選択"
    
    def change_pdf(self):
        pdf_name = self.pdf_name_enrty.get() + ".pdf"
        pdf_folder = filedialog.askdirectory() + "/"
        tools.concatPdf.ConcatPdfSome(self.filenames, pdf_folder+pdf_name)

        self.clear_pdfpath()

        self.convert_log.configure(state='normal')
        self.convert_log.insert(tk.END, "made "+pdf_name+"\n  "+pdf_folder+"\n")
        self.convert_log.configure(state='disable')

def change_main():
    frame.tkraise()

# components
def button_default(frame, text, command):
    return ttk.Button(frame, text=text, style="default.TButton", command=command)

def write_log(log_board, text):
    log_board.configure(state='normal')
    log_board.insert(tk.END, text+"\n")
    log_board.configure(state='disable')

class TopMenu:
    def __init__(self, parentFrame):
        self.frame_height = int(height/5)
        self.frame_width = width

        self.frame = tk.Frame(parentFrame, width=width, height=self.frame_height)
        self.style = ttk.Style()
        self.style.configure("topMenu.TButton")

        self.img_width = 5*self.frame_height
        self.img_height = self.frame_height
        self.logo_img = tk.PhotoImage(file='./imgs/my-toolkit-logo.png', width=500, height=100)
        self.logo_img = self.logo_img.subsample(5,5)

        self.canvas = tk.Canvas(self.frame, width=self.img_width, height=self.frame_height)

    def places(self):
        self.frame.grid(column=0,row=0)
        self.canvas.pack()
        # キャンバスにイメージを表示
        self.canvas.create_image(0, 0, image=self.logo_img, anchor=tkinter.NW)

        self.canvas.bind('<Button-1>', self.changeToMain)
    
    def changeToMain(self, event):
        mainMenu = MainMenu()
        mainMenu.change()

if __name__ == "__main__":
    root = tk.Tk()
    global main_color, normal_font
    main_color = "ghost white"
    normal_font = tkinter.font.Font(root, "Helvetica")

    # ttkのスタイル設定
    style = ttk.Style()
    style.configure("default.TButton", font=(normal_font))

    # rootメインウィンドウの設定
    root.title("toolkit")
    root.geometry("{}x{}".format(width,height))
    root.grid_rowconfigure(0, weight=1)
    root.grid_columnconfigure(0, weight=1)
    root.configure(bg=main_color) # background color

    MAINMENU = MainMenu()

    MAINMENU.change()

    root.mainloop()