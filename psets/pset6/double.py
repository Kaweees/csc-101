import argparse
import sys
from read import readPPM

def main():
  def part1():
    try:
      print(args.file)
      read_ppm = readPPM(args.file)
    except:
      sys.exit(0)
    with open(r'images\doubled.ppm', 'w') as fp:
      with open(args.file, 'r') as f:
        fp.write(f.readline().strip() + '\n')
        fp.write(f"{len(read_ppm[0]) * 2} {len(read_ppm) * 2}" + '\n')
        fp.write(f.readline().strip() + '\n')
        fp.write(f.readline().strip() + '\n')
      for i in range(len(read_ppm)):
        for j in range(len(read_ppm[i])):
          for n in range(2):
            for k in range(len(read_ppm[i][j])):
              fp.write(str(read_ppm[i][j][k])  + '\n')

  parser = argparse.ArgumentParser(
    description='''Open a given ppm file and read each line until its entire contents have been read''',
    epilog="""All is well that ends well.""")
  subparsers = parser.add_subparsers()
  # create the parser for the "a" command
  parser_part_1 = subparsers.add_parser('part1')
  parser_part_1.set_defaults(func=part1)
  parser_part_1.add_argument("file", metavar='FILE_PATH', help='the directory of the file to be read which should contain commands to be interpreted')

  args = parser.parse_args()
  args.func()
if __name__ == "__main__":
  main()