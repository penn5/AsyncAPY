# AsyncAPY - A fully fledged Python 3.6+ library to serve APIs asynchronously
# Copyright (C) 2019-2020 Nocturn9x <https://github.com/nocturn9x>
#
# This file is part of AsyncAPY.
#
# AsyncAPY is free software: you can redistribute it and/or modify
# it under the terms of the GNU Lesser General Public License as published
# by the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# AsyncAPY is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU Lesser General Public License for more details.
#
# You should have received a copy of the GNU Lesser General Public License
# along with AsyncAPY.  If not, see <http://www.gnu.org/licenses/>.

import setuptools
import os
import subprocess
import sys

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="AsyncAPY",
    version="0.2.3",
    author="Mattia Giambirtone aka Nocturn9x",
    author_email="nocturn9x@intellivoid.info",
    description="A fully fledged Python 3.6+ library to serve APIs asynchronously",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/nocturn9x/AsyncAPY",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "Operating System :: OS Independent",
        "License :: OSI Approved :: GNU Lesser General Public License v3 (LGPLv3)"
    ],
    install_requires=[
        "ziproto @ git+https://github.com/Netkas/ZiProto-Python"
    ],
    python_requires='>=3.6',
)
