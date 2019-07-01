import argparse
import sys
import os

# orig if, -V, -h, -b, -e

def exec_orig():
  print("use orig")
  cmd = ' '.join(sys.argv[1:])
  print(cmd)

if __name__ == '__main__':
  parser = argparse.ArgumentParser()
  parser.add_argument('cmd')
  parser.add_argument('source', metavar='URLs', type=str, nargs='+')

  logging = parser.add_argument_group('Logging and input file:')
  logging.add_argument('-o', '--output-file', metavar="FILE" , help="log messages to FILE")
  logging.add_argument('-a', '--append-output', metavar="FILE" , help="append messages to FILE")
  logging.add_argument('-d', '--debug', action='store_true', help="print lots of debugging information")
  logging.add_argument('-q', '--quiet', action='store_true', help="quiet (no output)")
  logging.add_argument('-v', '--verbose', action='store_true', help="be verbose (this is the default)")
  logging.add_argument('-nv', '--no-verbose', action='store_true',
                        help="turn off verboseness, without being quiet, if possible")
  logging.add_argument('-i', '--input-file', metavar="FILE" ,
                        help="download URLs found in local or external FILE")

  dnld = parser.add_argument_group('Download:')
  dnld.add_argument('-t', '--tries', help="set number of retries to NUMBER (0 unlimits)")
  dnld.add_argument('--retry-connrefused', action='store_true', help="retry even if connection is refused") # by default anyway
  dnld.add_argument('-O', '--output-document', metavar="FILE" , help="write documents to FILE")
  dnld.add_argument('-nc', '--no-clobber', action='store_true',
                      help="skip downloads that would download to existing files (overwriting them)")
  dnld.add_argument('--no-netrc', action='store_true', help="don't try to obtain credentials from .netrc")
  dnld.add_argument('-c', '--continue', dest="contin", action='store_true', help="resume getting a partially-downloaded file")
  dnld.add_argument('-N', '--timestamping', action='store_true', help="don't re-retrieve files unless newer than local") # by default anyway
  dnld.add_argument('-T', '--timeout', help="set all timeout values to SECONDS")
  dnld.add_argument('--connect-timeout', help="set the connect timeout to SECS")
  dnld.add_argument('-w', '--wait', help="wait SECONDS between retrievals")
  dnld.add_argument('--bind-address', help="bind to ADDRESS (hostname or IP) on local host")
  dnld.add_argument('--limit-rate', help="limit download rate to RATE")
  dnld.add_argument('--ignore-case', action='store_true', help="ignore case when matching files/directories")
  dnld.add_argument('-4', '--inet4-only', action='store_true', help="connect only to IPv4 addresses")
  dnld.add_argument('--user', help="set both ftp and http user to USER")
  dnld.add_argument('--password', help="set both ftp and http password to PASS")
  dnld.add_argument('--unlink', action='store_true', help="remove file before clobber")

  parser.add_argument('args', nargs=argparse.REMAINDER)
  args = parser.parse_args()
  print(args)

  if len(args.args) == 0:
    print("use aria2c")
    # construct aria2c command
    cmd = "aria2c "
    cmd += ' '.join(args.source)
    # conditions for executing original
    # -d, nv
    if args.output_file != None:
      # remove this file, so new data is written
      os.remove(args.output_file)
      cmd += " -l " + args.output_file
    if args.append_output != None:
      cmd += " -l " + args.append_output
    if args.debug is True:
      cmd += " --log-level=debug"
    if args.quiet is True:
      cmd += " -q"
    if args.input_file != None:
      cmd += " -i " + args.input_file

    if args.tries != None:
      cmd += " -m " + args.tries
    if args.output_document != None:
      cmd += " -o " + args.output_document
    if args.no_clobber is True:
      cmd += " --auto-file-renaming=false"
    if args.no_netrc is True:
      cmd += " --no-netrc"
    if args.contin is True:
      cmd += " -c"
    if args.timestamping is True:
      cmd += " --conditional-get"
    if args.timeout != None:
      cmd += " -t " + args.timeout
    if args.connect_timeout != None:
      cmd += " --connect-timeout " + args.connect_timeout
    if args.wait != None:
      cmd += " --retry-wait " + args.wait
    if args.bind_address != None:
      cmd += " --interface " + args.bind_address
    if args.limit_rate != None:
      cmd += " --max-overall-download-limit= " + args.limit_rate
    if args.bind_address != None:
      cmd += " --interface " + args.bind_address
    if args.ignore_case is True:
      cmd += " --auto-file-renaming=false"
    if args.inet4_only is True:
      cmd += " --disable-ipv6"
    if args.user != None:
      cmd += " --http-user " + args.user
      cmd += " --ftp-user " + args.user
    if args.password != None:
      cmd += " --http-passwd " + args.password
      cmd += " --ftp-passwd " + args.password
    if args.unlink is True:
      cmd += " --allow-overwrite"

    print(cmd)

  else:
    exec_orig()

