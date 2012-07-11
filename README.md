# snoing
### snocave installation method for SNO+. Sno packages fall from the web (sky), i.e. snoing.

To run source the env.sh file then run snoing. An example argument would be:

    ./snoing rat-3

This has the following options:

    Usage: snoing.py [options] [package]
    
    Options:
      --version       show program's version number and exit
      -h, --help      show this help message and exit
      -c CACHEPATH    Cache path.
      -i INSTALLPATH  Install path.
      -g              Graphical install?
      -q              Query Package Status?
      -r              Remove the package instead?
      -d              Dependencies only?
      -v              Verbose Install?
      -u USERNAME     Github username (for rat releases)
      -p PASSWORD     Github password (for rat releases)
