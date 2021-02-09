import requests
import psutil
import tkinter as tk
import shutil


from tkinter import filedialog
print('更新我的世界1.16资源包中...')
'''打开选择文件夹对话框'''
root = tk.Tk()
root.withdraw()

SourceUrl = 'http://downloader1.meitangdehulu.com:22943/Minecraft-Mod-Language-Modpack-1-16.zip'
res = requests.get(SourceUrl)

with open('C:\Minecrafti18nSpace\i18nResource.zip', 'wb') as f:
     f.write(res.content)
pathFile = open("C:\Minecrafti18nSpace\Minecrafti18nPath.txt","r")
local = pathFile.readline()
shutil.copy("C:\Minecrafti18nSpace\i18nResource.zip",local)
print('操作完成')
     
