import mysql.connector
from expl import Expl
import unittest
import datetime

class TestExpl(unittest.TestCase):
    def check_count(self):
        conn = mysql.connector.connect(user='root', password='Qwerty1bNb', host='127.0.0.1', database='db1')
        c = conn.cursor()
        c.execute('select count(*) from Эксплуатация;')
        res = c.fetchone()
        c.close()
        conn.close()
        return res[0]

    def take_data(self):
        conn = mysql.connector.connect(user='root', password='Qwerty1bNb', host='127.0.0.1', database='db1')
        c = conn.cursor()
        c.execute('SELECT * FROM Эксплуатация WHERE id_Эксплуатация=7')
        row = c.fetchall()
        c.close()
        conn.close()
        return row

    def test_a_get_expl(self):
        self.assertEqual(6, len(Expl.get_users()))

    def test_b_add_expl(self):
        c = self.check_count()
        Expl.add_user(7, '2010-02-02', '10', '2020-02-02')
        self.assertGreater(self.check_count(), c)

    def test_c_update_expl(self):
        Expl.update_user(7, date_start="2000-03-03")
        n = self.take_data()
        self.assertEqual(n[0][1], datetime.date(2000, 3, 3))

        Expl.update_user(7, expl_srok=20)
        n = self.take_data()
        self.assertEqual(n[0][2], 20)

        Expl.update_user(7, date_spis="2020-03-03")
        n = self.take_data()
        self.assertEqual(n[0][3], datetime.date(2020, 3, 3))

    def test_d_delete_expl(self):
        c = self.check_count()
        Expl.delete_user(7)
        self.assertGreater(c, self.check_count())

if __name__ == '__main__':
    unittest.main()