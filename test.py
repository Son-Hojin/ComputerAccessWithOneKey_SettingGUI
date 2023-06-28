def hex_to_rgb(hex):
    r = int(hex[1:3], 16)
    g = int(hex[3:5], 16)
    b = int(hex[5:7], 16)
    return r,g,b

while True:
    hex = input()
    print(type(hex_to_rgb(hex)))
    r,g,b = hex_to_rgb(hex)
    print(r)
    print(b)
    print(type(g))
    # print("rgb(",int("0x"+hex[0:2], 16),", ", int("0x"+hex[2:4], 16),", ", int("0x"+hex[4:6], 16),')', sep='')
