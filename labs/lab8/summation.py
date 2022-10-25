import argparse
import sys

def main():
  parser=argparse.ArgumentParser(
    description='''Open a given file and read each line until its entire contents have been read''',
    epilog="""All is well that ends well.""")
  parser.add_argument(dest='file', metavar='FILE_PATH', type=open, help='the directory of the file to be read')
  args=parser.parse_args()
  try:
    for line in args.file.read().splitlines():
      print(sum([float(word) for word in line.split(" ")]))
  except:
    print(parser)
    sys.exit(0)
if __name__ == "__main__":
  main()