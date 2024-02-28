import datetime
import random
import time
import requests
from lxml import etree
from utils import random_time, random_region
import uuid


def get_detail_urls(base_url, headers):
    # 获取商品详情页url
    for i in range(1, 200, 2):
        url = base_url + str(i)
        response = etree.HTML(requests.session().get(url, headers=headers).text)

        urls = response.xpath('/html/body/div[5]/div[2]/div[2]/div[1]/div/div[2]/ul/li[*]/div/div[3]/a/@href')

        with open('./data/detail_urls.txt', 'a', encoding='utf-8') as f:
            for u in urls:
                t = 'https:' + u
                s_id = t.replace('https://item.jd.com/', '').replace('.html', '')
                s_price = response.xpath('//*[@class="J_' + s_id + '"]/i/text()')[0]
                f.write(str([t, s_id, s_price]) + "\n")
                print([t, s_id, s_price])
            time.sleep(2)


def get_detail_info(detail_urls):
    # 采集每件商品的信息
    for detail_url, s_id, s_price in detail_urls:
        response = etree.HTML(requests.session().get(detail_url, headers=headers).text)

        # 商品id
        s_id = s_id
        # 商品名
        s_name = response.xpath('//*[@class="item ellipsis"]/text()')
        # 货源
        source = response.xpath('//*[@class="mt"]/h3/a/@title')
        # 商品单价
        s_price = s_price

        a = [0, 1, 2, 3]
        weight = [100, 50, 25, 5]

        with (open('./data/orders_2.csv', 'a', encoding='utf-8') as f):
            for x in range(random.randint(1, 3)):
                length = random.randint(50, 100)
                ran = random.choices(a, weight, k=length)
                # 订单id^商品id^商品名称^商品单价^商品数量^货源^下单用户id^ip属地^状态^下单时间
                for i in range(length):
                    info = '^'.join(map(str, [
                        uuid.uuid4(),
                        s_id,
                        s_name,
                        s_price,
                        random.randint(1, 5),
                        source,
                        random.randint(1, 1000),
                        random_region(),
                        ran[i],
                        random_time('2023-01-01 00:00:00', '2023-12-31 11:59:59')
                    ])).replace('[', '').replace(']', '').replace('\'', '')

                    print(info)

                    f.write(info + '\n')
        time.sleep(10)


if __name__ == "__main__":
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/121.0.0.0 Safari/537.36',
        'Cookie': '__jdu=17021874123781376103265; pinId=KYSmuupCiSQOGGlbd3ibcrV9-x-f3wj7; shshshfpa=eb5c9739-ebd4-0e41-124b-c6f0405c97ad-1702187609; shshshfpx=eb5c9739-ebd4-0e41-124b-c6f0405c97ad-1702187609; jcap_dvzw_fp=lnEB0XF88o4GhGLWhvzmtKlPFY5WEkbv39HB32jzIIGxjSwHaizylhG9k0tjhlS0T76cC6WrVd1FjILgOdj-gQ==; __jdv=181111935%7Cwww.google.com%7C-%7Creferral%7C-%7C1708669157509; autoOpenApp_downCloseDate_jd_homePage=1708669157791_1; pin=jd_7209bf1013d82; unick=eternal_complex; _tp=CPiavW20VeJkC0gKm6WV834d3IjNUb285fM5IZfvzAA%3D; _pst=jd_7209bf1013d82; ipLoc-djd=19-1607-0-0; jsavif=1; areaId=19; PCSYCityID=CN_440000_440300_0; shshshfpb=BApXeUtvG1-hAqjkpGZPg9aCCr4f7miZ3BkBZcSZ09xJ1Mh7mZIO2; 3AB9D23F7A4B3CSS=jdd033SJEA57QM3I562KFCFK2AXDBBRZXA6ZKGCCH6EDO4TZE2VSSXYNB7EENKDMHLOLXPV2E3XCIL4JMDLSES62PCYBA4YAAAAMN2TILJVIAAAAACVYV6M3IDX5MTAX; wlfstk_smdl=cbnictsr86cz0gny9lb4p2m7tqn46rti; 3AB9D23F7A4B3C9B=3SJEA57QM3I562KFCFK2AXDBBRZXA6ZKGCCH6EDO4TZE2VSSXYNB7EENKDMHLOLXPV2E3XCIL4JMDLSES62PCYBA4Y; TrackID=1IZFxOAsu50P28kuFL2mb0qjA9HOGzd6Uukpta6IJIC2v7Mw8ZAnaLh1DZPgRqjZbH7053zIdJd1-vZW4dat3PwwdPl8eO9qb7keM9Yc8ONw; thor=45A0E79DF4CB9F97AF2FF6E3ED700272564944F8F11C4718DDEB1A1F1FF21D468B2D1F77D629F284F004DE4AAB2367E922E8487E20F27C14C3B9B4719EA9EB8E286DFB43C11E66728065414B4AE24A9BC147D78E235E8AF630A7C1E7C8192DC4CA9E3BC3113473C1078B9B6ACB4ADA23122F935D321031935B1DACE8AC320CC7C2FF0F52C628E350B1F1D7534DAAFDA7E01006A42D35C115B360377AD89C2A17; flash=2_DpT57QD6UhhPDRWRusAvOec3UxbAmDA-AR8q2h_80YPyoDavS_lT7OxaCL2WyG11ctrs9GTth2YAme-GmCafE2lGDYl2XJCHnutUF-4zrfq*; ceshi3.com=103; __jda=173673530.17021874123781376103265.1702187412.1708669157.1708671194.10; __jdb=173673530.11.17021874123781376103265|10.1708671194; __jdc=173673530'
    }

    base_url = 'https://search.jd.com/search?keyword=%E7%99%BE%E4%BA%BF%E8%A1%A5%E8%B4%B4&page='

    # get_detail_urls(base_url, headers)

    with open('./data/detail_urls.txt', 'r', encoding='utf-8') as f:
        urls = f.readlines()

        detail_urls = []
        for url in urls:
            detail_url = url.replace('\n', '').split(',')
            detail_urls.append(detail_url)

        get_detail_info(detail_urls)
