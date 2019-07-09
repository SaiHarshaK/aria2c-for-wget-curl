#!/usr/bin/env python3
import argparse
import os
import subprocess
import sys

def exec_orig():
  print("Using curl:")
  cmd = []
  cmd.append('curl-orig')
  iterArgs = iter(sys.argv)
  next(iterArgs)
  for arg in iterArgs:
    cmd.append(arg)

  # remove "--orig" if present
  if '--orig' in cmd: cmd.remove('--orig')

  subprocess.run(cmd)

if __name__ == '__main__':
  parser = argparse.ArgumentParser(
            description='curl stub for aria2c.',
            prog='curl', usage='%(prog)s [options...] <url>', formatter_class=argparse.RawDescriptionHelpFormatter)
  parser.add_argument('source', metavar='URL', type=str, help=argparse.SUPPRESS)
  parser.add_argument('--orig', action='store_true', help="Use original curl")

#  parser.add_argument('--orig', action='store_true', help="Use original curl")

  parser.add_argument('args', nargs=argparse.REMAINDER, help=argparse.SUPPRESS)
  args = parser.parse_args()

  if len(args.args) == 0 and args.orig is False:
    # construct aria2c command
    cmd = []
    cmd.append("aria2c")

    cmd.append(args.source)

    print("Using aria2c:")
    subprocess.run(cmd)

  else:
    exec_orig()
