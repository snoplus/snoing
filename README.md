# snoing
### snocave installation method for SNO+. Sno packages fall from the web (sky), i.e. snoing.
```
Usage: snoing.py [options] [package]

Options:
  --version             show program's version number and exit
  -h, --help            show this help message and exit
  -c CACHE_PATH, --cache-path=CACHE_PATH
                        Cache path.
  -i INSTALL_PATH, --install-path=INSTALL_PATH
                        Install path.
  -v, --verbose         Verbose Install?
  -l, --list            List packages, without installing anything.
  -a, --all             All packages?
  -k, --clean           Clean temporary files.

  Optional Install modes:
    Default snoing action is to install non graphically, i.e. no viewer.
    This can be changed with the -g option.

    -g, --graphical     Graphical install?
    -x, --grid          Grid install (NO X11)?

  Optional Actions:
    Default snoing action is to install the specified package, which
    defaults to rat-dev.

    -q, --query         Query Package Status?
    -r, --remove        Remove the package?
    -d, --dependency    Install dependencies only?
    -p, --progress, --update
                        Progress/update the package?

  Github authentication Options:
    Supply a username or a github token, not both.

    -u USERNAME, --username=USERNAME
                        Github username
    -t TOKEN, --token=TOKEN
                        Github token
```
