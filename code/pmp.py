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
        p = str(password).encode()
        p = sha.sha256(p).digest()
        d.append(str(p))
        pickle.dump(d, file)  # TODO : FIX THIS
        file.close()
        return True
    except:
        return False


def compare(username, password):
    _clearbuffer()
    bf = open('./buffer.txt', 'wb')
    file = open('../pm/' + str(username) + '.txt', 'rb')
    p = str(password).encode()
    p = sha.sha256(p).digest()
    d = [str(p)]
    # tp = str(file.read())
    pickle.dump(d, bf)  # TODO : FIX THIS TOO
    bf.close()
    bf = open('./buffer.txt', 'rb')
    if bf.read() == file.read():
        return True
    else:
        return False


if __name__ == '__main__':
    encode('XerwinXpl', 'mypassowrd')
    print(compare('XerwinXpl', 'mypassword'))
    print(compare('XerwinXpl', 'anotherpassword'))
