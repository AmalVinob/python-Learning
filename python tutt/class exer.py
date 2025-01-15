class electronic_device:
    device = "these are the electronic devices"
    def elc(self):
        return f"{device}"
class pocket_gadget(electronic_device):
    device = "an electronic device"
    return f"this is also {device}"

class phone(pocket_gadget):
    device = "small electronic device"
    return f"this is a {device}"

mixer = electronic_device()
tablet = pocket_gadget()
mobile = phone()

print(mobile.)