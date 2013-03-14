# snoing
### snocave installation method for SNO+. Sno packages fall from the web (sky), i.e. snoing.
```
Usage: snoing.py [options] [package]

  Options:
  --version             show program's version number and exit
  -h, --help            show this help message and exit
  -c CACHE_PATH         Cache path.
  -i INSTALL_PATH       Install path.
  -v                    Verbose Install?
  -a                    All packages?

  Optional Install modes:
    Default snoing action is to install non graphically, i.e. no viewer.
    This can be changed with the -g option.

    -g                  Graphical install?
    -x                  Grid install (NO X11)?

  Optional Actions:
    Default snoing action is to install the specified package, which
    defaults to rat-dev.

    -q                  Query Package Status?
    -r                  Remove the package?
    -d                  Install dependencies only?
    -p                  Progress/update the package?

  Github authentication Options:
    Supply a username or a github token, not both.

    -u USERNAME         Github username
    -t TOKEN            Github token
```
