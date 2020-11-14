import mysql.connector
from datetime import date

class Sklad_and_kompl:

    def __init__(self, number=0, kompl=None):
        self.number = number
        self.kompl = kompl

    @staticmethod
    def get_sklad_and_kompl():
        conn = mysql.connector.connect(user='root', password='Qwerty1bNb', host='127.0.0.1', database='db1')
        c = conn.cursor()
        kompl = []
        c.execute('SELECT * FROM Комплектующие_и_Склад')
        rows = c.fetchall()
        for row in rows:
            sklad2 = Sklad_and_kompl(row[1], row[0])
            kompl.append(sklad2)
        c.close()
        conn.close()
        return kompl

    @staticmethod
    def add_sklad_and_kompl(number2, kompl):
        conn = mysql.connector.connect(user='root', password='Qwerty1bNb', host='127.0.0.1', database='db1')
        c = conn.cursor()
        c.execute('insert into Комплектующие_и_Склад values(%s, %s)', \
                  (int(number2), int(kompl)))
        conn.commit()
        c.close()
        conn.close()

    @staticmethod
    def delete_sklad_and_kompl(uid, uid2):
        conn = mysql.connector.connect(user='root', password='Qwerty1bNb', host='127.0.0.1', database='db1')
        c = conn.cursor()
        c.execute("DELETE FROM Комплектующие_и_Склад WHERE id_Склад = %i AND id_Комплектующие = %i" % (uid2, uid))
        conn.commit()
        c.close()
        conn.close()
