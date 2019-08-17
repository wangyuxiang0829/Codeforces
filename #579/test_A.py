import A


def test_query():
    assert A.query([1, 2, 3, 4], 4) == True
    assert A.query([1, 3, 2], 3) == True
    assert A.query([1, 2, 3, 5, 4], 5) == False
    assert A.query([1], 1) == True
    assert A.query([3, 2, 1, 5, 4], 5) == True
