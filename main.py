import tkinter as tk
import tkinter.ttk as ttk
from tkinter import filedialog, messagebox
import tools

class ImgToPdf:
    def __init__(self):
        self.filenames = []
        # アプリフレームの作成と設置
        self.frame_imgToPdf = ttk.Frame(root)
        self.frame_imgToPdf.grid(row=0, column=0, sticky="nsew", pady=20)
        self.convert_log_strings = ""
    
    def places(self):
        label1_frame_imgToPdf = ttk.Label(self.frame_imgToPdf, text="画像pdf変換")
        button_get_img_path = ttk.Button(self.frame_imgToPdf, text="画像を選択", command=ITP.get_imgpath)
        button_clear_img_path = ttk.Button(self.frame_imgToPdf, text="画像選択を解除", command=ITP.clear_imgpath)
        button_change_frame_imgToPdf = ttk.Button(self.frame_imgToPdf, text="メインウィンドウに移動", command=change_main)
        self.img_label = ttk.Label(self.frame_imgToPdf, text="0個の画像を選択")
        
        label1_frame_imgToPdf.pack()
        button_get_img_path.pack()
        button_clear_img_path.pack()
        button_change_frame_imgToPdf.pack()

        self.img_label.pack()

        self.pdf_name_enrty = tk.Entry(self.frame_imgToPdf)
        self.pdf_name_enrty.insert(tk.END,'pdfの名前を入力')
        self.pdf_name_enrty.pack()

        button_change_pdf_frame_imgToPdf = ttk.Button(self.frame_imgToPdf, text="pdfに変換", command=self.change_pdf)
        button_change_pdf_frame_imgToPdf.pack()

        self.convert_log = tk.Text(self.frame_imgToPdf, height=10)
        self.convert_log.configure(state='disable')
        self.convert_log.pack()
        
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
        tools.imgToPdf.ImgToPdf(self.filenames, pdf_folder, pdf_name)

        self.clear_imgpath()

        self.convert_log.configure(state='normal')
        self.convert_log.insert(tk.END, "made "+pdf_name+"\n  "+pdf_folder+"\n")
        self.convert_log.configure(state='disable')

def change_main():
    frame.tkraise()

if __name__ == "__main__":
    # rootメインウィンドウの設定
    root = tk.Tk()
    root.title("toolkit")
    root.geometry("300x300")
    root.grid_rowconfigure(0, weight=1)
    root.grid_columnconfigure(0, weight=1)

    ITP = ImgToPdf()


    # メインフレームの作成と設置
    frame = ttk.Frame(root)
    frame.grid(row=0, column=0, sticky="nsew", pady=20)

    # 各種ウィジェットの作成
    label1_frame = ttk.Label(frame, text="メインウィンドウ")
    entry1_frame = ttk.Entry(frame)
    button_change = ttk.Button(frame, text="画像pdf変換", command=ITP.change_imgToPdf)

    # 各種ウィジェットの設置
    label1_frame.pack()
    entry1_frame.pack()
    button_change.pack()

    ITP.places()

    # frameを前面にする
    frame.tkraise()

    root.mainloop()