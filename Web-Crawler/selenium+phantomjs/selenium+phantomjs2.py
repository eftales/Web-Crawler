from selenium import webdriver
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
import requests
import zjc_lib

path = "G:\\uestc\\假期作业\\2018\\计通网\\爬虫\\简单实战\\picture"
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/52.0.2743.116 Safari/537.36 Edge/15.15063'
}

done = ["偷窥孔 13卷", "偷窥孔 12卷", "偷窥孔 11卷", "偷窥孔 10卷","偷窥孔 09卷","偷窥孔 08卷","偷窥孔 07卷","偷窥孔 04卷" ,"偷窥孔 03卷" ,"偷窥孔 02卷" ,"偷窥孔 01卷" ]

def until30(url):
    try:
        r = requests.get(url, headers=headers, timeout=30)
    except requests.exceptions.MissingSchema:
        return None
    return r

def pic_download(url, save_path, name, driver, page):
    html = getHTMLText(url, driver)
    e_loc = html.find('.JPG', 0)
    b_loc = html.find('src', e_loc - 255)
    url = html[b_loc + 5:e_loc] + '.JPG'
    try:

        resp = until30(url)
        while resp == None:
            resp = until30(url)
        save_path += '\\' + str(page) + '.JPG'
        with open(save_path, 'wb') as f:
            f.write(resp.content)
        return 1


    except:
        return 0


def getHTMLText(url, driver):
    try:
        driver.get(url)  # 加载网页
        data = driver.page_source  # 获取网页文本
        return data
    except:
        print("爬取失败")
        return ""


def unic_Analysis( html, index, path, driver):
    beg_location = 0
    s_url = "http://www.hhmmoo.com/"
    n = 0
    while 1:

        try:
            beg_location = html.find(index, beg_location + 1)
            end_location = html.find("title=", beg_location)
            url = s_url + html[beg_location + 20:end_location - 18]
            name = html[end_location + 7:end_location + 14]
            if name in done :
                continue

            save_path = path + "\\" + name  ####章节名称
            save_path = save_path.replace(' ', '')
            zjc_lib.mkdir(save_path)

            does_exist = 1
            page = 1
            while does_exist:
                if name == "偷窥孔 06卷" and page <= 179:#====15?
                    page += 1
                    continue
                link = url.replace('1.html', '%d.html' % page)
                does_exist = pic_download(link, save_path, name, driver, page)
                page += 1
        except:
            break
        n += 1


def setdriver():
    driver = webdriver.PhantomJS()
    driver.maximize_window()  # 设置全屏
    driver.set_window_size('480', '800')  # 设置浏览器宽480，高800

    dcap = dict(DesiredCapabilities.PHANTOMJS)  # 设置useragent
    dcap['phantomjs.page.settings.userAgent'] = (
        'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.9; rv:25.0) Gecko/20100101 Firefox/25.0 ')  # 根据需要设置具体的浏览器信息
    driver = webdriver.PhantomJS(desired_capabilities=dcap)  # 封装浏览器信息
    return driver


def main():
    zjc_lib.mkdir(path)

    driver = setdriver()
    url = "http://www.hhmmoo.com/manhua8379.html"
    html = getHTMLText(url, driver)
    index = "a class="
    unic_Analysis(html, index, path, driver)
    driver.quit()


main()


