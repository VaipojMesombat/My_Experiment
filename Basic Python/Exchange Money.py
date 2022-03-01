'''
How to exchange to money to banknote and coin by // (หารแบบปัดเศษ) and % (หารเอาแต่เศษ)
'''
# Pre-defne Variable 

BankNote_1000 = 1000
BankNote_500 = 500
BankNote_100 = 100
BankNote_50 = 50
BankNote_20 = 20
Coin_10 = 10
Coin_5 = 5
Coin_1 = 1

Number_1000_BankNote = 0
Number_500_BankNote = 0
Number_100_BankNote = 0
Number_50_BankNote = 0
Number_20_BankNote = 0
Number_5_Coin = 0
Number_1_Coin = 0
Money = int (input ("Please enter your money to exchange : "))


if Money >= 1000 :
    Number_1000_BankNote = Money // BankNote_1000
    # Money = Money % BankNote_1000
    Money %= BankNote_1000
if Money >= 500 :
    Number_500_BankNote = Money // BankNote_500
    Money = Money % BankNote_500
if Money >= 100 :
    Number_100_BankNote = Money // BankNote_100
    Money = Money % BankNote_100
if Money >= 50 :
    Number_50_BankNote = Money // BankNote_50
    Money = Money % BankNote_50
if Money >= 20 :
    Number_20_BankNote = Money // BankNote_20
    Money = Money % BankNote_20
if Money >= 5 :
    Number_5_Coin = Money // Coin_5
    Money = Money % Coin_5
Number_1_Coin = Money

print ("Number of Banknote 1000 Baht are = ", Number_1000_BankNote)
print ("Number of Banknote 500 Baht are = ", Number_500_BankNote)
print ("Number 0f Banknote 100 Baht are = ",Number_100_BankNote)
print ("Number 0f Banknote 50 Baht are = ",Number_50_BankNote)
print ("Number 0f Banknote 20 Baht are = ",Number_20_BankNote)
print ("Number 0f Coin 5 Baht are = ",Number_5_Coin)
print ("Number of Coin 1 Baht are = ",Number_1_Coin)    