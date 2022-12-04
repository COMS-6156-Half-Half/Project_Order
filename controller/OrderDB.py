import pymysql
import os

class OrderDB:

    def __int__(self):
        pass

    @staticmethod
    def _get_connection():

        conn = pymysql.connect(
            user="root",
            password="13886003474cjw",
            host="e61561.cwsqeuuovxq1.us-east-1.rds.amazonaws.com",
            cursorclass=pymysql.cursors.DictCursor,
            autocommit=True
        )
        return conn

    @staticmethod
    def insert_record(order_id, seller_id, product_id, buyer_id):
        sql = "Insert into OrderRecord.record VALUES (%s, %s, %s, %s)"
        conn = OrderDB._get_connection()
        cur = conn.cursor()
        res = cur.execute(sql, args=[order_id, seller_id, product_id, buyer_id])

        return res

    @staticmethod
    def get_all():

        sql = "SELECT * FROM OrderRecord.record"
        conn = OrderDB._get_connection()
        cur = conn.cursor()
        res = cur.execute(sql)
        result = cur.fetchall()

        return result

    @staticmethod
    def get_by_sellerId(seller_id):
        sql = "SELECT * FROM OrderRecord.record where seller_id=%s"
        conn = OrderDB._get_connection()
        cur = conn.cursor()
        res = cur.execute(sql,args=seller_id)
        result = cur.fetchall()

        return result

    @staticmethod
    def get_by_buyerId(buyer_id):
        sql = "SELECT * FROM OrderRecord.record where buyer_id=%s"
        conn = OrderDB._get_connection()
        cur = conn.cursor()
        res = cur.execute(sql, args=buyer_id)
        result = cur.fetchall()

        return result

    @staticmethod
    def delete_by_orderId(order_id):
        sql = "DELETE from OrderRecord.record where order_id=%s"
        conn = OrderDB._get_connection()
        cur = conn.cursor()
        res = cur.execute(sql, args=order_id)

        return res
