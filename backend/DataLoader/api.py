import flask, json
from flask_cors import CORS

server = flask.Flask(__name__)
cors = CORS(server, resources={r"/api/*": {"origins": "*"}})

sales, hots, operation, region = [], [], [], []


def load_data():
    global sales, hots, operation, region
    # 销售额趋势图-折线图
    with open('./data/output/sales/000000_0', 'r', encoding='utf-8') as f:
        sales = list(map(lambda x: x.replace('\n', '').split('^'), f.readlines()))
    # 热门产品-列表
    with open('./data/output/hots/000000_0', 'r', encoding='utf-8') as f:
        hots = list(map(lambda x: x.replace('\n', '').split('^'), f.readlines()))
    # 用户购买行为-漏斗图
    with open('./data/output/operation/000000_0', 'r', encoding='utf-8') as f:
        operation = list(map(lambda x: x.replace('\n', '').split('^'), f.readlines()))[0]
    # 百亿补贴主要用户人群分布图
    with open('./data/output/region/000000_0', 'r', encoding='utf-8') as f:
        region = list(map(lambda x: x.replace('\n', '')
                          .replace('省', '')
                          .replace('自治区', '')
                          .replace('维吾尔', '')
                          .replace('特别行政区', '')
                          .replace('回族', '')
                          .replace('壮族', '')
                          .replace('市', '')
                          .split('^'), f.readlines()))


@server.route("/api/sales", methods=['get'])
def sales():
    """
    销售额趋势
    :return:
    """
    return json.dumps({"data": list(map(lambda x: x[1], sales))})


@server.route("/api/hots", methods=['get'])
def hots():
    """
    热门产品
    :return:
    """
    return json.dumps({"data": hots}, ensure_ascii=False)


@server.route("/api/operation", methods=['get'])
def operation():
    """
    用户购买行为
    :return:
    """
    return json.dumps({"data": operation})


@server.route("/api/region", methods=['get'])
def region():
    """
    百亿补贴主要用户人群分布
    :return:
    """
    return json.dumps({"data": list(map(lambda x: {'name': x[0], 'value': int(x[1])}, region))}, ensure_ascii=False)


if __name__ == "__main__":
    load_data()
    server.run(debug=True, port=8888, host='0.0.0.0')