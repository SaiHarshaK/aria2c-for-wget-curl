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
  parser.add_argument('source', metavar='URLs', type=str, nargs='+', help=argparse.SUPPRESS)
  parser.add_argument('--orig', action='store_true', help="Use original curl")
  parser.add_argument('-o', '--output', metavar='filename', help="Write to file instead of stdout")

  parser.add_argument('--cacert', metavar='file', help="CA certificate to verify peer against.  PKCS12 (.p12, .pfx) or in PEM format")
  parser.add_argument('--capath', metavar='dir', help="CA directory to verify peer against")
  parser.add_argument('--cert', metavar='certificate[:password]', help="Client certificate file and password.  PKCS12 (.p12, .pfx) or in PEM format")
  parser.add_argument('--cert-type', metavar='type', help="Certificate file type (DER/PEM/ENG). aria2c supports only PEM")
  parser.add_argument('--connect-timeout', metavar='seconds', help="Maximum time allowed for connection")
  parser.add_argument('--cookie', metavar='filename', help="Send cookies from file")
  parser.add_argument('--cookie-jar', metavar='filename', help="Write cookies to <filename> after operation")
  parser.add_argument('--create-dirs', action='store_true', help="Create necessary local directory hierarchy") #does this by default
  #parser.add_argument('-q', '--disable', action='store_true', help="Disable .curlrc")
  parser.add_argument('--disallow-username-in-url', action='store_true', help="Disallow username in url")
  parser.add_argument('-H', '--header', metavar='string', action='append', help="Pass custom header(s) to server")
  parser.add_argument('--hostpubmd5', metavar='md5', help="Acceptable MD5 hash of the host public key")
  parser.add_argument('--interface', metavar='name', help="Use network INTERFACE (or address)")
  parser.add_argument('-4', '--ipv4', action='store_true', help="Resolve names to IPv4 addresses")

  parser.add_argument('args', nargs=argparse.REMAINDER, help=argparse.SUPPRESS)
  args = parser.parse_args()

  if len(args.args) == 0 and args.orig == False and args.output != None and (args.cert_type == None or args.cert_type == "PEM"):
    # construct aria2c command
    cmd = []
    cmd.append("aria2c")
    # conditions for executing original
    path = ""
    if args.capath != None:
      path += args.capath
    if args.cacert != None:
      cmd.append("--ca-certificate")
      path += args.cacert
      cmd.append(path)
    if args.cert != None:
      # check if ':' is present
      if ':' in args.cert:
        vals = args.cert.rsplit(':', 1)
        cmd.append("--certificate")
        cmd.append(vals[0])
        cmd.append("--private-key")
        cmd.append(vals[1])
      else:
        cmd.append("--certificate")
        cmd.append(args.cert)
    if args.connect_timeout != None:
      cmd.append("--connect-timeout")
      cmd.append(args.connect_timeout)
    if args.cookie != None:
      cmd.append("--load-cookies")
      cmd.append(args.cookie)
    if args.cookie_jar != None:
      cmd.append("--save-cookies")
      cmd.append(args.cookie_jar)
    if args.disallow_username_in_url == True:
      print("curl: (67) Login denied")
      sys.exit()
    if args.output != None:
      cmd.append("-o")
      cmd.append(args.output)
    if args.hostpubmd5 != None:
      arg_build = "--ssh-host-key-md=" + "md5=" + args.hostpubmd5
      cmd.append(arg_build)
    if args.interface != None:
      cmd.append("--interface")
      cmd.append(args.interface)
    if args.ipv4 == True:
      cmd.append("--disable-ipv6")

    if args.header != None:
      for header in args.header:
        # check if file is passed
        if ('@' in args.header):
          exec_orig()
          sys.exit()
        cmd.append("--header")
        cmd.append(header)

    for source in args.source:
      cmd.append(source)

    print("Using aria2c:")
    subprocess.run(cmd)

  else:
    exec_orig()
