# Sitio web — MCF Ingeniería y Construcción SpA

Sitio estático de una página para una contratista chilena de fibra óptica y
obra civil. Sin framework, sin build, sin dependencias: HTML, CSS y un
archivo de JavaScript de treinta líneas para el menú del teléfono.

**En línea:** https://mcf-sitio-web.vercel.app
**Dominio definitivo:** `empresamcf.com`

## Cómo está armado

```
index.html          la página completa
css/estilo.css      todo el diseño; los colores están arriba, en :root
css/tipografias.css las fuentes
js/sitio.js         solo el menú del teléfono
img/                logo, iconos y la tarjeta para redes sociales
img/obra/           las fotos de faena, cada una en .webp y .jpg
fonts/              Archivo e IBM Plex Mono, servidas desde el propio sitio
herramientas/       scripts de mantención; no se publican
robots.txt
sitemap.xml
vercel.json
```

No hay nada que compilar. Para verlo mientras se edita basta con abrir
`index.html` en el navegador, o levantar un servidor:

```bash
python -m http.server 8777
```

## Cómo se cambia algo

1. Se edita el archivo.
2. `git add -A && git commit -m "qué cambió" && git push`
3. Vercel lo publica solo, en menos de un minuto.

**Los colores** están todos arriba en `css/estilo.css`, en `:root`. El acento
de hoy es el cian del logo:

```css
--acento: #35BBD6;   /* el naranja de la versión anterior era #E8541F */
```

## Cómo se agrega una foto

Las fotos del celular **no se pueden publicar tal como vienen**: traen encima
la barra de GPS Map Camera con la fecha, las coordenadas y la dirección
exacta, y a veces la viñeta de otra empresa. Hay un script para eso:

```bash
# primero probar dónde cae el corte, sin escribir nada
python herramientas/agregar-foto.py "C:\ruta\foto.jpeg" camara --alto 0.80 --probar

# cuando el recorte está bien, generar el .webp y el .jpg
python herramientas/agregar-foto.py "C:\ruta\foto.jpeg" camara --alto 0.80
```

`--alto 0.80` quiere decir que se conserva el 80% de arriba y se bota el 20%
de abajo, que es donde suele ir la barra del GPS.

El script imprime el bloque HTML listo para pegar en la sección
`09 / OBRAS` de `index.html`. Solo hay que escribir el `alt` y el
`figcaption`.

**Antes de subir una foto, mirarla completa** y confirmar que no se lea
ninguna marca de otra empresa ni quede visible una dirección.

## Convenciones

- Español de Chile, tuteo.
- Los textos van en el HTML, no en JavaScript: así los lee Google.
- Toda imagen lleva `alt` descriptivo y `width`/`height`, para que la página
  no salte mientras carga.
- Las fotos van siempre en `.webp` con respaldo `.jpg`.
- Nada de CDN ni Google Fonts: las fuentes se sirven desde el propio sitio.
