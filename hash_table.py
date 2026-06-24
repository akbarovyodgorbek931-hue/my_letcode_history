# class HashTable:
#     def __init__(self):
#         self.size = 10  # jadval o'lchami
#         self.table = [[] for _ in range(self.size)] # bo'sh ro'yxatlar

#     def _hash(self, key):
#         return hash(key) % self.size  # kalitni indeksga aylantiramiz

#     def set(self, key, value):
#         index = self._hash(key)  # indeks hisoblaymiz
#         for pair in self.table[index]:
#             if pair[0] == key:
#                 pair[1] = value  # kalit mavjud bo'lsa yangilaymiz
#                 return
#         self.table[index].append([key, value])  # yangi juft qo'shamiz

#     def get(self, key):
#         index = self._hash(key)  # indeks hisoblaymiz
#         for pair in self.table[index]:
#             if pair[0] == key:
#                 return pair[1]  # qiymatni qaytaramiz
#         return "Topilmadi!"  # kalit yo'q

#     def delete(self, key):
#         index = self._hash(key)  # indeks hisoblaymiz
#         for i, pair in enumerate(self.table[index]):
#             if pair[0] == key:
#                 self.table[index].pop(i)  # juftni o'chiramiz
#                 return "O'chirildi"
#         return "Topilmadi!"

#     def display(self):
#         for i, bucket in enumerate(self.table):
#             if bucket:  # bo'sh bo'lmagan qatorlarni chiqaramiz
#                 print(f"{i} -> {bucket}")


# # ishlatish
# ht = HashTable()
# ht.set("Ali", 25)
# ht.set("Bob", 30)
# ht.set("Sara", 22)

# print(ht.get("Ali"))
# print(ht.get("Bob"))
# ht.delete("Bob")
# print(ht.get("Bob"))
# ht.display()


















# hisob = float(input("Umumiy hisobni toldiring (so'mda): "))

# print("\nXizmat darajasini tanlang:")
# print("1 - Yaxshi (20%)")
# print("2 - Qoniqarli emas (15%)")
# print("3 - Yomon kot(10%)")

# tanlov = input("Tanlovingiz: ")

# if tanlov == "1":
#     foiz = 20
# elif tanlov == "2":
#     foiz = 15
# elif tanlov == "3":
#     foiz = 10
# else:
#     print("Noto'g'ri tanlov! 10% qabul qilindi.")
#     foiz = 10

# choychaqa = hisob * foiz / 100
# jami = hisob + choychaqa

# print("\n------ NATIJA ------")
# print("Hisob:", hisob, "so'm")
# print("Choychaqa:", choychaqa, "so'm")
# print("Jami to'lov:", jami, "so'm")





# collision (toqnashuv) - bu hash table da ikki xil kalitga (malumotga) hashfunciosi ->
# orqali bir xil indeks (manzil) berilib qolish holatlari.


# garderob = ["bosh","bosh","bosh","bosh","bosh","bosh","bosh","bosh","bosh","bosh"] 

# def hash_fumction(ism):
#     ilmoq_raqami = len(ism)
#     return ilmoq_raqami

# kurtka1_shaxsi = "islom"
# ilmoq1 = hash_fumction(kurtka1_shaxsi)

# garderob[ilmoq1] = "islomning qizil kurtkasi"

# print(f"+{kurtka1_shaxsi} kurtkasi {ilmoq1} - ilmoqga ilindi")

# kurtka2_shaxsi = "malika"
# ilmoq2 = hash_fumction(kurtka2_shaxsi)

# garderob[ilmoq2] = "malikaning sariq kurtkasi"

# print(f"+ {kurtka2_shaxsi} kurtkasini {ilmoq2} - ilmoqqa ildik")


# # garderob ichki holati

# print("GARDEROB HOLATI")
# for raqam, kiyim in enumerate(garderob):
#     print(f"ilmoq [{raqam}]:{kiyim}")

# # tezkor qidirish

# kimning_kiyimi = "islom"
# kerakli_ilmoq = hash_fumction(kimning_kiyimi)

# # togridan togri osha kiyim indexsini olamiz

# topilgan_kiyim = garderob[kerakli_ilmoq]
# print(f"qidiruv: {kimning_kiyimi} keldi {kerakli_ilmoq} - ilmoqdan olindi {topilgan_kiyim}")







# kutubxona. collision ga misol
# class Kutubxona:
#     def __init__(self, javonlar_soni=5):
#         self.size = javonlar_soni
#         self.javonlar = [[] for _ in range(self.size)]

#     def hash_function(self, kitob_nomi):
#         umumiy_kod = sum(ord(harf) for harf in kitob_nomi)
#         javon_indeksi = umumiy_kod % self.size
#         return javon_indeksi
        
#     def kitob_qoshish(self, kitob_nomi, muallif):
#         indeks = self.hash_function(kitob_nomi)
#         for i, (nom, muallif_ismi) in enumerate(self.javonlar[indeks]):
#             if nom == kitob_nomi:
#                 self.javonlar[indeks][i] = (kitob_nomi, muallif)
#                 print(f"'{kitob_nomi}' kitobi yangilandi.")
#                 return
#         self.javonlar[indeks].append((kitob_nomi, muallif))
#         print(f"'{kitob_nomi}' kitobi {indeks}-javonga muvaffaqiyatli joylandi")

#     def kitob_qidirish(self, kitob_nomi):
#         indeks = self.hash_function(kitob_nomi)
#         print(f"\n Qidiruv: {kitob_nomi} uchun hash funksiyasi {indeks}- javonni ko'rsatdi")
#         for nom, muallif in self.javonlar[indeks]:
#             if nom == kitob_nomi:
#                 return f"Topildi '{kitob_nomi}' kitobi {indeks} javonda ekan. Muallif {muallif}"
#         return "Uzur bunday kitob bizda yo'q"   

#     def kutubxona_holati(self):
#         print("\n ========== Kutubxona holati =======")
#         for i, javon in enumerate(self.javonlar):
#             print(f"Javon [{i}]: {javon}")
#         print("===============")



# while True:
#     print("\n=== KUTUBXONA TIZMI ===")
#     print("1. kitob qoshish")
#     print("2. Kitob qidirish")
#     print("3. Dasturni tugatish")

#     tanlov=input("Amalni tanlang 1/2/3:").strip()

#     if tanlov=="1":
#         nomi=input("Kitob nomini kiriting: ").strip()
#         muallifi = input("Kitob muallifini kiriting: ").strip()
#         if nomi and muallifi: 
#             Kutubxona.kitob_qoshish(nomi, muallifi)
#         else:
#             print("Xato: Kitob nomi yoki muallifi bo'sh bo'lishi mumkin emas!")
            
#     elif tanlov == "2":
#         nomi = input("Qidirilayotgan kitob nomini kiriting: ").strip()
#         if nomi:
#             natija = Kutubxona.kitob_qidirish(nomi)
#             print(natija)
#         else:
#             print("Xato: Qidirish uchun kitob nomini kiriting!")
            
        
#     elif tanlov == "3":
#         print("Dastur tugatildi. Sog' bo'ling!")
#         break
        
#     else:
#         print("Xato: Noto'g'ri buyruq kiritdingiz! Faqat 1, 2, 3 yoki 4 sonlarini kiriting.")






class Dokon:
    def __init__(self, joylar_soni=5): 
        self.size = joylar_soni
        self.rastalar = [[] for _ in range(self.size)]

    def hash_function(self, mahsulot_nomi):
        umumiy_kod = sum(ord(harf) for harf in mahsulot_nomi)
        rasta_indeksi = umumiy_kod % self.size
        return rasta_indeksi
        
    def mahsulot_qoshish(self, mahsulot_nomi, narxi):
        indeks = self.hash_function(mahsulot_nomi)
        for i, (nom, eski_narx) in enumerate(self.rastalar[indeks]):
            if nom == mahsulot_nomi:
                self.rastalar[indeks][i] = (mahsulot_nomi, narxi)
                print(f"'{mahsulot_nomi}' mahsulotining narxi yangilandi.")
                return   
        self.rastalar[indeks].append((mahsulot_nomi, narxi))
        print(f"'{mahsulot_nomi}' mahsuloti {indeks}-rastaga muvaffaqiyatli joylandi.")

    def mahsulot_qidirish(self, mahsulot_nomi):
        indeks = self.hash_function(mahsulot_nomi)
        print(f"\nQidiruv: '{mahsulot_nomi}' uchun hash funksiyasi {indeks}-rastani ko'rsatdi.")
        
        for nom, narx in self.rastalar[indeks]:
            if nom == mahsulot_nomi:
                return f"Topildi! '{mahsulot_nomi}' mahsuloti {indeks}-rastada ekan. Narxi: {narx} so'm."
        return "Dokonda bunarsa yoq"   

    def dokon_holati(self):
        print("\n========== DO'KON HOLATI (RASTALAR) =======")
        for i, rasta in enumerate(self.rastalar):
            print(f"Rasta [{i}]: {rasta}")
        print("===========================================")


mening_dokonim = Dokon(joylar_soni=5)

while True:
    print("\n=== DO'KON SAVDO TIZIMI ===")
    print("1. Mahsulot qo'shish (yoki narxini yangilash)")
    print("2. Mahsulot qidirish va narxini ko'rish")
    print("3. Do'kondagi barcha rastalarni ko'rish")
    print("4. Dasturni tugatish")

    tanlov = input("Amalni tanlang (1/2/3/4): ").strip()

    if tanlov == "1":
        nomi = input("Mahsulot nomini kiriting (masalan: Olma, Non): ").strip()
        narxi = input("Mahsulot narxini kiriting: ").strip()
        if nomi and narxi: 
            mening_dokonim.mahsulot_qoshish(nomi, narxi)
        else:
            print("Xato: Mahsulot nomi yoki narxi bo'sh bo'lishi mumkin emas!")
    elif tanlov == "2":
        nomi = input("Qidirilayotgan mahsulot nomini kiriting: ").strip()
        if nomi:
            natija = mening_dokonim.mahsulot_qidirish(nomi)
            print(natija)
        else:
            print("Xato: Qidirish uchun mahsulot nomini kiriting!")
    elif tanlov == "3":
        mening_dokonim.dokon_holati()
    elif tanlov == "4":
        print("Dastur tugatildi. Xaridlar uchun rahmat!")
        break
    else:
        print("Xato: Noto'g'ri buyruq kiritdingiz! Faqat 1, 2, 3 yoki 4 sonlarini tanlang.")