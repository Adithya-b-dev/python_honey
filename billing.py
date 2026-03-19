

from breezypythongui import EasyFrame
class BillingGUI(EasyFrame):
    def __init__(self):
        EasyFrame.__init__(self, title="Billing System")

        self.addLabel(text="Item Price:", row=0, column=0)
        self.priceField = self.addFloatField(value=0.0, row=0, column=1)

        self.addLabel(text="Quantity:", row=1, column=0)
        self.quantityField = self.addIntegerField(value=0, row=1, column=1)

        self.addButton(text="Generate Bill",row=2, column=0, columnspan=2,command=self.generateBill)

        self.addLabel(text="Final Amount:", row=3, column=0)
        self.resultField = self.addFloatField(value=0.0,row=3, column=1,precision=2)
        self.resultField["state"] = "readonly"

    def generateBill(self):
        try:
            price = self.priceField.getNumber()
            quantity = self.quantityField.getNumber()

            if price<0 or quantity<0:
                self.messageBox(title="Error",message="Price or quantity cannot be negative.")
            total = price * quantity

            if total > 1000:
                total *= 0.9

            self.resultField.setNumber(total)

        except ValueError:
            self.messageBox(title="Error",message="Enter valid price and quanitity.")

if __name__ == "__main__":
    BillingGUI().mainloop()
