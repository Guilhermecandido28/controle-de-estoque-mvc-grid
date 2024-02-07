from infra_db.configs.connection import DBConnection
from infra_db.entities.tabelas import *
from sqlalchemy.orm.exc import NoResultFound
from typing import Type, Dict, Union

class Repository:
    def __init__(self, Tabela: Type) -> None:
        """
        Inicializa o repositório com a tabela especificada.

        Args:
            Tabela (Type): A classe que representa a tabela no banco de dados.
        """
        self.tabela = Tabela

    def select(self):
        """
        Seleciona todos os registros da tabela.

        Returns:
            List: Uma lista contendo todos os registros da tabela.
        """
        with DBConnection() as db:
            data = db.session.query(self.tabela).all()
            return data
        
    def select_filter(self, coluna: str, filtro: str):
        """
        Seleciona registros da tabela com base em um filtro aplicado a uma coluna específica.

        Args:
            coluna (str): O nome da coluna na tabela que será usada como filtro para a seleção.
            filtro (str): O valor que será usado para filtrar os registros na coluna especificada.

        Returns:
            List: Uma lista contendo os registros da tabela que correspondem ao filtro aplicado.

        Example:
            # Selecionar todos os registros onde a coluna "nome" é igual a "João"
            repositorio.select_filter("nome", "João")
        """
        with DBConnection() as db:
            try:
                data = db.session.query(self.tabela).filter(self.tabela.__dict__[coluna].like(f"%{filtro}%")).all()
                return data
            except NoResultFound:
                return None
        
    def insert(self, colunas: Dict):
        """
        Insere um novo registro na tabela.

        Args:
            colunas (Dict): Um dicionário onde as chaves são os nomes das colunas e os valores são os valores
                            correspondentes que serão inseridos na tabela.
        """
        with DBConnection() as db:
            try:
                data_insert = self.tabela(**colunas)
                db.session.add(data_insert)
                db.session.commit()
            except Exception as ex:
                db.session.rollback()
                raise ex

    def delete(self, filtro: str, palavra_chave: Union[str, int, float, bytes]):
        """
        Exclui registros da tabela com base em um filtro e uma palavra-chave fornecidos.

        Args:
            filtro (str): O nome da tabela e da coluna na tabela, por exemplo: Tabela.coluna, onde a Tabela é o descritivo da tabela do banco de dados e a coluna que será usada como filtro para a exclusão.
            palavra_chave (Union[str, int, float, bytes]): O valor que será usado para filtrar os registros na tabela.
                Pode ser uma string, um inteiro, um float ou um objeto de bytes, dependendo do tipo de dado
                da coluna na tabela.
        """
        with DBConnection() as db:
            try:            
                db.session.query(self.tabela).filter(filtro == palavra_chave).delete()
                db.session.commit()
            except Exception as ex:
                db.session.rollback()
    
    def update(self, filtro: str, palavra_chave: Union[str, int, float, bytes], novos_dados: Dict):
        """
        Atualiza registros na tabela com base em um filtro e uma palavra-chave fornecidos.

        Args:
            filtro (str): O nome da coluna na tabela que será usada como filtro para a atualização.
            palavra_chave (Union[str, int, float, bytes]): O valor que será usado para filtrar os registros na tabela.
                Pode ser uma string, um inteiro, um float ou um objeto de bytes, dependendo do tipo de dado
                da coluna na tabela.
            novos_dados (Dict): Um dicionário onde as chaves são os nomes das colunas e os valores são os novos valores
                                que serão atualizados na tabela para os registros correspondentes ao filtro.
        """
        with DBConnection() as db:
            try:            
                db.session.query(self.tabela).filter(filtro == palavra_chave).update(novos_dados)
                db.session.commit()
            except Exception as ex:
                db.session.rollback()
