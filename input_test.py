
class Non_Exp(Exception):
    def __init__(self):
        pass

def dd():
    raise Non_Exp()

try:
    dd()
except ValueError:
    print('asd')