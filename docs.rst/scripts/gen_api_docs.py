# #
# Copyright 2015-2016 Ghent University
#
# This file is part of EasyBuild,
# originally created by the HPC team of Ghent University (http://ugent.be/hpc/en),
# with support of Ghent University (http://ugent.be/hpc),
# the Flemish Supercomputer Centre (VSC) (https://vscentrum.be/nl/en),
# the Hercules foundation (http://www.herculesstichting.be/in_English)
# and the Department of Economy, Science and Innovation (EWI) (http://www.ewi-vlaanderen.be/en).
#
# https://github.com/easybuilders/easybuild
#
# EasyBuild is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation v2.
#
# EasyBuild is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with EasyBuild.  If not, see <http://www.gnu.org/licenses/>.
# #
"""
Generates API documentation for readthedocs (rst format)
This script requires Sphinx to be installed (http://sphinx-doc.org/index.html).

@author Caroline De Brouwer (Ghent University)
"""
from __future__ import print_function

import os
import subprocess

from easybuild.base.generaloption import simple_option


options = {
    'out_folder': ('Path to folder where api docfiles will be written', 'string', 'store', 'api', 'o'),
    'module': ('Path to module for which api docs will be generated', 'string', 'store', None, 'm')
}
so = simple_option(options)

if so.options.module is None:
    import easybuild
    so.options.module = os.path.dirname(os.path.abspath(easybuild.__file__))

# calls sphinx's automatic apidoc generator
# -o specifies the output folder
# -f forces to overwrite existing files
# -e specifies that every module is written in a separate file
cmd = "sphinx-apidoc -o %s %s -f -e" % (so.options.out_folder, so.options.module)
print("$ %s" % cmd)
subprocess.call(cmd, shell=True)
