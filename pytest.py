import pytest
class str_test():
  def __init__(self):
    self.s = 'hello!'

  def test_type(self):
    print("type test")
    assert isinstance(self.s, str) == True

  def test_index(self):
    print("index test")
    try:
      assert self.s[10] == 'o' 
    except IndexError:
      pass
    
  def test_alph(self):
    print("alph test")
    assert self.s.isalpha() == False

class set_test():
  def __init__(self):
    self.A = {1,2,3}
    self.B = {1,2,3,4,6}

  def intersection_test(self):
    print("intersection test")
    assert self.A.intersection(self.B) == {2,3}

  @pytest.mark.parametrize("C, num", [({1,2,3,4}, 2), ({61,72,83}, 72), ({'n','o'}, 'o')])
  def in_test(C, num):
    print("in test")
    assert num in C
    print(num in C)

  def sub_test(self):
      print("sub test")
      assert self.A.issubset(self.B) == True