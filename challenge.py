ipAddress = input("Please, enter you IP address: ")

segment = 1
segment_length = 0
character = ""

if character in ipAddress:
    if character == '.':
        print("segment {} comtains {} characters".format(segment, segment_length))
        segment += 1
        segment_length = 0
    else:
        segment_length += 1

if character != '.':
    print("segment {} comtains {} characters".format(segment, segment_length))
