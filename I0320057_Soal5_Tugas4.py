s = "Kelinci abu-abu lucu"
# Panjangnya harusnya 20
print("panjang dari s = %d" % len(s))

# huruf pertama ‘a’ harusnya di index no 8
print("\nKemunculan pertama a = %d" % s.index("a"))

# jumlah huruf a harusnya 2
print("\na muncul sebanyak %d kali" % s.count("a"))

# memotong string berdasarkan index
print("\nLima karakter pertama adalah '%s'" % s[:5]) # Start to 5
print("Lima karakter berikutnya adalah '%s'" % s[5:10]) # 5 to 10
print("Karakter ketiga belas adalah '%s'" % s[12]) # Just number 12
print("Karakter dengan indeks ganjil adalah '%s'" %s[1::2]) #(0-based indexing)
print("Lima karakter terakhir adalah '%s'" % s[-5:]) # 5th-from-last to end

# konversikan ke upercase
print("\nString dalam huruf besar: %s" % s.upper())

# konversikan ke lowercase
print("\nString dalam huruf kecil: %s" % s.lower())

f = "Strong and Welcome!"
# cek bagaimana string itu dimulai
if f.startswith("Str"):
    print("\nString dimulai dengan 'Str'. Good!")

# cek bagaimana string itu diakhiri
if f.endswith("ome!"):
    print("\nString diakhiri dengan 'ome!'. Good!")

# Pisahkan string menjadi tiga string yang terpisah,
# masing-masing hanya berisi satu kata
print("\nPisahkan kata-kata dari string tersebut: %s" % f.split(" "))