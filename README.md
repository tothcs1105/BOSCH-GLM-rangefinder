# BOSCH-Rangefinder

Python3 script to remote control a BOSCH GLM 100C or GLM 50C rangefinder.

This script provides remote control features for the BOSCH GLM 100C/50C measuring device via its Bluetooth serial interface. The device uses the transfer protocol as described [in this blog post](https://www.eevblog.com/forum/projects/hacking-the-bosch-glm-20-laser-measuring-tape/msg1331649/#msg1331649).

## Dependencies

The script was only tested on Windows. But since the Python module used is multi-platform, it should also support Linux and MacOS. See [pybluez](https://github.com/pybluez/pybluez) for further information.

Install `pybluez` for the Python3 interpreter via `pip`:

```bash
pip3 install pybluez
```
