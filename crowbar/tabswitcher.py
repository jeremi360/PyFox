import os #, sys
#sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..'))
import grabbo
import crowbar

r = os.path.realpath(__file__)
r = os.path.dirname(r)
r = os.path.dirname(r)

TabS_UI = os.path.join(r, "ui", "TabSwitcher.xml")
class TabSwitcher (grabbo.Builder):
    def __init__(self, notebook, webviewcontiner):
        grabbo.Builder.__init__(self, TabS_UI)
        self.button = self.ui.get_object("button")
        self.removeB = self.ui.get_object("RemoveButton")

        self.webviewcontiner = webviewcontiner
        self.notebook = notebook

        self.button.connect("toggled", self.on_tab)
        self.removeB.connect("clicked", self.on_remove)

    def get(self):
        return self.ui.get_object("box")

    def join_group(self, group):
        self.button.join_group(group)

    def get_group(self):
        return self.button

    def set_label(self, label):
        self.button.set_label(label)

    def get_image(self):
        return self.button.get_image()

    def set_tooltip(self, tooltip):
        self.button.set_tooltip_text(tooltip)

    def get_num(self):
        return self.notebook.page_num(self.webviewcontiner)

    def on_tab(self, button):
        self.notebook.set_current_page(self.get_num())
        self.notebook.tabcontrols.set_webview(self.webviewcontiner.webview)

    def on_remove(self, button):
        #trashList = open(crowbar.trashFile, 'rb')
        #trashList.append(self.webviewcontiner)

        self.notebook.remove_page(self.get_num())
        self.notebook.maincotrols.TabsSwitcher.remove(self.get())
        self.notebook.auto_show_switcher()
        self.notebook.maincotrols.auto_set_TabSwitcher_width()

