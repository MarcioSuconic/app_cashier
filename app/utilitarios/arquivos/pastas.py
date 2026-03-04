import os

def verifica_se_caminho_existe(caminho_arquivo):

    if caminho_arquivo.exists():
        arquivo_existe = True
    else:
        arquivo_existe = False

    return(arquivo_existe)

def exists_database_out():

    from app.utilitarios.arquivo_vendas.utils import return_path_base
    from app.utilitarios.arquivos.pastas import verifica_se_caminho_existe
    import os
    from pathlib import Path

    path_file = Path(f'{return_path_base()}').joinpath("databases_out").joinpath("sales_x_products")

    existe_caminho = path_file.exists()

    if existe_caminho:
        print('O caminho database_out já existe.')
        return 0
    
    Path(path_file).mkdir(parents=True, exist_ok=True)
    print('O caminho database_out foi criado.')
    