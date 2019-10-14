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
  parser.add_argument('--key', metavar='filename', help="Private key file name")
  parser.add_argument('--key-type', metavar='type', help="Private key file type (DER/PEM/ENG).PEM format for aria2c")
  parser.add_argument('--limit-rate', metavar='speed', help="Limit transfer speed to RATE")
  parser.add_argument('--netrc-file', metavar='filename', help="Specify FILE for netrc. default home dir")
  parser.add_argument('--no-keepalive', action='store_true', help="Disable TCP keepalive on the connection")
  parser.add_argument('--noproxy', metavar='no-proxy-list', help="List of hosts which do not use proxy")
  parser.add_argument('-o', '--output', metavar='filename', help="Write to file instead of stdout")
  parser.add_argument('--proto-default', metavar='protocol', help="Use PROTOCOL for any URL missing a scheme")
  parser.add_argument('-x', '--proxy', metavar='[protocol://]host[:port]', help="Use this proxy")
  parser.add_argument('-p', '--proxytunnel', action='store_true', help="Operate through an HTTP proxy tunnel (using CONNECT)")
  parser.add_argument('-U', '--proxy-user', metavar='user:password', help="Proxy user and password")
  parser.add_argument('-e', '--referer', metavar='URL', help="Referrer URL")
  parser.add_argument('-O', '--remote-name', action='store_true', help="Write output to a file named as the remote file") # does by default
  parser.add_argument('--remote-name-all', action='store_true', help="Use the remote file name for all URLs") # does by default
  parser.add_argument('-R', '--remote-time', action='store_true', help="Set the remote file's time on the local output")
  parser.add_argument('--retry', metavar='num', help="Retry request if transient problems occur")
  parser.add_argument('--retry-delay', metavar='seconds', help="Wait time between retries")
  parser.add_argument('-s', '--silent', action='store_true', help="Silent mode")
  parser.add_argument('-Y', '--speed-limit', metavar='speed', help="Stop transfers slower than this")
  parser.add_argument('-3', '--sslv3', action='store_true', help="Use SSLv3")
  parser.add_argument('-1', '--tlsv1', action='store_true', help="Use TLSv1.0 or greater")
  parser.add_argument('--tlsv1.0', action='store_true', help="Use TLSv1.0 or greater")
  parser.add_argument('--tlsv1.1', action='store_true', help="Use TLSv1.1 or greater")
  parser.add_argument('--tlsv1.2', action='store_true', help="Use TLSv1.2 or greater")
  parser.add_argument('-u', '--user', metavar='user:password', help="Server user and password")
  parser.add_argument('-A', '--user-agent', metavar='name', help="Send User-Agent <name> to server")

  parser.add_argument('args', nargs=argparse.REMAINDER, help=argparse.SUPPRESS)
  args = parser.parse_args()
  print(args)

  if (len(args.args) == 0 and args.orig == False and
    (args.output != None or args.remote_name == True  or args.remote_name_all == True) and
    (args.cert_type == None or args.cert_type == "PEM") and
    (args.key_type == None or args.key_type == "PEM") and
    (args.proto_default == None or (args.proto_default == "http" or args.proto_default == "https"))):
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
    if args.key != None:
      cmd.append("--interface")
      cmd.append(args.key)
    if args.limit_rate != None:
      cmd.append("--max-overall-download-limit")
      cmd.append(args.limit_rate)
      cmd.append("--max-overall-upload-limit")
      cmd.append(args.limit_rate)
    if args.netrc_file != None:
      cmd.append("--netrc-path")
      cmd.append(args.netrc_file)
    if args.no_keepalive == True:
      cmd.append("--enable-http-keep-alive=false")
    if args.noproxy != None:
      cmd.append("--no-proxy")
      cmd.append(args.noproxy)
    if args.proto_default != None:
      default_proto = args.proto_default
    if args.proxy != None:
      # check if protocol is mentioned
      proto = ""
      if '://' in proxy:
        # get protocol
        proto = args.proxy.split('://')[0]
        if (proto != "http" or proto != "https"):
          exec_orig()
          sys.exit()
      # proxy-default is http
      url = ""
      if proto == "": # update proxy url
        url = "http://" + args.proxy
      cmd.append("--all-proxy")
      cmd.append(args.noproxy)
    if args.proxy_user != None:
      creds = args.proxy_user.split(":")
      if creds[0] != "":
        cmd.append("--all-proxy-user")
        cmd.append(creds[0])
      if creds[1] != "":
        cmd.append("--all-proxy-passwd")
        cmd.append(creds[1])
    if args.proxytunnel == True:
      cmd.append("--proxy-method=tunnel")
    if args.referer != None:
      cmd.append("--referer")
      cmd.append(args.referer)
    if args.remote_time == True:
      cmd.append("-R=true")
    if args.retry != None:
      cmd.append("-m")
      cmd.append(args.retry)
    if args.retry_delay != None:
      cmd.append("--retry-wait")
      cmd.append(args.retry_delay)
    if args.silent == True:
      cmd.append("-q")
    if args.speed_limit != None:
      cmd.append("--lowest-speed-limit")
      cmd.append(args.speed_limit)
    if args.sslv3 == True:
      cmd.append("--min-tls-version=SSLv3")
    if args.tlsv1 == True:
      cmd.append("--min-tls-version=TLSv1")
    if getattr(args, 'tlsv1.0') == True:
      cmd.append("--min-tls-version=TLSv1")
    if getattr(args, 'tlsv1.1') == True:
      cmd.append("--min-tls-version=TLSv1.1")
    if getattr(args, 'tlsv1.2') == True:
      cmd.append("--min-tls-version=TLSv1.2")
    if args.user != None:
      creds = args.user.split(":")
      if len(creds) != 2:
        exec_orig()
        sys.exit()
      cmd.append("--http-user")
      cmd.append(creds[0])
      cmd.append("--ftp-user")
      cmd.append(creds[0])
      if creds[1] != "":
        cmd.append("--http-passwd")
        cmd.append(creds[1])
        cmd.append("--ftp-passwd")
        cmd.append(creds[1])
    if args.user_agent != None:
      cmd.append("--user-agent")
      cmd.append(args.user_agent)

    if args.header != None:
      for header in args.header:
        # check if file is passed
        if ('@' in args.header):
          exec_orig()
          sys.exit()
        cmd.append("--header")
        cmd.append(header)

    for source in args.source:
      # need to add proto-default stuff here
      cmd.append(source)

    print("Using aria2c:")
    print(cmd)
    subprocess.run(cmd)

  else:
    exec_orig()
