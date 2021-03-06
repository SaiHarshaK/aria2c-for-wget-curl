# aria2c-for-wget-curl
Stubs of wget and curl for aria2c to download large files using Debian alternatives subsystem instead of changing the shell scripts.
aria2c is better when compareed to wget/curl because it tries to utilize your maximum download bandwidth.
Since, changing shell scripts from wget/curl to equivalent aria2c cli takes time, this stub translates the wget/curl command to equivalent aria2c command and executes it.
If not possible to do so, it executes the original command.

## Instructions for setup
* Install aria2c
* Install wget and(or) curl

### Wget
* Copy original wget to wget-orig
```console
$ sudo cp /usr/bin/wget /usr/bin/wget-orig
```
* Install the aria2stub package.
```console
$ pip3 install aria2stub
```
Now `wget` command runs the stub as default for the current user.

##### (BELOW STEPS ARE OPTIONAL) Make all users execute the stub by default.
* Move the installed binary(default=/usr/local/bin/) to /usr/bin/.
```console
$ sudo mv /usr/local/bin/wget /usr/bin/wget-stub
```
* Use update-alternatives to set default binary.
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

### Curl
* Copy original curl to curl-orig
```console
$ sudo cp /usr/bin/curl /usr/bin/curl-orig
```
* Install the aria2stub package.
```console
$ pip3 install aria2stub
```
Now `curl` command runs the stub as default for the current user.

##### (BELOW STEPS ARE OPTIONAL) Make all users to execute the stub by default.
* Move the installed binary(default=/usr/local/bin/) to /usr/bin/.
```console
$ sudo cp /usr/local/bin/curl /usr/bin/curl-stub
```
* Use update-alternatives to set default binary
 ```console
$ sudo update-alternatives --install /usr/bin/curl curl /usr/bin/curl-orig 30
update-alternatives: using /usr/bin/curl-orig to provide /usr/bin/curl (curl) in auto mode
$ sudo update-alternatives --install /usr/bin/curl curl /usr/bin/curl-stub 40
update-alternatives: using /usr/bin/curl-stub to provide /usr/bin/curl (curl) in auto mode
```
* Verify that curl-stub is default
 ```console
$ sudo update-alternatives --config curl
There are 2 choices for the alternative curl (providing /usr/bin/curl).

    Selection Path Priority Status

  ------------------------------------------------------------

  * 0 /usr/bin/curl-stub 40 auto mode

    1 /usr/bin/curl-orig 30 manual mode

    2 /usr/bin/curl-stub 40 manual mode
Press <enter> to keep the current choice[*], or type selection number:
```

* The setup is ready, try using curl now.

## Note
* If command cannot be translated to aria2c equivalent, then it falls back to the corresponding program.
* Use --orig flag to use the original program.
* .curlrc is not supported as of now
* To revert back to using the original command(if followed optional approach), run the following command for wget(similarly for curl):
 ```console
$ sudo update-alternatives --config wget
```

### Curl
* only files are supported for --cookie flag

## Screenshots
![wget-aria2c](https://raw.githubusercontent.com/SaiHarshaK/aria2c-for-wget-curl/master/wget/screenshots/wget-aria.png)
![wget-orig](https://raw.githubusercontent.com/SaiHarshaK/aria2c-for-wget-curl/master/wget/screenshots/wget-orig.png)
