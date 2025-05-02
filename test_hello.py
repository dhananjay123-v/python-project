from hellounit import hello
import pytest

def test_default():
    assert hello("gyan")=="hello,gyan"
  
def test_argument():
    for i in ["gyan","levi","super"]:
        assert hello(i)==f"hello,{i}"
        
    
