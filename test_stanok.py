import mysql.connector
from Stanok import Stanok
import unittest
import datetime

class TestExpl(unittest.TestCase):
    def check_count(self):
        conn = mysql.connector.connect(user='root', password='Qwerty1bNb', host='127.0.0.1', database='db1')
        c = conn.cursor()
        c.execute('select count(*) from Станок;')
        res = c.fetchone()
        c.close()
        conn.close()
        return res[0]

    def take_data(self):
        conn = mysql.connector.connect(user='root', password='Qwerty1bNb', host='127.0.0.1', database='db1')
        c = conn.cursor()
        c.execute('SELECT * FROM Станок WHERE ID_Станок=6')
        row = c.fetchall()
        c.close()
        conn.close()
        return row

    def test_a_get_stanok(self):
        self.assertEqual(4, len(Stanok.get_stanok()))

    def test_b_add_stanok(self):
        c = self.check_count()
        Stanok.add_stanok(6, 'AAA-4', 'фрезерный', 1, 6)
        self.assertGreater(self.check_count(), c)

    def test_c_update_stanok(self):
        Stanok.update_stanok(6, model_st="NEWAAA-8")
        n = self.take_data()
        self.assertEqual(n[0][1], "NEWAAA-8")

        Stanok.update_stanok(6, type_st="столярный")
        n = self.take_data()
        self.assertEqual(n[0][2], "столярный")

        Stanok.update_stanok(6, user=2)
        n = self.take_data()
        self.assertEqual(n[0][3], 2)

        Stanok.update_stanok(6, expl=3)
        n = self.take_data()
        self.assertEqual(n[0][4], 3)

    def test_d_delete_stanok(self):
        c = self.check_count()
        Stanok.delete_stanok(6)
        self.assertGreater(c, self.check_count())

if __name__ == '__main__':
    unittest.main()