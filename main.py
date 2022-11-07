import tkinter as tk
import tkinter.font
import tkinter.ttk as ttk
from tkinter import Text, filedialog, messagebox
from typing_extensions import IntVar

import tools

class ImgToPdf:
    def __init__(self):
        self.filenames = []
        # アプリフレームの作成と設置
        self.frame_imgToPdf = ttk.Frame(root)
        self.frame_imgToPdf.grid(row=0, column=0, sticky="nsew", pady=20)

        self.back_img = tk.PhotoImage(file='./imgs/back.png')
        self.back_img = self.back_img.subsample(10,10)
    
    def places(self):
        # back image
        
        back_button = ttk.Button(self.frame_imgToPdf, image=self.back_img, command=change_main)

        label1_frame_imgToPdf = ttk.Label(self.frame_imgToPdf, text="画像pdf変換")
        button_get_img_path = button_default(self.frame_imgToPdf, text="画像を選択", command=ITP.get_imgpath)
        button_clear_img_path = button_default(self.frame_imgToPdf, text="画像選択を解除", command=ITP.clear_imgpath)
        button_change_frame_imgToPdf = button_default(self.frame_imgToPdf, text="メインウィンドウに移動", command=change_main)
        self.img_label = ttk.Label(self.frame_imgToPdf, text="0個の画像を選択")
        
        back_button.pack(side="left", anchor="nw")
        label1_frame_imgToPdf.pack()
        button_get_img_path.pack()
        button_clear_img_path.pack()
        button_change_frame_imgToPdf.pack()

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
        
    def change_imgToPdf(self):
        self.clear_imgpath()
        self.frame_imgToPdf.tkraise()

    def get_imgpath(self):
        self.filenames = filedialog.askopenfilenames(filetypes = [("","*")])
        self.img_label["text"] = str(len(self.filenames))+"個の画像を選択"

    def clear_imgpath(self):
        self.filenames = []
        self.img_label["text"] = str(len(self.filenames))+"個の画像を選択"
    
    def change_pdf(self):
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
        self.convert_log.insert(tk.END, "made "+pdf_name+"\n  "+pdf_folder+"\n")
        self.convert_log.configure(state='disable')

class ConcatPdf:
    def __init__(self):
        self.filenames = []
        # アプリフレームの作成と設置
        self.frame_concatPdf = ttk.Frame(root)
        self.frame_concatPdf.grid(row=0, column=0, sticky="nsew", pady=20)
    
    def places(self):
        label1_frame_concatPdf = ttk.Label(self.frame_concatPdf, text="pdf結合")
        button_get_pdf_path = button_default(self.frame_concatPdf, text="pdfを選択", command=self.get_pdfpath)
        button_clear_pdf_path = button_default(self.frame_concatPdf, text="pdf選択を解除", command=self.clear_pdfpath)
        button_change_frame_concatPdf = button_default(self.frame_concatPdf, text="メインウィンドウに移動", command=change_main)
        self.pdf_label = ttk.Label(self.frame_concatPdf, text="0個のpdfを選択")
        
        label1_frame_concatPdf.pack()
        button_get_pdf_path.pack()
        button_clear_pdf_path.pack()
        button_change_frame_concatPdf.pack()

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
    root.geometry("300x300")
    root.grid_rowconfigure(0, weight=1)
    root.grid_columnconfigure(0, weight=1)
    root.configure(bg=main_color) # background color

    ITP = ImgToPdf()
    CPDF = ConcatPdf()

    # メインフレームの作成と設置
    frame = ttk.Frame(root)
    frame.grid(row=0, column=0, sticky="nsew", pady=20)

    # 各種ウィジェットの作成
    button_change = button_default(frame, text="画像pdf変換", command=ITP.change_imgToPdf)
    butoon_change_concatPdf = button_default(frame, text="pdf結合", command=CPDF.change_concatPdf)

    # 各種ウィジェットの設置
    button_change.pack()
    butoon_change_concatPdf.pack()

    ITP.places()
    CPDF.places()

    # frameを前面にする
    frame.tkraise()

    root.mainloop()