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
    with open(r'images\hidden.ppm', 'w') as fp:
      with open(args.file, 'r') as f:
        fp.write(f.readline().strip() + '\n')
        fp.write(f.readline().strip() + '\n')
        fp.write(f.readline().strip() + '\n')
      for i in range(len(read_ppm)):
        for j in range(len(read_ppm[i])):
          fp.write(str(read_ppm[i][j][0] * 10) + '\n')
          fp.write(str(read_ppm[i][j][0] * 10) + '\n')
          fp.write(str(read_ppm[i][j][0] * 10) + '\n')

  def part2():
    try:
      print(args.file)
      read_ppm = readPPM(args.file)
    except:
      sys.exit(0)
    with open(r'images\sepia.ppm', 'w') as fp:
      with open(args.file, 'r') as f:
        fp.write(f.readline().strip() + '\n')
        fp.write(f.readline().strip() + '\n')
        fp.write(f.readline().strip() + '\n')
      for i in range(len(read_ppm)):
        for j in range(len(read_ppm[i])):
          fp.write(str(0.393 * read_ppm[i][j][0] + 0.769 * read_ppm[i][j][1] + 0.189 * read_ppm[i][j][2]) + '\n')
          fp.write(str(0.349 * read_ppm[i][j][0] + 0.686 * read_ppm[i][j][1] + 0.168 * read_ppm[i][j][2]) + '\n')
          fp.write(str(0.272 * read_ppm[i][j][0] + 0.534 * read_ppm[i][j][1] + 0.131 * read_ppm[i][j][2]) + '\n')
  parser = argparse.ArgumentParser(
    description='''Open a given ppm file and read each line until its entire contents have been read''',
    epilog="""All is well that ends well.""")
  subparsers = parser.add_subparsers()
  # create the parser for the "a" command
  parser_part_1 = subparsers.add_parser('part1')
  parser_part_1.set_defaults(func=part1)
  parser_part_1.add_argument("file", metavar='FILE_PATH', help='the directory of the file to be read which should contain commands to be interpreted')
  
  # create the parser for the "b" command
  parser_part_2 = subparsers.add_parser('part2')
  parser_part_2.set_defaults(func=part2)
  parser_part_2.add_argument("file", metavar='FILE_PATH', help='the directory of the file to be read which should contain commands to be interpreted')

  args = parser.parse_args()
  args.func()

if __name__ == "__main__":
  main()