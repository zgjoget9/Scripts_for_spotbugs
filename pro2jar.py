# @author: zgjoget9
# @Date: 2021年03月19日19:10:09
# @Time: 19:10:09
# @File: process2jar.py

import os,shutil

def mkdir(path): 
	folder = os.path.exists(path) 
	if not folder:                   #判断是否存在文件夹如果不存在则创建为文件夹
		os.makedirs(path)            #makedirs 创建文件时如果路径不存在会创建这个路径
		print("create new folder")

def extra_jar(src,des_file):
    num=0
    for root,ds,fs in os.walk(src):
        for f in fs:
            portion=os.path.splitext(f)
            if portion[1]=='.jar':
                if portion[0].find('source')!=-1:
                    f=f[0:-12];
                    f+='.jar'
                    num+=1
                    filepath=os.path.join(root,f)
                    des_file.write(filepath)
                    des_file.write('\n')
    return num

def main():
    base= os.getcwd()
    ls=os.listdir(base)
    n=0
    for l in ls:
        if os.path.isdir(l):
            src=os.path.join(base,l)
            print("src",src)
            des=os.path.join(base,l,"jars.txt") 
            print("des",des)
            des_file=open(des,'w')
            n=extra_jar(src,des_file)
            print(n)
            des_file.close()
        else:
            continue


if __name__=='__main__':
    main()
       
        

