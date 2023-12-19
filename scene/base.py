from device.android_device import device as d


class SceneBase(object):
    def __init__(self, pkg_name):
        self.pkgName = pkg_name

    def stopApp(self):
        d.app_stop(self.pkgName)

    def startApp(self):
        d.app_start(self.pkgName, wait=True)

    def pressBack(self):
        d.press("back")

    def pressHome(self):
        d.press("home")
