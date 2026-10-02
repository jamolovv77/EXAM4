# mutible in yak ivazwavandai ast ki yane int mo adad medihem va doxilawro metavonem aliw kunem nekim immutablero nametavonem 

# c3).............................................................................................
# farki list az tuple in ast ki vakti soxtan aliw kardan yane taxir dodan mewavad amo
#  tuple ro taxirdodan namewavad va mumkin nest 

# tuple xubiaw daer in ast ki tez kor mekunad inxel guym pryamoy kor meknad va pamyati notbukamonro kam mexrad


# va tuple ro hamchun kalid luxat istifoda mekunem mewavad nekem listro nametonem 








#  c4)1 ....................................................................................................................

# int chikor mekunad ?
# int fakat rakam girifta metavonad harf girifta nametavonad va int rakamhoi azdahdoro girifta nametavonad fakat adad agar misol rakami azdahdor oyad uro hamchun int kkabul mekunad misol 1.5 oyad onro 1 hisob mekunad baroi ki int bo rakam azdahdor kor karda nametavonad misol


# a = int(input())
# b = int (input())


# print(f"javob : {a+b}")
# mo chikori xohem mettavonem kunem bo int misol jam kardan minus kardan zarb kardan  yo taksim yo modul


#c4) 2.....................................................................................

# float bowad fakat rakamhoi azdahdorro girifta metavonad misol  
# 2.5 + 2.5 jabo 5.0 mewavad


# a = float(input())
# b = float(input())

# print(f"javob : {a+b}")



#c4) 3.................................................................................................
# str bowad fakat harf girifta metavonad fakat bo harfo kor karda metavonad bo rakaho kor karda nametavo nad misol
#  menavisem Abdulloh {a} <- (programisti) mexonad  dar {b} <-(SoftClub) 

# a = str(input())
# b = str(input())

# print(f"Abdulloh {a}  mexonad va abdulloh dar {b}")





# c4)4............................................................................................................

# bool  bowad True yo False ro niwon medihad misol agar a = 1 bowad true agar ne  False 






# kismi 2. c5
# n =8
# num =[0, 1]

# for i in range(2,n):
#     num.append(num[i-1] +num[i-2])

# print(num)


# kismi 2
# num =[i for i in range(1,50) if i%2 == 0 and i%3 == 0]
# print(num)


# kismi3
# def word_count(text):
  
#     text =text.lower()
    
#     for i in [".", ",", "!", "?", ":", ";"]:
#         text =text.replace(i,"")
    
#     num =text.split()
    

#     cnt ={}
#     for i in num:
#         if i in cnt:
#             cnt[i] +=1
#         else:
#             cnt[i] =1   
#     return cnt


# m =word_count("Hello, hello! Python is great. Python is fun.")
# print(m)



# c9
# class BankAccount:
#     def __init__(self, owner,balance=0):
#         self.owner =owner
#         self.balance =balance

#     def deposit(self,amount):
#         self.balance +=amount

#     def withdraw(self,amount):
#         if amount < self.balance:
#             self.balance - amount
#         else:
#             print("Маблағ кофӣ нест")

#     def __str__(self):
#         return f"Owner: {self.owner}, Balance: {self.balance}"


# account =BankAccount("Alice",1000)
# account.deposit(500)
# account.withdraw(2000)
# print(account)




