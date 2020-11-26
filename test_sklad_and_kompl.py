import mysql.connector
from sklad_and_kompl import Sklad_and_kompl
import unittest

class TestKompl_n_st(unittest.TestCase):
    def check_count(self):
        conn = mysql.connector.connect(user='root', password='Qwerty1bNb', host='127.0.0.1', database='db1')
        c = conn.cursor()
        c.execute('select count(*) from Комплектующие_и_Склад;')
        res = c.fetchone()
        c.close()
        conn.close()
        return res[0]

    def test_a_get_kompl_n_st(self):
        self.assertEqual(9, len(Sklad_and_kompl.get_sklad_and_kompl()))

    def test_b_add_kompl_n_st(self):
        c = self.check_count()
        Sklad_and_kompl.add_sklad_and_kompl(10, 3)
        Sklad_and_kompl.add_sklad_and_kompl(9, 1)
        Sklad_and_kompl.add_sklad_and_kompl(9, 2)
        Sklad_and_kompl.add_sklad_and_kompl(9, 3)
        self.assertGreater(self.check_count(), c)

    def test_d_delete_kompl_n_st(self):
        c = self.check_count()
        Sklad_and_kompl.delete_sklad_and_kompl(10, 3)
        Sklad_and_kompl.delete_sklad_and_kompl(9, 1)
        Sklad_and_kompl.delete_sklad_and_kompl(9, 2)
        Sklad_and_kompl.delete_sklad_and_kompl(9, 3)
        self.assertGreater(c, self.check_count())

if __name__ == '__main__':
    unittest.main()