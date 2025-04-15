# MIT License
#
# Copyright (c) 2025 Keisuke Sehara
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in all
# copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.

from typing import Tuple
from pathlib import Path
from dataclasses import dataclass
from argparse import ArgumentParser
import sys
import subprocess as sp

DESCRIPTION = "installs packages required to run a set of functionalities."
USAGE = """
%(prog)s [--help|--no-install|--no-external-deps] [FEATURE[, FEATURE[, ...]]]

FEAURE may be one of ('core', 'atlas', 'video', 'browse', 'all'):

- 'core': the core functionality required for NWB file generation.
- 'atlas': the atlas-registration functionality.
- 'video': the video-related functionality (currently only including pupil-fitting).
- 'browse': the functionality for browsing the resulting NWB files.
- 'all': all functionalities of the above.
"""
EPILOG = ""


@dataclass
class Feature:
    directory: str
    names: Tuple[str]

    def package_paths(self, root: Path) -> Tuple[Path]:
        return tuple(str(root / self.directory / name) for name in self.names)


FEATURES = dict(
    core=Feature(
        directory='pipeline-core',
        names=(
            'bdbc-session-explorer',
            'bdbc-nwb-packager',
        ),
    ),
    atlas=Feature(
        directory='atlas-registration',
        names=(
            'ks-affine2d',
            'ks-affine-aligner',
            'ks-mesoscaler',
            'bdbc-atlas-registration',
        ),
    ),
    video=Feature(
        directory='video-tracking',
        names=(
            'ks-pupilfitting',
        ),
    ),
    browse=Feature(
        directory='repository-browsing',
        names=(
            'bdbc-nwb-explorer',
        ),
    )
)


# additional dependencies
# that may require some extra care
DEPENDENCIES = dict(
    core=(),
    atlas=('numpy<2', 'deeplabcut[tf]==2.3.10',),
    video=(),
    browse=(),
)


INTERDEPS = dict(
    core=(),
    atlas=('core',),
    video=(),
    browse=(),
)


parser = ArgumentParser(
    description=DESCRIPTION,
    usage=USAGE,
    epilog=EPILOG,
)
parser.add_argument(
    'features', nargs='*', metavar='FEATURE',
    help="specifies which feature(s) to be installed. without any specification, 'all' will be used.",
)
parser.add_argument(
    '--no-install', '-n', action='store_true', dest='no_install',
    help="lists up what will be installed, without actually installing them",
)
parser.add_argument(
    '--no-external-deps', '-x', action='store_true', dest='no_deps',
    help="attempts to install packages without installation of their external dependencies",
)


def install_packages(
    features,
    no_deps: bool = False,
    no_install: bool = False,
):
    if ('all' in features) or (len(features) == 0):
        features = tuple(FEATURES.keys())
    installed = list(features)
    extra = []
    root = Path()
    for f in features:
        if f not in FEATURES.keys():
            raise ValueError(f"unknown feature '{f}'")
        for dep in INTERDEPS[f]:
            if dep not in installed:
                installed.append(dep)
        if not no_deps:
            for dep in DEPENDENCIES[f]:
                if dep not in extra:
                    extra.append(dep)
    packages = tuple(extra) + sum(
        (FEATURES[f].package_paths(root) for f in installed),
        start=()
    )

    if no_install:
        for pkg in packages:
            print(pkg)
    else:
        python = sys.executable
        cmd = [python, '-m', 'pip', 'install'] + list(packages)
        ret = sp.run(cmd)
        if ret.returncode != 0:
            print(f"***error installing feature: {tuple(features)}")
            sys.exit(ret.returncode)


if __name__ == '__main__':
    args = parser.parse_args()
    install_packages(**vars(args))
