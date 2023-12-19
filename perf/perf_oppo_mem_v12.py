import time

from scene.app_store_oppo import OppoScene


def perfScene1(pkg_name):
    t = OppoScene(pkg_name)
    t.stopApp()

    for _ in range(300):
        t.startApp()
        time.sleep(1 / 100)
        t.pressHome()


def perfScene2(pkg_name):
    t = OppoScene(pkg_name)
    t.stopApp()

    for _ in range(300):
        t.startApp()
        time.sleep(1/100)
        t.pressBack()


def perfScene3(pkg_name):
    t = OppoScene(pkg_name)
    t.stopApp()
    t.startApp()
    t.searchPage()
    t.searchWord(word="vpn")
    for _ in range(300):
        t.searchResultDetail()
        time.sleep(1 / 100)
        t.appBack()


def perfScene4(pkg_name):
    t = OppoScene(pkg_name)
    t.stopApp()
    t.startApp()

    for _ in range(300):
        t.searchPage()
        time.sleep(1 / 100)
        t.searchCancel()


def perfScene5(pkg_name):
    t = OppoScene(pkg_name)
    t.stopApp()
    t.startApp()
    t.mePage()
    for _ in range(300):
        time.sleep(1 / 100)
        t.downLoadPage()
        t.pressBack()
        time.sleep(1 / 100)
        t.updatePage()
        t.pressBack()
        time.sleep(1 / 100)


def perfScene6(pkg_name):
    t = OppoScene(pkg_name)
    # t.stopApp()
    # t.startApp()
    t.mePage()
    for _ in range(300):
        time.sleep(1)
        t.downLoadPage()
        time.sleep(1)
        t.pressBack()
        time.sleep(1)
        t.updatePage()
        time.sleep(1)
        t.pressBack()
        time.sleep(1)
        t.mePage()


if __name__ == "__main__":
    perfScene6("com.heytap.market")
