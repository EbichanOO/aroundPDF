import img2pdf
from PIL import Image

def ImgToPdf(img_paths, img_names, outpdf_path, outpdf_name):
    imgs = []
    for i in range(len(img_paths)):
        imgs.append(Image.open(img_paths[i]+img_names[i]).filename)
    with open(outpdf_path + outpdf_name, "wb") as f:
        f.write(img2pdf.convert(imgs, viewer_magnification=img2pdf.parse_magnification('fit'), viewer_page_layout=img2pdf.parse_layout('single')))
    print("made "+outpdf_name)

if __name__ == '__main__':
    ImgToPdf(["./tmps/","./tmps/"], ["imgsample1.JPG","imgsample2.JPG"], "./tmps/", "test.pdf")