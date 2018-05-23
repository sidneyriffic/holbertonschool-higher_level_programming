#!/usr/bin/python3
"""Unittest module for Base, Square and Rectangle classes"""
import unittest
from models.base import Base
from models.rectangle import Rectangle
from models.square import Square


idct = 0
notintegers = [3.5, [], {}, {1, 2}, {1: 2, 3: 4}, "hi", b"hi", ()]

class TestBase(unittest.TestCase):
    """Test cases for Base geometry class"""

    def testdefault(self):
        global idct
        a = Base()
        idct += 1
        self.assertEqual(a.id, idct)

    def testincrement(self):
        global idct
        a = Base()
        idct += 1
        self.assertEqual(a.id, idct)
        b = Base()
        idct += 1
        self.assertEqual(b.id, idct)
        c = Base()
        idct += 1
        self.assertEqual(c.id, idct)
        d = Base()
        idct += 1
        self.assertEqual(d.id, idct)

    def testspecific(self):
        global idct
        a = Base(19)
        self.assertEqual(a.id, 19)

    def testspecincrement(self):
        """Tests that setting a specific id does not mess up incrementer"""
        global idct
        a = Base()
        idct += 1
        self.assertEqual(a.id, idct)
        b = Base(19)
        self.assertEqual(b.id, 19)
        c = Base()
        idct += 1
        self.assertEqual(c.id, idct)
        d = Base()
        idct += 1
        self.assertEqual(d.id, idct)

    def testnonnum(self):
        """Tries some non-numbers to make sure it assigns that as id"""
        global idct
        astr = "hello"
        a = Base(astr)
        blist = [10, 14, 30]
        b = Base(blist)
        self.assertEqual(a.id, astr)
        self.assertEqual(b.id, blist)

#test fewer args to inits
class TestRectangle(unittest.TestCase):
    """Tests the rectangle class"""

    def testbasicrect(self):
        """Makes a basic rectangle with only valid width/height"""
        global idct
        a = Rectangle(10, 5)
        idct += 1
        self.assertEqual(a.id, idct)
        self.assertEqual(a.width, 10)
        self.assertEqual(a.height, 5)

    def testnegwidth(self):
        """Tries a negative width"""
        with self.assertRaises(ValueError) as e:
            a = Rectangle(-10, 5)
        self.assertEqual(e.exception.args[0], "width must be > 0")

    def testzerowidth(self):
        """Tries a zero width"""
        with self.assertRaises(ValueError) as e:
            a = Rectangle(0, 5)
        self.assertEqual(e.exception.args[0], "width must be > 0")

    def testnegheight(self):
        """Tries a negative height"""
        with self.assertRaises(ValueError) as e:
            a = Rectangle(10, -5)
        self.assertEqual(e.exception.args[0], "height must be > 0")

    def testzeroheight(self):
        """Tries a zero height"""
        with self.assertRaises(ValueError) as e:
            a = Rectangle(10, 0)
        self.assertEqual(e.exception.args[0], "height must be > 0")

    def testrectwithx(self):
        """Make a rectangle with only an x position"""
        global idct
        a = Rectangle(10, 5, 3)
        idct += 1
        self.assertEqual(a.id, idct)
        self.assertEqual(a.width, 10)
        self.assertEqual(a.height, 5)
        self.assertEqual(a.x, 3)

    def testrectwithy(self):
        """Make a rectangle with x and y position"""
        global idct
        a = Rectangle(10, 5, 3, 2)
        idct += 1
        self.assertEqual(a.id, idct)
        self.assertEqual(a.width, 10)
        self.assertEqual(a.height, 5)
        self.assertEqual(a.x, 3)
        self.assertEqual(a.y, 2)

    def testnegx(self):
        """Tries a negative x"""
        with self.assertRaises(ValueError) as e:
            a = Rectangle(10, 5, -1)
        self.assertEqual(e.exception.args[0], "x must be >= 0")

    def testnegy(self):
        """Tries a negative y"""
        with self.assertRaises(ValueError) as e:
            a = Rectangle(10, 5, 1, -1)
        self.assertEqual(e.exception.args[0], "y must be >= 0")

    def testid(self):
        """Test rectangle construction given an id"""
        a = Rectangle(1, 2, 3, 4, 5)
        self.assertEqual(a.id, 5)
        self.assertEqual(a.width, 1)
        self.assertEqual(a.height, 2)
        self.assertEqual(a.x, 3)
        self.assertEqual(a.y, 4)

    def testwidthtype(self):
        """Test invalid types for width"""
        for ele in notintegers:
            with self.subTest(type=type(ele)):
                with self.assertRaises(TypeError) as e:
                    Rectangle(ele, 4)
                self.assertEqual(e.exception.args[0],
                                  "width must be an integer")

    def testheighttype(self):
        """Test invalid types for height"""
        for ele in notintegers:
            with self.subTest(type=type(ele)):
                with self.assertRaises(TypeError) as e:
                    Rectangle(4, ele)
                self.assertEqual(e.exception.args[0],
                                  "height must be an integer")

    def testxtype(self):
        """Test invalid types for x"""
        for ele in notintegers:
            with self.subTest(type=type(ele)):
                with self.assertRaises(TypeError) as e:
                    Rectangle(4, 5, ele)
                self.assertEqual(e.exception.args[0],
                                  "x must be an integer")

    def testytype(self):
        """Test invalid types for y"""
        for ele in notintegers:
            with self.subTest(type=type(ele)):
                with self.assertRaises(TypeError) as e:
                    Rectangle(4, 5, 6, ele)
                self.assertEqual(e.exception.args[0],
                                  "y must be an integer")

    def testarea(self):
        """Tests rectangle area function"""
        global idct
        a = Rectangle(3, 4)
        idct += 1
        self.assertEqual(a.area(), 12)

    def testarea2(self):
        """tests rectangle area function"""
        a = Rectangle(4, 5, 100, 20, 10)
        self.assertEqual(a.area(), 20)

#test fewer args to inits
class TestSquare(unittest.TestCase):
    """Tests the square class"""

    def testbasicrect(self):
        """Makes a basic square with only valid width/height"""
        global idct
        a = Square(10)
        idct += 1
        self.assertEqual(a.id, idct)
        self.assertEqual(a.width, 10)
        self.assertEqual(a.height, 10)

    def testnegsize(self):
        """Tries a negative size"""
        with self.assertRaises(ValueError) as e:
            a = Square(-10)
        self.assertEqual(e.exception.args[0], "width must be > 0")

    def testzerosize(self):
        """Tries a zero width"""
        with self.assertRaises(ValueError) as e:
            a = Square(0)
        self.assertEqual(e.exception.args[0], "width must be > 0")

    def testsqwithx(self):
        """Make a square with only an x position"""
        global idct
        a = Square(10, 5)
        idct += 1
        self.assertEqual(a.id, idct)
        self.assertEqual(a.width, 10)
        self.assertEqual(a.height, 10)
        self.assertEqual(a.x, 5)

    def testsqwithy(self):
        """Make a square with x and y position"""
        global idct
        a = Square(10, 5, 3)
        idct += 1
        self.assertEqual(a.id, idct)
        self.assertEqual(a.width, 10)
        self.assertEqual(a.height, 10)
        self.assertEqual(a.x, 5)
        self.assertEqual(a.y, 3)

    def testnegx(self):
        """Tries a negative x"""
        with self.assertRaises(ValueError) as e:
            a = Square(10, -1)
        self.assertEqual(e.exception.args[0], "x must be >= 0")

    def testnegy(self):
        """Tries a negative y"""
        with self.assertRaises(ValueError) as e:
            a = Square(10, 1, -1)
        self.assertEqual(e.exception.args[0], "y must be >= 0")

    def testid(self):
        """Test square construction given an id"""
        a = Square(1, 2, 3, 4)
        self.assertEqual(a.id, 4)
        self.assertEqual(a.width, 1)
        self.assertEqual(a.height, 1)
        self.assertEqual(a.x, 2)
        self.assertEqual(a.y, 3)

    def testwidthtype(self):
        """Test invalid types for size"""
        for ele in notintegers:
            with self.subTest(type=type(ele)):
                with self.assertRaises(TypeError) as e:
                    Square(ele)
                self.assertEqual(e.exception.args[0],
                                  "width must be an integer")

    def testxtype(self):
        """Test invalid types for x"""
        for ele in notintegers:
            with self.subTest(type=type(ele)):
                with self.assertRaises(TypeError) as e:
                    Square(4, ele)
                self.assertEqual(e.exception.args[0],
                                  "x must be an integer")

    def testytype(self):
        """Test invalid types for y"""
        for ele in notintegers:
            with self.subTest(type=type(ele)):
                with self.assertRaises(TypeError) as e:
                    Square(4, 5, ele)
                self.assertEqual(e.exception.args[0],
                                  "y must be an integer")

    def testarea(self):
        """Tests rectangle area function"""
        global idct
        a = Square(4)
        idct += 1
        self.assertEqual(a.area(), 16)

    def testarea2(self):
        """tests rectangle area function"""
        a = Square(4, 100, 20, 10)
        self.assertEqual(a.area(), 16)
