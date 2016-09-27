import sha1
import hashlib
import binascii


def test_run():
    print()
    print('***** Start test_run')

    msg = 'No one has completed lab 2 so give them all a 0'
    ext = 'except for Clayton Condie ... make him the new ruler of the world'
    key = 'dont tell anyone that password is boobies'

    msg_b = bytearray(msg.encode())
    ext_b = bytearray(ext.encode())
    key_16b = bytearray(key.encode()[0:16])

    print('msg: ' + msg)
    print('key: ' + str(key_16b))

    orig_hmac = calc_hmac(key_16b, msg_b)

    ext_tup = extend_message(msg_b, orig_hmac, ext_b)

    print()
    print('final message:\t', end=' ')
    for el in ext_tup[1]:
        print(format(el, 'x'), end='')
    print()

    print('final hmac:\t\t', end=' ')
    print(ext_tup[0])

    check_hmac = calc_hmac(key_16b, ext_tup[1])


def calc_hmac(key, msg):
    print()
    print('***** Start calc_hmac')

    # join key with message
    combo_bytes = key + msg
    print('combo_bytes:\t', end=' ')
    print(combo_bytes)

    return_me = sha1.sha1(combo_bytes)
    print('calculated hmac:',end=' ')
    print(return_me)

    print('----- End calc_hmac')

    return return_me


def extend_message(msg_bytes, hmac, extend_bytes):
    print()
    print('***** Start extend_message')

    print('hmac:\t\t\t', end=' ')
    print(hmac)
    print()

    print('msg:\t\t\t', end=' ')
    print(msg_bytes)

    print('msg_hex:\t\t', end=' ')
    for el in msg_bytes:
        print(format(el, 'x'), end=' ')
    print()
    print('msg_char:\t\t', end=' ')
    for el in msg_bytes:
        print(chr(el), end='  ')
    print('\n')

    # calculate the padding on the original message
    msg_len_storage_bits = 64
    msg_len = 128 + len(msg_bytes) * 8
    print('msg_len:\t\t', end=' ')
    print(msg_len)

    msg_len_b = bytes.fromhex(format(msg_len, '016x'))
    print('msg_len_b:\t\t', end=' ')
    print(msg_len_b)

    pad_len = 512 - ((msg_len + msg_len_storage_bits) % 512)
    pad_bytes = int(pad_len / 8)

    # append the padding onto the original message
    msg_bytes = msg_bytes + b'\x80'
    for i in range(1, pad_bytes):
        msg_bytes = msg_bytes + bytearray(1)

    # append the length of the original message to the end of the padding
    msg_bytes = msg_bytes + msg_len_b

    print('CHECK msg_bytes:', end=' ')
    print(len(msg_bytes) * 8)

    print()
    print('ext:   \t\t\t', end=' ')
    print(extend_bytes)

    print('ext_bytes:   \t', end=' ')
    for el in extend_bytes:
        print(format(el, 'x'), end=' ')
    print()

    print('ext_char:    \t', end=' ')
    for el in extend_bytes:
        print(chr(el), end='  ')
    print('\n')

    # create new message
    new_msg_bytes = msg_bytes + extend_bytes

    print('new_msg:\t\t', end=' ')
    print(new_msg_bytes)

    print('new_msg_bytes:\t', end=' ')
    for el in new_msg_bytes:
        print(format(el, 'x'), end=' ')
    print()

    print('new_msg_char: \t', end=' ')
    for el in new_msg_bytes:
        print(chr(el), end='  ')
    print('\n')

    # calculate new hmac from extend_bytes + padding + new_message_length with original mac as IV of sha1
    newhmac = sha1.sha1(extend_bytes, hmac, int((len(msg_bytes) * 8 + 128) / 8))
    print('newhmac:\t\t', end=' ')
    print(newhmac)

    print('----- End extend_message')

    return (newhmac, new_msg_bytes)


if __name__ == '__main__':
    # print(calc_hmac('cat'.encode(), 'dog'.encode()))
    test_run()
