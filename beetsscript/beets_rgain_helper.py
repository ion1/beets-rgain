#!/usr/bin/env python
# coding=utf-8

# beets-rgain – A replay gain plugin for Beets
#
# Copyright © 2013 Johan Kiviniemi <devel@johan.kiviniemi.name>
#
# Permission to use, copy, modify, and/or distribute this software for any
# purpose with or without fee is hereby granted, provided that the above
# copyright notice and this permission notice appear in all copies.
#
# THE SOFTWARE IS PROVIDED "AS IS" AND THE AUTHOR DISCLAIMS ALL WARRANTIES
# WITH REGARD TO THIS SOFTWARE INCLUDING ALL IMPLIED WARRANTIES OF
# MERCHANTABILITY AND FITNESS. IN NO EVENT SHALL THE AUTHOR BE LIABLE FOR
# ANY SPECIAL, DIRECT, INDIRECT, OR CONSEQUENTIAL DAMAGES OR ANY DAMAGES
# WHATSOEVER RESULTING FROM LOSS OF USE, DATA OR PROFITS, WHETHER IN AN
# ACTION OF CONTRACT, NEGLIGENCE OR OTHER TORTIOUS ACTION, ARISING OUT OF
# OR IN CONNECTION WITH THE USE OR PERFORMANCE OF THIS SOFTWARE.

from rgain import rgcalc
import sys
import yaml

def main():
    req = yaml.load(sys.stdin)

    paths   = req['paths']
    force   = req['force']
    ref_lvl = req['ref_lvl']

    (tracks_rg, album_rg) = \
        rgcalc.calculate(paths, force=force, ref_lvl=ref_lvl)

    res = {
        'tracks': tracks_rg,
        'album':  album_rg,
    }

    yaml.dump(res, sys.stdout)

if __name__ == '__main__':
    main()
