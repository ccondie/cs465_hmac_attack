import sha1
import hashlib


def run():
    print('sha1:\t\t', end='')
    print(sha1.sha1(b'this is data'))

    print('hashlib:\t', end='')
    print(hashlib.sha1(b'this is data').hexdigest())

    print('sha1:\t\t', end='')
    print(sha1.sha1(b'this is data', 0x67452301EFCDAB8998BADCFE10325476C3D2E1F0))

    print()

    print('sha1:\t\t', end='')
    print(sha1.sha1(b'this is data', 0xf4b645e89faaec2ff8e443c595009c16dbdfba4b))

    print('sha1:\t\t', end='')
    print(sha1.sha1(b'this is data', 0xf4b645e89faaec2ff8e443c595009c16dbdfba4b))


if __name__ == '__main__':
    run()
