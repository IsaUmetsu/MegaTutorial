def chapter12_1():
    from datetime import datetime
    print(str(datetime.now()))
    print(str(datetime.utcnow()))

def chapter14_1():
    from app.translate import translate
    print(translate('Hi, how are you today?'))
# execute
chapter14_1()