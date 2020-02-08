#!/usr/bin/env python
#_*_coding: utf8 _*_
# Findbuckets3 es un script para la recopilación de s3 buckets traidos por el buscador grayhatwarfare
# Autor: Claudio Herrera - claudioherrera@protonmail.ch
# Version de prueba 1.0.0 Beta
# Ejecutar con Python 3.*

import re
import requests
import mechanize, os
import argparse
import sys
from os import path
from bs4 import BeautifulSoup
from pyfiglet import Figlet

sis_op = sys.platform
sis_op = sis_op[:3]
if sis_op == 'lin':
    os.system('clear')
elif sis_op == 'win':
    os.system('cls')
else:
    pass

print('')
custom_fig = Figlet(font='threepoint')
print(custom_fig.renderText(' F i n d b u c k e c t s 3'))

print('- Ejecutar con Python 3.*\n')

parse = argparse.ArgumentParser(description="Buscador")
parse.add_argument('-b','--buscar', help='Opcion buscar')
parse = parse.parse_args()

print('- Crear directorio de salida, ejemplo: /home/user/recon\n')
path_folder = input("- Ingrese PATH: ")
print('')

def main():
    if parse.buscar:
        if path.exists(path_folder):
            company  = (parse.buscar)
            company = 's3-'+company
            os.system('mkdir /{}/{}'.format(path_folder,company))

            try:
                busc = mechanize.Browser()
                busc.set_handle_robots(False)
                busc.set_handle_equiv(False)
                busc.addheaders = [('User-Agent', 'Mozilla/5.0 (compatible; Googlebot/2.1; +http://www.google.com/bot.html)')]

                busc.open('https://buckets.grayhatwarfare.com')

                #for n in busc.forms():
                #    print(n)

                busc.select_form(nr=0)
                busc['keywords'] = parse.buscar
                busc.submit()

                #print(busc.response().read())

                try:
                    path_file_all = '{}/{}/file_all.txt'.format(path_folder, company)
                    path_file_purge = '{}/{}/file_purge.txt'.format(path_folder, company)

                    file_recon = open(path_file_all, 'r')
                    print("Se sobrescribe archivo inicial ...\n")
                except:
                    file_recon = open(path_file_all, 'a+')
                    print("Se inicializa archivo..\n")

                
                    p = BeautifulSoup(busc.response().read(),'html5lib')
                    for link in p.find_all('a'):
                        u = link.get('href')
                        if u == 'http://www.grayhatwarfare.com/':
                            file_recon.writelines(' \n')
                        if u == '/':
                            file_recon.writelines(' \n')
                        else:
                            file_recon.writelines(u + '\n')
                            print("Found => " + u)
                    

                    for pag in p.find_all('a', {'class':'page-link'}):
                        #print(pag)
                        u = pag.get('href')
                        #print('https://buckets.grayhatwarfare.com'+u)
                        page_link = 'https://buckets.grayhatwarfare.com' + u
                        header = {'User-Agent':'Firefox'}
                        reqst = requests.get(url=page_link, headers=header)
                        soup = BeautifulSoup(reqst.text, 'html5lib')

                        for m in soup.find_all('a'):
                            a = m.get('href')
                            if u == 'http://www.grayhatwarfare.com/':
                                file_recon.writelines(' \n')
                            if u == '/':
                                file_recon.writelines(' \n')
                            else:
                                file_recon.writelines(a + '\n')
                                print("Found => " + a)
                                
                    file_recon.close()

#---------------------------------------------- File for work ---------------------------------------#

                    file_purge = open(path_file_purge, 'a+')
                    file_open_purge = open(path_file_all, 'r')
                    file_read = file_open_purge.readlines()

                    for indx, line in enumerate(file_read):
                        if line == '/contact\n':
                            file_read.pop(indx)
                        if line == 'http://www.grayhatwarfare.com/\n':
                            file_read.pop(indx)
                        if line == '/\n':
                            file_read.pop(indx)
                        if line == '/\n':
                            file_read.pop(indx)
                        if line == '#\n':
                            file_read.pop(indx)

                    file_purge.writelines(file_read)
                    file_recon.close()
                    file_purge.close()

                    os.system('rm {}/{}/file_all.txt'.format(path_folder, company))

            except:
                print("\n ¡¡¡ ERROR de Conección !!!\n") 
        else:
            print("!!!Error en la ruta al crear carpeta!!!")              
    else:
        print("Introduzca una palabra a buscar")

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("Interrumpido por el usuario...")
