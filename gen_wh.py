# -*-coding:utf-8-*-

dist = "/Users/fuyu/Desktop/dist/" #生成目录
w_prefix_default = "w_" #默认宽前缀
h_prefix_default = "h_" #默认高前缀
w_suffix_default = "_w" #默认宽后缀
h_suffix_default = "_h" #默认高后缀
class Describe(object):
    def __init__(self, file_name, w_density, h_density, w_prefix = w_prefix_default, h_prefix = h_prefix_default,w_suffix = w_suffix_default , h_suffix = h_suffix_default):
        self.file_name = file_name#目录文件夹名称
        self.w_density  = w_density#宽密度
        self.h_density  = h_density#高密度
        self.w_prefix = w_prefix#宽前缀
        self.h_prefix = h_prefix#高前缀
        self.w_suffix = w_suffix#宽后缀
        self.h_suffix = h_suffix#高后缀

files    = (
Describe("values",1,2),
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

lines     = range(start,end + 1,distance)

import os
def main():
    for flie in files:
        file_name = flie.file_name
        w_prefix  = flie.w_prefix
        h_prefix  = flie.h_prefix
        w_suffix  = flie.w_suffix
        h_suffix  = flie.h_suffix
        w_density = flie.w_density
        h_density = flie.h_density
        dimens    = []
        isExists = os.path.exists(dist + file_name)
        if not isExists:
            print("%s创建文件夹%s"%("="*20,dist + file_name))
            os.makedirs(dist + file_name)
        file_object = open(dist + file_name + "/dimens.xml", "w")
        for line in lines:
            width  = " <dimen name=\"%s%s%s\">%spx</dimen>\n"%(w_prefix,line  / accuracy,w_suffix,line / accuracy / w_density)
            height = " <dimen name=\"%s%s%s\">%spx</dimen>\n"%(h_prefix,line  / accuracy,h_suffix,line / accuracy / h_density)
            dimens.append(width)
            dimens.append(height)
        # print(dimens)
        try:
            print("%s往%s内写文件"%("="*20,dist + file_name + "/dimens.xml"))
            file_object.writelines(dimens)
        finally:
            print("%s释放%s资源"%("="*20,dist + file_name + "/dimens.xml"))
            file_object.close()

if __name__ == "__main__":
    main()




