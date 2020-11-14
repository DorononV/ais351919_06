import mysql.connector
from datetime import date

class Expl:

    def __init__(self, number=0, date_start=None, expl_srok=None, date_spis=None):
        self.number = number
        self.date_start = date_start
        self.expl_srok = expl_srok
        self.date_spis = date_spis

    @staticmethod
    def get_users():
        conn = mysql.connector.connect(user='root', password='Qwerty1bNb', host='127.0.0.1', database='db1')
        c = conn.cursor()
        result = []
        c.execute('SELECT * FROM Эксплуатация')
        rows = c.fetchall()
        for row in rows:
            expl = Expl(row[0], row[1], row[2], row[3])
            result.append(expl)
        c.close()
        conn.close()
        return result

    @staticmethod
    def add_user(number, date_start, expl_srok, date_spis):
        conn = mysql.connector.connect(user='root', password='Qwerty1bNb', host='127.0.0.1', database='db1')
        c = conn.cursor()
        c.execute('insert into Эксплуатация values(%s, %s, %s, %s)', \
                  (int(number), date.fromisoformat(date_start), int(expl_srok), date.fromisoformat(date_spis),))
        conn.commit()
        c.close()
        conn.close()

    @staticmethod
    def delete_user(uid):
        conn = mysql.connector.connect(user='root', password='Qwerty1bNb', host='127.0.0.1', database='db1')
        c = conn.cursor()
        c.execute("DELETE FROM Эксплуатация WHERE id_Эксплуатация = %i" % (uid))
        conn.commit()
        c.close()
        conn.close()

    @staticmethod
    def update_user(number, date_start='', expl_srok='', date_spis=''):
        conn = mysql.connector.connect(user='root', password='Qwerty1bNb', host='127.0.0.1', database='db1')
        c = conn.cursor()
        if date_start != '':
            c.execute("""UPDATE Эксплуатация SET Дата_начала_работы_станка = '%s' WHERE id_Эксплуатация = %s""" % (date.fromisoformat(date_start), int(number)))
        if expl_srok != '':
            c.execute("""UPDATE Эксплуатация SET Эксплуатационный_срок = '%s' WHERE id_Эксплуатация = %s""" % (int(expl_srok), int(number)))
        if date_spis != '':
            c.execute("""UPDATE Эксплуатация SET Дата_списания_станка = '%s' WHERE id_Эксплуатация = %s""" % (date.fromisoformat(date_spis), int(number)))
        conn.commit()
        c.close()
        conn.close()