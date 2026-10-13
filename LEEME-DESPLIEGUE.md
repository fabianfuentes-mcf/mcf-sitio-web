# Cómo publicar y cómo actualizar

El sitio vive en GitHub y lo publica Vercel. Una vez conectados los dos, el
ciclo completo es: editas, haces `git push`, y en menos de un minuto está en
línea. No hay que tocar Vercel nunca más.

---

## Ya está hecho (8 de octubre de 2026)

| | |
|---|---|
| **En línea** | <https://mcf-sitio-web.vercel.app> |
| GitHub | `fabianfuentes-mcf/mcf-sitio-web`, público |
| Vercel | cuenta `fabianfuentes`, plan Hobby, proyecto `mcf-sitio-web` |

Los dos están conectados. No hay que volver a tocar Vercel.

Si algún día hay que rehacer la conexión: `gh auth login`, después
`gh repo create ... --source=. --push`, y en Vercel **Add New → Project →
Import**, con Framework **Other** y sin build.

---

## De ahí en adelante

```bash
git add -A
git commit -m "qué cambió"
git push
```

Vercel publica solo. Cada `push` queda además con su propia URL, así que si
algo sale mal se puede volver a la versión anterior desde el panel de Vercel.

---

## El dominio

`empresamcf.com` ya está apuntando a Vercel (12 de octubre de 2026). El sitio
responde en `https://empresamcf.com/` y `www` redirige al dominio sin www.

El dominio se administra en **Hostinger**, pero no en la cuenta personal de
Fabián: está en la cuenta a la que pertenecen las diez casillas de correo
(`arturo.prestifilippo@empresamcf.com` y las demás). Si hay que volver a tocar
DNS, hay que entrar con esa cuenta.

**Los nameservers siguen en Hostinger** (`ns1`/`ns2.dns-parking.com`) y no se
mueven nunca: pasarlos a Vercel rompe el correo corporativo. Todo se hace con
registros DNS en el panel de Hostinger:

| Tipo | Nombre | Valor | TTL |
|---|---|---|---|
| A | `@` | `216.198.79.1` | 300 |
| CNAME | `www` | `814ce3cc86db91c1.vercel-dns-017.com.` | 14400 |

El CNAME de `www` es específico de este proyecto: Vercel lo genera por
proyecto, así que no sirve copiarlo para otro sitio. Si alguna vez hay que
rehacerlo, el valor correcto se lee en **Vercel → Settings → Domains**, no de
acá; Vercel ha cambiado estos destinos antes (el viejo `76.76.21.21` y
`cname.vercel-dns.com` siguen funcionando, pero ya no son lo que muestra).

Los MX (`mx1`/`mx2.hostinger.com`), el SPF, el DMARC y los tres DKIM se quedan
intactos. Vercel emite el certificado SSL solo, unos minutos después de que el
DNS propaga.

En Vercel hay tres entradas en **Settings → Domains**: `empresamcf.com`
conectado a Producción, `www.empresamcf.com` como redirección 308 al dominio
sin www, y `mcf-sitio-web.vercel.app`, que sigue andando como respaldo.

---

## Nota sobre Google

El `canonical`, el `sitemap.xml`, el JSON-LD y las etiquetas `og:` apuntan
todos a `https://empresamcf.com/`, así que la dirección de Vercel no compite
con el sitio definitivo aunque siga en línea.

Lo que falta es registrar el dominio en **Google Search Console** y enviar el
sitemap (`https://empresamcf.com/sitemap.xml`). Sin eso Google igual va a
encontrar el sitio, pero se demora bastante más.
