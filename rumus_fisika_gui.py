from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput

class FisikaApp(App):
    def build(self):
        layout = BoxLayout(orientation='vertical')
        
        label = Label(text="Selamat datang di kumpulan rumus fisika")
        layout.add_widget(label)
        
        menu_button = Button(text="Menu Fisika", size_hint=(None, None), size=(150, 50))
        menu_button.bind(on_press=self.show_menu)
        layout.add_widget(menu_button)
        
        return layout
    
    def show_menu(self, instance):
        self.clear_widgets()
        layout = BoxLayout(orientation='vertical')
        
        label = Label(text="Menu Fisika:")
        layout.add_widget(label)
        
        buttons = [
            ("Rumus Kuat Arus Listrik", self.kuat_arus),
            ("Rumur Resistor Paralel", self.resistor_paralel),
            ("Rumus Resistor Seri", self.resistor_seri),
            ("Rumus Watt", self.watt),
            ("Rumus Lilitan Trafo", self.rumus_trafo),
            ("Hukum Kapasitor", self.hukum_kapasitor)
        ]
        
        for text, callback in buttons:
            button = Button(text=text, size_hint=(None, None), size=(200, 50))
            button.bind(on_press=callback)
            layout.add_widget(button)
            
        back_button = Button(text="Kembali", size_hint=(None, None), size=(150, 50))
        back_button.bind(on_press=self.build)
        layout.add_widget(back_button)
        
        self.root = layout
    
    def hukum_kapasitor(self, instance):
        self.clear_widgets()
        layout = BoxLayout(orientation='vertical')
        
        label = Label(text="Hukum kapasitor adalah serangkaian rumus yang menjelaskan perilaku kapasitor dalam sirkuit listrik. Pilih rumus yang Anda inginkan:")
        layout.add_widget(label)
        
        buttons = [
            ("Hubungan Muatan dan Tegangan pada Kapasitor", self.hubungan_muatan_tegangan),
            ("Kapasitansi Kapasitor", self.kapasitansi_kapasitor),
            ("Energi Tersimpan pada Kapasitor", self.energi_tersimpan)
        ]
        
        for text, callback in buttons:
            button = Button(text=text, size_hint=(None, None), size=(300, 50))
            button.bind(on_press=callback)
            layout.add_widget(button)
            
        back_button = Button(text="Kembali", size_hint=(None, None), size=(150, 50))
        back_button.bind(on_press=self.show_menu)
        layout.add_widget(back_button)
        
        self.root = layout
    
    def hubungan_muatan_tegangan(self, instance):
        self.clear_widgets()
        layout = BoxLayout(orientation='vertical')
        
        label = Label(text="Hubungan Muatan dan Tegangan pada Kapasitor dapat kita rumuskan sebagai berikut:")
        layout.add_widget(label)
        
        c_input = TextInput(hint_text="Masukkan nilai C (kapasitor dalam satuan farad)")
        layout.add_widget(c_input)
        
        v_input = TextInput(hint_text="Masukkan nilai tegangan (volt)")
        layout.add_widget(v_input)
        
        calculate_button = Button(text="Hitung", size_hint=(None, None), size=(100, 50))
        calculate_button.bind(on_press=lambda x: self.calculate_hmt(c_input.text, v_input.text))
        layout.add_widget(calculate_button)
        
        back_button = Button(text="Kembali", size_hint=(None, None), size=(150, 50))
        back_button.bind(on_press=self.hukum_kapasitor)
        layout.add_widget(back_button)
        
        self.root = layout
    
    def calculate_hmt(self, c, v):
        try:
            c = float(c)
            v = float(v)
            q = c * v
            result_label = Label(text=f"Hasilnya adalah {q} coulomb")
            self.root.add_widget(result_label)
        except ValueError:
            error_label = Label(text="Pastikan Anda memasukkan angka!")
            self.root.add_widget(error_label)
    
    def kapasitansi_kapasitor(self, instance):
        # Implementasi rumus kapasitansi kapasitor
        pass
    
    def energi_tersimpan(self, instance):
        # Implementasi rumus energi tersimpan
        pass
    
    # Implementasi fungsi-fungsi lainnya seperti kuat_arus, resistor_seri, resistor_paralel, watt, rumus_trafo, dll.
    # Fungsi-fungsi ini akan dipanggil dari tombol menu yang sesuai.

if __name__ == "__main__":
    FisikaApp().run()
