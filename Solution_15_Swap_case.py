def swap_case(s):
    anastring = "" #boş string
    for i in s:
        if i == i.upper():
            anastring += i.lower()  #s olarak verilen stringin indexleri sıra sıra giriyor. eğer index büyük harfse
            #anastring olarak oluşturduğum boş stringe küçük harf olarak yazılıyor.
        else:
            anastring += i.upper() #tam tersi
    return anastring #fonksiyon en sonunda anastring olarak kendini döndürüyor.


if __name__ == '__main__':
    s = input()
    result = swap_case(s)
    print(result)