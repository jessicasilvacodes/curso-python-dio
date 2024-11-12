import os
import shutil
from pathlib import Path

ROOT_PATH = Path(__file__).parent     #parent = pasta que está acima


os.mkdir(ROOT_PATH / "novo_diretorio")     #criar nova pasta


arquivo = open( ROOT_PATH / 'novo_arquivo1.txt', 'w')      #criar arquivo dentro da pasta
arquivo.close()


#p/ renomear:
os.rename(ROOT_PATH/'novo_arquivo1.txt', ROOT_PATH/'novo_arquivo.txt')


#p/ remover o arquivo:
os.remove(ROOT_PATH/'novo_arquivo.txt')


#p/ mover um arquivo:
shutil.move(ROOT_PATH / 'novo_arquivo.txt', ROOT_PATH / 'novo_diretorio' / 'novo_arquivo.txt')
