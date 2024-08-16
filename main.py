import customtkinter as ctk
from tkinter import messagebox  # Hata mesajı göstermek için

# Uygulama penceresini oluştur
root = ctk.CTk()
root.title("Kimyasal Hesaplama Uygulaması")
root.geometry("800x500")

# Sağ tarafta büyük bir ana çerçeve oluştur
main_frame = ctk.CTkFrame(root)
main_frame.pack(side="right", fill="both", expand=True, padx=20, pady=20)

# Başlık etiketi
title_label = ctk.CTkLabel(main_frame, text="Kimyasal Hesaplama Uygulaması", font=ctk.CTkFont(size=20, weight="bold"))
title_label.pack(pady=(10, 10))

footer_label = ctk.CTkLabel(main_frame, text="Arda Kuvanç", font=ctk.CTkFont(size=12))
footer_label.pack(side="bottom", pady=(15,5), anchor="se")  # Sağ alt köşeye hizalanır

def buttons(hesap):
    # Hesapla butonuna ekstra boşluk ekliyoruz
    hesapla_button = ctk.CTkButton(main_frame, text="Hesapla", command=hesap)
    hesapla_button.pack(pady=(15, 10))  # 15 piksel üstten, 5 piksel alttan boşluk

    geri_button = ctk.CTkButton(main_frame, text="Geri", command=clear_widgets)
    geri_button.pack(pady=5)

# Frame'leri temizleyen fonksiyon
def clear_widgets():
    for widget in main_frame.winfo_children():
        widget.destroy()
    title_label = ctk.CTkLabel(main_frame, text="Kimyasal Hesaplama Uygulaması", font=ctk.CTkFont(size=20, weight="bold"))
    title_label.pack(pady=(10, 10))

def mol_hesaplama():
    
    # Ana pencerede gerekli kısımları oluşturma
    mass_label = ctk.CTkLabel(main_frame, text="Kütle:")
    mass_label.pack(pady=5)

    mass_entry = ctk.CTkEntry(main_frame)
    mass_entry.pack(pady=5)

    ma_label = ctk.CTkLabel(main_frame, text="Molekül Ağırlığı:")
    ma_label.pack(pady=5)

    ma_entry = ctk.CTkEntry(main_frame)
    ma_entry.pack(pady=5)
    
    def mol_hesap():
        
        try:
            # Girişlerden veriyi al ve float'a dönüştür
            mass = float(mass_entry.get())
            ma = float(ma_entry.get())
            
            # Mol hesapla
            mol_sonuc = mass / ma
            
            # Sonucu etiketle göster
            sonuc_label.configure(text=f"Mol Sayısı: {mol_sonuc:.3f}")
            
        except ValueError:
            # Eğer girişler sayı değilse hata mesajı göster
            messagebox.showerror("Hata", "Lütfen geçerli sayılar girin.")
        except ZeroDivisionError:
            # Eğer bölme işleminde 0 hatası varsa
            messagebox.showerror("Hata", "Molekül ağırlığı sıfır olamaz.")


    # Hesapla butonuna ekstra boşluk ekliyoruz
    hesapla_button = ctk.CTkButton(main_frame, text="Hesapla", command=mol_hesap)
    hesapla_button.pack(pady=(40, 10))  # 15 piksel üstten, 5 piksel alttan boşluk

    # Hesaplama sonucunu göstermek için bir etiket ekleyelim
    sonuc_label = ctk.CTkLabel(main_frame, text="")
    sonuc_label.pack(pady=5)

    geri_button = ctk.CTkButton(main_frame, text="Geri", command=clear_widgets)
    geri_button.pack(pady=5)
    
    
# pH Hesaplama Fonksiyonu
def ph_hesaplama():
    pass  # Bu fonksiyonun içine hesaplama işlemlerini ekleyebilirsin.

# Mol Kütle Hesaplama Fonksiyonu
def normalite_hesaplama():
    cozunen_kutlesi_label = ctk.CTkLabel(main_frame, text="Çözünen Kütlesi:")
    cozunen_kutlesi_label.pack(pady=5)

    cozunen_kutlesi_entry = ctk.CTkEntry(main_frame)
    cozunen_kutlesi_entry.pack(pady=5)
    
    molekul_kutlesi_label = ctk.CTkLabel(main_frame, text="Molekül Kütlesi:")
    molekul_kutlesi_label.pack(pady=5)

    molekul_kutlesi_entry = ctk.CTkEntry(main_frame)
    molekul_kutlesi_entry.pack(pady=5)
    
    tesir_label = ctk.CTkLabel(main_frame, text="Tesir Değerliği:")
    tesir_label.pack(pady=5)

    tesir_entry = ctk.CTkEntry(main_frame)
    tesir_entry.pack(pady=5)
    
    # Sonuç etiketini burada tanımlıyoruz
    sonuc_label = ctk.CTkLabel(main_frame, text="")
    sonuc_label.pack(pady=5)
    
    def normalite_hesap():
        try:
            cozunen_kutlesi = float(cozunen_kutlesi_entry.get())
            molekul_kutlesi = float(molekul_kutlesi_entry.get())
            tesir_degerligi = int(tesir_entry.get())

            if tesir_degerligi == 0:
                ekivalen_gram = molekul_kutlesi
            else:
                ekivalen_gram = molekul_kutlesi / tesir_degerligi
            
            esdeger_gram = cozunen_kutlesi / ekivalen_gram
            sonuc_label.configure(text=f"Normalite: {esdeger_gram:.3f}")
        
        except ValueError:
            sonuc_label.configure(text="Hatalı giriş! Lütfen sayısal değerler girin.")
        except ZeroDivisionError:
            sonuc_label.configure(text="Tesir değeri sıfır olamaz.")
        except Exception as e:
            sonuc_label.configure(text=f"Bir hata oluştu: {str(e)}")
    
    # Hesapla butonunu sonuç etiketinin altına yerleştiriyoruz
    buttons(normalite_hesap)


# Derişim Hesaplama Fonksiyonu
def derisim_hesaplama():
    pass  # Bu fonksiyonun içine hesaplama işlemlerini ekleyebilirsin.

# Gaz Kanunu Hesaplamaları Fonksiyonu
def molarite_hesaplama():
    #n/v
    
    mol_label = ctk.CTkLabel(main_frame, text="Mol Sayısı")
    mol_label.pack(pady=5)
    
    mol_entry = ctk.CTkEntry(main_frame)
    mol_entry.pack(pady=5)
    
    hacim_label = ctk.CTkLabel(main_frame, text="Hacim Miktarı (Litre)")
    hacim_label.pack(pady=5)
    
    hacim_entry = ctk.CTkEntry(main_frame)
    hacim_entry.pack(pady=5)
    
    sonuc_label = ctk.CTkLabel(main_frame, text="")
    sonuc_label.pack(pady=5)
    
    def molarite_hesap():
        
        mol = float(mol_entry.get())
        hacim = float(hacim_entry.get())
        molarite = mol / hacim
        sonuc_label.configure(text=f"Molarite: {molarite:.3f}")

        
    buttons(molarite_hesap)

# Çözelti Hazırlama Fonksiyonu
def molalite_hesaplama():
    
    mol_label = ctk.CTkLabel(main_frame, text="Mol Sayısı")
    mol_label.pack(pady=5)
    
    mol_entry = ctk.CTkEntry(main_frame)
    mol_entry.pack(pady=5)
    
    kg_label = ctk.CTkLabel(main_frame, text="Kütle (Kg)")
    kg_label.pack(pady=5)
    
    kg_entry = ctk.CTkEntry(main_frame)
    kg_entry.pack(pady=5)
    
    sonuc_label = ctk.CTkLabel(main_frame, text="")
    sonuc_label.pack(pady=5)
    
    def molalite_hesap():
        
        mol = float(mol_entry.get())
        hacim = float(kg_entry.get())
        molalite = mol / hacim
        sonuc_label.configure(text=f"Molalite: {molalite:.3f}")

        
    buttons(molalite_hesap)

# Asit-Baz Titrasyonu Hesaplama Fonksiyonu
def asit_baz_titrasyonu_hesaplama():
    pass  # Bu fonksiyonun içine hesaplama işlemlerini ekleyebilirsin.

# Yüzde Verim Hesaplama Fonksiyonu
def yuzde_verim_hesaplama():
    pass  # Bu fonksiyonun içine hesaplama işlemlerini ekleyebilirsin.

# Entalpi Hesaplama Fonksiyonu
def entalpi_hesaplama():
    pass  # Bu fonksiyonun içine hesaplama işlemlerini ekleyebilirsin.

# Reaksiyon Hızı Hesaplama Fonksiyonu
def reaksiyon_hizi_hesaplama():
    pass  # Bu fonksiyonun içine hesaplama işlemlerini ekleyebilirsin.

# Elektrokimya Hesaplamaları Fonksiyonu
def elektrokimya_hesaplama():
    pass  # Bu fonksiyonun içine hesaplama işlemlerini ekleyebilirsin.

# Seçilen hesaplama türüne göre sayfayı güncelleyen fonksiyon
def show_selected_function():
    clear_widgets()
    
    selected_function = combo_box.get()
    
    if selected_function == "Mol Hesaplama":
        label = ctk.CTkLabel(main_frame, text="Mol Hesaplama", font=ctk.CTkFont(size=20, weight="bold"))
        label.pack(pady=10)
        mol_hesaplama()
    
    elif selected_function == "pH Hesaplama":
        label = ctk.CTkLabel(main_frame, text="pH Hesaplama", font=ctk.CTkFont(size=20, weight="bold"))
        label.pack(pady=10)
        ph_hesaplama()
    
    elif selected_function == "Normalite Hesaplama":
        label = ctk.CTkLabel(main_frame, text="Normalite Hesaplama", font=ctk.CTkFont(size=20, weight="bold"))
        label.pack(pady=10)
        normalite_hesaplama()
    
    elif selected_function == "Molarite Hesaplama":
        label = ctk.CTkLabel(main_frame, text="Molarite Hesaplama", font=ctk.CTkFont(size=20, weight="bold"))
        label.pack(pady=10)
        molarite_hesaplama()

    elif selected_function == "Molalite Hesaplama":
        label = ctk.CTkLabel(main_frame, text="Molalite Hesaplama", font=ctk.CTkFont(size=20, weight="bold"))
        label.pack(pady=10)
        molalite_hesaplama()

    elif selected_function == "Asit-Baz Titrasyonu Hesaplama":
        label = ctk.CTkLabel(main_frame, text="Asit-Baz Titrasyonu Hesaplama", font=ctk.CTkFont(size=20, weight="bold"))
        label.pack(pady=10)
        asit_baz_titrasyonu_hesaplama()

    elif selected_function == "Yüzde Verim Hesaplama":
        label = ctk.CTkLabel(main_frame, text="Yüzde Verim Hesaplama", font=ctk.CTkFont(size=20, weight="bold"))
        label.pack(pady=10)
        yuzde_verim_hesaplama()

    elif selected_function == "Entalpi Hesaplama":
        label = ctk.CTkLabel(main_frame, text="Entalpi Hesaplama", font=ctk.CTkFont(size=20, weight="bold"))
        label.pack(pady=10)
        entalpi_hesaplama()

    elif selected_function == "Reaksiyon Hızı Hesaplama":
        label = ctk.CTkLabel(main_frame, text="Reaksiyon Hızı Hesaplama", font=ctk.CTkFont(size=20, weight="bold"))
        label.pack(pady=10)
        reaksiyon_hizi_hesaplama()

    elif selected_function == "Elektrokimya Hesaplamaları":
        label = ctk.CTkLabel(main_frame, text="Elektrokimya Hesaplamaları", font=ctk.CTkFont(size=20, weight="bold"))
        label.pack(pady=10)
        elektrokimya_hesaplama()

# Soldaki menü için bir çerçeve (frame) oluştur
left_frame = ctk.CTkFrame(root, width=250)
left_frame.pack(side="left", fill="y")

# ComboBox ile seçim yapılacak hesaplamalar
combo_box = ctk.CTkComboBox(left_frame, values=[
    "Mol Hesaplama",
    "pH Hesaplama",
    "Normalite Hesaplama",
    "Molarite Hesaplama",
    "Molalite Hesaplama",
    "Asit-Baz Titrasyonu Hesaplama",
    "Yüzde Verim Hesaplama",
    "Entalpi Hesaplama",
    "Reaksiyon Hızı Hesaplama",
    "Elektrokimya Hesaplamaları"
], width=150, state="readonly")
combo_box.pack(pady=20, padx=10)

# Hesaplama ekranını gösteren buton
show_button = ctk.CTkButton(left_frame, text="Seçim Yap", command=show_selected_function)
show_button.pack(pady=10, padx=10)



# Karanlık/aydınlık mod değiştirici buton
def toggle_appearance_mode():
    current_mode = ctk.get_appearance_mode()
    if current_mode == "Light":
        ctk.set_appearance_mode("Dark")
        appearance_button.configure(text="☀️")
    else:
        ctk.set_appearance_mode("Light")
        appearance_button.configure(text="🌙")

appearance_button = ctk.CTkButton(root, text="🌙", command=toggle_appearance_mode, width=30, height=30)
appearance_button.place(relx=0.95, rely=0.05, anchor="ne")

# Uygulamayı başlat
root.mainloop()
