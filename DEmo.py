from breezypythongui import EasyFrame
class DemoGUI(EasyFrame):
    def __init__(self):
        EasyFrame.__init__(self,title="GUI Demo")

        self.label=self.addLabel(text="Python GUI Demo",row=0,column=0,columnspan=2,sticky="NSEW")
        self.clearButton=self.addButton(text="Clear",row=1,column=0,command=self.clearLabel)
        self.restoreButton=self.addButton(text="Restore",row=1,column=1,command=self.restoreLabel)
        self.restoreButton["state"]="disabled"

    def clearLabel(self):
        self.label["text"]=""
        self.clearButton["state"]="disabled"
        self.restoreButton["state"]="normal"

    def restoreLabel(self):
        self.label["text"]="Python GUI Demo"
        self.clearButton["state"]="normal"
        self.restoreButton["state"]="disabled"

if __name__=="__main__":
    DemoGUI().mainloop()
