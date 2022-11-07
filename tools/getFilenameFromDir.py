from natsort import natsorted
from . import concatPdf
import os, re

correspond_file_pat = '.+\.(png|PNG|jpg|JPG|jpeg|JPEG|webp|WEBP)'
file_pattern = re.compile(correspond_file_pat)

def GetFilenameFromDir(dir_path_and_name):
    in_folder_list = os.listdir(path=dir_path_and_name)
    if(len(in_folder_list)==0):
        return []
    # 対応ファイル以外を除外する
    file_names = [dir_path_and_name+'/'+name for name in in_folder_list if file_pattern.match(name)]
    # ナチュラルソート
    return natsorted(file_names)

def GetImageFileNames(dir_path_and_name):
    in_folder_list = os.listdir(path=dir_path_and_name)
    # 対応ファイル以外を除外する
    return [dir_path_and_name+'/'+name for name in in_folder_list if file_pattern.match(name)]