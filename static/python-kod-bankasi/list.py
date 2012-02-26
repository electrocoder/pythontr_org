
# 22-09-2010
# List nesnesinin incelenmesi.
# Http://PythonTR.Org

#i listesine string eklendi
i=["esma", "ebru", "yusuf", "sahin"]

#j listesine string eklendi ve i dizisi j listesine ekleniyor.
j=["is", "okul", "ev", "market", i]

#i nin icerigi
print i

#j nin icerigi
print j

#i nin uzunlugu (Onemli : j listesinde 4 eleman olmasina ragmen i dizisi +1 olarak ekleniyor.
print len(i)

#j nin uzunlugu
print len(j)

"""buradaki for icindeki 2 'i' ye dikkat edelim."""

#su anda 'i' ile i listesinin elemanlarina eristik
for i in i:
	print i

#cunku  range(len(i)) ile i listesinin sayisal uzunlugu alindi
for i in range(len(i)):
	print i

j.append("sinema")
print j
