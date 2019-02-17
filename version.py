import sys

from tensorflow.python.client import device_lib

print(sys.version)
print(device_lib.list_local_devices())
