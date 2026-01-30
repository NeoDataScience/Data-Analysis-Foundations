devam = ("evet")

while devam == "evet":
  şifre = input("Şifrenizi giriniz: ")

  if şifre == "Morpheus":
    print("SİSTEME GİRİŞ BAŞARILI HOŞGELDİN NEO!")
    break
  else:
    print("SİSTEME GİRİŞ BAŞARISIZ LÜTFEN TEKRAR DENEYİNİZ.")

  devam = input("Tekrar denemek istiyor musunuz? (evet/hayır): ")

print("SİSTEMDEN ÇIKIŞ YAPILDI.")
