import mysql.connector
from user import Users
import unittest
import datetime

class TestUsers(unittest.TestCase):
    def check_count(self):
        conn = mysql.connector.connect(user='root', password='Qwerty1bNb', host='127.0.0.1', database='db1')
        c = conn.cursor()
        c.execute('select count(*) from Пользователи;')
        res = c.fetchone()
        c.close()
        conn.close()
        return res[0]

    def take_user_data(self):
        conn = mysql.connector.connect(user='root', password='Qwerty1bNb', host='127.0.0.1', database='db1')
        c = conn.cursor()
        c.execute('SELECT * FROM Пользователи WHERE id_Пользователя=5')
        row = c.fetchall()
        c.close()
        conn.close()
        return row

    def test_a_get_users(self):
        self.assertEqual(8, len(Users.get_users()))

    def test_b_add_user(self):
        c = self.check_count()
        Users.add_user(5, 'Ульрих', 'Иванович', 'Ципляев', '2020-02-02')
        self.assertGreater(self.check_count(), c)

    def test_c_update_user(self):
        Users.update_user(5, birthday="1987-03-03")
        n = self.take_user_data()
        self.assertEqual(n[0][4], datetime.date(1987, 3, 3))
        Users.update_user(5, firstname="Игнат")
        n = self.take_user_data()
        self.assertEqual(n[0][1], "Игнат")
        Users.update_user(5, lastname="Петров")
        n = self.take_user_data()
        self.assertEqual(n[0][2], "Петров")
        Users.update_user(5, midname="Валентинович")
        n = self.take_user_data()
        self.assertEqual(n[0][3], "Валентинович")

    def test_d_delete_user(self):
        c = self.check_count()
        Users.delete_user(5)
        self.assertGreater(c, self.check_count())

if __name__ == '__main__':
    unittest.main()