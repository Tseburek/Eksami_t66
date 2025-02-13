class cal(): #klass
    def __init__(self,a,b):  #funktsioon kus me sisestame a ja b-sse saadetud esimese ja teise numbrid.
        self.a = a #salvestame a numbri aatribuuti
        self.b = b #salvestame b numbri aatribuuti

    def liitmine(self):   #Funktsioon liitmine
        return self.a + self.b #saadame liidetud numbri vastuse tagasi.
    def lahutamine(self): #Funktsioon lahutamine
        return self.a - self.b #saadame lahutatud numbri vastuse tagasi.
    def korrutamine(self): #Funktsioon korrutamine
        return self.a * self.b #saadame korrutatud numbri vastuse tagasi.
    def jagamine(self):  #Funktsioon jagamine
        return self.a / self.b #saadame jagatud numbri vastuse tagasi.
    def jaak(self):#Funktsioon jäägi leidmine
        return self.a % self.b #saadame jäägi leitud numbri vastuse tagasi.
    def astendamine(self):  #Funktsioon astendamine
        return self.a ** self.b #saadame astendatud numbri vastuse tagasi.

while True: #korrutab seda koodi blokki igavesti
    a = int(input("Sisesta esimene number: ")) #Küsime kasutajalt esimest numbrit
    b = int(input("Sisesta teine number: ")) #Küsime kasutajalt teist numbrit.
    x = ('1. Liitmine \n2. lahutamine\n3. korrutamine\n4. jagamine\n5. Jäägi leidmine\n6. astendamine. ') #muutuja x mis sisaldab teksti.
    print(x) #väljastame muutuja x teksti.
    valik = int(input('Sisesta üks valikutest: ')) #Küsime kasutajalt valikut
    kalk = cal(a, b) # sisestame klassi esimese ja teise numbrid
    if valik == 1: #Kui kasutaja valis valikuks 1, siis.
        print("Vastus: ",kalk.liitmine()) #Prindime välja vastuse
      # break <- see kood väljatad koodi blokki korrutajatest
    elif valik == 2: #Kui kasutaja valis valikuks 2, siis.
        print("Vastus: ",kalk.lahutamine()) #Prindime välja vastuse
      #  break <- see kood väljatad koodi blokki korrutajatest
    elif valik == 3: #Kui kasutaja valis valikuks 3, siis.
        print("Vastus: ",kalk.korrutamine()) #Prindime välja vastuse
       # break <- see kood väljatad koodi blokki korrutajatest
    elif valik == 4: #Kui kasutaja valis valikuks 4, siis.
        print("Vastus: ",kalk.jagamine()) #Prindime välja vastuse
        #break <- see kood väljatad koodi blokki korrutajatest
    elif valik == 5: #Kui kasutaja valis valikuks 5, siis.
        print("Vastus: ",kalk.jaak()) #Prindime välja vastuse
        #break <- see kood väljatad koodi blokki korrutajatest
    elif valik == 6: #Kui kasutaja valis valikuks 6, siis.
        print("Vastus: ",kalk.astendamine()) #Prindime välja vastuse
        #break <- see kood väljatad koodi blokki korrutajatest
    else: #Kui mitte kumbki eelmistest polnud see number, siis
        print('Sisesta uuesti üks liitmise operaator') #Prindime välja vastuse
        #break <- see kood väljatad koodi blokki korrutajatest



