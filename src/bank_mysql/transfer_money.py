# coding=utf-8
'''
Created on 2017年6月26日

@author: Jianrong
'''
import sys
import pymysql


class transfer_money(object):
    def __init__(self, conn):
        self.conn = conn
        

    def check_account_available(self, account):
        try:
            cursor = self.conn.cursor()
            sql = 'select * from account where account = %s' % account
            cursor.execute(sql)
            if cursor.rowcount != 1:
                raise Exception("account %s not exist!" % account)
        finally:
            cursor.close()
        
    
    def has_enough_money(self, account, number_of_money):
        try:
            cursor = self.conn.cursor()
            sql = 'select money from account where account = %s' % account
            cursor.execute(sql)
            if cursor.fetchone() < number_of_money:
                raise Exception("has no enough money!")
        finally:
            cursor.close()
    
    
    def reduce_money(self, from_account, number_of_money):
        try:
            cursor = self.conn.cursor()
            sql = 'update account set money = money - %s where account = %s' % (number_of_money, from_account)
            cursor.execute(sql)
            if cursor.rowcount != 1:
                raise Exception("reduce money failed!")
        finally:
            cursor.close()
    
    
    def add_money(self, to_account, number_of_money):
        try:
            cursor = self.conn.cursor()
            sql = 'update account set money = money + %s where account = %s' % (number_of_money, to_account)
            cursor.execute(sql)
            if cursor.rowcount != 1:
                raise Exception("add money failed!")
        finally:
            cursor.close()
    
    
    def transfer(self, from_account, to_account, number_of_money):
        try:
            self.check_account_available(from_account)
            self.check_account_available(to_account)
            self.has_enough_money(from_account, number_of_money)
            self.reduce_money(from_account, number_of_money)
            self.add_money(to_account, number_of_money)
            self.conn.commit()
        except Exception as e:
            self.conn.rollback()
            raise e

if __name__ == "__main__":
    from_account = sys.argv[1]
    to_account = sys.argv[2]
    number_of_money = sys.argv[3]
    
    conn = pymysql.Connection(
                            host='localhost',
                            user='root',
                            password='root',
                            db='bank'
                            )
    tr_money = transfer_money(conn)
    
    try:
        tr_money.transfer(from_account, to_account, number_of_money)
    except Exception as e:
        print 'error:' + str(e)
        raise e
    finally:
        conn.close()
