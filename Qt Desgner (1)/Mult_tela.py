from PyQt5 import uic, QtWidgets #biblioteca 
import mysql.connector 
   
conexao = mysql.connector.connect(
        host='localhost',
        user='root',
        password='202173',
        database='kitton_info'
    )

def chama_login_fucionario(): #Operação de chama a tela de login de funcionario
    inicial.hide() #esconder tela inicial
    login1.show() #Aparecer tela de login 
   
def chama_cadastro_produto(): #Operação de chama a tela de cadastro de produto
   
    global nome_id
    
    nome_id= login1.id.text()
    senha= login1.senha.text()
    
    cursor = conexao.cursor ()
    
    ver=("select id, cpf from funcionario where id ='{}' and cpf = '{}'".format(nome_id,senha))
    
    cursor.execute (ver)

    for (id, cpf) in cursor:
        if  nome_id == id or senha == cpf:
            login1.hide() #esconder tela de login funcionario
            cadaspro.show() #aparecer tela de cadastro de produto
            nome_id= login1.id.setText("")
            senha= login1.senha.setText("")
        else:
            login1.id.setText("Nome de usuario ou senha incorretas")
            nome_id= login1.id.setText("")
            senha= login1.senha.setText("")

def cadastra_produto():
    nome= cadaspro.nome_pro.text()
    categoria= cadaspro.categoria.currentText()
    fornecedor= cadaspro. fonercedor_pro.text()
    custo_fabrica= cadaspro.custo_fab.text()
    funcionario= cadaspro.fun.currentText()
    valor_venda= cadaspro.val_venda.text()
            
    inserir2= "insert into cadastro_produto (cod, nome, categoria, fornecedor, custo_fabrica, funcionario, valor_venda) values (null,%s,%s,%s,%s,%s,%s)"
    val2=(nome, categoria, fornecedor, custo_fabrica, funcionario, valor_venda)
            
    cursor = conexao.cursor ()
    cursor.execute (inserir2,val2)
    conexao.commit()
    
    cadaspro.nome_pro.setText("")
    cadaspro.categoria.setCurrentText("Selecione")
    cadaspro. fonercedor_pro.setText("")
    cadaspro.custo_fab.setText("")
    cadaspro.fun.setCurrentText("Selecionar Funcionario")
    cadaspro.val_venda.setText("")
    cursor.close()
    
def chama_configuracao():
    cadaspro.hide()
    configuracao.show()  
    
    cursor = conexao.cursor()
    ler="select * from cadastro_produto"
    cursor.execute(ler)
    dados= cursor.fetchall()
    configuracao.tableWidget.setRowCount(len(dados))
    configuracao.tableWidget.setRowCount(7)
    
    for i in range(0, len(dados)):
        for j in range (0,7):
            configuracao.tableWidget.setItem(i,j,QtWidgets.QTableWidgetItem(str(dados[i][j])))

    
def pesquisa_produto():
    
    cursor = conexao.cursor()
    pesquisa= configuracao.pesquisa.text()
    verificar= "select * from cadastro_produto where cod = '{}'".format(pesquisa)
    cursor.execute(verificar)
    dados= cursor.fetchall()
    configuracao.tableWidget.setRowCount(len(dados))
    configuracao.tableWidget.setRowCount(7)
    
    for i in range(0, len(dados)):
        for j in range (0,7):
            configuracao.tableWidget.setItem(i,j,QtWidgets.QTableWidgetItem(str(dados[i][j])))
            
def pesquisa_produto2():
    cursor = conexao.cursor()
    pesquisa2= configuracao.categoria.currentText()
    verificar= "select * from cadastro_produto where categoria = '{}'" .format(pesquisa2)
    cursor.execute(verificar)
    dados= cursor.fetchall()
    configuracao.tableWidget.setRowCount(len(dados))
    configuracao.tableWidget.setRowCount(7)
    
    for i in range(0, len(dados)):
        for j in range (0,7):
            configuracao.tableWidget.setItem(i,j,QtWidgets.QTableWidgetItem(str(dados[i][j])))

def alter_table():
    
   cod=configuracao.cod_pro.text()
   nome=configuracao.nome_pro_alt.text()
   fornecedor=configuracao.fornecedor_alt.text()
   custo_fab=configuracao.custo_fab_alt.text()
   valor_ved=configuracao.valor_ved_alt.text()
   
   cursor = conexao.cursor()
   alt="UPDATE cadastro_produto SET nome = '{}', fornecedor = '{}', custo_fabrica = '{}', valor_venda = '{}' where cod = '{}' ".format (nome,fornecedor,custo_fab,valor_ved, cod)
   cursor.execute(alt)
     
def chama_login_cliente(): #Operação de chama a tela de login do cliente
    inicial.hide() #esconder tela inicial 
    login2.show() #Aparecer tela de login do cliente

def chama_cadastro(): #Operação chama tela de cadastro do cliente
    login2.hide() #Esconder tela de login do cliente
    cadas1.show() #aparecer tela de cadastro cliente

def chama_venda(): #Operação chama tela de venda 
    
    global email1
    email1=login2.email_campo.text()
    senha2=login2.senha_campo.text()
    cursor=conexao.cursor()
    
    ver2=("select email, senha from cadastro where email ='{}' and senha = '{}'".format(email1,senha2))
    cursor.execute(ver2)
    
    for (email, senha) in cursor:
        if  email == email1 and senha == senha2:
            login1.hide() #esconder tela de login funcionario
            venda.show() #aparecer tela de cadastro de produto
            email1=login2.email_campo.setText("")
            senha2=login2.senha_campo.setText("")
        elif email != email1:
            login2.email_campo.setText("Nome de usuario ou senha incorretas")
        else:
            login2.email_campo.setText("Nome de usuario ou senha incorretas")
            

            
def cadastro_cliente(): #Operação voltar a tela de login cliente 
   
    cpf=cadas1.cpf_campo.text()
    nome=cadas1.nome_campo.text()
    data_nasc=cadas1.datanas_campo.text()
    tel=cadas1.contato_campo.text()
    cep=cadas1.cep_campo.text()
    rua=cadas1.rua_campo.text()
    bairro=cadas1.bairro_campo.text()
    cidade=cadas1.cidade_campo.text()
    uf=cadas1.uf_campo.text()
    num_casa=cadas1.numero_campo.text()
    email= cadas1.email_campo.text()
    senha=cadas1.senha_campo.text()
    
    inserir="insert into cadastro (cpf,nome,data_nasc,tel,cep,rua,bairro,cidade,uf,num_casa,email,senha) VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"
    val=(cpf, nome, data_nasc,tel, cep, rua, bairro, cidade, uf, num_casa,email,senha)
    
    cursor = conexao.cursor ()
    cursor.execute (inserir,val)
    conexao.commit()
    
    cadas1.cpf_campo.setText("")
    cadas1.nome_campo.setText("")
    cadas1.datanas_campo.setText("")
    cadas1.contato_campo.setText("")
    cadas1.cep_campo.setText("")
    cadas1.rua_campo.setText("")
    cadas1.bairro_campo.setText("")
    cadas1.cidade_campo.setText("")
    cadas1.uf_campo.setText("")
    cadas1.numero_campo.setText("")
    cadas1.email_campo.setText("")
    cadas1.senha_campo.setText("")
    
    cursor.close()
    
    cadas1.hide()
    login2.show()
    

def voltar_tela_inicial(): #Operação para voltar tela inicial
    cadaspro.hide() #esconder tela de cadostro de produto
    inicial.show() #aparecer tela inicial
    
def voltar_tela_inicial2(): #Operação para volatar tela inicial 2
    venda.hide() #escoder tela de venda
    inicial.show() #aparecer tela inicial

app= QtWidgets.QApplication ([]) #funções do PyQt5 

inicial=uic.loadUi("tela_inicial.ui") #link da tela inicial 
login1=uic.loadUi("tela_login_f.ui") #link da tela de login funcionario
cadas1=uic.loadUi("tela_cadastro.ui") #link da tela de cadastro de cliente
cadaspro=uic.loadUi("tela_cadastro_produto.ui") #link tela de cadastro de produto
login2=uic.loadUi("tela _login_c.ui") #link tela de login cliente 
venda=uic.loadUi("tela_venda.ui") #link tela de vendas
configuracao=uic.loadUi("tela_configuracao.ui")

inicial.botaofun.clicked.connect(chama_login_fucionario) # ação do botão da tela de login funcionario, para proxima tela. 
inicial.botaocli.clicked.connect(chama_login_cliente) #ação do botão da tela de login cliente, para próxima tela.
login2.botaocad1.clicked.connect(chama_cadastro) #ação do botão da tela de cadastro do cliente, para próxima tela.
login1.botaolo.clicked.connect(chama_cadastro_produto) # ação botão da tela de cadastro do produto, para próxima tela.
login2.botaolo.clicked.connect(chama_venda) #ação botão da tela de vendas, para próxima tela.
cadas1.botaocad.clicked.connect(cadastro_cliente) #ação do botão para voltar na tela de login de cliente, para volatar a tela.
cadaspro.botaomenu.clicked.connect(cadastra_produto) #ação do botão para voltara tela inicial, para volatar a tela.
cadaspro.botao_configuracao.clicked.connect(chama_configuracao)
cadaspro.Button_Cadastrar.clicked.connect(cadastra_produto)
venda.botaomenu.clicked.connect(voltar_tela_inicial2)#ação do botão para voltara tela inicial 2, para volatar a tela.
configuracao.botao_pesquisa.clicked.connect(pesquisa_produto)
configuracao.botao_pesquisa.clicked.connect(pesquisa_produto2)
configuracao.botao_alt.clicked.connect(alter_table)

inicial.show() #iniciar programa
app.exec() #executar o programa 