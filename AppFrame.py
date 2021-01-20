## ********** FuhrerhLemon ********* ##
import wx
import knowledgegraph

class Grafo(wx.Frame):
    def __init__(self, parent, id, title):
        wx.Frame.__init__(self, parent, id, title)
        self.PhotoMaxSize = 400
        self.img = wx.EmptyImage(700, 450)
        self.titulo = wx.StaticText(self, label = "Ingresa el parrafo:", pos=(20,60))
        self.text = wx.TextCtrl(self, value = '', pos=(150, 60), size=(140,-1))
        self.image = wx.StaticBitmap(self, 
                                     wx.ID_ANY,
                                     wx.BitmapFromImage(self.img))
        self.Enviar = wx.Button(self, -1, u'Enviar Texto')
        self.__do_layout()
        self.__set_properties()
        self.__set_event()
     
    # Tamaño, posicion de los elementos
    def __do_layout(self):
        sizer_1 = wx.BoxSizer(wx.VERTICAL)
        sizer_2 = wx.BoxSizer(wx.HORIZONTAL)
        sizer_1.Add(self.titulo, 0, wx.EXPAND|wx.ALL, 5)
        sizer_1.Add(self.text, 0, wx.EXPAND|wx.ALL, 5)
        sizer_2.Add(self.image, 1, wx.EXPAND|wx.RIGHT, 0)
        sizer_2.Add(self.Enviar, 0, wx.ALL, 10)
        sizer_1.Add(sizer_2, 0, wx.ALL, 5)
        
        self.SetSizer(sizer_1)
        self.Layout()
     
    # Esta función establecerá las propiedades a los elementos
    def __set_properties(self):
        self.SetSize( (810, 600) )
        self.Enviar.SetBackgroundColour( wx.Colour(182, 39, 171) )
        self.text.SetFont( wx.Font(12, wx.DEFAULT, wx.NORMAL, wx.NORMAL) )
        self.titulo.SetFont( wx.Font(18, wx.DEFAULT, wx.NORMAL, wx.NORMAL) )
    
    # Eventos de los botones
    def __set_event(self):
        self.Bind(wx.EVT_BUTTON, self.enviar, self.Enviar)
     
    def enviar(self, event):
        data = self.text.GetValue()
        knowledgegraph.main(data)
        self.viwImg()
        event.Skip()
        
    def viwImg(self):
        img = 'KnowledgeGraph.jpg'
        self.image.SetBitmap(wx.BitmapFromImage(img))
        self.panel.Refresh()
        
if __name__ == '__main__':
    app = wx.App(0)
    frame = Grafo(None, -1, 'KnowLedge Graph')
    frame.Show()
    app.MainLoop()