import os, re

correspond_file_pat = '.+\.(png|PNG|jpg|JPG|jpeg|JPEG|webp|WEBP)'
file_pattern = re.compile(correspond_file_pat)

def GetImageFileNames(dir_path_and_name):
    in_folder_list = os.listdir(path=dir_path_and_name)
    # 対応ファイル以外を除外する
    return [name for name in in_folder_list if file_pattern.match(name)]