import flask, json
from flask import request
from HiveClient import HiveClient


server = flask.Flask(__name__)
hive = HiveClient()


# TODO 销售额趋势图
# TODO 热门产品
# TODO 用户购买行为漏斗图
# TODO 百亿补贴主要用户人群分布图
@server.route("/test", methods=['get'])
def tt():
    """
    热门产品
    :return:
    """
    sql = "select s_name, count(s_price * s_num) from orders group by s_name"
    res = hive.query(sql)
    return json.dumps({"data": res})


if __name__ == "__main__":
    server.run(debug=True, port=8888, host='0.0.0.0')
