from imgurpython import ImgurClient
from multiprocessing.pool import ThreadPool
import os
import urllib.request
import time
from multiprocessing import Pool

secret_client = "5f8c3cce299db5e26a2eb96b0b7809a82805c9ad"
id_client = "bfa0e227a1c5643"
client = ImgurClient(id_client,secret_client)

#Metodo para la descarga
def descarga(link):
    img_name = link.split('/')[3] #Corta el URL de la imagen
    img_format = img_name.split('.')[1] #Obtiene el formato
    img_name = img_name.split('.')[0] #Obtiene el nombre dela imagen
    print(img_name,img_format)
    url_local = "/Users/fabri/Documents/imagenes/{}.{}"
    #Guardar nne local las imagenes
    urllib.request.urlretrieve(link, url_local.format(img_name, img_format))


def main():
    id_album = "bUaCfoz"
    imagenes = client.get_album_images(id_album)
    
    for imagen in imagenes:
        descarga(imagen.link)

    # Cuenta el tiempo transcurrido de este rastreador
    t1 = time.time()
        
    with Pool(10) as p: # Es la cantidad de CPU's simuladas
        print(p.apply_async(descarga))  
        
    t2 = time.time()
    print('Usando Multiprocessing, tiempo total:% s' % (t2 - t1))
        

if __name__ == "__main__":
   main()