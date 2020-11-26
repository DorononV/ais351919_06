import mysql.connector
from kompl import Kompl
import unittest

class TestKompl(unittest.TestCase):
    def check_count(self):
        conn = mysql.connector.connect(user='root', password='Qwerty1bNb', host='127.0.0.1', database='db1')
        c = conn.cursor()
        c.execute('select count(*) from Комплектующие;')
        res = c.fetchone()
        c.close()
        conn.close()
        return res[0]

    def take_data(self):
        conn = mysql.connector.connect(user='root', password='Qwerty1bNb', host='127.0.0.1', database='db1')
        c = conn.cursor()
        c.execute('SELECT * FROM Комплектующие WHERE id_Комплектующие=11')
        row = c.fetchall()
        c.close()
        conn.close()
        return row

    def test_a_get_kompl(self):
        self.assertEqual(10, len(Kompl.get_kompl()))

    def test_b_add_kompl(self):
        c = self.check_count()
        Kompl.add_kompl(11, 'шуруп-T5')
        self.assertGreater(self.check_count(), c)

    def test_c_update_kompl(self):
        Kompl.update_kompl(11, detalname="гайка-T5")
        n = self.take_data()
        self.assertEqual(n[0][1], "гайка-T5")

    def test_d_delete_kompl(self):
        c = self.check_count()
        Kompl.delete_kompl(11)
        self.assertGreater(c, self.check_count())

if __name__ == '__main__':
    unittest.main()