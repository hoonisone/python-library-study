import argparse

parser = argparse.ArgumentParser()
parser.add_argument("--name", type=str, help="enter user name")
parser.add_argument("--age", type=int, help="enter user age")
flags = parser.parse_args()
print(flags)
print(flags.name)
print(flags.age)