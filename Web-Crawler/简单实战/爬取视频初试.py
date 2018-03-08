import requests
import os

url = "https://v.stu.126.net/mooc-video/nos/mp4/2017/02/28/1005853338_9d53de1c54154b49870ddabec598a073_sd.mp4"
root = r"G:\uestc\假期作业\2018\计通网\爬虫\"
#注意写root的时候，最后要加上一个\
path = root + url.split('/')[-1]
try:
    if not os.path.exists(root):
        os.mkdir(root)
    if not os.path.exists(path):
        r = requests.get(url)
        with open(path,'wb') as f:
            f.write(r.content)
        print("保存成功")
    else :
        print("文件已存在")
except:
    print("爬去失败")
