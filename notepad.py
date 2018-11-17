import subprocess as sp
import time
from pywinauto.application import Application

class notepad():

    app = Application()

    # This will open a blank notepad file
    def Open_Blank_Notepad(self):
        self.app.start("Notepad.exe")

    # This will write on existing notepad file
    def Write_To_Notepad(self, text, filename):
        sp.Popen(["notepad.exe", filename])
        time.sleep(2)
        self.app = self.app.connect(title_re=".*" + filename)
        self.app.window(title_re=".*Notepad").Edit.type_keys(text, with_spaces=True)

    # This will save existing notepad file
    def Save_Existing_Notepad(self, filename):
        self.app = self.app.connect(title_re=".*" + filename)
        self.app.window(title_re=".*Notepad").menu_select("File->Save")

    # This will save new notepad file
    def Save_New_Notepad(self, filename):
        self.app = self.app.connect(title_re=".*" + filename)
        self.app.window(title_re=".*Notepad").menu_select("File->SaveAs")
        self.app.SaveAs.edit1.set_edit_text(filename+'.txt')
        self.app.SaveAs.Save.click()

    # This will close notepad
    def Close_Notepad(self):
        self.app = self.app.connect(title_re=".*Notepad")
        self.app.window(title_re=".*Notepad").menu_select("File->Exit")
