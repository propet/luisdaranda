% Este portfolio
%
% 2019-01-22

[_Echa un vistazo al repositorio._](https://github.com/propet/luisdaranda)



En cuarto cursé una asignatura de web dinámicas. De las
mejores que he tenido durante toda la carrera, a pesar de
no estar directamente relacionada con mi titulación (era
    una asignatura de competencias, opcional). La daba Raquel Martínez.
Muy buena profesora, que se le notaba que le gustaba el tema, y
enseñaba a toda pastilla bases de datos con MySQL, php, html, css, y
finalmente javascript.

Cada semana teníamos un trabajillo que entregar, y al final del
curso presentábamos una pequeña
web en equipos de tres.

Nuestra idea era hacer una página para organizar eventos, donde
la gente pudiera crear planes, apuntarse a los ya existentes,
hacer eventos privados para conocidos, etc. Un poco como
[eventbrite](https://www.eventbrite.es/), aunque yo al menos no sabía 
de su existencia hasta después de empezar
con el trabajo.

Al final quedó bastante chula, pero ninguno teníamos
intención de hacer una página web de verdad. Así que después de
presentar, la página quedó perdida por algún sitio (supongo que en una
   carpeta de dropbox). Tampoco sabíamos realmente cómo montar una página
de verdad, porque nunca vimos cómo iba el tema de dominios, hosting, etc.
Solo
se nos daba acceso a un servidor de la escuela con IP estática, y con
eso trabajábamos.


## **Índice**
* [¿Por qué un portfolio?](#¿Por qué un portfolio?)
* [Herramientas](#herramientas)
* [Dominio y hosting](#dominio y hosting)


## **¿Por qué un portfolio?**

En el momento de hacer el curriculum, ya que había dado algo de
tecnologías web, pues quería meterlo también como una habilidad más que tenía.
Por si podía interesarle a algún contratante. Pero entonces pensé que iba a quedar
un poco sospechoso decir que sabía hacer webs, sin presentar ninguna.
En general, siempre quedaría un poco sospechoso afirmar que era capaz de
hacer algo sin nunca enseñar nada para respaldarlo.

Adicionalmente, es una forma de obligarte a ti mismo a documentar mejor
tus futuros trabajos, y luego tenerlos ahí de referencia.

Por último, ya que no di en su día cómo era eso de comprar dominios,
alojar en un servidor externo, vincular tu dominio con la ip del servidor...
pues ya aprovecho y aprendo un poco. También por curiosidad.

## **Herramientas**

Utilicé las tecnologías más básicas: html, css,
y javascript. Sin plantillas, sin temas. La mayor ayuda que he usado ha
sido [bootstrap](http://getbootstrap.com/), una
libreria de clases css para darle estructura al contenido
html (en filas y columnas), y que este sea <em>responsive</em>. Es decir,
que se adapte a cualquier tipo o tamaño de pantalla (puedes comprobarlo
reduciendo el tamaño de la ventana, o visitando la página desde un móvil).

Con javascript fundamentalmente he usado Jquery (una librería de uso
bastante extendido) para facilitarme la selección de los elementos de
la página (referidos como partes del DOM: Document Object Model). Y
luego también empleé la libería [mathjax](https://www.mathjax.org/)
para incorporar alguna ecuación escrita en LaTeX.

Seguramente el proceso habría sido más fluido usando alguna herramienta
de creación más gráfica, como podría ser wordpress, divi, o wix.
Pero también creo que me ha valido la pena usar solo html, css y javascript,
para revisar las bases que cómo se compone una página, y así no terminar
siendo esclavo de una sola utilidad.

De todas formas, no descarto empezar a usar wordpress en el futuro más inmediato
para tener mejor organizado el contenido que vaya metiendo, y sobre todo
independizarlo del estilo. A la fecha de escribir estas líneas, estoy
escribiendo sobre html, y no estoy convencido de que sea la mejor idea.

## **Dominio y hosting**

Debido a que ya había utilizado antes la nube de amazon, lo primero
en lo que pensé fue en una instancia
(tipo de servidor) de pocos recursos para alojar el portfolio.
Que sería el equivalente a un ordenador de poca potencia, por tanto,
también más barato. Así que
alquilé un servidor tipo <em>t2.nano</em>, el tipo de instancia más
pequeña.

![Consola de administración en la nube de amazon (servicio EC2)](./images/instanciaAmazon.jpg)


Y como amazon también hace de <em>registrar</em> (vendedor de dominios),
pues también compré ahí el nombre del dominio por un año.

Finalmente, para vincular el dominio a la IP del servidor, resultó
fácil poner los registros en los servidores DNS de amazon, tal como
indicaban las instrucciones.

Conforme explore algo más, a lo mejor cambio el hosting hacia alguna
alternativa más barata (la instancia nano de amazon son unos 6 euros
al mes). Aunque también tendría que tener en cuenta qué funcionalidad
se ofrece, porque me parece que la mayoria de hosters no te dan acceso
a un servidor
completo (como si fuera un ordenador), sino más bien te dan acceso
a una carpeta, y de ahí no puedes salir. Tampoco
puedes instalar nuevo software.
