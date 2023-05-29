import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd

heigh = np.array([[153],[154],[154],[155],[158],[159],[160],[161],[163],[164],[165],[165],
                  [165],[166],[167],[167],[168],[168],[170],[170],[170],[171],[173],[174],
                  [174],[174],[175],[175],[176],[177],[178],[178],
                  [179],[179],[179],[180],[180],[183],[185]])

shoe_size = np.array([[5],[6],[6],[6],[5],[7],[6],[5],[6],[7],[7],[6],
                      [7],[10],[9.5],[13],[10],[9],[10.5],[9.5],[8.5],[9],[10],[8],
                     [10],[9],[12],[11],[9],[10],[11],[11],
                     [12],[10.5],[11.5],[13],[13],[12],[12.5]])

print(heigh.shape) #rozmiar tablicy numpy

#1 sredni rozmiar buta
sredni_rozmiar_buta=shoe_size.mean()
print("sredni rozmiar buta=",sredni_rozmiar_buta)

#2 maksymalny rozmiar buta
maksymalny_rozmiar_buta = shoe_size.max()
print("maksymaly rozmiar buta=",maksymalny_rozmiar_buta)

#sredni wzrost u osob z maksymalnym rozmiarem buta
#indeks = shoe_size.argmax() #argument ktory ma najwieksza wartosc


#3 Znajdowanie indeksów osób z największym rozmiarem buta
max_shoe_size_indexes = np.where(shoe_size == shoe_size.max())

# Obliczanie średniego wzrostu osób z największym rozmiarem buta
average_height = np.mean(heigh[max_shoe_size_indexes])

# Wyświetlanie średniego wzrostu
print("Średni wzrost osób z największym rozmiarem buta:", average_height)

#4 jaki jest najmniejszy wzrost osób z maksymalnym wymienionym rozmiarem buta?
najmniejszy_wzrost_z_maks_rozmiar_buta= np.min(heigh[max_shoe_size_indexes])
print("najmnieszy wzrost u osob z maks rozmiarem buta",najmniejszy_wzrost_z_maks_rozmiar_buta)

#5sredni rozmiar buta u osob kazdego wzrotu
#krok 1 łaczymy tablice

#polaczona_tablica=np.concatenate((heigh,shoe_size))
polaczona_tablica=np.hstack((heigh,shoe_size))
print(polaczona_tablica)

#krok 2 tworzymy slownik ktorego kluczem jest wzrost a wartoscia jest rozmiar buta

slownik = {}
for wiersz in polaczona_tablica:
    wzrost = wiersz[0]
    rozmiar_buta=wiersz[1]
    slownik[wzrost]=rozmiar_buta
print(slownik)

#piszemy petle ktora przejdzie przez slownik i dla kazdego klucza obliczy srednia
#jego wartosci

for wzrost,rozmiar_buta in slownik.items():
    sredni_rozmiar_buta_dla_wzrostu = np.mean(rozmiar_buta)
    print("WZROST",wzrost,"-SREDNI ROZMIAR BUTA:",sredni_rozmiar_buta_dla_wzrostu)

#6 sredni wzrost
sredni_wzrost = heigh.mean()
print(sredni_wzrost)

#7 najmnieszy i najwiekszy wzrost u osob z rozmiarem buta 10

indeksy_osob_z_rozmiarem_buta_10 = np.where(shoe_size == 10)

#nawyzsza osoba z tym rozmiarem
najwyzsza_z_tym = np.max(heigh[indeksy_osob_z_rozmiarem_buta_10])
najnizsza_z_tym = np.min(heigh[indeksy_osob_z_rozmiarem_buta_10])

print("najwyzsza osoba z rozmiarem 10:", najwyzsza_z_tym)
print("najnizsza osoba z rozmiarem 10:", najnizsza_z_tym)

####
####
#zadanie 2

#x=np.linspace(-2,2)
#y=x
#y1=x**2

#plt.plot(x,y,color='orange',label='y=x')
#plt.plot(x,y1,color='blue', label = 'y=x^2')

#plt.legend()

#plt.show()

x = np.linspace(-2, 2)
y = x
y_squared = x**2

sns.scatterplot(x=x, y=y, color='orange', label='y = x')
sns.scatterplot(x=x, y=y_squared, color='blue', label='y = x^2')

plt.legend()
plt.xlabel('x')
plt.ylabel('y')
plt.title('Wykresy punktowe')
# Ustawienie tła na czarne
plt.gca().set_facecolor('black') #zrobienie czarnego kolorku
plt.show()

#zadanie nr 3
data = pd.read_csv( 'wyniki.csv' , sep=';' ,index_col =0, encoding='UTF=8' )
print(data)
# punkt_1
x=data["Komisje obwodowe otrzymały kart do głosowania"].sum()
print(x)
#punkt_2
dane2=(data["Liczba kopert zwrotnych, w których nie było oświadczenia o osobistym i tajnym oddaniu głosu"]/
       data["Komisje obwodowe otrzymały kart do głosowania"])*100 #robi tabele
dane2.plot(kind='bar') #robi wykres slupkowy
plt.xticks(rotation=30) #odwraca etykiety
plt.show() #rysuje ten wykres

#suma glosow dla kazdego kandydata
#robimy sobie podtabele z nazwami kandytatow
#przechodzimy petla przez wszytskich w kandydaci
#dla kolumny w tabeli data o nazwie z tabeli kandydaci wyswietlami jej sume a przed tym nazwe kandytata
kandydaci=["Robert BIEDROŃ","Krzysztof BOSAK","Andrzej Sebastian DUDA","Szymon Franciszek HOŁOWNIA",
           "Marek JAKUBIAK","Władysław Marcin KOSINIAK-KAMYSZ","Mirosław Mariusz PIOTROWSKI","Paweł Jan TANAJNO",
           "Rafał Kazimierz TRZASKOWSKI","Waldemar Włodzimierz WITKOWSKI","Stanisław Józef ŻÓŁTEK"]
for x in kandydaci:
    print(x)
    print(data[x].sum())

#wykres osob z najwieksza liczba glosow w danym powiecie
dane3=data.groupby(data["Kod TERYT"])[kandydaci].sum()

dane3.plot(kind="bar",stacked=True)
plt.legend(loc='upper right')
plt.show()



