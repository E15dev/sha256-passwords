import os
import _sha256 as sha


def encode(username, password):
    try:
        file = open('../pm/' + str(username) + '.txt', 'w')
        u = ste(username).encode()
        u = sha.sha256(u).digest()
        p = str(password).encode()
        p = sha.sha256(p).digest()
        file.write(str(p) + str(u))
        file.close()
        return True
    except:
        return False
    

def compare(username, password):
    file = open('../pm/' + str(username) + '.txt', 'r')
    u = ste(username).encode()
    u = sha.sha256(u).digest()
    p = str(password).encode()
    p = sha.sha256(p).digest()
    tp = str(file.read())
    file.close()
    if (str(p) + str(u)) == tp:
        return True
    else:
        return False
    return False


if __name__  == '__main__':
    encode('XerwinXpl', 'mypassowrd')
    print(compare('XerwinXpl', 'mypassword'))
    print(compare('XerwinXpl', 'anotherpassword'))
