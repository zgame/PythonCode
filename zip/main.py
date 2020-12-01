# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
import zlib
import gzip

def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.

    message = 'hello'
    compressed = zlib.compress(message.encode())
    decompressed = zlib.decompress(compressed)

    print('original:', repr(message))
    print_hex(compressed)
    print('decompressed:', repr(decompressed))
    # with open('1.txt', 'w', encoding='utf-8') as f:  # python3
    #     f.write(compressed.decode(encoding="utf-8"))

    print('----------------------------')
    f_in = open("1.txt", "rb")  # 打开文件
    f_out = gzip.open("data.txt.gz", "wb")  # 创建压缩文件对象
    f_out.writelines(f_in)
    f_out.close()
    f_in.close()


def print_hex(bytes):
    l = [hex(int(i)) for i in bytes]
    print(" ".join(l))

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('zlib')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
