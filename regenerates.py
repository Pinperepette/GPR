# -*- coding: utf-8 -*-
import sys
import zlib
import PIL.Image
import pyzbar.pyzbar
import base45
import cbor2
from cbor2 import dump, CBORTag, load
import qrcode

def rigenera(part_i, part_u, part_t):
    with open('output.cbor', 'wb') as fp:
        dump(CBORTag(18, [part_i, {}, part_t, part_u]),fp)
    with open('output.cbor', 'rb') as fp:
        obj = load(fp)
    z = zlib.compress(cbor2.dumps(obj))
    out = base45.b45encode(z)
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=6,
        border=1,
    )
    qr.add_data(out)
    qr.make(fit=True)
    img = qr.make_image(fill_color="black", back_color="white")
    img.save("rigenerato.jpeg")

data = pyzbar.pyzbar.decode(PIL.Image.open(sys.argv[1]))
cert = data[0].data.decode()
b45data = cert.replace("HC1:", "")
zlibdata = base45.b45decode(b45data)
cbordata = zlib.decompress(zlibdata)
decoded = cbor2.loads(cbordata)
part_i = decoded.value[0]
part_u = decoded.value[3]
part_t = decoded.value[2]

rigenera(part_i, part_u, part_t)
