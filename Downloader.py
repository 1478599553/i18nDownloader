import tkinter as tk
import os
import glob
from tkinter import filedialog
import pathlib
from pathlib import Path
import tkinter.messagebox
import shutil
import requests
import os
import time


Doit = True
verSwitched = False

#ResourceSourceUrl = 'http://downloader1.meitangdehulu.com:22943/Minecraft-Mod-Language-Modpack-1-16.zip'
selfLocate=os.getcwd()
selfLocatePlus = selfLocate +'/Downloader.exe'

if os.path.exists(r'C:\Minecrafti18nSpace'):
     print ('工作空间已部署')
else:
     print('部署工作空间中...')
     os.mkdir(r'C:\Minecrafti18nSpace')
     os.chdir(r'C:\Minecrafti18nSpace')

def DoBoot():
     fb=open(r'C:/Minecrafti18nSpace/IfRunOnBooting.txt',"w+")
     fb.truncate(0)
     fb.write('1')
     fb.close()

def DonotBoot():
     dfb=open(r'C:/Minecrafti18nSpace/IfRunOnBooting.txt',"w+")
     dfb.truncate(0)
     dfb.write('2')
     dfb.close()

def KillBoot():
     IsBoot = "否"
     if os.path.exists(r'C:/ProgramData/Microsoft/Windows/Start Menu/Programs/StartUp/Downloader.exe'):
          os.remove("C:/ProgramData/Microsoft/Windows/Start Menu/Programs/StartUp/Downloader.exe")
          print ('不再开机启动')
          tkinter.messagebox.showinfo('成功！','不再开机启动')
     else:
          print ('汉化资源包下载工具未设为开机自启动')
          
def CpToBoot():
     selfLocate=os.getcwd()
     selfLocatePlus = selfLocate +'/Downloader.exe'
     shutil.copy(selfLocate+'/Downloader.exe','C:/ProgramData/Microsoft/Windows/Start Menu/Programs/StartUp/Downloader.exe')
     selfLocate=os.getcwd()
     selfLocatePlus = selfLocate +'/Downloader.exe'
     print (selfLocatePlus)
     tkinter.messagebox.showinfo('成功！','已设为开机自启动')
def SwitchFolder():
     Folderpath = filedialog.askdirectory() 
     print('已选定资源包路径:',Folderpath)
     f=open(r'C:\Minecrafti18nSpace\Minecrafti18nPath.txt', "w+")
     f.truncate(0)
     f.writelines(Folderpath)
     tkinter.messagebox.showinfo('成功！','已选择资源包路径为：'+Folderpath)
def Download():
     readVer = open(r'C:\Minecrafti18nSpace\Version.txt',"r")
     Ver = readVer.readline()
     if Ver == "":
          tkinter.messagebox.showinfo('错误！','未指定资源包版本，无法下载')
     else:
          Resourceres = requests.get(Ver)
          
          with open('C:\Minecrafti18nSpace\i18nResource.zip', 'wb') as file:
                    file.write(Resourceres.content)
          Pathfile=open(r'C:\Minecrafti18nSpace\Minecrafti18nPath.txt', "r")
          Path = Pathfile.readline()
          if Path == "":
               tkinter.messagebox.showinfo('错误！','未指定资源包文件夹路径，但已下载资源包至C:\Minecrafti18nSpace\i18nResource.zip')
          else:
               shutil.copy(r'C:\Minecrafti18nSpace\i18nResource.zip',Path)
               tkinter.messagebox.showinfo('成功！','已下载资源包至'+Path)
     

def write112():
     w112 = open(r'C:\Minecrafti18nSpace\Version.txt',"w+")
     w112.write('http://downloader1.meitangdehulu.com:22943/Minecraft-Mod-Language-Modpack.zip')
     
     tkinter.messagebox.showinfo('成功！','已将下载资源包版本设为1.12')
def write116():
     w112 = open(r'C:\Minecrafti18nSpace\Version.txt',"w+")
     w112.write('http://downloader1.meitangdehulu.com:22943/Minecraft-Mod-Language-Modpack-1-16.zip')
     
     tkinter.messagebox.showinfo('成功！','已将下载资源包版本设为1.16')

def Exit():
     os._exit(0)

def pre():
     if os.path.exists('') == False:
          shutil.copy(selfLocatePlus,'C:\Minecrafti18nSpace\Downloader.exe')
          tkinter.messagebox.showinfo('成功！','已创建用于启动器预启动的副本，在 C:\Minecrafti18nSpace\Downloader.exe')
     else:
          tkinter.messagebox.showinfo('没事！','早就已经创建了用于启动器预启动的副本！在 C:\Minecrafti18nSpace\Downloader.exe')
while Doit:
     
     #if Ver == "":
     #     tkinter.messagebox.showinfo('错误！','未指定资源包版本，无法下载')
     #else:
     #     Resourceres = requests.get(Ver)
     print(selfLocatePlus)
     if selfLocatePlus == r'C:\WINDOWS\system32/Downloader.exe':
          IsDownloader = True
          print ('以下载器模式启动')
          readVer = open(r'C:\Minecrafti18nSpace\Version.txt',"r")
          Ver = readVer.readline()
          print('更新Minecraft汉化资源包中...')
          if Ver == "":
               tkinter.messagebox.showinfo('错误！','未指定资源包版本，请打开主程序配置')
               time.sleep(15)
               os._exit(0)
          else:
               Resourceres = requests.get(Ver)
               with open('C:\Minecrafti18nSpace\i18nResource.zip', 'wb') as file:
                         file.write(Resourceres.content)
               Pathfile=open(r'C:\Minecrafti18nSpace\Minecrafti18nPath.txt', "r")
               Path = Pathfile.readline()
               shutil.copy(r'C:\Minecrafti18nSpace\i18nResource.zip',Path)
               time.sleep(114514)
     else:
          if selfLocatePlus ==r'C:\Minecrafti18nSpace\Downloader.exe':
               IsDownloader = True
               print ('以下载器模式启动')
               readVer = open(r'C:\Minecrafti18nSpace\Version.txt',"r")
               Ver = readVer.readline()
               print('更新Minecraft汉化资源包中...')
               if Ver == "":
                    tkinter.messagebox.showinfo('错误！','未指定资源包版本，请打开主程序配置')
                    time.sleep(15)
                    os._exit(0)
               else:
                    Resourceres = requests.get(Ver)
                    with open('C:\Minecrafti18nSpace\i18nResource.zip', 'wb') as file:
                              file.write(Resourceres.content)
                    Pathfile=open(r'C:\Minecrafti18nSpace\Minecrafti18nPath.txt', "r")
                    Path = Pathfile.readline()
                    shutil.copy(r'C:\Minecrafti18nSpace\i18nResource.zip',Path)
                    os._exit(0)
          else:

               print('以启动器方式启动')
               root = tk.Tk()
               root.title('汉化资源包外置下载工具')
               d112= tk.Button ( root, text = '将资源包版本设为1.12', command = write112)
               d112.pack()
               d116= tk.Button ( root, text = '将资源包版本设为1.16', command = write116)
               d116.pack()
               Downloader = tk.Button (root,text = "下载资源包",command = Download)
               
               Switcher = tk.Button(root, text = '选择资源包文件夹',command =SwitchFolder)
               Switcher.pack()
               Boot = tk.Button ( root,text = "设为开机启动" ,command =CpToBoot)
               Boot.pack()
               DonotBoot = tk.Button ( root, text = '关闭开机启动', command = KillBoot)
               DonotBoot.pack()
               TipLabel = tk.Label (root , text = "下载资源包可能导致程序暂时无响应，请耐心等待！")
               TipLabel.pack()
               Downloader.pack()
               RePathfile=open(r'C:\Minecrafti18nSpace\Minecrafti18nPath.txt', "r")
               RePath = RePathfile.readline()
               PathLabel = tk.Label (root , text = "当前资源包文件夹路径：" + RePath)
               PathLabel.pack()
               PreBoot = tk.Button(root,text = "创建用于 HMCL / MMC预启动的副本",command = pre)
               PreBoot.pack()
               Exit = tk.Button (root , text = "退出程序",command = Exit)
               Exit.pack()
               
               root.mainloop()
               time.sleep(1)
     
