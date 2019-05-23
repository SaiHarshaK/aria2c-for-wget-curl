import argparse
import sys
import os

# orig if, -V, -h, -b, -e

def exec_orig():
  cmd = ' '.join(sys.argv[1:])
  print(cmd)

if __name__ == '__main__':
  parser = argparse.ArgumentParser()
  parser.add_argument('cmd')
  parser.add_argument('source', metavar='URLs', type=str, nargs='+')

  logging = parser.add_argument_group('Logging and input file:')
  logging.add_argument('-o', '--output-file', metavar="FILE" ,help="log messages to FILE")
  logging.add_argument('-a', '--append-output', metavar="FILE" ,help="append messages to FILE")
  logging.add_argument('-d', '--debug', action='store_true', help="print lots of debugging information")
  logging.add_argument('-q', '--quiet', action='store_true', help="quiet (no output)")
  logging.add_argument('-v', '--verbose', action='store_true', help="be verbose (this is the default)")
  logging.add_argument('-nv', '--no-verbose', action='store_true',
                        help="turn off verboseness, without being quiet, if possible")

  dnld = parser.add_argument_group('Download:')
  dnld.add_argument('-t', '--tries', help="log messages to FILE")

  parser.add_argument('args', nargs=argparse.REMAINDER)
  args = parser.parse_args()
  print(args)

  if len(args.args) == 0:
    # construct aria2c command
    cmd = "aria2c "
    cmd += ' '.join(args.source)
    if args.output_file != None:
      # remove this file, so new data is written
      os.remove(args.output_file)
      cmd += " -l " + args.output_file
    if args.append_output != None:
      cmd += " -l " + args.append_output
    if args.quiet is True:
      cmd += " -q"

  else:
    exec_orig()

