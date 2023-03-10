#Challenger05
"""
 * Crea un programa que se encargue de calcular el aspect ratio de una
 * imagen a partir de una url.
 * - Url de ejemplo: https://raw.githubusercontent.com/mouredev/
 *   mouredev/master/mouredev_github_profile.png
 * - Por ratio hacemos referencia por ejemplo a los "16:9" de una
 *   imagen de 1920*1080px.
"""
# importing the module
import PIL # toca descargar la libreria previamente 
from PIL import Image
  
# loading the image
img = PIL.Image.open("NASA.jpg")
  
# fetching the dimensions
wid, hgt = img.size
# el rario se calcula dividiendo la anchura entre la altura
#3:2, significa que por cada tres unidades a lo largo hay dos unidades a lo alto.
ratio = wid/hgt
# mostramos el ratio 
print(ratio)

"""
import urllib.request

urllib.request.urlretrieve("https://raw.githubusercontent.com/mouredev/mouredev/master/mouredev_github_profile.png",
"NASA.jpg")

print("download successful")
"""


