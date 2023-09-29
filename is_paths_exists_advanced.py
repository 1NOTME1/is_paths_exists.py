#more advanced version of FileExistenceChecker repository
import os
import PyPDF2

def sprawdz_sciezki(nazwa_pliku_txt, wynikowy_plik_txt="nieprawidlowe_sciezki.txt"):
    with open(nazwa_pliku_txt, 'r', encoding='utf-8') as plik:
        sciezki = plik.readlines()

    informacje = []

    for sciezka in sciezki:
        sciezka = sciezka.strip()
        
        if os.path.exists(sciezka):
            print(f"Ścieżka istnieje: {sciezka}")
            if sciezka.lower().endswith('.pdf'):
                try:
                    with open(sciezka, 'rb') as f:
                        PyPDF2.PdfReader(f)
                except Exception as e:
                    print(f"Nie można otworzyć pliku PDF: {e}")
                    informacje.append(f"Niepoprawny plik PDF: {sciezka}")
        else:
            print(f"Ścieżka NIE istnieje: {sciezka}")
            informacje.append(f"Nieistniejąca ścieżka: {sciezka}")

    with open(wynikowy_plik_txt, 'w', encoding='utf-8') as plik_wynikowy:
        for info in informacje:
            plik_wynikowy.write(info + "\n")

nazwa_pliku = "sciezki.txt"
sprawdz_sciezki(nazwa_pliku)
