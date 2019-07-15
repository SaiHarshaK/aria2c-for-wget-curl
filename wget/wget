#!/usr/bin/env python3
import argparse
import os
import subprocess
import sys

def exec_orig():
  print("Using wget:")
  cmd = []
  cmd.append('wget-orig')
  iterArgs = iter(sys.argv)
  next(iterArgs)
  for arg in iterArgs:
    cmd.append(arg)

  # remove "--orig" if present
  if '--orig' in cmd: cmd.remove('--orig')

  subprocess.run(cmd)

if __name__ == '__main__':
  parser = argparse.ArgumentParser(
            description='GNU Wget stub for aria2c.\n' +
            'Mandatory arguments to long options are mandatory for short options too.',
            prog='wget', usage='%(prog)s [OPTION]... [URL]...', formatter_class=argparse.RawDescriptionHelpFormatter)
  parser.add_argument('source', metavar='URLs', type=str, nargs='+', help=argparse.SUPPRESS)
  parser.add_argument('--orig', action='store_true', help="Use original GNU wget")

  logging = parser.add_argument_group('Logging and input file')
  logging.add_argument('-o', '--output-file', metavar="FILE" , help="log messages to FILE")
  logging.add_argument('-a', '--append-output', metavar="FILE" , help="append messages to FILE")
  logging.add_argument('-d', '--debug', action='store_true', help="print lots of debugging information")
  logging.add_argument('-q', '--quiet', action='store_true', help="quiet (no output)")
  logging.add_argument('-v', '--verbose', action='store_true', help="be verbose (this is the default)")
  logging.add_argument('-nv', '--no-verbose', action='store_true',
                        help="turn off verboseness, without being quiet, if possible")
  logging.add_argument('-i', '--input-file', metavar="FILE" ,
                        help="download URLs found in local or external FILE")

  dnld = parser.add_argument_group('Download')
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

  direc = parser.add_argument_group('Directories')
  direc.add_argument('-P', '--directory-prefix', help="save files to PREFIX/..")

  http_opt = parser.add_argument_group('HTTP options')
  http_opt.add_argument('--http-user', help="set http user to USER")
  http_opt.add_argument('--http-password', help="set http password to PASS")
  http_opt.add_argument('--no-cache', action='store_true', help="disallow server-cached data")
  http_opt.add_argument('--header', action='append', help="insert STRING among the headers")
  http_opt.add_argument('--proxy-user', help="set USER as proxy username")
  http_opt.add_argument('--proxy-password', help="set PASS as proxy password")
  http_opt.add_argument('--referer', help="include 'Referer: URL' header in HTTP request")
  http_opt.add_argument('-U', '--user-agent', help="identify as AGENT instead of Wget/VERSION")
  http_opt.add_argument('--no-http-keep-alive', action='store_true', help="disable HTTP keep-alive (persistent connections)")
  http_opt.add_argument('--load-cookies', help="load cookies from FILE before session")
  http_opt.add_argument('--save-cookies', help="save cookies to FILE after session (session cookies are also saved)")
  http_opt.add_argument('--auth-no-challenge', action='store_true', help="send Basic HTTP authentication information without first waiting for the server's challenge")

  https_opt = parser.add_argument_group('HTTPS (SSL/TLS) options')
  https_opt.add_argument('--certificate', help="client certificate file. PKCS12 (.p12, .pfx) or in PEM format")
  https_opt.add_argument('--private-key', help="private key file. PEM format")
  https_opt.add_argument('--ca-certificate', help="file with the bundle of CAs. PEM format.")

  ftp_opt = parser.add_argument_group('FTP options')
  ftp_opt.add_argument('--ftp-user', help="set ftp user to USER")
  ftp_opt.add_argument('--ftp-password', help="set ftp password to PASS")
  ftp_opt.add_argument('--no-passive-ftp', action='store_true', help='disable the "passive" transfer mode')

  parser.add_argument('args', nargs=argparse.REMAINDER, help=argparse.SUPPRESS)
  args = parser.parse_args()

  if len(args.args) == 0 and args.orig is False:
    # construct aria2c command
    cmd = []
    cmd.append("aria2c")
    # conditions for executing original
    if args.output_file != None:
      # remove this file, so new data is written
      os.remove(args.output_file)
      cmd.append("-l")
      cmd.append(args.output_file)
    if args.append_output != None:
      cmd.append("-l")
      cmd.append(args.append_output)
    if args.debug == True:
      cmd.append("--log-level=debug")
    if args.quiet == True:
      cmd.append("-q")
    if args.input_file != None:
      cmd.append("-i")
      cmd.append(args.input_file)

    if args.tries != None:
      cmd.append("-m")
      cmd.append(args.tries)
    if args.output_document != None:
      cmd.append("-o")
      cmd.append(args.output_document)
    if args.no_clobber == True:
      cmd.append("--auto-file-renaming=false")
    if args.no_netrc == True:
      cmd.append("--no-netrc")
    if args.contin == True:
      cmd.append("-c")
    if args.timestamping == True:
      cmd.append("--conditional-get")
    if args.timeout != None:
      cmd.append("-t")
      cmd.append(args.timeout)
    if args.connect_timeout != None:
      cmd.append("--connect-timeout")
      cmd.append(args.connect_timeout)
    if args.wait != None:
      cmd.append("--retry-wait")
      cmd.append(args.wait)
    if args.bind_address != None:
      cmd.append("--interface")
      cmd.append(args.bind_address)
    if args.limit_rate != None:
      cmd.append("--max-overall-download-limit=")
      cmd.append(args.limit_rate)
    if args.ignore_case == True:
      cmd.append("--auto-file-renaming=false")
    if args.inet4_only == True:
      cmd.append("--disable-ipv6")
    if args.user != None:
      cmd.append("--http-user")
      cmd.append(args.user)
      cmd.append("--ftp-user")
      cmd.append(args.user)
    if args.password != None:
      cmd.append("--http-passwd")
      cmd.append(args.password)
      cmd.append("--ftp-passwd")
      cmd.append(args.password)
    if args.unlink == True:
      cmd.append("--allow-overwrite")

    if args.directory_prefix != None:
      cmd.append("--dir")
      cmd.append(args.directory_prefix)

    if args.http_user != None:
      cmd.append("--http-user")
      cmd.append(args.http_user)
    if args.http_password != None:
      cmd.append("--http-passwd")
      cmd.append(args.http_password)
    if args.no_cache == True:
      cmd.append("--http-no-cache")
    if args.proxy_user != None:
      cmd.append("--http-proxy-user")
      cmd.append(args.proxy_user)
    if args.proxy_password != None:
      cmd.append("--http-proxy-passwd")
      cmd.append(args.proxy_password)
    if args.referer != None:
      cmd.append("--referer")
      cmd.append(args.referer)
    if args.user_agent != None:
      cmd.append("--user-agent")
      cmd.append(args.user_agent)
    if args.no_http_keep_alive == True:
      cmd.append("--enable-http-keep-alive=false")
    if args.load_cookies != None:
      cmd.append("--load-cookies")
      cmd.append(args.load_cookies)
    if args.save_cookies != None:
      cmd.append("--save-cookies")
      cmd.append(args.save_cookies)
    if args.auth_no_challenge == False:
      cmd.append("--http-auth-challenge=true")

    if args.certificate != None:
      cmd.append("--certificate")
      cmd.append(args.certificate)
    if args.private_key != None:
      cmd.append("--private-key")
      cmd.append(args.private_key)
    if args.ca_certificate != None:
      cmd.append("--ca-certificate")
      cmd.append(args.ca_certificate)

    if args.ftp_user != None:
      cmd.append("--ftp-user")
      cmd.append(args.ftp_user)
    if args.ftp_password != None:
      cmd.append("--ftp-passwd")
      cmd.append(args.ftp_password)
    if args.no_passive_ftp == True:
      cmd.append("--ftp-pasv=false")

    if args.header != None:
      for header in args.header:
        cmd.append("--header")
        cmd.append(header)

    for source in args.source:
      cmd.append(source)

    print("Using aria2c:")
    subprocess.run(cmd)

  else:
    exec_orig()
