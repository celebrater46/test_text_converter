# This is simple converter to convert "Hello World" to "Hello Everyone".
def convert_text():
    # print("Hello world!")

    f = open("input/test.txt", "r") # r = readonly
    # print(f.read())
    # print(f.read(4)) # Hell
    # str = f.read()
    # print(str)
    # str = str.replace("World", "Everyone")

    lines = f.readlines()
    # print(type(lines))
    # print(lines) # ['Hello World 1!!!!!!!!!!!!!!!!!!\n', 'Hello World 2......\n', 'Hello World 3!?!?!?']

    # print("### print lines with foreach")
    # for line in lines:
    #     print(line)


    print("### write lines to result.txt with foreach")
    f2 = open("output/result.txt", "w") # w = create or overwrite
    for line in lines:
        temp = line.replace("World", "Everyone")
        f2.write(temp)

    f.close()
    f2.close()

convert_text()