from tkinter import *

class GUI(Tk):
    def __init__(self):
        super().__init__()
        self.title("AutoNumX")
        self.Stand= StringVar()
        self.Stand.trace("w", self.Verify)
        self.pacientef= self.Form("Digite o nome do paciente:")
        self.pathf= self.Form("Cole o caminho da pasta: ")
        self.alinf= self.Form("Digite a quantidade de alinhadores: Sup-Inf")
        label= Label(self, text="Tem attach? ", fg="white",bg="orange", font="Arial 25 bold")
        self.labelatt= label
        self.startf= self.Form("Digite o Começo-Fim: (Deixe vazio se não houver)")
        self.startf["entry"]["textvariable"]= self.Stand
        label.pack(pady="10px")
        string= StringVar(self)
        string.set("Selecione uma opção: ")
        entrada= OptionMenu(self, string, *["Superior","Inferior","Ambas","Não tem"], command= self.change)
        entrada.pack(pady="10px")
        self.enter= entrada
        self.config(bg="orange", pady="10px", padx="10px")
        self.btn= Button(self, text="Processar", bg="green", fg="white", font= "Arial 18 bold", command= self.End)
        self.btn.pack(pady="5px")
        self.mainloop()
    def change(self, att):
        self.att= att
    def Verify(self, *args):
        if(self.Stand.get() == "" or "1-" in self.Stand.get()):
            self.btn.pack_forget()
            self.labelatt.pack(pady="10px")
            self.enter.pack(pady="10px")
            self.btn.pack(pady="5px")
        else:
            self.enter.pack_forget()
            self.labelatt.pack_forget()
    def Form(self, text):
        label= Label(self, text=text, fg="white",bg="orange", font="Arial 25 bold")
        label.pack(pady="10px")
        entrada= Entry(self, font="Arial 18 bold", justify="center")
        entrada.pack(pady="10px")

        return {
            "text": label,
            "entry": entrada
            }
    def End(self):
        self.path= self.pathf["entry"].get()
        self.paciente= self.pacientef["entry"].get()
        self.sup, self.inf= self.alinf["entry"].get().split("-")
        self.sup = int(self.sup)
        try:
            self.start, self.end= self.startf["entry"].get().split("-")
        except Exception:
            self.start= 1
            self.end= ""
        self.inf= int(self.inf)
        try:
            testar= "" + self.att
        except Exception:
            self.att= "Não tem"
        self.destroy()
