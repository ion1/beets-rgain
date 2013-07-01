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

from beets.plugins import BeetsPlugin
from beets.util import displayable_path, syspath
import logging
import subprocess
import yaml

log = logging.getLogger('beets')

# TODO: Make these configurable.
FORCE   = True
REF_LVL = 89

class RGainPlugin(BeetsPlugin):
    def __init__(self):
        super(RGainPlugin, self).__init__()
        self.import_stages = [self.imported]

    def imported(self, session, task):
        lib = session.lib
        if task.is_album:
            self.album_imported(lib, lib.get_album(task.album_id))
        else:
            self.item_imported(lib, task.item)

    def album_imported(self, lib, album):
        tracks_rg, album_rg = self.calculate_items(album.items())

        self.update_album(lib, album, album_rg)
        self.update_items(lib, album.items(), tracks_rg)

    def item_imported(self, lib, item):
        tracks_rg, album_rg = self.calculate_items([item])

        # store will be called by update_items.
        item.rg_album_gain = None
        item.rg_album_peak = None

        self.update_items(lib, [item], tracks_rg)

    def calculate_items(self, items):
        paths = [ syspath(item.path) for item in items ]

        req = {
            'force':   FORCE,
            'ref_lvl': REF_LVL,
            'paths':   paths,
        }

        cmd = ["beets_rgain_helper"]
        p = subprocess.Popen(cmd,
                             stdin=subprocess.PIPE,
                             stdout=subprocess.PIPE)

        yaml.dump(req, p.stdin)
        p.stdin.close()

        res = yaml.load(p.stdout)

        ret = p.wait()
        if ret != 0:
            raise subprocess.CalledProcessError(returncode=ret, cmd=cmd)

        return (res['tracks'], res['album'])

    def update_album(self, lib, album, rg):
        album.rg_album_gain = rg.gain
        album.rg_album_peak = rg.peak

        log.debug(u'rgain: album %d: gain=%.2f peak=%.8f' %
                  (album.id, rg.gain, rg.peak))

    def update_items(self, lib, items, rg_dict):
        for item in items:
            rg = rg_dict[syspath(item.path)]

            item.rg_track_gain = rg.gain
            item.rg_track_peak = rg.peak

            lib.store(item)

            log.debug(u'rgain: item %d %s: gain=%.2f peak=%.8f' %
                      (item.id, displayable_path(item.path), rg.gain, rg.peak))
