# Author: Maria Emilia Ramirez Gomez
# Year: 2024
# License: MIT License
#
# This code is released under the MIT License. See the LICENSE file for more details.

import os
import pyudev
import subprocess as sp

class USBManager:
    def __init__(self):
        self.context = pyudev.Context()
        self.monitor = pyudev.Monitor.from_netlink(self.context)
        self.monitor.filter_by(subsystem="block", device_type="partition")
        self.flag = True

        return
    
    def autoMount(self, path):
        args = ["udisksctl", "mount", "-b", path]
        sp.run(args)

        return 
    
    def autoUnmount(self, path):
        args = ["udisksctl", "unmount", "-b", path]
        sp.run(args)

        return
    
    def getMountPoint(self, path):
        args = ["findmnt", "-unl", "-S", path]
        cp = sp.run(args, capture_output=True, text=True)
        out = cp.stdout.split(" ")[0]

        return out
    
    def usbDetection(self):
        mountPoint = None

        while self.flag:

            device = self.monitor.poll(timeout=1)
            if device is None:
                continue
            else:
                action = device.action

                if action != "add":
                    print(self.flag)
                    continue

                devicePath = "/dev/" + device.sys_name
                self.autoMount(devicePath)
                mountPoint = self.getMountPoint(devicePath)
                self.flag = False

        return mountPoint
