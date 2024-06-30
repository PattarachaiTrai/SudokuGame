import unittest
from sudoku import Sudoku

class Sudoku_Test(unittest.TestCase):

    def test_sudoku_1(self):
        sudo = Sudoku([[0 for col in range(9)] for row in range(9)]) #set0ทั้งตารางไม่มีช่องว่าง
        res = sudo.get_value(5, 1) #เอาrow5col1
        res = sudo.solve()
        self.assertTrue(res)

    def test_sudoku_2(self):
        sudo = Sudoku([[0 for col in range(9)] for row in range(9)]) #set0ทั้งตารางไม่มีช่องว่าง
        res = sudo.get_value(6, 2) #เอาrow6col2
        res = sudo.solve()
        self.assertTrue(res)
    
    def test_sudoku_3(self):
        sudo = Sudoku([[0 for col in range(9)] for row in range(9)]) #set0ทั้งตารางไม่มีช่องว่าง
        res = sudo.get_value(3, 3) #เอาrow3col3
        res = sudo.solve()
        self.assertTrue(res)

    def test_sudoku_4(self):
        sudo = Sudoku([[0 for col in range(9)] for row in range(9)]) #set0ทั้งตารางไม่มีช่องว่าง
        res = sudo.get_value(8, 2) #เอาrow8col2
        res = sudo.solve()
        self.assertTrue(res)

    def test_sudoku_5(self):
        sudo = Sudoku([[0 for col in range(9)] for row in range(9)]) #set0ทั้งตารางไม่มีช่องว่าง
        res = sudo.get_value(7, 4) #เอาrow7col4
        res = sudo.solve()
        self.assertTrue(res)

    def test_sudoku_6(self):
        sudo = Sudoku([[0 for col in range(9)] for row in range(9)]) #set0ทั้งตารางไม่มีช่องว่าง
        res = sudo.get_value(5, 5) #เอาrow5col5
        res = sudo.solve()
        self.assertTrue(res)

    def test_sudoku_7(self):
        sudo = Sudoku([[0 for col in range(9)] for row in range(9)]) #set0ทั้งตารางไม่มีช่องว่าง
        res = sudo.get_value(1, 1) #เอาrow1col1
        res = sudo.solve()
        self.assertTrue(res)

    def test_sudoku_8(self):
        sudo = Sudoku([[0 for col in range(9)] for row in range(9)]) #set0ทั้งตารางไม่มีช่องว่าง
        res = sudo.get_value(8, 8) #เอาrow8col8
        res = sudo.solve()
        self.assertTrue(res)
    
    def test_sudoku_9(self):
        sudo = Sudoku([[0 for col in range(9)] for row in range(9)]) #set0ทั้งตารางไม่มีช่องว่าง
        res = sudo.get_value(3, 1) #เอาrow3col1
        res = sudo.solve()
        self.assertTrue(res)

    def test_sudoku_10(self):
        sudo = Sudoku([[0 for col in range(9)] for row in range(9)]) #set0ทั้งตารางไม่มีช่องว่าง
        res = sudo.get_value(1, 7) #เอาrow1col7
        res = sudo.solve()
        self.assertTrue(res)