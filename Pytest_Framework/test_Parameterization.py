import pytest

class TestClass:

    @pytest.mark.parametrize('num1,num2',[(1,2)(4,4)(11,11)(10,9)])
    def test_Calculate(self,num1,num2):
        assert num1==num2