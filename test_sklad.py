import mysql.connector
from sklad import Sklad
import unittest

class TestSklad(unittest.TestCase):
    def check_count(self):
        conn = mysql.connector.connect(user='root', password='Qwerty1bNb', host='127.0.0.1', database='db1')
        c = conn.cursor()
        c.execute('select count(*) from Cклад;')
        res = c.fetchone()
        c.close()
        conn.close()
        return res[0]

    def take_data(self):
        conn = mysql.connector.connect(user='root', password='Qwerty1bNb', host='127.0.0.1', database='db1')
        c = conn.cursor()
        c.execute('SELECT * FROM Cклад WHERE id_Склад=4')
        row = c.fetchall()
        c.close()
        conn.close()
        return row

    def test_a_get_sklad(self):
        self.assertEqual(3, len(Sklad.get_sklad()))

    def test_b_add_sklad(self):
        c = self.check_count()
        Sklad.add_sklad(4, 'Иваньковская', 6, 17000)
        self.assertGreater(self.check_count(), c)

    def test_c_update_sklad(self):
        Sklad.update_sklad(4, ylica="Ренатовская")
        n = self.take_data()
        self.assertEqual(n[0][1], "Ренатовская")

        Sklad.update_sklad(4, num_home=4)
        n = self.take_data()
        self.assertEqual(n[0][2], 4)

        Sklad.update_sklad(4, ploshad=20000)
        n = self.take_data()
        self.assertEqual(n[0][3], 20000)

    def test_d_delete_sklad(self):
        c = self.check_count()
        Sklad.delete_sklad(4)
        self.assertGreater(c, self.check_count())

if __name__ == '__main__':
    unittest.main()