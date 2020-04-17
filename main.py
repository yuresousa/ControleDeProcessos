#!/usr/bin/env python3
# -*- coding: UTF-8 -*-

#-------------------------------------------------------------------------------
# Name:        main.py
# Purpose:
#
# Author:      Yure Sousa (yureabc@gmail.com)
#
# Created:     10/04/2020
# Copyright:   (c) Yure Sousa 2020
# Licence:     MIT
#-------------------------------------------------------------------------------
from maskedentry import *
from tkinter import *
from tkinter import scrolledtext
from processo import Processo

class main():
    def __init__(self,root=None):
        self.fontePadrao = ("Baskerville","12")
        self.fonteDois = ("Baskerville","15")


        #Laibel, 1 coluna
        self.master = Frame(root)
        self.master['padx']=50
        self.master['pady']=50
        self.master.pack(side=LEFT)

        self.sistema_label = Label(self.master,text='Sistema: ',font=self.fontePadrao,pady=7).grid(row=1,column=1,sticky=W)
        self.NumeroDoOficio_label = Label(self.master,text='Nª Do Ofício: ',font=self.fontePadrao,pady=7).grid(row=2,column=1,sticky=W)
        self.Empreendimento_label = Label(self.master,text='Empreendimento: ',font=self.fontePadrao,pady=7).grid(row=3,column=1,sticky=W)
        self.NumeroDoProcesso_label = Label(self.master,text='Nª Do Processo*:',font=self.fontePadrao,pady=7).grid(row=4,column=1,sticky=W)
        self.DataRecebimento_label = Label(self.master,text='Data De Receb.:',font=self.fontePadrao,pady=7).grid(row=5,column=1,sticky=W)
        self.Tipo_label = Label(self.master,text='Tipo:',font=self.fontePadrao,pady=7).grid(row=6,column=1,sticky=W)
        self.EncaminhamentoPara_label = Label(self.master,text='Encaminhado P/:',font=self.fontePadrao,pady=7).grid(row=7,column=1,sticky=W)
        self.DataDaVistoria_label = Label(self.master,text='Data Da Vistoria:',font=self.fontePadrao,pady=7).grid(row=8,column=1,sticky=W)
        self.PrazoParaLaudo_label = Label(self.master,text='Prazo Para Laudo:',font=self.fontePadrao,pady=7).grid(row=9,column=1,sticky=W)
        self.Observacoes_label = Label(self.master,text='Observações:',font=self.fontePadrao,pady=7).grid(row=10,column=1,sticky=W)


        #Entry, 2 coluna
        self.sistema_entry = Entry(self.master,background='white',foreground='black')
        self.sistema_entry.grid(row=1,column=2)
        self.NumeroDoOficio_entry = Entry(self.master,background='white',foreground='black')
        self.NumeroDoOficio_entry.grid(row=2,column=2)
        self.Empreendimento_entry = Entry(self.master,background='white',foreground='black')
        self.Empreendimento_entry.grid(row=3,column=2)
        self.NumeroDoProcesso_entry  = Entry(self.master,background='white',foreground='black')
        self.NumeroDoProcesso_entry.grid(row=4,column=2)
        self.DataRecebimento_entry  = MaskedWidget(self.master, 'fixed', mask='99/99/9999')
        self.DataRecebimento_entry.grid(row=5,column=2)
        self.Tipo_entry  = Entry(self.master,background='white',foreground='black')
        self.Tipo_entry.grid(row=6,column=2)
        self.EncaminhamentoPara_entry  = Entry(self.master,background='white',foreground='black')
        self.EncaminhamentoPara_entry.grid(row=7,column=2)
        self.DataDaVistoria_entry  = MaskedWidget(self.master, 'fixed', mask='99/99/9999')
        self.DataDaVistoria_entry.grid(row=8,column=2)
        self.PrazoParaLaudo_entry  = Entry(self.master,background='white',foreground='black')
        self.PrazoParaLaudo_entry.grid(row=9,column=2)
        self.Observacoes_entry  = Entry(self.master,background='white',foreground='black')
        self.Observacoes_entry.grid(row=10,column=2)
        linha = Label(self.master,text='Status:________________________________________',fg='gray',pady=4).grid(row=11,column=1,columnspan=2,sticky=W)
        self.status = Label(self.master,text='',pady=20,font=self.fonteDois,foreground='orange')
        self.status.grid(row=12,column=1,columnspan=2,sticky=W)


        #botoes, 3 coluna
        
        espaco = Label(self.master,text='      ').grid(row = 1,column=3)
        pesquisar = Button(self.master,text='Buscar',command=self.buscar).grid(row = 1,column=4)
        inserir = Button(self.master,text='Inserir',command=self.inserir).grid(row = 1,column=5)
        atualizar = Button(self.master,text='Atualizar',command=self.atualizar).grid(row = 1,column=6)
        apagar = Button(self.master,text='Excluir',command=self.excluir).grid(row = 1,column=7)

        limparCampos = Button(self.master,text='Limpar',padx=11,command=self.limparCampos).grid(row = 3,column=4)
        buscar_Todos = Button(self.master,text='   Buscar todos  ',command=self.buscar_Todos).grid(row = 3,column=5,columnspan=2)
        relatorio = Button(self.master,text='Relato.',command=self.relatorio,padx=11).grid(row = 3,column=7)

        self.display = scrolledtext.ScrolledText(self.master,width=35,height=15,fg='black')
        self.display.grid(row=6,column=4,columnspan=4,rowspan=9)
        self.display.insert(INSERT,"Nota:\n  ")

        
    def inserir(self):
        processo = Processo()
        
        if len(self.NumeroDoProcesso_entry.get()):
            processo.Sistema = self.sistema_entry.get()
            processo.Empreendimento = self.Empreendimento_entry.get()
            processo.NumeroDoProcesso = self.NumeroDoProcesso_entry.get()  
            processo.DataRecebimento = self.DataRecebimento_entry.get() 
            processo.Tipo = self.Tipo_entry.get()  
            processo.EncaminhamentoPara = self.EncaminhamentoPara_entry.get()
            processo.DataDaVistoria = self.DataDaVistoria_entry.get()
            processo.PrazoParaLaudo = self.PrazoParaLaudo_entry.get()
            processo.NumeroDoOficio = self.NumeroDoOficio_entry.get()
            processo.Observacoes = self.Observacoes_entry.get()

            self.status['text'] = processo.adcionarProcesso()
        else:

            self.status['text'] = "Erro_Campo vazio"
             

        self.limparCampos()
    
    def buscar(self):
        processo = Processo()

        if len(self.NumeroDoProcesso_entry.get()):
            processo.NumeroDoProcesso = self.NumeroDoProcesso_entry.get()

            self.status['text'] = processo.consultar()

            self.limparCampos()
            self.sistema_entry.insert(INSERT,processo.Sistema)
            self.Empreendimento_entry.insert(INSERT,processo.Empreendimento)      
            self.NumeroDoProcesso_entry.insert(INSERT,processo.NumeroDoProcesso)
            self.DataRecebimento_entry.insert(0,re.sub('[^0-9]','',processo.DataRecebimento))
            self.Tipo_entry.insert(INSERT,processo.Tipo)
            self.EncaminhamentoPara_entry.insert(INSERT,processo.EncaminhamentoPara)
            self.DataDaVistoria_entry.insert(0,re.sub('[^0-9]','',processo.DataDaVistoria))
            self.PrazoParaLaudo_entry.insert(INSERT,processo.PrazoParaLaudo)
            self.NumeroDoOficio_entry.insert(INSERT,processo.NumeroDoOficio)
            self.Observacoes_entry.insert(INSERT,processo.Observacoes)
        else:
            self.status['text'] = "Erro_Campo vazio"
            self.limparCampos()


    def buscar_Todos(self):

        processo = Processo()

        dados_brutos = processo.consultar_todos()
     
    
        pop = Toplevel(width=700,height=700)
        pop.title("Processos cadastrados")
        pop.geometry("500x500+300+150")
        scrollbar = Scrollbar(pop)
        scrollbar.pack( side = RIGHT, fill = Y )
        lista = Listbox(pop, yscrollcommand = scrollbar.set,font=('Helvetica','12'))
   
      #  lista.insert(END,'   Sistema | Empreendimento | NumeroDoProcesso | DataRecebimento | Tipo | EncaminhamentoPara | DataDaVistoria | PrazoParaLaudo | NumeroDoOficio | Observacoes'.upper())        
        numDeLinha = 0
        lista.insert(END,' ')
        for linha in dados_brutos:
            numDeLinha +=1
            for r in "()''":
                linha = str(linha).replace(r,"")
            lista.insert(END," "+str(numDeLinha)+"ª  "+linha.replace(',',"   |   ").upper())
            lista.insert(END," ")
            lista.insert(END," ")

    
        lista.pack(fill=BOTH,expand=1)
        scrollbar.config( command = lista.yview )



    def excluir(self):
        processo = Processo()

        if len(self.NumeroDoProcesso_entry.get()):
            processo.NumeroDoProcesso = self.NumeroDoProcesso_entry.get()

            self.status['text'] = processo.excluir()

        else:
            self.status['text'] = "Erro_Campo vazio"
    
        self.limparCampos()

    def atualizar(self):
        processo = Processo()
        if len(self.NumeroDoProcesso_entry.get()):

            processo.Sistema = self.sistema_entry.get()
            processo.Empreendimento = self.Empreendimento_entry.get()
            processo.NumeroDoProcesso = self.NumeroDoProcesso_entry.get()  
            processo.DataRecebimento = self.DataRecebimento_entry.get() 
            processo.Tipo = self.Tipo_entry.get()  
            processo.EncaminhamentoPara = self.EncaminhamentoPara_entry.get()
            processo.DataDaVistoria = self.DataDaVistoria_entry.get()
            processo.PrazoParaLaudo = self.PrazoParaLaudo_entry.get()
            processo.NumeroDoOficio = self.NumeroDoOficio_entry.get()
            processo.Observacoes = self.Observacoes_entry.get()

            self.limparCampos()

            self.status['text'] =  processo.editar()
        else:
            self.status['text'] =  "Erro_Campo vazio "

    def limparCampos(self):
        self.sistema_entry.delete(0,END)
        self.Empreendimento_entry.delete(0,END)
        self.NumeroDoProcesso_entry.delete(0,END)      
        self.DataRecebimento_entry.insert(0,'00000000')
        self.Tipo_entry.delete(0,END)
        self.EncaminhamentoPara_entry.delete(0,END)       
        self.DataDaVistoria_entry.insert(0,'00000000')  
        self.PrazoParaLaudo_entry.delete(0,END)        
        self.NumeroDoOficio_entry.delete(0,END)
        self.Observacoes_entry.delete(0,END) 

    def relatorio(self):
        Toplevel()

root = Tk()

#configuracoes tkinter
root.geometry("720x500+300+100")
root.resizable(0,0)
root.title("Controle de Processos")
img = PhotoImage(file="./img/icone.gif")
root.tk.call('wm', 'iconphoto',root._w, img)


main(root)

root.mainloop()