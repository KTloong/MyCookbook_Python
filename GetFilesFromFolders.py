import os
import shutil

root_path = r"C:\Users\kingl\Desktop\06100611"

folders = os.listdir(root_path)

folder_paths = [os.path.join(root_path, fpath) for fpath in folders]

p_collection = []

for fp in folder_paths:
    temp = [fpath for fpath in os.listdir(fp) if "0003" in fpath or "0004" in fpath]
    p_t = [os.path.join(fp, spath) for spath in temp]
    p_collection = p_collection + p_t

newdir = r"C:\Users\kingl\Desktop\CBD"

for oldname in p_collection:
    base = os.path.basename(oldname)
    newname = os.path.join(newdir, base)
    shutil.copyfile(oldname, newname)

print("finish")