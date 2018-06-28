import os
from os import listdir
from os.path import join
import shutil
from shutil import copyfile
#directory from where to copy files
frompath="/home/animesh/Documents/Ecell"
os.chdir(frompath)
#list of files ending with '.html',change it according to need
html_files = [join(frompath, f) for f in os.listdir(frompath) if f.endswith('.html')]

#shows the list of html files with path directory
print html_files
#directory to paste the extracted html files
topath="/home/animesh/Documents/Ecell/newdir"
os.mkdir(topath, 0755)
for f in html_files:
    shutil.copy(f,topath)