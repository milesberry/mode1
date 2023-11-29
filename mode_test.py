from mode import mode

def test_mode():
    assert mode([3,1,4,1,5])=={1}
    assert mode(["a","b","a"])=={"a"}
    assert mode([2,1,2,1,3])=={2,1}
