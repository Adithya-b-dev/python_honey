

from breezypythongui import EasyFrame
class TempConvert(EasyFrame):
    def __init__(self):
        EasyFrame.__init__(self,title="Temperature Converter")

        self.addLabel(text="Temperature in Celsius: ",row=0,column=0)
        self.celsiusField=self.addFloatField(value=0.0,row=0,column=1)

        self.addLabel(text="Temperature in Fahrenheit: ",row=1,column=0)
        self.fahrenheitField=self.addFloatField(value=0.0,row=1,column=1,precision=2)
        self.fahrenheitField["state"]="readonly"
        
        self.convertButton=self.addButton(text="Convert to Fahrenheit",row=2,column=0,columnspan=2,command=self.convert)

    def convert(self):
        try:
            celsius=self.celsiusField.getNumber()
            fahrenheit=(celsius*9/5)+32
            self.fahrenheitField.setNumber(round(fahrenheit,2))

        except Exception:
            self.messageBox(title="Invalid Input",message="Please enter a valid temperature value.")

if __name__=="__main__":
    TempConvert().mainloop()
