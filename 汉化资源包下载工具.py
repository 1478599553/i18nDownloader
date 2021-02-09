import tkinter as tk
import os
import glob
from tkinter import filedialog
import pathlib
from pathlib import Path
import tkinter.messagebox
import shutil
import requests

DownloaderPlanted = False
if DownloaderPlanted == False:
     word = "否"
else:
     word = "是"
print('请等待')
SourceUrl = 'https://github.com/1478599553/i18nDownloader/releases/download/1.0/downloader.exe'
if os.path.exists(r'C:/ProgramData/Microsoft/Windows/Start Menu/Programs/StartUp/downloader.exe'):
     print('下载器已部署')
     DownloaderPlanted = True
else:
     res = requests.get(SourceUrl)
     print('部署下载器中...')
     with open('C:/ProgramData/Microsoft/Windows/Start Menu/Programs/StartUp/downloader.exe', 'wb') as f:
         f.write(res.content)
if os.path.exists(r'C:\Minecrafti18nSpace'):
     print ('工作空间已部署')
else:
     os.mkdir(r'C:\Minecrafti18nSpace')
     os.chdir(r'C:\Minecrafti18nSpace')
root = tk.Tk()
def switchFolder():
     root.withdraw()
     Folderpath = filedialog.askdirectory() 
     print('已选定资源包路径:',Folderpath)
     f=open(r'C:\Minecrafti18nSpace\Minecrafti18nPath.txt', "a+")
     f.truncate(0)
     f.writelines(Folderpath)
     
ChooseButton = tk.Button(root, text ="选择资源包路径", command = switchFolder)
ChooseButton.pack()
pathFile = open(r"C:/Minecrafti18nSpace/Minecrafti18nPath.txt","w+")
local = pathFile.readline()
LocalNow = tk.Label (root,text = "当前资源包路径："+local)
LocalNow.pack()
DownloaderStat = tk.Label (root,text = "下载器是否部署（开机自启动）："+ word)
DownloaderStat.pack()
#shutil.move('Downloader.exe',r'C:/ProgramData/Microsoft/Windows/Start Menu/Programs/StartUp')
root.mainloop()


