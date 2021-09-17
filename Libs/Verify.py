import os
import shutil
from tkinter import *
from tkinter import ttk
from tkinter import messagebox
import time

class Verify:
        def __init__(self,master):
                self.master= master
                self.setVars()
		
        def setVars(self):
                self.master.tree= {}
                self.GUI= Tk()
                self.GUI.config(bg="orange", pady="15px", padx="15px")
                self.label= Label(self.GUI, text="Contando alinhadores... 0%", font="Arial 18", fg="white", bg="orange", width=50)
                self.label.pack(pady="5px")
                self.Barra= ttk.Progressbar(self.GUI, mode="determinate", orient="horizontal", length= 100)
                self.Barra.pack(pady="10px")
                self.MoM()
                self.setBar("Criando caminhos e Comparativos... 20%",20)
                self.master.maiorcpy= self.master.maior
                self.master.menorcpy= self.master.menor
                self.CondVars()
                self.setBar("Verificando arquivos na pasta... 40%",40)
                self.VerifyFiles()
                self.setBar("Movendo e Renomeando arquivos STL... 60%",60)
                self.Move()
                self.setBar("Deletando pastas... 80%",80)
                self.RmDirs()
                self.setBar("Finalizando... 99%",99)
                self.Destruct()
                self.GUI.mainloop()
        def Update(self):
                time.sleep(1)
                self.GUI.update()
        def Destruct(self):
                self.GUI.destroy()
        def AnalyseDirs(self):
                self.setBar("Contando diretórios... 30%",30)
                while len(os.listdir(self.master.path)) < self.master.quantDocs:
                        self.GUI.update()
        def GetPaths(self):
                temp= {}
                aux= 0
                print("Vinculando caminhos")
                if(self.master.maiorcpy > int(self.master.maior)):
                        aux= 1
                        for i in os.listdir(self.master.path):
                                try:
                                        int(i[i.index("Subsetup") + 8])
                                except Exception:
                                        shutil.rmtree(self.master.path + "\\" + i)
                                        break
                for i in os.listdir(self.master.path):
                        try:
                                int(i[i.index("Subsetup") + 8])
                                pos1= i[i.index("Subsetup") + 8]
                        except Exception:
                                temp[int(self.master.maior)] = self.master.path + "\\" + i
                                continue
                        try:
                                int(i[i.index("Subsetup") + 9])
                                pos2= i[i.index("Subsetup") + 9]
                        except Exception:
                                temp[int(pos1)]= self.master.path + "\\" + i
                                continue
                        if(pos1 == self.master.maior):
                                temp[int(pos1)]= self.master.path + "\\" + i
                                continue
                        posR= int(pos1 + pos2)
                        temp[posR] = self.master.path + "\\" + i
                for i in range(1,int(self.master.start)):
                        try:
                                shutil.rmtree(temp[i])
                                temp.pop(i)
                        except Exception:
                                continue
                if(aux == 1):
                        for i in range(int(self.master.maior) + 1, int(self.master.maiorcpy) + 1):
                                try:
                                        shutil.rmtree(temp[i])
                                        temp.pop(i)
                                except Exception:
                                        continue

                return temp
                        
        def CondVars(self):
                if(self.master.end == ""):
                        self.master.end= self.master.maior
                if(int(self.master.start) != 1):
                        self.master.att= "Não tem"
                if(self.master.end != self.master.maior):
                        self.master.maior= self.master.end
                '''if(self.master.menor != self.master.start):
                        self.master.menor = self.master.start'''
                self.master.quantDocs= int(self.master.end) - int(self.master.start) + 1

                indmaior= self.master.tmaior.split(".")
                indmaior= indmaior[0]
                indmaioraatt= indmaior[0] + "_with_attachments.stl"
                indmenor= self.master.tmenor.split(".")
                indmenor= indmenor[0]
                indmenoraatt= indmaior[0] + "_with_attachments.stl"

                self.AnalyseDirs()
                self.master.map= self.GetPaths()
                        
                for i in range(int(self.master.start), int(self.master.maior) + 1):
                        self.master.tree[i]= {}

                for i in range(int(self.master.start), int(self.master.maior) + 1):
                        self.master.tree[i][indmaior]= self.master.map[i] + "\\" + self.master.tmaior
                        
                if(self.master.menor == 0):
                        pass
                else:
                        for i in range(int(self.master.start), int(self.master.menor) + 1):
                                self.master.tree[i][indmenor]= self.master.map[i] + "\\" + self.master.tmenor
                        
                if(int(self.master.start) == 1):
                        self.master.tree[0]= {}
                        if(self.master.att == "Superior"):
                                self.master.tree[0]["Maxillary"] = self.master.map[1] + "\\Maxillary_with_attachments.stl"
                        elif(self.master.att == "Inferior"):
                                self.master.tree[0]["Mandibular"] = self.master.map[1] + "\\Mandibular_with_attachments.stl"
                        elif(self.master.att == "Ambas"):
                                self.master.tree[0]["Maxillary"] = self.master.map[1] + "\\Maxillary_with_attachments.stl"
                                self.master.tree[0]["Mandibular"] = self.master.map[1] + "\\Mandibular_with_attachments.stl"
                        else:
                                pass
                else:
                        pass
                try:
                        if(self.master.tree[0] == {}):
                                self.master.tree.pop(0)
                except Exception:
                        pass
                aux2= 0
                for i in self.master.tree:
                        for p in self.master.tree[i]:
                                aux2 += 1
                self.master.quantFiles= aux2
                print(self.master.tree)

        def VerifyFiles(self):
                print("Verificando arquivos")
                for i in self.master.tree:
                        for p in self.master.tree[i]:
                                while not os.path.isfile(self.master.tree[i][p]):
                                        continue
        def RmDirs(self):
                print("Removendo diretorios")
                for i in os.listdir(self.master.path):
                        if(os.path.isdir(self.master.path + "\\" + i)):
                                try:
                                        os.rmdir(self.master.path + "\\" + i)
                                except Exception:
                                        messagebox.showwarning(title= "Atenção",message="Existe uma pasta com modelos, por favor confira-se colocou a quantidade certa no formulário")
                                        continue
                                        
        def Move(self):
                print("Renomeando arquivos")
                for i in self.master.tree:
                        for p in self.master.tree[i]:
                                os.rename(self.master.tree[i][p], self.master.path + "\\" + self.master.paciente + " " + str(p) + " " + str(i) + ".stl")
        def setBar(self, txt, valor):
                self.label["text"] = txt
                self.Barra["value"] = valor
                self.Update()
        def MoM(self):
                master= self.master
                if(master.sup > master.inf):
                        master.maior= master.sup
                        master.menor= master.inf
                        master.tmaior= "Maxillary.stl"
                        master.tmenor= "Mandibular.stl"
                else:
                        master.maior= master.inf
                        master.menor= master.sup
                        master.tmaior= "Mandibular.stl"
                        master.tmenor= "Maxillary.stl"
                if(self.master.end == ""):
                        master.end= master.maior
                if(int(master.menor) > int(master.end)):
                        master.menor= master.end
