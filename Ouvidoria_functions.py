import mysql.connector

class Commands:
    conexao = mysql.connector.connect(
        host = "localhost",
        user = "root",
        password = "root",
        database = "bancodedados")
    
    cursor = conexao.cursor()
    
    def __init__(self):
        pass
    
    def insert(self,ocorrencia,texto): #ok
        
        CommandSql = "insert into dados (ocorrencia,texto) values (%s,%s)"   
        data=(ocorrencia,texto)

        self.cursor.execute(CommandSql,data)
        self.conexao.commit()   

    def listing(self,ocorrencia):

        CommandSql = f"select * from dados where ocorrencia = '{ocorrencia}'"

        self.cursor.execute(CommandSql)

        results = self.cursor.fetchall()
        if len(results) == 0:            
            print('Não há dados!')

        for data in results:  
            print(f" ID:{data[0]}  Nome:{data[1]} <<Ocorrência:{data[2]}>>  >> Comentário: {data[3]}")

    def listingAll(self):

        CommandSql = f"select * from dados"

        self.cursor.execute(CommandSql)

        results = self.cursor.fetchall()
        if len(results) == 0:            
            print('Não há dados!')

        for data in results:  
             print(f" ID:{data[0]}  Nome:{data[1]} <<Ocorrência:{data[2]}>>  >> Comentário: {data[3]}")

    def delete(self,ocorrencia):

        CommandSql = f"DELETE FROM dados WHERE ocorrencia = '{ocorrencia}'"
        
        self.cursor.execute(CommandSql)
        self.conexao.commit()

    def deleteAll(self):

        CommandSql = 'TRUNCATE TABLE dados;' 

        self.cursor.execute(CommandSql)       
        self.conexao.commit()     

    def deleteID(self,id):

        CommandSql = f"DELETE FROM dados WHERE id = {id}"

        self.cursor.execute(CommandSql)
        self.conexao.commit()

    def change(self,texto,id):
        
        CommandSql = "UPDATE dados SET texto = %s WHERE id = %s"
        data=(texto,id)

        self.cursor.execute(CommandSql,data)
        self.conexao.commit()
    