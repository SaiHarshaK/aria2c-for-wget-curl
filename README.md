
# aria2c-for-wget-curl
Stubs of wget and curl for aria2c to download large files using Debian alternatives subsystem instead of changing the shell scripts.

## Instructions
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
