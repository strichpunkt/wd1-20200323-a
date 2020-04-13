def greater_less_detector(x, y):
    return 0

def test_greater_less_detector():
    assert greater_less_detector(1,2) == "greater"
    assert greater_less_detector(3,3) == "equal"
    assert greater_less_detector(3, -3) == "less"
    assert greater_less_detector(100., 1300.) == "greater"

if __name__ == '__main__':
    test_greater_less_detector()
    print("SUCCESS")
