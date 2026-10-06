# Cómo publicar y cómo actualizar

El sitio vive en GitHub y lo publica Vercel. Una vez conectados los dos, el
ciclo completo es: editas, haces `git push`, y en menos de un minuto está en
línea. No hay que tocar Vercel nunca más.

---

## Primera vez (esto se hace una sola vez)

### 1. Entrar a GitHub desde el computador

```bash
gh auth login
```

Elige **GitHub.com** → **HTTPS** → **sí** a autenticar git → **Login with a
web browser**. Te da un código de ocho caracteres, lo pegas en el navegador y
listo. Esto además deja las credenciales guardadas para los `push`.

### 2. Crear el repositorio y subirlo

Desde esta carpeta:

```bash
gh repo create mcf-sitio-web --public --source=. --remote=origin --push
```

Eso crea el repositorio en tu cuenta, lo conecta y sube el código.

### 3. Conectar Vercel

1. Entra a <https://vercel.com> y crea la cuenta **con GitHub**.
2. **Add New → Project** → elige `mcf-sitio-web` → **Import**.
3. No cambies nada: Framework **Other**, sin build, sin output directory.
   Es un sitio estático, Vercel lo sirve tal cual.
4. **Deploy**.

Queda en una URL tipo `https://mcf-sitio-web.vercel.app`. Esa es la que se
comparte para pedir opiniones.

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
