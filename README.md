# beets-rgain

An alternative to the [Beets](http://beets.radbox.org/) `replaygain` plugin
that supports more formats (including Vorbis and FLAC). Uses
[rgain](https://bitbucket.org/fk/rgain).

## TODO

* Figure out a way to name the plugin `rgain` while still being able to import
  `rgain.rgcalc` without `ImportError: No module named rgcalc`.

* Figure out why importing from `rgain` replaces the `beet --help` output with
  the GStreamer help. ಠ\_ಠ

* Add a `beet` subcommand.

* Make forcing and the reference level configurable.

* Contribute the plugin to beets.
