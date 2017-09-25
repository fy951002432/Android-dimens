# -*-coding:utf-8-*-


prefix_default = "__" #默认前缀
suffix_default = "__" #默认后缀
dpi_default = 320     #默认屏幕密度 240x320:120 320x480:160 480x800:240 720x1280:320	 1080x1920:480
class Describe(object):
    def __init__(self, file_name, dpi, prefix = prefix_default,suffix = suffix_default):
        self.file_name = file_name #目录文件夹名称
        self.dpi  = dpi            #屏幕密度
        self.prefix = prefix       #前缀
        self.suffix = suffix       #后缀

dist = "/Users/fuyu/Desktop/dist/" #生成目录
distance = 1 #隔多少位
start    = 0 #开始
end      = 10000 #结束
accuracy = 10.0  #多少位代表一个单位
lines     = range(start,end + 1,distance)
files    = (
Describe("values",320),
Describe("values-ldpi",120),
Describe("values-mdpi",160),
Describe("values-hdpi",240),
Describe("values-xhdpi",320),
Describe("values-xxhdpi",480)
)
import os
def main():
    for flie in files:
        file_name = flie.file_name
        prefix    = flie.prefix
        suffix    = flie.suffix
        dpi       = flie.dpi
        dimens    = []
        isExists = os.path.exists(dist + file_name)
        if not isExists:
            print("%s创建文件夹%s"%("="*20,dist + file_name))
            os.makedirs(dist + file_name)
        file_object = open(dist + file_name + "/dimens.xml", "w")
        for line in lines:
            dimen  = " <dimen name=\"%s%s%s\">%spx</dimen>\n"%(prefix,line  / accuracy,suffix,line / accuracy * dpi / dpi_default)
            dimens.append(dimen)
        # print(dimens)
        try:
            print("%s往%s内写文件"%("="*20,dist + file_name + "/dimens.xml"))
            file_object.writelines(dimens)
            print("%s往%s内写文件完成"%("="*20,dist + file_name + "/dimens.xml"))
        except:
            print("%s往%s内写文件错误" % ("=" * 20, dist + file_name + "/dimens.xml"))
        finally:
            print("%s释放%s资源"%("="*20,dist + file_name + "/dimens.xml"))
            file_object.close()

if __name__ == "__main__":
    main()




