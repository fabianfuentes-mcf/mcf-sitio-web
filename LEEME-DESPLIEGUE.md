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

## Cuando llegue el dominio

Hoy `empresamcf.com` está estacionado en Hostinger: solo correo, sin plan de
hosting, sin SSL y sin registro `www`.

Para apuntarlo a Vercel **no hay que mover los nameservers**: eso rompería el
correo corporativo. Se hace con registros DNS en el panel de Hostinger:

| Tipo | Nombre | Valor |
|---|---|---|
| A | `@` | `76.76.21.21` |
| CNAME | `www` | `cname.vercel-dns.com` |

Los registros MX del correo se quedan intactos. Vercel emite el certificado
SSL solo.

En Vercel: **Settings → Domains → Add** `empresamcf.com`. Confirma los
valores ahí antes de escribirlos, por si Vercel cambia la IP.

Cuando el dominio esté andando, en `index.html` el `canonical` y las etiquetas
`og:` ya apuntan a `https://empresamcf.com/`, así que no hay que tocar nada.

---

## Nota sobre Google

Mientras la web viva en `.vercel.app`, el `canonical` del HTML le dice a
Google que la dirección buena es `empresamcf.com`. Por eso no se arma un
duplicado que compita con el sitio definitivo. No hay que hacer nada.
