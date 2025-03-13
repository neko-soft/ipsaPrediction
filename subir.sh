# Este script es para pushear al GitHub, para ahorrarse tener que escribir los comandos a cada rato.

DEST="$HOME/ipsaPrediction"

cd "$DEST"
git add .
git commit -S -m "Actualización de Archivos"
git push origin main