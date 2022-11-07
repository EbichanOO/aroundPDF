import shutil, os, re
from natsort import natsorted

def Unzip(zip_path, out_path):
    shutil.unpack_archive(zip_path, out_path)

if __name__=='__main__':
    Unzip("/home/ebihara/ダウンロード/Photos-001.zip", "/home/ebihara/ダウンロード/Photos-001/")