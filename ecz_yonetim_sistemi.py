import json
from datetime import datetime
import tkinter as tk
from tkinter import messagebox, simpledialog

class Ilac:
    def __init__(self, ad, barkod, uretici, fiyat, stok, son_kullanma_tarihi):
        self.ad = ad
        self.barkod = barkod
        self.uretici = uretici
        self.fiyat = fiyat
        self.stok = stok
        self.son_kullanma_tarihi = son_kullanma_tarihi

class Eczane:
    def __init__(self):
        self.ilac_listesi = []

    def ilac_ekle(self, ilac):
        self.ilac_listesi.append(ilac)

    def ilaclari_goster(self):
        return self.ilac_listesi

    def kritik_stok_kontrolu(self, alt_limit):
        return [ilac for ilac in self.ilac_listesi if ilac.stok < alt_limit]

    def son_kullanma_kontrolu(self):
        bugun = datetime.now().date()
        return [
            ilac
            for ilac in self.ilac_listesi
            if datetime.strptime(ilac.son_kullanma_tarihi, "%Y-%m-%d").date() <= bugun
        ]

# Eczane oluştur ve sabit ilaçları ekle
eczane = Eczane()
eczane.ilac_listesi = [
    Ilac("Parol", "1000000001", "Abdi İbrahim", 15.50, 100, "2025-05-15"),
    Ilac("Aspirin", "1000000002", "Bayer", 12.00, 200, "2024-11-20"),
    Ilac("Majezik", "1000000006", "Deva", 23.45, 90, "2024-09-10"),
    Ilac("Nurofen", "1000000004", "Sanofi", 25.30, 180, "2025-01-25"),
    Ilac("Dolven", "1000000005", "Santa Farma", 18.99, 140, "2025-12-12"),
    Ilac("Majezik", "1000000006", "Deva", 23.45, 90, "2024-09-10"),
    Ilac("Vermidon", "1000000007", "Sanovel", 13.60, 75, "2024-08-05"),
    Ilac("Lustral", "1000000008", "Pfizer", 50.00, 50, "2027-07-15"),
    Ilac("Tylolhot", "1000000009", "Bayer", 8.00, 300, "2026-02-28"),
    Ilac("Cipro", "1000000010", "GSK", 35.25, 110, "2025-04-20"),
    Ilac("Euthyrox", "1000000011", "Abdi İbrahim", 20.50, 130, "2026-08-15"),
    Ilac("Glifor", "1000000012", "Santa Farma", 16.80, 120, "2025-11-05"),
    Ilac("Xanax", "1000000013", "Pfizer", 48.00, 50, "2027-05-30"),
    Ilac("Zentiva", "1000000014", "Sanofi", 27.00, 80, "2025-12-25"),
    Ilac("Efervesan", "1000000015", "Santa Farma", 10.00, 250, "2026-03-05"),
    Ilac("Ventolin", "1000000016", "GSK", 22.40, 300, "2025-07-10"),
    Ilac("Rennie", "1000000017", "Sanofi", 12.75, 150, "2024-10-30"),
    Ilac("Nexium", "1000000018", "AstraZeneca", 36.00, 120, "2025-06-20"),
    Ilac("Metpamid", "1000000019", "Santa Farma", 19.80, 200, "2026-02-15"),
    Ilac("Biteral", "1000000020", "Deva", 28.50, 100, "2025-09-01"),
    Ilac("Zyrtec", "1000000021", "UCB", 24.30, 130, "2026-04-10"),
    Ilac("Dexofen", "1000000022", "Menarini", 18.90, 90, "2025-08-15"),
    Ilac("Lipitor", "1000000023", "Pfizer", 42.00, 70, "2026-01-25"),
    Ilac("Januvia", "1000000024", "MSD", 47.50, 60, "2025-03-15"),
    Ilac("Crestor", "1000000025", "AstraZeneca", 39.99, 80, "2026-07-01"),
    Ilac("Plavix", "1000000026", "Sanofi", 51.75, 50, "2024-12-20"),
    Ilac("Arveles", "1000000027", "Menarini", 32.00, 140, "2025-11-30"),
    Ilac("Onglyza", "1000000028", "AstraZeneca", 45.00, 70, "2026-05-05"),
    Ilac("Durogesic", "1000000029", "Janssen", 85.00, 40, "2025-08-10"),
    Ilac("Prozac", "1000000030", "Eli Lilly", 55.00, 60, "2026-03-20"),
   
]

# Tkinter Arayüzü
def ilaclari_listele():
    listbox.delete(0, tk.END)
    for ilac in eczane.ilaclari_goster():
        listbox.insert(tk.END, f"{ilac.ad} - {ilac.barkod} - {ilac.stok} adet")

def yeni_ilac_ekle():
    ad = simpledialog.askstring("İlaç Ekle", "İlaç adı:")
    barkod = simpledialog.askstring("İlaç Ekle", "Barkod:")
    uretici = simpledialog.askstring("İlaç Ekle", "Üretici firma:")
    fiyat = simpledialog.askfloat("İlaç Ekle", "Fiyat:")
    stok = simpledialog.askinteger("İlaç Ekle", "Stok:")
    son_kullanma_tarihi = simpledialog.askstring("İlaç Ekle", "Son kullanma tarihi (YYYY-AA-GG):")
    
    if ad and barkod and uretici and fiyat and stok and son_kullanma_tarihi:
        ilac = Ilac(ad, barkod, uretici, fiyat, stok, son_kullanma_tarihi)
        eczane.ilac_ekle(ilac)
        messagebox.showinfo("Başarılı", "İlaç başarıyla eklendi!")
        ilaclari_listele()

def kritik_stok_kontrolu():
    alt_limit = simpledialog.askinteger("Stok Kontrolü", "Kritik stok limiti:")
    if alt_limit is not None:
        kritik_ilaclar = eczane.kritik_stok_kontrolu(alt_limit)
        mesaj = "\n".join([f"{ilac.ad} - {ilac.stok} adet" for ilac in kritik_ilaclar])
        if mesaj:
            messagebox.showinfo("Kritik Stok", mesaj)
        else:
            messagebox.showinfo("Kritik Stok", "Kritik seviyede ilaç yok.")

def son_kullanma_kontrolu():
    gecikmis_ilaclar = eczane.son_kullanma_kontrolu()
    mesaj = "\n".join([f"{ilac.ad} - {ilac.son_kullanma_tarihi}" for ilac in gecikmis_ilaclar])
    if mesaj:
        messagebox.showwarning("Son Kullanma Tarihi", mesaj)
    else:
        messagebox.showinfo("Son Kullanma Tarihi", "Tüm ilaçlar güncel.")

# Ana pencere
root = tk.Tk()
root.title("Eczane Yönetim Sistemi")

frame = tk.Frame(root)
frame.pack(pady=10, padx=10)

listbox = tk.Listbox(frame, width=150, height=30)
listbox.pack(side=tk.LEFT, padx=10)

scrollbar = tk.Scrollbar(frame, orient=tk.VERTICAL, command=listbox.yview)
scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

listbox.config(yscrollcommand=scrollbar.set)

btn_frame = tk.Frame(root)
btn_frame.pack(pady=10)

btn_ilac_listele = tk.Button(btn_frame, text="İlaçları Listele", command=ilaclari_listele)
btn_ilac_listele.grid(row=0, column=0, padx=5)

btn_yeni_ilac = tk.Button(btn_frame, text="Yeni İlaç Ekle", command=yeni_ilac_ekle)
btn_yeni_ilac.grid(row=0, column=1, padx=5)

btn_stok_kontrol = tk.Button(btn_frame, text="Kritik Stok Kontrolü", command=kritik_stok_kontrolu)
btn_stok_kontrol.grid(row=0, column=2, padx=5)

btn_son_kullanma = tk.Button(btn_frame, text="Son Kullanma Tarihi Kontrolü", command=son_kullanma_kontrolu)
btn_son_kullanma.grid(row=0, column=3, padx=5)

# Programı başlat
ilaclari_listele()
root.mainloop()
