import img2pdf
from PIL import Image
from . import concatPdf
import os

def ImgToPdf(img_paths_and_name, outpdf_path, outpdf_name):
    imgs = []
    pdfs = []
    for i in range(len(img_paths_and_name)):
        imgs.append(Image.open(img_paths_and_name[i]).filename)
        if (i+1)%10==0:
            pdfs.append(outpdf_path + str(int((i+1)/10)) + ".pdf")
            with open(outpdf_path + str(int((i+1)/10)) + ".pdf", "wb") as f:
                f.write(img2pdf.convert(imgs, viewer_magnification=img2pdf.parse_magnification('fit'), viewer_page_layout=img2pdf.parse_layout('single')))
                imgs = []
            yield i+1
        
    if len(img_paths_and_name)%10 != 0:
        pdfs.append(outpdf_path + str(int((i+1)/10)+1) + ".pdf")
        with open(outpdf_path + str(int((i+1)/10) + 1) + ".pdf", "wb") as f:
            f.write(img2pdf.convert(imgs, viewer_magnification=img2pdf.parse_magnification('fit'), viewer_page_layout=img2pdf.parse_layout('single')))
    
    concatPdf.ConcatPdfSome(pdfs, outpdf_path+outpdf_name)
    for name in pdfs:
        os.remove(name)
