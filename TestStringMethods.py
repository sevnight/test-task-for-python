import unittest
from os import remove
import test # файл test.py содержащий все разработанные функции (добавлен в гитигнор, ибо они отображены в jupyter notebook)

class TestStringMethods(unittest.TestCase):

    def test_func_1(self):
        name_test_file = 'test1.json'
        my_file = open(name_test_file, 'w')
        my_file.write('[{"title": "Title#1", "body": "Hello,World1!" },{ "title": "Title#2","body": "Hello,World2!"}]')
        my_file.close()
        self.assertEqual(test.func_1(name_test_file), '<h1>Title#1</h1><p>Hello,World1!</p><h1>Title#2</h1><p>Hello,World2!</p>')
        remove(name_test_file)

    def test_func_2(self):
        name_test_file = 'test2.json'
        my_file = open(name_test_file, 'w')
        my_file.write('[ { "h3": "Title#1", "div": "Hello,World1!" }]')
        my_file.close()
        self.assertEqual(test.func_2(name_test_file), '<h3>Title#1</h3><div>Hello,World1!</div>')
        remove(name_test_file)
   
    def test_func_3(self):
        name_test_file = 'test3.json'
        my_file = open(name_test_file, 'w')
        my_file.write('[{"h3": "Title#1", "div": "Hello,World1!"},{"h3": "Title#2","div": "Hello,World2!" }]')
        my_file.close()
        self.assertEqual(test.func_3(name_test_file) , '<ul><li><h3>Title#1</h3><div>Hello,World1!</div></li><li><h3>Title#2</h3><div>Hello,World2!</div></li></ul>')
        remove(name_test_file)

    def test_func_4(self):
        name_test_file = 'test4_1.json'
        my_file = open(name_test_file, 'w')
        my_file.write('[{"span":"Title#1","content":[{"p":"Example1","header":"header1"}]},{"div":"div1"}]')
        my_file.close()
        self.assertEqual(test.func_4(name_test_file), '<ul><li><span>Title#1</span><content><ul><li><p>Example1</p><header>header1</header></li></ul></content></li><li><div>div1</div></li></ul>')
        remove(name_test_file)
        name_test_file = 'test4_2.json'
        my_file = open(name_test_file, 'w')
        my_file.write('{"p":"hello1"}')
        my_file.close()
        self.assertEqual(test.func_4(name_test_file), '<p>hello1</p>')
        remove(name_test_file)

    def test_func_5(self):
        name_test_file = 'test4_1.json'
        my_file = open(name_test_file, 'w')
        my_file.write('{"p.my-class#my-id":"hello","p.my-class1.my-class2":[{"div.my-clas2s#my-id3":"hello2","div.my-clas5":"hello2","div#my-id8":"hello2","div":"hello2"}]}')
        my_file.close()
        self.assertEqual(test.func_5n(name_test_file), '<p id="my-id" class="my-class">hello</p><p class="my-class1 my-class2"><ul><li><div id="my-id3" class="my-clas2s">hello2</div><div class="my-clas5">hello2</div><div id="my-id8">hello2</div><div>hello2</div></li></ul></p>')
        remove(name_test_file)

if __name__ == '__main__':
    unittest.main()
