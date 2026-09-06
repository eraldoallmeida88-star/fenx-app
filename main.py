import os
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.textinput import TextInput
from kivy.uix.label import Label
from kivy.uix.recyclerview import RecyclerView
from kivy.uix.recycleboxlayout import RecycleBoxLayout
from kivy.properties import ListProperty
import pandas as pd

class MaterialApp(App):
    resultados_data = ListProperty([])

    def build(self):
        self.title = "Fênx infoShop"
        self.df = None
        
        # Carrega a planilha embutida no APK de forma segura
        try:
            caminho_excel = "CODIGO VS ENGENHARIA.xlsx"
            if os.path.exists(caminho_excel):
                self.df = pd.read_excel(caminho_excel, sheet_name="CODIGO ")
                self.df['Cód. Material'] = self.df['Cód. Material'].astype(str).str.strip()
                self.df['Cód. Interno Material'] = self.df['Cód. Interno Material'].astype(str).str.strip()
                self.df['Desc. Material'] = self.df['Desc. Material'].astype(str).str.strip()
        except Exception as e:
            print(f"Erro ao carregar planilha: {e}")

        root = BoxLayout(orientation='vertical', padding=15, spacing=10)
        
        # Título e Cabeçalho
        root.add_widget(Label(text="Fênx infoShop", font_size=24, bold=True, size_hint_y=None, height=40))
        root.add_widget(Label(text="Consulta de Engenharia Offline", font_size=14, color=(0.5,0.5,0.5,1), size_hint_y=None, height=25))

        # Campo de Busca
        self.search_input = TextInput(
            hint_text="Digite o código da peça ou material...",
            multiline=False,
            size_hint_y=None,
            height=50,
            font_size=16
        )
        self.search_input.bind(text=self.realizar_busca)
        root.add_widget(self.search_input)

        # Lista de Resultados
        self.rv = RecyclerView(size_hint=(1, 1))
        self.rv.viewclass = 'Label'
        self.rv.layout_manager = RecycleBoxLayout(orientation='vertical', default_size=(None, 80), default_size_hint=(1, None), size_hint_y=None)
        self.rv.layout_manager.bind(minimum_height=self.rv.layout_manager.setter('height'))
        
        root.add_widget(self.rv)
        return root

    def realizar_busca(self, instance, value):
        if self.df is None:
            return
        
        termo = value.strip().lower()
        if not termo:
            self.rv.data = []
            return

        res = self.df[
            (self.df['Cód. Material'].str.lower().str.contains(termo)) |
            (self.df['Cód. Interno Material'].str.lower().str.contains(termo))
        ]

        dados_tela = []
        for index, row in res.head(20).iterrows():
            texto_item = f"Cód: {row['Cód. Material']} | Int: {row['Cód. Interno Material']}\nDesc: {row['Desc. Material']}"
            dados_tela.append({'text': texto_item, 'size_hint_y': None, 'height': 75, 'color': (1,1,1,1)})

        self.rv.data = dados_tela

if __name__ == '__main__':
    MaterialApp().run()
