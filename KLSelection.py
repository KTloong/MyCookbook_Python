import os
from tkinter import filedialog

class KLSelection:
    #pop up a window to select a folder
    def Sfolder(self):
        dirname = filedialog.askdirectory(initialdir=os.getcwd(),title='Please select a folder')
        return dirname #type of dirname is str
    #pop up a window to select a file
    #return a list, [fullname, filename]
    def Sfile(self):
        rawname = filedialog.askopenfilename(title="Please choose a file").split()#divided by space
        fullname = rawname[0]+"/"+rawname[1]
        filename = rawname[1]
        del rawname
        return fullname, filename
    #get the filename list in a folder
    def Gflist(self,fpath):
        flist = os.listdir(fpath)
        print(flist)
        return flist #flist is a list of all the filename in the folder
    #list concatenate fullname
    def Catfullname(self,folder,flist):
        flistfull = []
        for name in flist:
            flistfull.append(folder+"/"+name)
        return flistfull


KLS = KLSelection()
dirfolder = KLS.Sfolder()
flist = KLS.Gflist(dirfolder)
flist_full = KLS.Catfullname(dirfolder,flist)
print(flist_full)
