# Soal
# buatlah sebuah program python yang dapat menccari data-data yang sudah disediakan dengan output
# 1. Arsel di index 0, avivah di index 1, daiva di index 2
# 2 Wahyu di index 3 kolom 0
# 3. Wibi di index 3 kolom 1

# create with jump search

data = [
    "Arsel",
    "Avivah",
    "Daiva",
    ["Wahyu", "Wibi"]
] 
# list data, berisikan nama-nama sesuai soal

def jumpSearch (data, nama): 
# fungsi jump search yang menerima 2 parameter yaitu data dan nama

    Found = False
    # variabel boolean untuk mengecek apakah data ditemukan atau tidak

    for i in range(len(data)):
    # looping untuk mengecek setiap data yang ada di list data

        if type(data[i]) == list:
        # pengkondisian untuk mengecek apakah data yang ada di list data merupakan list atau bukan

            for j in range(len(data[i])):
            # jika data merupakan list maka akan dilakukan looping untuk mengecek setiap data yang ada di list data[i]

                if data[i][j].lower() == nama.lower():
                # jika data yang ada di list data[i] sama dengan inputan nama yang dicari 
                # sebelum itu nama inputan di convert ke huruf kecil dan nama yang ada di list data[i] juga di convert ke huruf kecil
                # agar tidak terjadi kesalahan pengecekan

                    print(f'{ nama } di Index { i } pada kolom { j }')
                    # menampilkan output nama yang dicari di index ke berapa dan kolom ke berapa jika data ditemukan

                    Found = True
                    # jika data ditemukan maka variabel boolean akan bernilai True
    
        else:
        # jika data yang ada di list data bukan list maka akan dilakukan pengecekan apakah 
        # data yang ada di list data sama dengan inputan nama yang dicari

            if data[i].lower() == nama.lower():
            # jika data yang ada di list data bukan list maka akan dilakukan pengecekan apakah data yang ada di list data sama dengan inputan nama yang dicari
            # sebelum itu nama inputan di convert ke huruf kecil dan nama yang ada di list data juga di convert ke huruf kecil
            # agar tidak terjadi kesalahan pengecekan

                print(f'{ nama } di Index { i }')
                # menampilkan output nama yang dicari di index ke berapa jika data ditemukan

                Found = True
                # jika data ditemukan maka variabel boolean akan bernilai True
    
    if not Found:
    # jika data tidak ditemukan maka akan menampilkan output nama tidak ditemukan

        print(f'{ nama } tidak ditemukan')


if __name__ == "__main__":
# fungsi utama

    # memanggil fungsi jumpSearch dengan parameter data dan nama yang dicari
    jumpSearch(data, 'Arsel')
    jumpSearch(data, 'Avivah')
    jumpSearch(data, 'Daiva')
    jumpSearch(data, 'Wahyu')
    jumpSearch(data, 'Wibi')
