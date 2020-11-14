import mysql.connector
from datetime import date

class Bill:

    def __init__(self, number=0, sklad=None, detail=None, date_poluch=None, price=None, remontnik=None):
        self.number = number
        self.sklad = sklad
        self.detail = detail
        self.date_poluch = date_poluch
        self.price = price
        self.remontnik = remontnik

    @staticmethod
    def get_bill():
        conn = mysql.connector.connect(user='root', password='Qwerty1bNb', host='127.0.0.1', database='db1')
        c = conn.cursor()
        result = []
        c.execute('SELECT * FROM Накладная')
        rows = c.fetchall()
        for row in rows:
            bill = Bill(row[0], row[1], row[2], row[3], row[4], row[5])
            result.append(bill)
        c.close()
        conn.close()
        return result

    @staticmethod
    def add_bill(number, sklad, detail, date_poluch, price, remontnik):
        conn = mysql.connector.connect(user='root', password='Qwerty1bNb', host='127.0.0.1', database='db1')
        c = conn.cursor()
        c.execute('insert into Накладная values(%s, %s, %s, %s, %s, %s)', \
                  (int(number), int(sklad), int(detail), date.fromisoformat(date_poluch), price, int(remontnik),))
        conn.commit()
        c.close()
        conn.close()

    @staticmethod
    def delete_bill(uid):
        conn = mysql.connector.connect(user='root', password='Qwerty1bNb', host='127.0.0.1', database='db1')
        c = conn.cursor()
        c.execute("DELETE FROM Накладная WHERE id_Накладная = %i" % (uid))
        conn.commit()
        c.close()
        conn.close()

    @staticmethod
    def update_bill(number, sklad='', detail='', date_poluch='', price='', remontnik=''):
        conn = mysql.connector.connect(user='root', password='Qwerty1bNb', host='127.0.0.1', database='db1')
        c = conn.cursor()
        if sklad != '':
            c.execute("""UPDATE Накладная SET Склад = '%s' WHERE id_Накладная = %s""" % (int(sklad), int(number)))
        if detail != '':
            c.execute("""UPDATE Накладная SET Название_детали = '%s' WHERE id_Накладная = %s""" % (int(detail), int(number)))
        if date_poluch != '':
            c.execute("""UPDATE Накладная SET Дата_получения = '%s' WHERE id_Накладная = %s""" % (date.fromisoformat(date_poluch), int(number)))
        if price != '':
            c.execute("""UPDATE Накладная SET Цена_детали_на_дату_получения = '%s' WHERE id_Накладная = %s""" % (price, int(number)))
        if remontnik != '':
            c.execute("""UPDATE Накладная SET Ремонтник = '%s' WHERE id_Накладная = %s""" % (int(remontnik), int(number)))
        conn.commit()
        c.close()
        conn.close()