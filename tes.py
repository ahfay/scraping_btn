from ekstrak import EkstrakFeature
import pandas as pd

subcity = pd.read_csv('id_wilayah.csv')
ekstrak = EkstrakFeature('https://rumahmurah.btn.co.id/btn/detail/38121/bnas-220905',['ACEH'],subcity[subcity['Prov'] == 11]['NamaKab'].unique(),['Limapuluh', 'Pekanbaru'])
row = []
data = [[None,None,None,None,None,None,None,None,None,None,None,None,None]]
coloumn = ['harga','luas_tanah','luas_bangunan', 'lebar_jalan', 'type','sertifikat','tanggal','kec','kab/kota','prov','alamat_lengkap','id_rumah','link']
tanggal = ekstrak.ekstrak_date() # Ekstrak Tanggal Posting
harga = ekstrak.ekstrak_price() # Ekstrak Harga
luas_bangunan = ekstrak.ekstrak_lb() # Ekstrak Luas Bangunan
luas_tanah = ekstrak.ekstrak_lt() # Ekstrak Luas Tanah
sertifikat = ekstrak.ekstrak_certifikat() # Ekstrak Sertifikat
kab = ekstrak.ekstrak_kab() # Ekstrak Kabupaten
kec = ekstrak.ekstrak_kec() # Ekstrak Kecataman
prov = ekstrak.ekstrak_prov() # Menambahkan provinsi
type = ekstrak.ekstrak_type() # Menambahkan Tipe Properti
lebar_jalan = ekstrak.ekstrak_lj() # Menambahkan luas Lebar Jalan Depan Rumah
alamat_lengkap = ekstrak.ekstrak_address() # Menambahkan Alamat Lengkap
id = ekstrak.ekstrak_id() # Menambahkan Id Produk
link_id = 'https://rumahmurah.btn.co.id/btn/detail/38121/bnas-220905'


row.append(harga)
row.append(luas_tanah)
row.append(luas_bangunan )
row.append(lebar_jalan)
row.append(type)
row.append(sertifikat)
row.append(tanggal)
row.append(kec)
row.append(kab)
row.append(prov)
row.append(alamat_lengkap)
row.append(id)
row.append(link_id)
data.append(row)

df = pd.DataFrame(data=data[1:], columns=coloumn)
df.to_csv('D:/FAYYYAD/PROGRES MAGANG/btn/test/Indonesia/test.csv', index=False)