import mysql.connector
from datetime import date

class Kompl_n_st:

    def __init__(self, number=0, kompl=None):
        self.number = number
        self.kompl = kompl

    @staticmethod
    def get_kompl_n_st():
        conn = mysql.connector.connect(user='root', password='Qwerty1bNb', host='127.0.0.1', database='db1')
        c = conn.cursor()
        kompl = []
        c.execute('SELECT * FROM Комплектующие_и_Станок')
        rows = c.fetchall()
        for row in rows:
            sklad2 = Kompl_n_st(row[1], row[0])
            kompl.append(sklad2)
        c.close()
        conn.close()
        return kompl

    @staticmethod
    def add_kompl_n_st(number, kompl):
        conn = mysql.connector.connect(user='root', password='Qwerty1bNb', host='127.0.0.1', database='db1')
        c = conn.cursor()
        c.execute('insert into Комплектующие_и_Станок values(%s, %s)', \
                  (int(number), int(kompl)))
        conn.commit()
        c.close()
        conn.close()

    @staticmethod
    def delete_kompl_n_st(uid, uid2):
        conn = mysql.connector.connect(user='root', password='Qwerty1bNb', host='127.0.0.1', database='db1')
        c = conn.cursor()
        c.execute("DELETE FROM Комплектующие_и_Станок WHERE id_Станок = %i AND id_Комплектующие = %i" % (uid2, uid))
        conn.commit()
        c.close()
        conn.close()
