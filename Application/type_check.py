class TestClass:

    def __init__(self, title):
        self.title = title


tuple_instance = ('tupple', 'instance')
print(type(tuple_instance))
list_instance = ['list', 'instance']
print(type(list_instance))
dict_instance = {'1': 'dict', '2': 'instance'}
print(type(dict_instance))
class_instance = TestClass('class')
print(type(class_instance))


python_list = []
python_list.append('python')
python_list.append('izm')
python_list.append(tuple_instance)
python_list.append(list_instance)
python_list.append(dict_instance)
python_list.append(class_instance)

for parent in python_list:
    if isinstance(parent, tuple):
        print('++++ tuple ++++')
        for child in parent:
            print(child)

    elif isinstance(parent, list):
        print('++++ list ++++')
        for child in parent:
            print(child)

    elif isinstance(parent, dict):
        print('++++ dict ++++')
        print(parent)
        for child in parent:
            print(child)

    elif isinstance(parent, TestClass):
        print('++++ TestClass ++++')
        print(parent.title)

    else:
        print('---string---')
        print(parent)


class AttrTest():

    def __init__(self):
        self.code = -1


attr_test = AttrTest()
attr_test.name = 'python-izm'

# hasattr関数
# print(hasattr(attr_test, 'code'))
# print(hasattr(attr_test, 'name'))
# print(hasattr(attr_test, 'kana'))

# gatter関数
print(getattr(attr_test, 'code'))
print(getattr(attr_test, 'name'))
print(getattr(attr_test, 'kana', 'No Attr'))
