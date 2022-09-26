def atualiza(): 
    
    alter_meiri.show()
    tela_login.hide()

    cursor = connect.cursor()
    sql = "Select * from cadastro"
    cursor.execute(sql)

    leitura_sql = cursor.fetchall()

    alter_meiri.tableWidget.setRowCount(len(leitura_sql))
    alter_meiri.tableWidget.setColumnCount(9)

    for i in range(0, len(leitura_sql)):
        for j in range(0, 9):
            alter_meiri.tableWidget.setItem(i, j, QtWidgets.QTableWidgetItem(str(leitura_sql[i][j])))

def excluir_dados(): 

    linha =  alter_meiri.tableWidget.currentRow()
    alter_meiri.tableWidget.removeRow(linha)

    cursor = connect.cursor()
    cursor.execute('SELECT id FROM cadastro')
    execute_sql = cursor.fetchall()
    valor_id = execute_sql[linha][0]
    cursor.execute("DELETE FROM cadastro WHERE id = " + str(valor_id))
