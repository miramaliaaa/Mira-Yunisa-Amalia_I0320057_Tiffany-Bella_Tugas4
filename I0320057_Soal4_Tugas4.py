print('==Pendaftaran Kursus Online==')
print('Jawablah pertanyaan berikut')
a = int(input('\na. Berapa usia kamu? '))
if a >= 21:
    b = input('b. Apakah Anda sudah lulus ujian kualifikasi?(Y/T)').upper()
    if b=='Y':
        print('Anda dapat mendaftar di kursus ini.')
    elif b=='T':
        print('Input Tidak dapat mendaftar di kursus ini.')
elif a < 21:
    print('Anda tidak dapat mendaftar di kursus ini.')