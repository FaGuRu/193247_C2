from imgurpython import ImgurClient
from concurrent.futures import ThreadPoolExecutor
import os
import urllib.request
import timeit

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
    imagenes = [imagen.link for imagen in client.get_album_images(id_album)] #Pasamos el for de sincrono a la variable

    with ThreadPoolExecutor(max_workers=10) as executor:  # Es la cantidad de hilos max_workers
        executor.map(descarga,imagenes) #Asignamos una tarea a nuestro ThreadPool

if __name__ == "__main__":
    print("Tiempo de descarga {}".format(timeit.Timer(main).timeit(number=1)))