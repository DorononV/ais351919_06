import mysql.connector
from Nakladnaya import Bill
import unittest
import datetime

class TestSklad(unittest.TestCase):
    def check_count(self):
        conn = mysql.connector.connect(user='root', password='Qwerty1bNb', host='127.0.0.1', database='db1')
        c = conn.cursor()
        c.execute('select count(*) from Накладная;')
        res = c.fetchone()
        c.close()
        conn.close()
        return res[0]

    def take_data(self):
        conn = mysql.connector.connect(user='root', password='Qwerty1bNb', host='127.0.0.1', database='db1')
        c = conn.cursor()
        c.execute('SELECT * FROM Накладная WHERE id_Накладная=1')
        row = c.fetchall()
        c.close()
        conn.close()
        return row

    def test_a_get_bill(self):
        self.assertEqual(3, len(Bill.get_bill()))

    def test_b_add_bill(self):
        c = self.check_count()
        Bill.add_bill(1, 2, 9, "2019-08-05", 1999, 2)
        self.assertGreater(self.check_count(), c)

    def test_c_update_bill(self):
        Bill.update_bill(1, sklad=1)
        n = self.take_data()
        self.assertEqual(n[0][1], 1)

        Bill.update_bill(1, detail=8)
        n = self.take_data()
        self.assertEqual(n[0][2], 8)

        Bill.update_bill(1, date_poluch="2018-06-06")
        n = self.take_data()
        self.assertEqual(n[0][3], datetime.date(2018, 6, 6))

        Bill.update_bill(1, price=17000)
        n = self.take_data()
        self.assertEqual(n[0][4], 17000)

        Bill.update_bill(1, remontnik=1)
        n = self.take_data()
        self.assertEqual(n[0][5], 1)

    def test_d_delete_bill(self):
        c = self.check_count()
        Bill.delete_bill(1)
        self.assertGreater(c, self.check_count())

if __name__ == '__main__':
    unittest.main()