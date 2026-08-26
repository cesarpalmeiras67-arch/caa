from kivy.app import App
from kivy.lang import Builder
from kivy.properties import StringProperty
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.core.window import Window
from kivy.metrics import dp
from kivy.utils import platform

# Tenta usar a API nativa de Text-to-Speech no Android.
tts = None
if platform == "android":
    try:
        from jnius import autoclass
        TextToSpeech = autoclass("android.speech.tts.TextToSpeech")
        Locale = autoclass("java.util.Locale")
        PythonActivity = autoclass("org.kivy.android.PythonActivity")
        activity = PythonActivity.mActivity
        tts = TextToSpeech(activity, None)
        tts.setLanguage(Locale("pt", "BR"))
    except Exception:
        tts = None

KV = r"""
#:import dp kivy.metrics.dp

ScreenManager:
    HomeScreen:
    CategoryScreen:

<HomeScreen>:
    name: "home"
    BoxLayout:
        orientation: "vertical"
        spacing: dp(8)
        padding: dp(10)

        Label:
            text: "🗣️ MINHA COMUNICAÇÃO"
            font_size: "25sp"
            bold: True
            size_hint_y: None
            height: dp(60)
            color: 1,1,1,1
            canvas.before:
                Color:
                    rgba: 0.10,0.46,0.82,1
                Rectangle:
                    pos: self.pos
                    size: self.size

        Label:
            id: visor
            text: root.frase
            font_size: "23sp"
            bold: True
            halign: "center"
            valign: "middle"
            text_size: self.width-dp(20), self.height-dp(10)
            size_hint_y: None
            height: dp(105)
            color: 0.1,0.1,0.1,1
            canvas.before:
                Color:
                    rgba: 1,0.93,0.35,1
                RoundedRectangle:
                    pos: self.pos
                    size: self.size
                    radius: [dp(10),]

        BoxLayout:
            size_hint_y: None
            height: dp(62)
            spacing: dp(6)

            Button:
                text: "🔊 FALAR"
                font_size: "17sp"
                bold: True
                background_color: 0.18,0.49,0.20,1
                on_release: root.falar()

            Button:
                text: "⌫ APAGAR"
                font_size: "17sp"
                bold: True
                background_color: 0.94,0.43,0.02,1
                on_release: root.apagar()

            Button:
                text: "🗑 LIMPAR"
                font_size: "17sp"
                bold: True
                background_color: 0.83,0.12,0.12,1
                on_release: root.limpar()

        Label:
            text: "Frases rápidas"
            font_size: "18sp"
            bold: True
            size_hint_y: None
            height: dp(35)
            color: 0.2,0.25,0.3,1

        ScrollView:
            size_hint_y: None
            height: dp(100)
            do_scroll_x: True
            do_scroll_y: False

            BoxLayout:
                id: quick_box
                size_hint_x: None
                width: self.minimum_width
                spacing: dp(6)
                padding: dp(2)

        Label:
            text: "Escolha uma categoria"
            font_size: "20sp"
            bold: True
            size_hint_y: None
            height: dp(40)
            color: 0.25,0.30,0.35,1

        ScrollView:
            GridLayout:
                id: categories
                cols: 2
                spacing: dp(8)
                padding: dp(2)
                size_hint_y: None
                height: self.minimum_height

<CategoryScreen>:
    name: "category"
    BoxLayout:
        orientation: "vertical"
        spacing: dp(8)
        padding: dp(10)

        BoxLayout:
            size_hint_y: None
            height: dp(58)
            spacing: dp(8)

            Button:
                text: "← VOLTAR"
                font_size: "17sp"
                bold: True
                size_hint_x: 0.35
                on_release: root.voltar()

            Label:
                id: title
                text: root.titulo
                font_size: "21sp"
                bold: True
                color: 0.15,0.20,0.25,1

        ScrollView:
            GridLayout:
                id: words
                cols: 2
                spacing: dp(8)
                padding: dp(2)
                size_hint_y: None
                height: self.minimum_height
"""

categorias = {
    "🏠 Necessidades": [
        ("ÁGUA","água"),("COMIDA","comida"),("BANHEIRO","banheiro"),
        ("DORMIR","dormir"),("AJUDA","preciso de ajuda"),("DESCANSAR","quero descansar"),
        ("FRIO","estou com frio"),("CALOR","estou com calor"),("FOME","estou com fome"),
        ("SEDE","estou com sede")],
    "❤️ Sentimentos": [
        ("FELIZ","estou feliz"),("TRISTE","estou triste"),("BRAVO","estou bravo"),
        ("MEDO","estou com medo"),("CANSADO","estou cansado"),("NERVOSO","estou nervoso"),
        ("TRANQUILO","estou tranquilo"),("AMOR","eu te amo"),("SAUDADE","estou com saudade")],
    "🩺 Saúde": [
        ("DOR","estou com dor"),("CABEÇA","minha cabeça está doendo"),
        ("BARRIGA","minha barriga está doendo"),("DENTE","meu dente está doendo"),
        ("GARGANTA","minha garganta está doendo"),("MÉDICO","quero ir ao médico"),
        ("REMÉDIO","preciso do meu remédio"),("MELHOR","estou melhor"),("PIOR","estou pior")],
    "👨‍👩‍👧 Pessoas": [
        ("MAMÃE","mamãe"),("PAPAI","papai"),("VOVÓ","vovó"),("VOVÔ","vovô"),
        ("IRMÃO","meu irmão"),("IRMÃ","minha irmã"),("PROFESSOR","professor"),
        ("AMIGO","meu amigo"),("FAMÍLIA","minha família")],
    "🎯 Ações": [
        ("QUERO","quero"),("NÃO QUERO","não quero"),("GOSTO","eu gosto"),
        ("NÃO GOSTO","eu não gosto"),("IR","quero ir"),("VOLTAR","quero voltar"),
        ("ABRIR","quero abrir"),("FECHAR","quero fechar"),("PEGAR","quero pegar"),("DAR","quero dar")],
    "🎮 Atividades": [
        ("BRINCAR","quero brincar"),("JOGAR","quero jogar"),("DESENHAR","quero desenhar"),
        ("PINTAR","quero pintar"),("MÚSICA","quero ouvir música"),("TV","quero assistir televisão"),
        ("CELULAR","quero usar o celular"),("PASSEAR","quero passear"),("LIVRO","quero ler um livro")],
    "🍎 Comidas": [
        ("ARROZ","arroz"),("FEIJÃO","feijão"),("CARNE","carne"),("FRANGO","frango"),
        ("PÃO","pão"),("BOLO","bolo"),("FRUTA","fruta"),("LEITE","leite"),("SUCO","suco"),("ÁGUA","água")],
    "⭐ Respostas": [
        ("SIM","sim"),("NÃO","não"),("TALVEZ","talvez"),("POR FAVOR","por favor"),
        ("OBRIGADO","obrigado"),("DESCULPA","desculpa"),("OLÁ","olá"),("TCHAU","tchau"),
        ("NOVAMENTE","novamente"),("PARE","pare")]
}

frases_rapidas = [
    "Eu preciso de ajuda",
    "Eu quero água",
    "Eu estou com dor",
    "Eu quero ir embora",
    "Eu não estou bem"
]

class HomeScreen(Screen):
    frase = StringProperty("Escolha uma palavra ou frase")

    def on_pre_enter(self):
        from kivy.uix.button import Button
        box = self.ids.quick_box
        box.clear_widgets()
        for text in frases_rapidas:
            b = Button(text=text, size_hint=(None,1), width=dp(190), font_size="14sp")
            b.bind(on_release=lambda btn, t=text: self.frase_rapida(t))
            box.add_widget(b)

        cats = self.ids.categories
        cats.clear_widgets()
        for name in categorias:
            b = Button(text=name, size_hint_y=None, height=dp(105),
                       font_size="17sp", bold=True,
                       background_color=(0.10,0.46,0.82,1))
            b.bind(on_release=lambda btn, n=name: self.abrir_categoria(n))
            cats.add_widget(b)

    def adicionar(self, texto):
        if self.frase == "Escolha uma palavra ou frase":
            self.frase = texto
        else:
            self.frase += " " + texto

    def frase_rapida(self, texto):
        self.frase = texto

    def apagar(self):
        if self.frase not in ("", "Escolha uma palavra ou frase"):
            partes = self.frase.split()
            partes.pop()
            self.frase = " ".join(partes) if partes else "Escolha uma palavra ou frase"

    def limpar(self):
        self.frase = "Escolha uma palavra ou frase"

    def falar(self):
        texto = self.frase
        if not texto or texto == "Escolha uma palavra ou frase":
            return
        if tts:
            try:
                tts.speak(texto, 0, None, "comunicacao")
            except Exception:
                pass

    def abrir_categoria(self, nome):
        screen = self.manager.get_screen("category")
        screen.carregar(nome)
        self.manager.current = "category"


class CategoryScreen(Screen):
    titulo = StringProperty("Categoria")

    def carregar(self, nome):
        from kivy.uix.button import Button
        self.titulo = nome
        box = self.ids.words
        box.clear_widgets()

        for rotulo, texto in categorias[nome]:
            b = Button(
                text=rotulo,
                size_hint_y=None,
                height=dp(105),
                font_size="18sp",
                bold=True
            )
            b.bind(on_release=lambda btn, t=texto: self.selecionar(t))
            box.add_widget(b)

    def selecionar(self, texto):
        home = self.manager.get_screen("home")
        home.adicionar(texto)
        self.manager.current = "home"

    def voltar(self):
        self.manager.current = "home"


class ComunicacaoApp(App):
    title = "Minha Comunicação - CAA"

    def build(self):
        Window.clearcolor = (0.96, 0.97, 0.98, 1)
        return Builder.load_string(KV)

    def on_stop(self):
        global tts
        if tts:
            try:
                tts.shutdown()
            except Exception:
                pass


if __name__ == "__main__":
    ComunicacaoApp().run()
