import json

while True :
    emr=input('Yeni telebe elave etmek isteyirsiniz mi (Y/N) :')
    if emr=='Y' :
        ad = input('Adinizi daxil edin : ')
        soyad = input('Soyadinizi daxil edin : ')
        yas = int(input('Yashinizi daxil edin : '))
    else:
        break

dict = {
    'istifadeci adi' : ad,
    'istifadeci soyadi' : soyad,
    'istifadeci yas' : yas
}

print(dict)

users = [dict]
print(users)

data = json.dumps(users)
conn = open('data.json', 'w')
conn.write(data)
