import uiautomator2 as u2


class Device:
    def __init__(self):
        self.device = u2.connect()
        # print(self.device.app_info("com.applovin.array.apphub.samsung"))
        self.pkg_name = ""
    def getDeviceInfo(self):
        print(self.device.app_list())
        return self.device.info

    def getDevice(self):
        return self.device


device = Device().getDevice()


if __name__ == "__main__":
    pass
