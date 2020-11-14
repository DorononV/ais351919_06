import mysql.connector
from datetime import date

class Users:

    def __init__(self, number=0, firstname=None, lastname=None, midname=None, birthday=None):
        self.number = number
        self.firstname = firstname
        self.lastname = lastname
        self.midname = midname
        self.birthday = birthday

    #@property
    #def info(self):
        #return f'{self.number} | {self.firstname} | {self.midname} | {self.lastname} | {self.birthday}'

    @staticmethod
    def get_users():
        conn = mysql.connector.connect(user='root', password='Qwerty1bNb', host='127.0.0.1', database='db1')
        c = conn.cursor()
        result = []
        c.execute('SELECT * FROM Пользователи')
        rows = c.fetchall()
        for row in rows:
            user = Users(row[0], row[1], row[3], row[2], row[4])
            result.append(user)
        c.close()
        conn.close()
        return result

    @staticmethod
    def add_user(number, firstname, lastname, midname, birthday):
        conn = mysql.connector.connect(user='root', password='Qwerty1bNb', host='127.0.0.1', database='db1')
        c = conn.cursor()
        c.execute('insert into Пользователи values(%s, %s, %s, %s, %s)', \
                  (int(number), firstname, lastname, midname, date.fromisoformat(birthday),))
        conn.commit()
        c.close()
        conn.close()

    @staticmethod
    def delete_user(uid):
        conn = mysql.connector.connect(user='root', password='Qwerty1bNb', host='127.0.0.1', database='db1')
        c = conn.cursor()
        c.execute("DELETE FROM Пользователи WHERE id_Пользователя = %i" % (uid))
        conn.commit()
        c.close()
        conn.close()

    @staticmethod
    def update_user(number, firstname='', lastname='', midname='', birthday=''):
        conn = mysql.connector.connect(user='root', password='Qwerty1bNb', host='127.0.0.1', database='db1')
        c = conn.cursor()
        if firstname != '':
            c.execute("""UPDATE Пользователи SET Имя = '%s' WHERE id_Пользователя = %s""" % (firstname, int(number)))
        if lastname != '':
            c.execute("""UPDATE Пользователи SET Фамилия = '%s' WHERE id_Пользователя = %s""" % (lastname, int(number)))
        if midname != '':
            c.execute("""UPDATE Пользователи SET Очество = '%s' WHERE id_Пользователя = %s""" % (midname, int(number)))
        if birthday != '':
            c.execute("""UPDATE Пользователи SET Дата_рождения = '%s' WHERE id_Пользователя = %s""" % (date.fromisoformat(birthday), int(number)))
        conn.commit()
        c.close()
        conn.close()