import mysql.connector
from datetime import date

class Kompl:

    def __init__(self, number=0, detalname=None):
        self.number = number
        self.detalname = detalname

    @staticmethod
    def get_kompl():
        conn = mysql.connector.connect(user='root', password='Qwerty1bNb', host='127.0.0.1', database='db1')
        c = conn.cursor()
        result = []
        c.execute('SELECT * FROM Комплектующие')
        rows = c.fetchall()
        for row in rows:
            kompl = Kompl(row[0], row[1])
            result.append(kompl)
        c.close()
        conn.close()
        return result

    @staticmethod
    def add_kompl(number, detalname):
        conn = mysql.connector.connect(user='root', password='Qwerty1bNb', host='127.0.0.1', database='db1')
        c = conn.cursor()
        c.execute('insert into Комплектующие values(%s, %s)', \
                  (int(number), detalname,))
        conn.commit()
        c.close()
        conn.close()

    @staticmethod
    def delete_kompl(uid):
        conn = mysql.connector.connect(user='root', password='Qwerty1bNb', host='127.0.0.1', database='db1')
        c = conn.cursor()
        c.execute("DELETE FROM Комплектующие WHERE id_Комплектующие = %i" % (uid))
        conn.commit()
        c.close()
        conn.close()

    @staticmethod
    def update_kompl(number, detalname=''):
        conn = mysql.connector.connect(user='root', password='Qwerty1bNb', host='127.0.0.1', database='db1')
        c = conn.cursor()
        if detalname != '':
            c.execute("""UPDATE Комплектующие SET Название_детали = '%s' WHERE id_Комплектующие = %s""" % (detalname, int(number)))
        conn.commit()
        c.close()
        conn.close()