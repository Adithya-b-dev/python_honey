from breezypythongui import EasyFrame
class Calculator(EasyFrame):
    def __init__(self):
        EasyFrame.__init__(self,title="Calculator")

        self.addLabel(text='First number: ',row=0,column=0)
        self.firstField=self.addIntegerField(value=0,row=0,column=1)

        self.addLabel(text="Second number: ",row=1,column=0)
        self.secondField=self.addIntegerField(value=0,row=1,column=1)

        self.addButton(text="Add",row=2,column=0,command=self.add)
        self.addButton(text="Subtract",row=2,column=1,command=self.subtract)
        self.addButton(text="Multiply",row=3,column=0,command=self.multiply)
        self.addButton(text="Divide",row=3,column=1,command=self.divide)

        self.addLabel(text="Result: ",row=4,column=0)
        self.resultField=self.addFloatField(value=0.0,row=4,column=1,precision=2)
        self.resultField["state"]="readonly"

    def getInput(self):
        try:
            num1=self.firstField.getNumber()
            num2=self.secondField.getNumber()
            return num1,num2

        except ValueError:
             self.messageBox(title="Error",message="Please enter integer values!")

    def add(self):
        num1,num2=self.getInput()
        self.resultField.setNumber(num1+num2)

    def subtract(self):
        num1,num2=self.getInput()
        self.resultField.setNumber(num1-num2)

    def multiply(self):
        num1,num2=self.getInput()
        self.resultField.setNumber(num1*num2)

    def divide(self):
        num1,num2=self.getInput()
        try:
            result=num1/num2
            self.resultField.setNumber(result)
        except ZeroDivisionError:
            self.messageBox(title="Error",message="Cannot divide by zero!")

if __name__=="__main__":
    Calculator().mainloop()
