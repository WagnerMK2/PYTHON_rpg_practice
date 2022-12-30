import random
import secrets

def Roll(sides):
    '''
    This is a  random chance for dice rolling. it will work for other odds than the typical.
    :param sides:
    :return:
    '''
    x = []
    for _ in range(256):
        x.append(random.randint(1,sides))
#    print(x)
#    print(secrets.choice(x))
    x = secrets.choice(x)
    print(x)
    return x

Roll(20)
