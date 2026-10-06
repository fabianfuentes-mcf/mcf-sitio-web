#!/usr/bin/env python3
"""
Prepara una foto de faena para la web.

Casi ninguna foto del celular se puede publicar tal como viene: traen encima
la barra de GPS Map Camera con fecha, coordenadas y direccion exacta, y a
veces la vineta de un contratista que no corresponde mostrar. Este script
recorta lo de abajo, reescala, y deja el .webp y el .jpg en img/obra/.

Uso
---
    python herramientas/agregar-foto.py "C:\\ruta\\foto.jpeg" tendido

    # si la barra del GPS ocupa mas o menos espacio, se ajusta el recorte:
    python herramientas/agregar-foto.py foto.jpeg tendido --alto 0.78

    # para ver donde quedaria el corte antes de generar nada:
    python herramientas/agregar-foto.py foto.jpeg tendido --probar

--alto es la fraccion de la foto que se CONSERVA desde arriba.
0.78 significa: me quedo con el 78% de arriba y boto el 22% de abajo.
1.0 (lo que trae por defecto) es no recortar nada.

Al terminar imprime el bloque HTML listo para pegar en index.html.
"""

import argparse
import pathlib
import sys

try:
    from PIL import Image, ImageOps
except ImportError:
    sys.exit("Falta Pillow. Instalalo con:  pip install Pillow")

RAIZ = pathlib.Path(__file__).resolve().parent.parent
DESTINO = RAIZ / "img" / "obra"
ANCHO_POR_DEFECTO = 900


def main():
    ap = argparse.ArgumentParser(add_help=True)
    ap.add_argument("origen", help="la foto original, tal como salio del telefono")
    ap.add_argument("nombre", help="nombre corto sin extension, ej: tendido")
    ap.add_argument("--alto", type=float, default=1.0,
                    help="fraccion de alto que se conserva desde arriba (0.78 bota el 22%% de abajo)")
    ap.add_argument("--ancho", type=int, default=ANCHO_POR_DEFECTO,
                    help=f"ancho de salida en pixeles (por defecto {ANCHO_POR_DEFECTO})")
    ap.add_argument("--probar", action="store_true",
                    help="solo muestra como quedaria, no escribe en img/obra/")
    args = ap.parse_args()

    origen = pathlib.Path(args.origen)
    if not origen.exists():
        sys.exit(f"No encuentro la foto: {origen}")
    if not 0.1 <= args.alto <= 1.0:
        sys.exit("--alto tiene que estar entre 0.1 y 1.0")

    im = ImageOps.exif_transpose(Image.open(origen)).convert("RGB")
    ancho_original, alto_original = im.size

    if args.alto < 1.0:
        im = im.crop((0, 0, ancho_original, int(alto_original * args.alto)))

    if im.size[0] > args.ancho:
        nuevo_alto = round(im.size[1] * args.ancho / im.size[0])
        im = im.resize((args.ancho, nuevo_alto), Image.LANCZOS)

    w, h = im.size

    if args.probar:
        prueba = RAIZ / "herramientas" / f"prueba-{args.nombre}.png"
        im.save(prueba)
        print(f"Prueba guardada en {prueba}")
        print(f"Original {ancho_original}x{alto_original}  ->  {w}x{h}")
        print("Abrela y revisa que no quede nada de la barra del GPS ni marcas")
        print("de otra empresa. Si falta recortar, baja el --alto y repite.")
        return

    DESTINO.mkdir(parents=True, exist_ok=True)
    webp = DESTINO / f"{args.nombre}.webp"
    jpg = DESTINO / f"{args.nombre}.jpg"
    im.save(webp, quality=74, method=6)
    im.save(jpg, quality=80, optimize=True, progressive=True)

    print(f"Listo:  {w}x{h}")
    print(f"  {webp.name}  {webp.stat().st_size // 1024} KB")
    print(f"  {jpg.name}  {jpg.stat().st_size // 1024} KB")
    print()
    print("Pega esto en index.html, dentro de <div class=\"galeria\"> de la")
    print("seccion 09 / OBRAS, y cambia el texto del alt y del figcaption:")
    print()
    print(f"""        <figure>
          <picture>
            <source srcset="img/obra/{args.nombre}.webp" type="image/webp">
            <img src="img/obra/{args.nombre}.jpg" width="{w}" height="{h}" loading="lazy"
                 alt="DESCRIBE AQUI LO QUE SE VE EN LA FOTO">
          </picture>
          <figcaption>TITULO CORTO</figcaption>
        </figure>""")
    print()
    print("Despues:  git add -A  &&  git commit -m \"foto nueva\"  &&  git push")


if __name__ == "__main__":
    main()
