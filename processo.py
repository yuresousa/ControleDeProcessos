from banco import Banco

class Processo():

    def __init__(self,Sistema='',NumeroDoOficio='',Empreendimento='',NumeroDoProcesso='',DataRecebimento='',Tipo='',EncaminhamentoPara='',DataDaVistoria ='',PrazoParaLaudo='',Observacoes=''):
        self.Sistema = Sistema
        self.NumeroDoOficio = NumeroDoOficio
        self.Empreendimento = Empreendimento
        self.NumeroDoProcesso = NumeroDoProcesso
        self.DataRecebimento = DataRecebimento
        self.Tipo = Tipo
        self.EncaminhamentoPara = EncaminhamentoPara
        self.DataDaVistoria = DataDaVistoria
        self.PrazoParaLaudo = PrazoParaLaudo
        self.Observacoes = Observacoes

    def adcionarProcesso(self):
        
        conecta = Banco()
        c = conecta.conexao.cursor()
        try:
            c.execute("insert into ControleDeProcessos(Sistema,NumeroDoOficio,Empreendimento,NumeroDoProcesso,DataRecebimento,Tipo,EncaminhamentoPara,DataDaVistoria,PrazoParaLaudo,Observacoes) values('"+
            self.Sistema+"','"+self.NumeroDoOficio+"','"+self.Empreendimento+"','"+self.NumeroDoProcesso+"','"+self.DataRecebimento+"','"+self.Tipo+"','"+self.EncaminhamentoPara+"','"+self.DataDaVistoria+"','"+self.PrazoParaLaudo+"','"+self.Observacoes+"')")
        except:
            return "Processo já cadastrado"
        c.close()
        conecta.conexao.commit()
        return "Cadastrado feito com sucesso!"
#consultar todos os processos
    def consultar(self):
        conecta = Banco()
        c = conecta.conexao.cursor()
        c.execute('select * from ControleDeProcessos where NumeroDoProcesso="'+self.NumeroDoProcesso+'"')

        for linha in c:
            self.Sistema = linha[0]
            self.NumeroDoOficio  = linha[1]
            self.Empreendimento = linha[2]
            self.NumeroDoProcesso = linha[3]
            self.DataRecebimento = linha[4]
            self.Tipo  = linha[5]
            self.EncaminhamentoPara  = linha[6]
            self.DataDaVistoria  = linha[7]
            self.PrazoParaLaudo = linha[8]
            self.Observacoes = linha[9]
            
            c.close()
            return "Consulta realizada com sucesso."
        c.close()  
        return 'Processo não cadastrado.'
        
    def consultar_todos(self):
        conecta = Banco()
        c = conecta.conexao.cursor()
        c.execute('select * from ControleDeProcessos')
        lista = []
        for linha in c:
            lista.append(linha)
        
        c.close()
        return lista

        
#consultar com filtro
    def filtro(self,filtro):
        pass

#editar
    def editar(self):
        conecta = Banco()
        c = conecta.conexao.cursor()
        c.execute('update ControleDeProcessos set Sistema="'+self.Sistema+'",NumeroDoOficio="'+self.NumeroDoOficio+'",Empreendimento="'+self.Empreendimento+'",NumeroDoProcesso="'+self.NumeroDoProcesso+'",DataRecebimento="'+self.DataRecebimento+'",Tipo="'+self.Tipo+'",EncaminhamentoPara="'+self.EncaminhamentoPara+'",DataDaVistoria="'+self.DataDaVistoria+'",PrazoParaLaudo="'+self.PrazoParaLaudo+'",Observacoes="'+self.Observacoes+'" where NumeroDoProcesso="'+self.NumeroDoProcesso+'"')
        conecta.conexao.commit() 
        c.close()  
        return "Atualizado com sucesso"
        
#excuir
    def excluir(self):
        
        conecta = Banco()
        c = conecta.conexao.cursor()
        c.execute('delete from ControleDeProcessos where NumeroDoProcesso="'+self.NumeroDoProcesso+'"')
        c.close()
        conecta.conexao.commit()
        return "Excluido com sucesso!"
