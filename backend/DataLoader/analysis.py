from HiveClient import HiveClient

hive = HiveClient()


# TODO 销售额趋势图
def sales():
    sql = """
        insert overwrite local directory '/home/hadoop/output/sales'
        row format delimited fields terminated by '^'
        select 
            mounth, 
            sum(total) 
        from
            (select 
                date_format(order_time, 'MM') as mounth, 
                cast(sum(s_price * s_num) as decimal(10, 2)) as total 
            from orders group by order_time) as t1
        group by t1.mounth
    """
    hive.query(sql)


# TODO 热门产品
def hots():
    sql = """
        insert overwrite local directory '/home/hadoop/output/hots'
        row format delimited fields terminated by '^'
        select 
            s_name, 
            sum(s_num) as num 
        from orders 
        group by s_name 
        having s_name != ""
        sort by num desc 
        limit 10
    """
    hive.query(sql)


# TODO 用户购买行为漏斗图
# 浏览选购
# 添加购物车
# 提交订单
# 完成支付
def operation():
    sql = """
        insert overwrite local directory '/home/hadoop/output/operation'
        row format delimited fields terminated by '^'
        select 
            count(if(status=0, 1, null)) as c1, 
            count(if(status=1, 1, null)) as c2, 
            count(if(status=2, 1, null)) as c3, 
            count(if(status=3, 1, null)) as c4 
        from orders
    """
    hive.query(sql)


# TODO 百亿补贴主要用户人群分布图
def region():
    sql = """
        insert overwrite local directory '/home/hadoop/output/region'
        row format delimited fields terminated by '^'
        select 
            region, 
            count(1) as cnt 
        from orders 
        group by region 
        order by cnt
    """
    hive.query(sql)


if __name__ == '__main__':
    sales()
    hots()
    operation()
    region()