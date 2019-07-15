
# aria2c-for-wget-curl
Stubs of wget and curl for aria2c to download large files using Debian alternatives subsystem instead of changing the shell scripts.

## Instructions for setup
### Wget
* Rename original wget to wget-orig
```console
$ sudo cp /usr/bin/wget /usr/bin/wget-orig
```
* Copy the downloaded wget as wget-stub
```console
$ sudo cp ~/path/to/wget-stub /usr/bin/wget-stub
```
* Use update-alternatives to set default binary
 ```console
$ sudo update-alternatives --install /usr/bin/wget wget /usr/bin/wget-orig 30
update-alternatives: using /usr/bin/wget-orig to provide /usr/bin/wget (wget) in auto mode
$ sudo update-alternatives --install /usr/bin/wget wget /usr/bin/wget-stub 40
update-alternatives: using /usr/bin/wget-stub to provide /usr/bin/wget (wget) in auto mode
```
* Verify that wget-stub is default
 ```console
$ sudo update-alternatives --config wget
There are 2 choices for the alternative wget (providing /usr/bin/wget).

    Selection Path Priority Status

  ------------------------------------------------------------

  * 0 /usr/bin/wget-stub 40 auto mode

    1 /usr/bin/wget-orig 30 manual mode

    2 /usr/bin/wget-stub 40 manual mode
Press <enter> to keep the current choice[*], or type selection number:
```

* The setup is ready, try using wget now.

## Note
* If command cannot be translated to aria2c equivalent, then falls back the the corresponding program.
* Use --orig flag to use the original program.
* curl-stub is WIP.
* .curlrc is not supported as of now

### Curl
* only files are supported for --cookie flag

## Screenshots
![wget-aria2c](https://raw.githubusercontent.com/SaiHarshaK/aria2c-for-wget-curl/master/wget/screenshots/wget-aria.png)
![wget-orig](https://raw.githubusercontent.com/SaiHarshaK/aria2c-for-wget-curl/master/wget/screenshots/wget-orig.png)
