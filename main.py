import tkinter as tk
import tkinter.font
import tkinter.ttk as ttk
from tkinter import Text, filedialog, messagebox
from typing_extensions import IntVar

import tools
import controller

width = 300
height = 300

class TEMPLATEAPP:
    def __init__(self):
        self.frame = tk.Frame(appBody, width=width, height=height-20, bg=main_color)
        self.frame.propagate(False)
        self.frame.place(x=0,y=0)
        self.frameList = [self.frame]
 
    def init_vals(self):
        pass

    def getFrame(self):
        return self.frameList

class MainMenu(TEMPLATEAPP):
    def __init__(self):
        super().__init__()

        # 各種ウィジェットの作成
        button_change = button_default(self.frame, text="画像pdf変換", command=lambda:change("itp"))
        butoon_change_concatPdf = button_default(self.frame, text="pdf結合", command=lambda:change("cp"))

        # 各種ウィジェットの設置
        button_change.pack()
        butoon_change_concatPdf.pack()

class ImgToPdf(TEMPLATEAPP):
    def __init__(self):
        super().__init__()

        self.filenames = []

        label1_frame_imgToPdf = label_title(self.frame, text="画像pdf変換")
        button_get_folder_path = button_default(self.frame, text="フォルダで一括選択", command=self.get_folderpath)
        button_get_img_path = button_default(self.frame, text="画像またはzipファイルを選択", command=self.get_imgpath)
        self.img_label = label_default(self.frame, text="0個の画像を選択")
        
        label1_frame_imgToPdf.pack()
        button_get_folder_path.pack()
        button_get_img_path.pack()

        self.img_label.pack()

        entryFrame = tk.Frame(self.frame, width=width)
        entryFrame.pack()
        self.frameList.append(entryFrame)

        self.pdf_name_enrty = tk.Entry(entryFrame)
        self.pdf_name_enrty.insert(tk.END,'pdfの名前を入力')
        self.pdf_name_enrty.pack(side="left", padx=5, fill="x")

        button_change_pdf_frame_imgToPdf = button_default(entryFrame, text="pdfに変換", command=self.change_pdf)
        button_change_pdf_frame_imgToPdf.pack(side="left")

        self.convert_log, self.pgb = convertLogAndConvertProgressBar(self.frame)
    
    def init_vals(self):
        self.clear_imgpath()

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

    def initPdfName(self):
        self.pdf_name_enrty.delete(0, tk.END)
        self.pdf_name_enrty.insert(tk.END, "pdfの名前を入力")
    
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
        self.initPdfName()

        self.convert_log.configure(state='normal')
        self.convert_log.insert(tk.END, "made "+pdf_name+"\n  "+"for  "+pdf_folder+"\n")
        self.convert_log.configure(state='disable')

class ConcatPdf(TEMPLATEAPP):
    def __init__(self):
        super().__init__()
        self.filenames = []
        
        label1_frame_concatPdf = label_title(self.frame, text="pdf結合")
        button_get_pdf_path = button_default(self.frame, text="pdfを選択", command=self.get_pdfpath)
        self.pdf_label = label_default(self.frame, text="0個のpdfを選択")

        label1_frame_concatPdf.pack()
        button_get_pdf_path.pack()

        self.pdf_label.pack()

        entryFrame = tk.Frame(self.frame, width=width)
        entryFrame.pack()
        self.frameList.append(entryFrame)

        self.pdf_name_enrty = tk.Entry(entryFrame)
        self.pdf_name_enrty.insert(tk.END,'出力pdfの名前を入力')
        self.pdf_name_enrty.pack(side="left", fill="x")

        button_change_pdf_frame_concatPdf = button_default(entryFrame, text="結合", command=self.change_pdf)
        button_change_pdf_frame_concatPdf.pack(side="left")

        self.convert_log, self.pgb = convertLogAndConvertProgressBar(self.frame)
    
    def init_vals(self):
        self.clear_pdfpath()

    def get_pdfpath(self):
        self.filenames = filedialog.askopenfilenames(filetypes = [("","*")])
        self.pdf_label["text"] = str(len(self.filenames))+"個のpdfを選択"

    def clear_pdfpath(self):
        self.filenames = []
        self.pdf_label["text"] = str(len(self.filenames))+"個のpdfを選択"
    
    def initPdfName(self):
        self.pdf_name_enrty.delete(0, tk.END)
        self.pdf_name_enrty.insert(tk.END, "pdfの名前を入力")
    
    def change_pdf(self):
        pdf_name = self.pdf_name_enrty.get() + ".pdf"
        pdf_folder = filedialog.askdirectory() + "/"
        tools.concatPdf.ConcatPdfSome(self.filenames, pdf_folder+pdf_name)

        self.clear_pdfpath()
        self.initPdfName()

        self.convert_log.configure(state='normal')
        self.convert_log.insert(tk.END, "made "+pdf_name+"\n  "+pdf_folder+"\n")
        self.convert_log.configure(state='disable')

# components
def button_default(frame, text, command):
    return ttk.Button(frame, text=text, style="default.TButton", command=command)

def label_default(frame, text):
    return ttk.Label(frame, text=text, style="default.TLabel", background=main_color)

def label_title(frame, text):
    return ttk.Label(frame, text=text, style="title.TLabel", background=main_color)

def convertLogAndConvertProgressBar(frame):
    pgb = ttk.Progressbar(frame,orient="horizontal",value=0,maximum=100,length=200,mode='determinate')
    pgb.pack(side="bottom", pady=5)

    convert_log = tk.Text(frame, height=5)
    convert_log.configure(state='disable')
    convert_log.pack(side="bottom")
    return convert_log, pgb

def write_log(log_board, text):
    log_board.configure(state='normal')
    log_board.insert(tk.END, text+"\n")
    log_board.configure(state='disable')

class TopMenu:
    def __init__(self):
        self.frame_height = 20
        self.frame_width = width

        self.frame = tk.Frame(root, width=width, height=self.frame_height)
        self.frame.propagate(False)
        self.frame.pack()

        img_width = 500/5
        img_height = 100/5
        self.logo_img = tk.PhotoImage(file='./imgs/my-toolkit-logo.png', width=500, height=100)
        self.logo_img = self.logo_img.subsample(5,5)

        self.canvas = tk.Canvas(self.frame, width=img_width, height=img_height)
        # キャンバスにイメージを表示
        self.canvas.create_image(0, 0, image=self.logo_img, anchor=tkinter.NW)
        # キャンパスの配置
        self.canvas.pack()

        self.canvas.bind('<Button-1>', self.changeToMain)
    
    def getFrame(self):
        return self.frame

    def changeToMain(self, event):
        change("main")

def change(changeName):
    router[changeName].init_vals()
    for frame in router[changeName].getFrame():
        frame.tkraise()

if __name__ == "__main__":
    root = tk.Tk()
    global main_color, normal_font
    main_color = "ghost white"
    normal_font = tkinter.font.Font(root, "Helvetica")

    # ttkのスタイル設定
    style = ttk.Style()
    style.configure("default.TButton", font=(normal_font))
    style.configure("default.TLabel",font=(normal_font, 10))
    style.configure("title.TLabel",font=(normal_font, 15))

    # rootメインウィンドウの設定
    root.title("toolkit")
    root.geometry("{}x{}".format(width,height))
    root.grid_rowconfigure(0, weight=1)
    root.grid_columnconfigure(0, weight=1)
    root.configure(bg=main_color) # background color

    header = TopMenu()
    header.getFrame().tkraise()

    appBody = ttk.Frame(root, width=width, height=height-20)
    # ウェッジのサイズに応じて伸び縮みしない
    appBody.propagate(False)
    appBody.pack()

    mainpage = MainMenu()
    itppage = ImgToPdf()
    cppage = ConcatPdf()
    router = {
        'main': mainpage,
        'itp': itppage,
        'cp': cppage
    }

    change('main')

    root.mainloop()