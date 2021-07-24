#!/usr/bin/env python
# -*- coding: utf-8 -*-
import sys, zlib, PIL.Image, base45, cbor2, pyzbar.pyzbar,rich
rich.print (cbor2.loads(cbor2.loads(zlib.decompress(base45.b45decode(pyzbar.pyzbar.decode(PIL.Image.open(sys.argv[1]))[0].data.decode().replace("HC1:", "")))).value[2]))
