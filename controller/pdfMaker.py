import tools
import tempfile, os
from natsort import natsorted

def getFileNameFromZip(zip_path):
    path = "/".join(zip_path.split("/")[:-1])+"/tmp/"
    tools.unzip.Unzip(zip_path, path)
    filenames = tools.getFilenameFromDir.GetImageFileNames(path)
    return natsorted(filenames)

def getFileNameFromFolder(folder_path):
    return natsorted(tools.getFilenameFromDir.GetFilenameFromDir(folder_path))