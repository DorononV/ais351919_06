import mysql.connector
from kompl_and_st import Kompl_n_st
import unittest

class TestKompl_n_st(unittest.TestCase):
    def check_count(self):
        conn = mysql.connector.connect(user='root', password='Qwerty1bNb', host='127.0.0.1', database='db1')
        c = conn.cursor()
        c.execute('select count(*) from Комплектующие_и_Станок;')
        res = c.fetchone()
        c.close()
        conn.close()
        return res[0]

    def test_a_get_kompl_n_st(self):
        self.assertEqual(4, len(Kompl_n_st.get_kompl_n_st()))

    def test_b_add_kompl_n_st(self):
        c = self.check_count()
        Kompl_n_st.add_kompl_n_st(1, 5)
        Kompl_n_st.add_kompl_n_st(2, 5)
        Kompl_n_st.add_kompl_n_st(5, 5)
        self.assertGreater(self.check_count(), c)

    def test_d_delete_kompl_n_st(self):
        c = self.check_count()
        Kompl_n_st.delete_kompl_n_st(1, 5)
        Kompl_n_st.delete_kompl_n_st(2, 5)
        Kompl_n_st.delete_kompl_n_st(5, 5)
        self.assertGreater(c, self.check_count())

if __name__ == '__main__':
    unittest.main()