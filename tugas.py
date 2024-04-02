listpendidikan = ['smk','sma','ma','sarjana']
nama = str(input('Masukan Nama : '))
umur = int(input('Masukan Umur : '))
min_pendidikan = str(input('Masukan min.pendidikan : '))
kesehatan = str(input('Sehat atau tidak : '))

if umur >= 17 and min_pendidikan in listpendidikan and kesehatan == 'sehat':
    print('Selamat Anda Lolos Menjadi Anggota KPPS')
    print('AYO BERJUANG UNTUK MENYUKSESKAN PEMILU TAHUN INI')
else:
    print('WAH SAYANG SEKALI ANDA BELUM BERKESEMPATAN UNTUK MENJADI ABDI NEGARA')
