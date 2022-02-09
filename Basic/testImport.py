import testmod

from testmod import TestClass
# 別名インポート as ・・・
from datetime import datetime as d

test_class_1 = testmod.TestClass()
test_class_1.test_method('1')

test_class_2 = TestClass()
test_class_2.test_method('2')

d.today()
