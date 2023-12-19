import time
from device.android_device import device as d
from scene.base import SceneBase


class OppoScene(SceneBase):

    def getDevice(self):
        return d
    def mePage(self):
        d(resourceId=self.pkgName + ":id/iv_nav_3").click()

    def downLoadPage(self):
        d(resourceId=self.pkgName + ":id/card_download").click()

    def updatePage(self):
        d(resourceId=self.pkgName + ":id/card_updates").click()

    def appBack(self):
        d(resourceId=self.pkgName + ":id/backImage").click()

    def searchPage(self):
        d(resourceId=self.pkgName + ":id/search_bar").click()

    def searchCancel(self):
        d(resourceId=self.pkgName + ":id/tv_cancel").click()

    def searchWord(self,word):
        d.send_keys(word, clear=True)

    def searchResult(self):
        print(d.xpath('//*[@resource-id="com.heytap.market:id/search_results"]').all())

    def searchResultDetail(self):
        d.xpath('//*[@resource-id="com.heytap.market:id/search_results"]/android.view.ViewGroup[1]/android.view.ViewGroup[1]').click()

    def swipe(self) -> None:
        d.swipe(100, 800, 100, 600, 50)
        d.swipe(100, 600, 100, 800, 50)



if __name__ == "__main__":
    d.app_stop("com.heytap.market")
    t = OppoScene("com.heytap.market")
    t.startApp()
    time.sleep(2)
    t.searchPage()
    t1 = time.perf_counter()
    t.searchResult()
    time.sleep(2)
    t.searchWord("vpn")
    t.searchResult()
    print(f'coast:{time.perf_counter() - t1:.8f}s')
