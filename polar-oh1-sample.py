import hid


for device in hid.enumerate(0, 0):
    prod = device['product_string']
    print(prod)
    if "Polar" in prod:
        vid = device["vendor_id"]
        pid = device["product_id"]


polar = hid.Device(vid, pid)

polar.open()

# hogehoge

polar.close()
