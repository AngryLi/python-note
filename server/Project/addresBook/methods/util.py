
import random
import hashlib

class Util:
    Key = '9dfs8ads8f9s0ad8f09sdfa';
    @staticmethod
    def guid():
        const = 'xxxxxxxx-xxxx-4xxx-yxxx-xxxxxxxxxxxxx'
        guid = ''
        for item in const:
            if item == 'x':
                guid += str(random.randint(0, 10))
            elif item == 'y':
                guid += str((random.randint(0, 10) | 0) & 0x03 | 0x8)
            else:
                guid += item
        return guid.upper()
    @staticmethod
    def md5(password):
        m = hashlib.md5()
        m.update(password.encode('utf-8'))
        m.update('fiosaufsdiaufdsufdsf0'.encode('utf-8'))
        return m.hexdigest()

if __name__ == '__main__':
    print(Util.md5('sa8df9ds8f'))
