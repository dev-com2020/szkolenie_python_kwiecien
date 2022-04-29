# import zipfile
#
# z = zipfile.ZipFile("sekwencje.zip", "r")
# for plik in z.namelist():
#     print("Plik:", plik)
#     bajty = z.read(plik)
#     print("ma", len(bajty), 'bajtów.')

# import tarfile
#
# tar = tarfile.TarFile.open('plik.tar.bz2', 'w:bz2')
# tar.add('output/powitanie.exe')
# tar.close()

import zlib
import glob

for file in glob.glob("*"):
    wejscie = open(file, "rb").read()
    wyjscie = zlib.compress(wejscie, zlib.Z_BEST_COMPRESSION)

    pliczek = file + '.zlib'
    plik = open(pliczek, 'wb')
    plik.write(wyjscie)
    plik.close()

    print(file, len(wejscie), "->", len(wyjscie))
    print("%d%%" % (len(wyjscie) * 100 / len(wejscie)))
