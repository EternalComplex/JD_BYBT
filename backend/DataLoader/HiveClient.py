from pyhive import hive


class HiveClient:
    def __init__(self, host='192.168.10.102', port=10000, username='hadoop', database='jd'):
        self.conn = hive.Connection(
            host=host,
            port=port,
            username=username,
            database=database
        )

    def query(self, sql):
        with self.conn.cursor() as cursor:
            cursor.execute(sql)
            return cursor.fetchall()

    def insert(self, sql):
        with self.conn.cursor() as cursor:
            try:
                cursor.execute(sql)
                self.conn.commit()
            except:
                self.conn.rollback()


if __name__ == '__main__':
    hive = HiveClient()
    # hive.insert('create table test(id int, name String)')
    print(hive.query('show tables'))
    # print(hive.query("load data local inpath 'd:/backend/DataLoader/data/order.csv' into table orders"))
    print(hive.query('select * from orders'))