#!/usr/bin/env python
# -*- coding: utf-8 -*-
from __future__ import print_function
import os
import hy
import sys
import zipfile
import argparse

__version__ = '0.1.0'


def compile_hy(target):
    hy.importer.write_hy_as_pyc(target)
    with open(target.replace('.hy', '.pyc'), 'rb') as f:
        pyc_src = f.read()
    os.remove(target.replace('.hy', '.pyc'))
    return os.path.basename(target).replace('.hy', '.pyc'), pyc_src


def make_hyapp(main, output, *targets):
    targets += (main, )
    with zipfile.ZipFile(output, 'w') as zf:
        for target in targets:
            if not os.path.exists(target):
                raise IOError('File does not exist: {}'.format(target))
            ext = os.path.splitext(target)[-1]
            if ext == '.hy':
                fname, src = compile_hy(target)
                zf.writestr(fname, src)
                print('compile: {}'.format(target))
            else:
                raise IOError('Invalid file format: {}'.format(ext))
        print('creating executable archive...')
        ext = os.path.splitext(main)[-1]
        if ext == '.hy':
            _, main_src = compile_hy(main)
            zf.writestr('__main__.pyc', main_src)
        else:
            raise IOError('Invalid file format: {}'.format(ext))

    with open(output, 'rb') as f:
        tmp = f.read()
    with open(output, 'wb') as f:
        f.write(b'#!/usr/bin/env python\n')
        f.write(tmp)
    os.chmod(output, 0o755)


def main():
    prog = os.path.basename(sys.argv[0])
    parser = argparse.ArgumentParser(
        prog=prog,
        usage='%(prog)s [options] <targets>',
        add_help=False,
        formatter_class=argparse.RawTextHelpFormatter)
    parser._optionals.title = 'options'

    # def error(self, *args):
    #     parser.print_usage(sys.stderr)
    #     parser.exit(2, 'try \'{} --help\'\n'.format(prog))

    # parser.error = error

    parser.add_argument(
        "-o", metavar="file", nargs='?', default="a", help="output name")
    parser.add_argument("main", help=argparse.SUPPRESS)
    parser.add_argument("file", nargs='*', help=argparse.SUPPRESS)
    parser.add_argument(
        "--version",
        action="version",
        version="%(prog)s {}".format(__version__))
    parser.add_argument(
        '--help', action='help', help='show this message and exit\n')

    ops = parser.parse_args()
    make_hyapp(ops.main, ops.o, *ops.file)
