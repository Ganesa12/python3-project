from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput

class kuatarusApp(App):
    def build(self):
        self.layout = BoxLayout(orientation='vertical')

        self.label = Label(text='rumus kuat arus listrik adalah I = v : r')
        teks_v = TextInput(hint_text='tulisakan v (volt)')
        teks_r = TextInput(hint_text='tulisakan r ( hambatan)')
        tombol= Button(text='Hitung')
        tombol.bind(on_press=lambda x: self.hitung(teks_v.text, teks_r.text))

       
        self.layout.add_widget(self.label)
        self.layout.add_widget(teks_v)
        self.layout.add_widget(teks_r)
        self.layout.add_widget(tombol)

        return self.layout

    def hitung(self, v, r) :
        v = float(v)
        r = float(r)
        q = v / r

        label_hasil = Label(text=f"hasilanya adalah {q} Ampere")
        self.layout.add_widget(label_hasil)



if __name__ == "__main__":
    kuatarusApp().run()