import binascii

def count_char(count_me):
    count = 0
    for el in count_me:
        count += 1
    print(count)



def run():
    num_val = 43188
    hex_val = bytes.fromhex(hex(num_val)[2:])
    hex_val = bytes.fromhex('1f80')

    test = bytes.fromhex(format(168,'016x'))
    for el in test:
        print(el)



run()

