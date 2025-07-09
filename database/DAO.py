from database.DB_connect import DBConnect
from model.retailer import Retailer


class DAO():
    def __init__(self):
        pass

    @staticmethod
    def get_nodis(nazione):
        conn = DBConnect.get_connection()
        result = []
        cursor = conn.cursor(dictionary=True)
        query = """select gr.Retailer_code , gr.Country,gr.Retailer_name  from go_retailers gr 
                    where gr.Country=%s"""
        cursor.execute(query, (nazione,))
        for row in cursor:
            ret=Retailer(row["Retailer_code"], row["Country"],row["Retailer_name"])
            result.append(ret)
        cursor.close()
        conn.close()
        return result

    @staticmethod
    def get_archis(nazione,anno):
        conn = DBConnect.get_connection()
        result = []
        cursor = conn.cursor(dictionary=True)
        query =""" Select DISTINCT o1.Retailer_code as r1,o2.Retailer_code as r2,count(DISTINCT o1.Product_number) as somma 
					from go_daily_sales o1 , go_daily_sales o2 , go_retailers gr  , go_retailers gr2
                    where   gr2.Country=%s and gr.Country=gr2.Country and
                            gr.Retailer_code=o1.Retailer_code and
                            gr2.Retailer_code=o2.Retailer_code and
                            year(o2.`Date` )=%s  and year(o1.`Date`) = year(o2.`Date`)  and
                            o1.Product_number=o2.Product_number  and o1.Retailer_code!=o2.Retailer_code 
                            group by o1.Retailer_code,o2.Retailer_code"""
        cursor.execute(query, (nazione,anno,))
        for row in cursor:
            result.append([row["r1"],row["r2"], row["somma"]])
        cursor.close()
        conn.close()
        return result

    @staticmethod
    def get_nazioni():
        conn = DBConnect.get_connection()
        result = []
        cursor = conn.cursor(dictionary=True)
        query = """ Select DISTINCT Country from go_retailers"""
        cursor.execute(query)
        for row in cursor:
            result.append(row["Country"])
        cursor.close()
        conn.close()
        return result

    @staticmethod
    def get_anni():
        result = [2015,2016,2017,2018]
        return result

