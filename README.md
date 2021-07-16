# egl_probe

Author: Fei Xia (feixia@stanford.edu)

Adapted from (https://github.com/erwincoumans/egl_example).

## Install from pypi

```bash
pip install egl_probe
python -m egl_probe.get_available_devices
```

## Install from source

```bash
pip install -e .
python get_available_devices.py
```

## Example output

```
INFO:root:Device 0 is available for rendering
INFO:root:Device 1 is available for rendering
INFO:root:Device 2 is available for rendering
INFO:root:Device 3 is available for rendering
INFO:root:Graphics Devices: [0, 1, 2, 3]
INFO:root:Graphics Device CUDA Ids: [3, 2, 1, 0]
```

