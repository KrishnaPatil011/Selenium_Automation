import pytest

class TestClass:
    @pytest.mark.parametrize('num1,num2',[(1,1),(3,5),(4,4),(5,7)])
    def test_calculation(self,num1,num2):
        assert num1==num2