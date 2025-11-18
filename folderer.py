import os

for i in range(1,21):
    carpeta = f"carpeta_{i:02}"
    try:
        os.mkdir(carpeta)
    except FileExistsError:
        print(carpeta[i])
    