import pickle
import _sha256 as sha


def _clearbuffer():
    bf = open('./buffer.txt', 'w')
    bf.write('')
    bf.close()


def encode(username, password):
    try:
        _clearbuffer()
        file = open('../pm/' + str(username) + '.txt', 'wb')
        d = []
        u = ste(username).encode()
        u = sha.sha256(u).digest()
        p = str(password).encode()
        p = sha.sha256(p).digest()
        d.append(str(p) + str(u))
        pickle.dump(d, file)
        file.close()
        return True
    except:
        return False


def compare(username, password):
    _clearbuffer()
    bf = open('./buffer.txt', 'wb')
    file = open('../pm/' + str(username) + '.txt', 'rb')
    u = ste(username).encode()
    u = sha.sha256(u).digest()
    p = str(password).encode()
    p = sha.sha256(p).digest()
    d = [str(p) + str(u)]
    # tp = str(file.read())
    pickle.dump(d, bf)
    bf.close()
    bf = open('./buffer.txt', 'rb')
    if bf.read() == file.read():
        return True
    else:
        return False


if __name__ == '__main__':
    encode('XerwinXpl', 'mypassword')
    print(compare('XerwinXpl', 'mypassword'))
    print(compare('XerwinXpl', 'anotherpassword'))
