import mysql.connector
from datetime import date

class Sklad:

    def __init__(self, number=0, ylica=None, num_home=None, ploshad=None):
        self.number = number
        self.ylica = ylica
        self.num_home = num_home
        self.ploshad = ploshad

    @staticmethod
    def get_sklad():
        conn = mysql.connector.connect(user='root', password='Qwerty1bNb', host='127.0.0.1', database='db1')
        c = conn.cursor()
        result = []
        c.execute('SELECT * FROM Cклад')
        rows = c.fetchall()
        for row in rows:
            sklad = Sklad(row[0], row[1], row[2], row[3])
            result.append(sklad)
        c.close()
        conn.close()
        return result

    @staticmethod
    def add_sklad(number, ylica='', num_home='', ploshad=''):
        conn = mysql.connector.connect(user='root', password='Qwerty1bNb', host='127.0.0.1', database='db1')
        c = conn.cursor()
        c.execute('insert into Cклад values(%s, %s, %s, %s)', \
                (int(number), ylica, int(num_home), int(ploshad)))
        conn.commit()
        c.close()
        conn.close()

    @staticmethod
    def delete_sklad(uid):
        conn = mysql.connector.connect(user='root', password='Qwerty1bNb', host='127.0.0.1', database='db1')
        c = conn.cursor()
        c.execute("DELETE FROM Cклад WHERE id_Склад = %i" % (uid))
        conn.commit()
        c.close()
        conn.close()

    @staticmethod
    def update_sklad(number, ylica='', num_home='', ploshad=''):
        conn = mysql.connector.connect(user='root', password='Qwerty1bNb', host='127.0.0.1', database='db1')
        c = conn.cursor()
        if ylica != '':
            c.execute("""UPDATE Cклад SET Адрес_склада_улица = '%s' WHERE id_Склад = %s""" % (ylica, int(number)))
        if num_home != '':
            c.execute("""UPDATE Cклад SET Адрес_склада_номер_дома = '%s' WHERE id_Склад = %s""" % (int(num_home), int(number)))
        if ploshad != '':
            c.execute("""UPDATE Cклад SET Количество_метров_занимаемой_площади = '%s' WHERE id_Склад = %s""" % (int(ploshad), int(number)))
        conn.commit()
        c.close()
        conn.close()