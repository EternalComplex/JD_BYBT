import datetime
import random
import time

from selenium import webdriver
from HiveClient import HiveClient


def random_time(start, end, fmt='%Y-%m-%d %H:%M:%S'):
    stime = datetime.datetime.strptime(start, fmt)
    etime = datetime.datetime.strptime(end, fmt)
    time_datetime = (random.random() * (etime - stime) + stime).strftime(fmt)

    return time_datetime


def random_region():
    t = [
        '北京市', '天津市', '河北省', '山西省', '内蒙古自治区',
        '辽宁省', '吉林省', '黑龙江省',
        '上海市', '浙江省', '安徽省', '福建省', '江西省', '山东省', '台湾省',
        '河南省', '湖北省', '湖南省', '广东省', '广西壮族自治区', '海南省', '香港特别行政区', '澳门特别行政区',
        '重庆市', '四川省', '贵州省', '云南省', '西藏自治区',
        '陕西省', '甘肃省', '青海省', '宁夏回族自治区', '新疆维吾尔自治区',
    ]

    return t[random.randint(0, 32)]


def load_to_hive():
    hive = HiveClient()
    sql = """
        create external table orders(id string, s_id string, s_name string, s_price double, s_num int, source string, u_id string, region string, emt int, plus int, order_time date) row format delimited fields terminated by '^'
        location 'D://JD_BYBT/backend/DataLoader/data/order.csv'
    """
    hive.insert(sql)


if __name__ == "__main__":
    print(random_time('2023-01-01 00:00:00', '2023-12-31 11:59:59'))
    # load_to_hive()