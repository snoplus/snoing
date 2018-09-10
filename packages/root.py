#!/usr/bin/env python
#
# Root
#
# The root package installers
#
# Author P G Jones - 12/05/2012 <p.g.jones@qmul.ac.uk> : First revision
# Author P G Jones - 13/05/2012 <p.g.jones@qmul.ac.uk> : Added 5.32, 5.28, 5.24 versions (rat v3, v2, v1)
#        O Wasalski - 13/06/2012 <wasalski@berkeley.edu> : Building python module
# Author P G Jones - 22/09/2012 <p.g.jones@qmul.ac.uk> : Major refactor of snoing.
# Author K E Gilje - 10/09/2018 <gilje@ualberta.ca> : Allow use of local version of cmake.
####################################################################################################

from distutils.version import StrictVersion
import installmode
import os
import re
import system

from localpackage import LocalPackage


class Root(LocalPackage):
    """Base root installer, different versions only have different names."""

    def __init__(self, name, system, tar_name):
        """Initialise the root package."""
        super(Root, self).__init__(name, system)
        self._src_path = self.get_install_path() + '_source'
        self._tar_name = tar_name
        self._fftw_version = '3.3.4'
        self._gsl_version = '1.16'
        self._xrootd_version = '4.3.0'

    def get_dependencies(self):
        """Return the dependency names as a list of names."""

        deps = ['make', 'g++', 'gcc', 'ld', 'cmake-2.8.12',
                'fftw-%s' % self._fftw_version,
                'gsl-%s' % self._gsl_version,
                'python', ['python-dev', 'python-dev-2.4', 'python-dev-2.6']]

        if self._system.get_install_mode() == installmode.Grid:
            return deps + ['xrootd-%s' % self._xrootd_version]
        return deps + ['X11', 'Xpm', 'Xft', 'Xext']

    def _is_downloaded(self):
        """Check the tar ball has been downloaded."""
        return self._system.file_exists(self._tar_name)

    def _is_installed(self):
        """Check if root is installed."""
        if self._system.get_install_mode() == installmode.Grid:  # no X11, no bit/root
            return self._system.file_exists('root.exe', os.path.join(self.get_install_path(), 'bin'))
        else:
            return os.path.exists(os.path.join(self.get_install_path(), 'bin', 'root'))

    def _download(self):
        """Download from cern."""
        self._system.download_file('https://root.cern.ch/download/' + self._tar_name)

    def _configuration_args(self):
        """Return configuration arguments."""

        args = ['-Dminuit2:BOOL=ON', '-Droofit:BOOL=ON', '-Dpython:BOOL=ON', '-Dmathmore:BOOL=ON',
                '-Dfortran:BOOL=OFF',
                '-Dfftw3:BOOL=ON', '-DFFTW_DIR:PATH=%s' \
                    % os.path.join(self._system.get_install_path(), 'fftw-%s' % self._fftw_version),
                '-Dgsl_shared:BOOL=ON', '-DGSL_DIR:PATH=%s' \
                    % os.path.join(self._system.get_install_path(), 'gsl-%s' % self._gsl_version)]

        if self._system.get_install_mode() == installmode.Grid:
            return args + ['-Dcaster:BOOL=OFF', '-Drfio:BOOL=OFF', '-Dx11:BOOL=OFF', '-Dgfal:BOOL=OFF',
                           '-Dxrootd:BOOL=ON', '-DXROOTD_ROOT_DIR:PATH=%s' \
                               % os.path.join(self._system.get_install_path(), 'xrootd-%s' % self._xrootd_version)]
        return args + ['-Dgdml:BOOL=ON']

    def _install_setup(self):
        """Extract the files to install."""
        self._system.untar_file(self._tar_name, self._src_path, 1)

    def _install(self):
        """Install root."""
        self._install_setup()
        self._system.build_path(self.get_install_path())
        self._system._arguments['root'].append(self._src_path)  # ensure path is at the very end

        # Check if cmake was installed locally, if so, add to path
        if self._dependency_paths['cmake-2.8.12'] is not None: # Special cmake installed
            try:
                location = self._system.execute_command("which",  ["cmake"])
            except:
                os.environ["PATH"] += os.pathsep + "%s/bin" % self._dependency_paths['cmake-2.8.12']

        # Run the cmake command
        self._system.configure_command(
            command='cmake', args=self._configuration_args(),
            cwd=self.get_install_path(), config_type='root')
        self._system.execute_command('make', cwd=self.get_install_path())

        if self._system.get_install_mode() == installmode.Grid:
            shutil.rmtree(self._src_path)


class RootWithConfigure(Root):
    """Install older versions of ROOT with configure/make; ROOT < v5.30/00."""

    def get_dependencies(self):
        """Return the dependency names as a list of names."""

        # remove CMake from dependencies
        deps = super(RootWithConfigure, self).get_dependencies()
        return [dep for dep in deps
                if not ('cmake' in dep or any('cmake' in d for d in dep))]


    def _configuration_args(self):
        """Return configuration arguments."""

        args = ['--enable-minuit2', '--enable-roofit', '--enable-python', '--enable-mathmore',
                '--with-fftw3-incdir=%s' \
                    % os.path.join(self._system.get_install_path(), 'fftw-%s' % self._fftw_version, 'include'),
                '--with-fftw3-libdir=%s' \
                    % os.path.join(self._system.get_install_path(), 'fftw-%s' % self._fftw_version, 'lib'),
                '--with-gsl-incdir=%s' % os.path.join(self._system.get_install_path(),
                    'gsl-%s' % self._gsl_version, 'include'),
                '--with-gsl-libdir=%s' \
                    % os.path.join(self._system.get_install_path(), 'gsl-%s' % self._gsl_version, 'lib')]

        if self._system.get_install_mode() == installmode.Grid:
            return args + ['--disable-castor', '--disable-rfio', '--disable-x11', '--disable-gfal',
                           '--with-xrootd=%s' \
                               % os.path.join(self._system.get_install_path(), 'xrootd-%s' % self._xrootd_version)]
        return args + ['--enable-gdml']

    def _install_setup(self):
        """Extract the files to install."""
        self._system.untar_file(self._tar_name, self.get_install_path(), 1)

    def _install(self):
        """Install root."""
        self._install_setup()
        self._system.configure_command(
            args=self._configuration_args(),
            cwd=self.get_install_path(),
            config_type='root')
        self._system.execute_command('make', cwd=self.get_install_path())


class RootDevelopment(Root):
    """Base root installer for development versions."""

    def __init__(self, name, system):
        """Initialise the root package"""
        super(RootDevelopment, self).__init__(name, system, None)

    def _is_downloaded(self):
        """Check if git directory exists."""
        return os.path.exists(self.get_install_path())

    def _download(self):
        """Git clone ROOT."""
        git_version = self._system.execute_command('git', ['--version'])
        git_version = re.search(r'(\d+\.*)+', git_version).group()
        git_version = StrictVersion(git_version)
        single_branch = ''
        if git_version >= StrictVersion('1.7.10'):
            single_branch = '--single-branch'

        self._system.execute_command('git', ['clone', '-b', 'v5-34-00-patches', single_branch,
                                             'http://root.cern.ch/git/root.git', self._src_path],
                                     verbose=True)

    def _install_setup(self):
        """Override with NOOP: already on needed branch."""
        pass

    def _update(self):
        """Update ROOT 5 development."""
        command_text = '#!/bin/bash\ncd %s\ngit checkout v5-34-00-patches\ngit fetch\ngit reset --hard FETCHHEAD' \
                % self._src_path
        self._system.execute_complex_command(command_text, verbose=True)
        self.install()
