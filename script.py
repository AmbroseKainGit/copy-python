import os.path
import shutil

# Ruta actual del disco duro
home_folder = os.path.expanduser('~')


def formatRuta(ruta):
    newHome = ''
    for a in ruta:
        if a == '\\':
            newHome = newHome + '/'
        else:
            newHome = newHome + a
    return newHome


print(home_folder)
# Formatea la ruta del disco duro padre
newHome = formatRuta(home_folder) + '/'
print(newHome)
# Consigue la ruta actual en este caso la del script.
rutaActual = os.path.abspath(os.getcwd())
# Formatea la ruta de la usb.
rutaActual = formatRuta(rutaActual)

if __name__ == '__main__':
    # Lista todos los archivos en la ruta que se le pase en este caso la del disco duro
    for filename in os.listdir(newHome):
        name, extension = os.path.splitext(newHome + filename + '/')
        if filename == 'Pictures':
            shutil.copytree(name, rutaActual+'/recovery_data')
