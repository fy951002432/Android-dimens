# -*-coding:utf-8-*-
dist             = "/Users/fuyu/-/example-wh/" #生成目录 结尾加/
w_prefix_default = "w_"                        #默认宽前缀
h_prefix_default = "h_"                        #默认高前缀
w_suffix_default = "_w"                        #默认宽后缀
h_suffix_default = "_h"                        #默认高后缀
width_default    = 720                         #默认屏幕宽
height_default   = 1280                        #默认屏幕高
class Describe(object):
    def __init__(self, file_name, width, height, w_prefix = w_prefix_default, h_prefix = h_prefix_default,w_suffix = w_suffix_default , h_suffix = h_suffix_default):
        self.file_name = file_name #目录文件夹名称
        self.width     = width     #宽
        self.height    = height    #高
        self.w_prefix  = w_prefix  #宽前缀
        self.h_prefix  = h_prefix  #高前缀
        self.w_suffix  = w_suffix  #宽后缀
        self.h_suffix  = h_suffix  #高后缀

files    = (
Describe("values",720,1080),
Describe("values-240x320",240,320),
Describe("values-320x480",320,480),
Describe("values-480x800",480,800),
Describe("values-720x1280",720,1280),
Describe("values-1080x1920",1080,1920)
)

start    = 0        #开始
end      = 10000    #结束
accuracy = 10.0     #多少位代表一个单位
distance = 1        #隔多少位

lines    = range(start,end + 1,distance)

import os
def main():
    for flie in files:
        file_name = flie.file_name
        w_prefix  = flie.w_prefix
        h_prefix  = flie.h_prefix
        w_suffix  = flie.w_suffix
        h_suffix  = flie.h_suffix
        width     = flie.width
        height    = flie.height
        dimens    = []
        isExists = os.path.exists(dist + file_name)
        if not isExists:
            print("%s创建文件夹%s"%("="*20,dist + file_name))
            os.makedirs(dist + file_name)
        file_object = open(dist + file_name + "/dimens.xml", "w")
        for line in lines:
            dimen_width  = " <dimen name=\"%s%s%s\">%spx</dimen>\n"%(w_prefix,line  / accuracy ,w_suffix,str(line * width / accuracy  / width_default))
            dimen_height = " <dimen name=\"%s%s%s\">%spx</dimen>\n"%(h_prefix,line  / accuracy ,h_suffix,str(line * height / accuracy  / height_default))
            dimens.append(dimen_width)
            dimens.append(dimen_height)
        # print(dimens)
        try:
            print("%s往%s内写文件"%("="*20,dist + file_name + "/dimens.xml"))
            file_object.writelines(dimens)
        finally:
            print("%s释放%s资源"%("="*20,dist + file_name + "/dimens.xml"))
            file_object.close()

if __name__ == "__main__":
    main()




