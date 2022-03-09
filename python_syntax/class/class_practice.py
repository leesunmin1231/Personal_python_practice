class one:
    def __init__(self):
        print("첫번째")

class two:
    def __init__(self):
        print("두번째")

class one_two(one,two):
    def __init__(self):
        super().__init__()  # 이경우 '첫번째'만 출력되는 문제가 발생한다.

# 따라서 다중상속 하는 경우 one.__init__()으로 호출해야 한다.

one_two()