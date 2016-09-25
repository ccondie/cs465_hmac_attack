import sha1
import hashlib
import binascii


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


def test_run():
    message = 'No one has completed lab 2 so give them all a 0'
    key_long = 'dont tell anyone that password is boobies'
    key_128bit = key_long.encode()[0:16]

    hmac = hashlib.sha1(key_128bit + message.encode()).hexdigest()

    extend_message(message, hmac.encode())


def extend_message(msg, hmac):
    """

    :param msg: a string representation of the message
    :param hmac: a byte array representation of the original hmac
    :return: a tuple with the new message and hmac (message, hmac)
    """
    msg_bytes = bytearray(msg.encode())
    extend_bytes = bytearray('except for Clayton Condie ... make him the new ruler of the world'.encode())

    print('message:\t\t', end=' ')
    print(msg)
    print('message_hex:\t', end=' ')
    for el in msg_bytes:
        print(format(el, 'x'),end=' ')
    print()
    print('hmac:\t\t\t', end=' ')
    print(hmac)



    # calculate the padding on the original message
    orig_msg_len = 128 + len(msg_bytes) * 8
    pad_len = orig_msg_len % 512
    pad_bytes = int(pad_len / 8)

    # append the padding onto the new message
    for i in range(0, pad_bytes):
        extend_bytes = bytearray(1) + extend_bytes

    print('extend_bytes:\t',end=' ')
    for el in extend_bytes:
        print(format(el,'x'),end=' ')
    print()

    # create new message
    new_msg_bytes = msg_bytes + extend_bytes
    print('new_msg_bytes:\t',end=' ')
    for el in new_msg_bytes:
        print(format(el, 'x'),end=' ')
    print()

    # calculate new hmac from extend_bytes + padding + new_message_length with original mac as IV of sha1
    pass


if __name__ == '__main__':
    test_run()
