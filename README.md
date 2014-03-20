An extremely simple proof of concept implementation of running a GNURadio application with *execnet*, potentially remotely. The remote machine doesn't need to have anything other than a working unmodified GNURadio installation.

The app script *dial_tone.py* had to be modified slightly to add the `__name__ == '__channelexec__'` check.
