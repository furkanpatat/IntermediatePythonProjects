with open("futbolcular.txt","w",encoding = "utf-8") as file:
    file.write("Fernando Muslera,Galatasaray\n")
    file.write("Atiba Hutchinson,Beşiktaş\n")
    file.write("Simon Kjaer,Fenerbahçe\n")
    file.write("Drogba,Galatasaray\n")
    file.write("Alex de Souza,Fenerbahçe\n")
    file.write("Quaresma,Beşiktaş")
with open("futbolcular.txt","r+",encoding="utf-8") as file4:
    file4.seek(0)

    gs = list()
    fb = list()
    bjk = list()

    for satir in file4:
        satir = satir[:-1]
        satir_elemanları = satir.split(",")
        if(satir_elemanları[1] == "Fenerbahçe"):
            fb.append(satir+"\n")
        elif(satir_elemanları[1] == "Galatasaray"):
            gs.append(satir+"\n")
        else:
            bjk.append(satir+"\n")

with open("gs.txt","w",encoding="utf-8") as file1:
    for i in gs:
        file1.write(i)

with open("fb.txt","w",encoding="utf-8") as file2:
    for i in fb:
        file2.write(i)

with open("bjk.txt","w",encoding="utf-8") as file3:
    for i in bjk:
        file3.write(i)