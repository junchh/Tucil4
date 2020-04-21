import re 

def matchKeyword(text, keyword, choice):
    if(choice == 3):

        keyword = keyword.lower()
        p = re.compile(keyword)
        it = p.finditer(text)
        rem = []
        for m in it:
            rang = m.span()
            res = keyword
            for j in range(rang[1], len(text)):
                if(text[j] == '.'):
                    if(text[j - 1].isdigit() == False or text[j + 1].isdigit() == False):
                        break
                    else:
                        res += text[j]
                else:
                    res += text[j]
            for j in range(rang[0] - 1, 0, -1):
                if(text[j] == '.'):
                    if(text[j - 1].isdigit() == False or text[j + 1].isdigit() == False):
                        break
                    else:
                        res = text[j] + res
                else:
                    res = text[j] + res
            rem.append(res)
        return rem

text = "421​ Orang di Jabar Terkonfirmasi Positif COVID-19 Yudha Maulana - detikNews Sabtu, 11 Apr 2020 20:07 WIB Bandung - ​Angka positif virus ​Corona atau COVID-19 di Jawa Barat menembus angka ​400 kasus. Laman Pusat Informasi dan Koordinasi COVID-19 Jabar (Pikobar) pada ​Sabtu (11/4/2020) pukul 18.43 WIB​, mencatat terdapat ​421​ orang yang terkonfirmasi positif COVID-19. Dibandingkan ​sehari sebelumnya​, jumlah tercatat yaitu ​388 orang. Terjadi penambahan ​8,5 persen atau ​33​ kasus per harinya. Sementara itu, secara nasional terdapat ​3.842​ kasus positif COVID-19. Dari ​421 kasus tersebut, ​40 orang meninggal dunia dengan keterangan terpapar ​COVID-19​. Sedangkan, angka kesembuhan di Jabar masih tetap berada di angka ​19​ orang. Per hari jumlah Orang Dalam Pemantauan (ODP) di Jabar mencapai ​28.775 orang. Sebanyak ​15.363 di antaranya masih menjalani proses pemantauan dan ​13.412 orang lainnya telah selesai menjalani proses pemantauan. Sementara itu jumlah Pasien Dalam Pengawasan (PDP) mencapai ​2.27​8 orang. Tercatat ​1.344 orang masih menjalani proses pengawasan dan 934 orang lainnya telah selesai menjalani proses pengawasan."
text = text.lower()
b = re.findall("terkonfirmasi", text)
print(b[0])