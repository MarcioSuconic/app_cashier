def cria_caminho(caminho):
    caminho.mkdir(parents=True, exist_ok=True)

def inicio():
    from pathlib import Path
    caminho = Path("2025").joinpath("vendas").joinpath('01')
    cria_caminho(caminho)

    print(Path().absolute())

#inicio()

from pathlib import Path

cam = Path().absolute()
print(cam)



