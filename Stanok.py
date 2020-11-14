import mysql.connector
from datetime import date

class Stanok:

    def __init__(self, number=0, model_st=None, type_st=None, user=None, expl=None):
        self.number = number
        self.model_st = model_st
        self.type_st = type_st
        self.user = user
        self.expl = expl

    @staticmethod
    def get_stanok():
        conn = mysql.connector.connect(user='root', password='Qwerty1bNb', host='127.0.0.1', database='db1')
        c = conn.cursor()
        result = []
        c.execute('SELECT * FROM Станок')
        rows = c.fetchall()
        for row in rows:
            stanok = Stanok(row[0], row[1], row[2], row[3], row[4])
            result.append(stanok)
        c.close()
        conn.close()
        return result

    @staticmethod
    def add_stanok(number, model_st, type_st, user, expl):
        conn = mysql.connector.connect(user='root', password='Qwerty1bNb', host='127.0.0.1', database='db1')
        c = conn.cursor()
        c.execute('insert into Станок values(%s, %s, %s, %s, %s)', \
                  (int(number), model_st, type_st, int(user), int(expl)))
        conn.commit()
        c.close()
        conn.close()

    @staticmethod
    def delete_stanok(uid):
        conn = mysql.connector.connect(user='root', password='Qwerty1bNb', host='127.0.0.1', database='db1')
        c = conn.cursor()
        c.execute("DELETE FROM Станок WHERE id_Станок = %i" % (uid))
        conn.commit()
        c.close()
        conn.close()

    @staticmethod
    def update_stanok(number, model_st='', type_st='', user='', expl=''):
        conn = mysql.connector.connect(user='root', password='Qwerty1bNb', host='127.0.0.1', database='db1')
        c = conn.cursor()
        if model_st != '':
            c.execute("""UPDATE Станок SET Модель_станка = '%s' WHERE id_Станок = %s""" % (model_st, int(number)))
        if type_st != '':
            c.execute("""UPDATE Станок SET Тип_станка = '%s' WHERE id_Станок = %s""" % (type_st, int(number)))
        if user != '':
            c.execute("""UPDATE Станок SET Пользователь = '%s' WHERE id_Станок = %s""" % (int(user), int(number)))
        if expl != '':
            c.execute("""UPDATE Станок SET Эксплуатация = '%s' WHERE id_Станок = %s""" % (int(expl), int(number)))
        conn.commit()
        c.close()
        conn.close()