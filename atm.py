class Atm(object):
    def __init__(self,atmCardNumber,pinNumber):
        self.atmCardNumber= atmCardNumber
        self.pinNumber=pinNumber
    def cashWithdrawal(self):
        print ("Cash Withdrawal")
    def balanceEnquiry(self):
        print ("Balance Enquiry")

Ram=Atm("AXNV302",3435)

print(Ram.balanceEnquiry())
