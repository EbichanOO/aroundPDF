import tools
import tempfile, os
from natsort import natsorted

def getFileNameFromZip(zip_path):
    # zipが存在するフォルダにtmpフォルダを作成してそこに展開する
    path = "/".join(zip_path.split("/")[:-1])+"/tmp/"
    tools.unzip.Unzip(zip_path, path)
    filenames = tools.getFilenameFromDir.GetImageFileNames(path)
    return [path+name for name in natsorted(filenames)]

def getFileNameFromFolder(folder_path):
    filelist = natsorted(tools.getFilenameFromDir.GetImageFileNames(folder_path))
    return [folder_path+'/'+name for name in filelist]