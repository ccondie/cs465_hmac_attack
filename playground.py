import binascii


def run():
    message = 'ca t'.encode()
    dummy = message.zfill(7)
    print(dummy)
    print(len(message.zfill(7)))

    print(b''.join([message, dummy]))

run()
