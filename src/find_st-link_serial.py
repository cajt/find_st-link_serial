#!/usr/bin/python3.5
#
# Copyright (c) 2017 Carl Treudler
# For licensing see LICENSE in repository. (MIT license)
#
# Scan USB for STlink V2 and V2.1 JTAG Adapters, and shows their SNs in a
# format suitable for use with OpenOCD.
# This tool will help you setup a worklfow for embedded projects using multiple
# STlinks simultaneously.
#
# install python libusb1 with:
#  pip3 install libusb1
#
# TODO: Test with more Boards
#
# Tested with:
# - STM32f429-Discovery
# - STM32f4-Discovery
# - STM32f401C-Disco
# - Nucleo-F429ZI

import usb1
def main():
    with usb1.USBContext() as context:
        for device in context.getDeviceIterator(skip_on_error=True):
            if (device.getVendorID(), device.getProductID()) == (0x0483,0x3748) or \
            (device.getVendorID(), device.getProductID()) == (0x0483,0x374b):
                print('%s (%04x:%04x)' % (device.getProduct(), device.getVendorID(), device.getProductID()) )
                oos=""
                try:
                    sn=device.getSerialNumber()
                    for x in sn:
                        oos +="\\x%02x"%ord(x)
                    print("hls_serial \""+sn+"\"")  # this was the easy before, but we print it anyways
                    print("hls_serial \""+oos+"\"") # everything escaped and ready for OpenOCD's tcl scripts
                except:
                    pass

if __name__ == '__main__':
    main()
