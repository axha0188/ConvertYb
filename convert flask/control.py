#import eel
from pytube import YouTube
#---------------------------
class Yb():
    def Convert(self,url,op):
        try:
            link = YouTube(url)
            if op == '1':
                link.streams.filter(only_audio=True).first().download("./YbPy/audios")
            if op == '2':
                link.streams.first().download('./YbPy/Videos')
            self.msj = "Muchas gracias por su descarga"
            print(self.msj)
        except:
            self.msj = "Error al intentar convertir"
            print(self.msj)
            print("error")
