# Ejercicios de Herencias de POO

## Fabiola de Arizon, Judith Salas, Virginia Díaz y Pablo Márquez

- **A- Herencia "simple"**

***Clase Punto:***

La clase Punto se utiliza como una clase base para representar un punto en un espacio de coordenadas.

El método _init_ inicializa un punto con un número variable de coordenadas. Estas coordenadas se almacenan en una lista interna llamada _coords.

El método traslacion permite trasladar el punto por un vector de desplazamiento dado. Toma un número variable de argumentos deltas que representan las cantidades a agregar a cada coordenada del punto.

El método _str_ devuelve una representación legible del punto. Si el punto es de 2D, muestra las coordenadas X y Y; si es de 3D, también muestra la coordenada Z.


***Clase Punto2D:***

Punto2D es una subclase de Punto, especializada para representar puntos en un plano 2D.

En su inicialización (_init_), toma dos argumentos x e y que representan las coordenadas en el plano 2D. Llama al inicializador de la clase base (Punto) con estas coordenadas.

***Clase Punto3D:***

Punto3D es una subclase de Punto, especializada para representar puntos en el espacio tridimensional.
En la herencia simple, los objet
En su inicialización (_init_), toma tres argumentos x, y y z que representan las coordenadas en el espacio 3D. Llama al inicializador de la clase base (Punto) con estas coordenadas.


**UML Herencia Simple:** [Haz click aquí](https://viewer.diagrams.net/?tags=%7B%7D&highlight=0000ff&edit=_blank&layers=1&nav=1&title=UML_Herencia_Simple.drawio#R7ZhLU9swEMc%2FjWfgQMcPYuDYPKD0MW2HQ6GXjGILW1TxGnlNHD59ZUuK49oJyUxIYKaXjPavx65%2Ba600sbzBtLgSJI2%2FQUi55dphYXlDy3V7fk%2F%2BlsJcCb6nhUiwUElOLdywZ6pFW6s5C2nWGIgAHFnaFANIEhpgQyNCwKw57B5402tKItoSbgLC2%2BovFmKs1POeXeufKIti49mxdc%2BUmMFayGISwmxJ8kaWNxAAqFrTYkB5yc5wUfMuV%2FQuAhM0wU0m%2FGSP9PKaOxefr5050NuE5JMTvcoT4bne8I88QdAR49xgEJAnIS1Xsi2vP4sZ0puUBGXvTOZdajFOubQc2WxHZtxQgbRYknSkVxSmFMVcDtG9pxqa%2BWq0OatT4JgUxEv4zTiisx4tFq7ByIZmswUnt8UpABChdPNRypxl%2BNaQOe6GzE5fi5nXYma5Ppde%2ByF7ks0Iq40rKUtJ0uDnP%2BblyejfQ4InWVUXStSOmxZqmu43C43HLGE4HkubTEu6ySRLq377SOdKu5KbUd42jGBCgj9Rlc2TADgIFUjpjRHeGctxO4i1rqXcgWQbStvHaJaciI5oXifITVOJgmScBMwaeFbfK9c6krcKkj1n8H%2FGtjh8GYrx%2BOhYjZPGlqG9sdq56X3jeDsonleP393h8%2Fnvuy8FPPRHxXVBVl7M7nAXrFpgOvCtZOU5%2F8ByOmBdvNLl3Mmq12JCQ%2FmI0yYIjCGChPBRrfab1OoxXwFSzeqBIs71i5Tk8lHUIEkLhrd6etm%2BW2oPi2VjboxEbvbWTC%2BNas6Hs56x63mVZSaq7ZV7Wp8yiQByEdA1qPQ7BomIKL703ml%2FAoJyguypGcfO89l%2BbB3q4VCoufcciHzgDdRHv1C2vSTe2sE9O%2FTBPe0uct7hi5xvv1zkFrfGXlidv%2B8it8ca57dr3Oor9lA1zn8nNU4pz%2B%2B36rVOckfV29VJlmb9f07Vt%2FSnmDf6Cw%3D%3D)


- **B- Puzzle**
Este código en Python define dos clases: Base y Derivada donde derivada hereda de Base. Aquí está una explicación detallada del código y su salida:

***Clase Base:***
Constructor (_init_): Define tres atributos (a, b, c) con valores predeterminados ("a", "b", "c").

Métodos (A, B, C): Cada uno imprime el valor del atributo correspondiente.


***Clase Derivada:***
Constructor (_init_): Sobrescribe el valor de a a "aa", luego llama al constructor de la clase base para inicializar los otros atributos (b y c), y finalmente sobrescribe el valor de c a "cc".

Métodos (A, B): A imprime el valor de a, B modifica el valor de b a "bb" y luego llama al método B de la clase base.


***Función main():***
Se crean instancias de ambas clases: base y derivada y se llama a cada método de las clases Base y Derivada.

Luego se asigna la instancia base a la variable derivada, lo que significa que derivada ahora apunta a la misma instancia que base.

Se llama al método C de la clase Derivada (que ahora apunta a la instancia base), lo que da como resultado la salida “c”.

En la salida estándar se muestra:
- base.A() imprime "a"
- derivada.A() imprime "aa", ya que Derivada.A() imprime el valor del atributo a que fue sobrescrito en su constructor.
- base.B() imprime "b"
- derivada.B() imprime "bb" dos veces. La primera vez, modifica el valor de b a "bb" y luego llama al método B de la clase base, que imprime el valor de b. La segunda vez imprime el valor de b nuevamente, que sigue siendo "bb".
- base.C() imprime "c"
- derivada.C() imprime "cc" dos veces. La primera vez imprime "cc" ya que derivada apunta a la instancia de Derivada y Derivada.C() imprime el valor de c que fue sobrescrito en su constructor. La segunda vez imprime "c" ya que derivada ahora apunta a la instancia base, y Base.C() imprime el valor de c.


**UML Puzzle:** [Haz click aquí](https://viewer.diagrams.net/?tags=%7B%7D&highlight=0000ff&edit=_blank&layers=1&nav=1&title=UML_puzzle#R7Vldc9o6EP01zPQ%2BpGPZmJBHPvLRNreTht7kvjHCFrYa2aKygJBf35UtYxsZAiGUaYeZzCAdrSRrz1l5N244vej5WuBJ%2BC%2F3CWvYlv%2FccPoN20boogk%2FCllkiOu2MiAQ1NdGBTCgL0SDlkan1CdJxVByziSdVEGPxzHxZAXDQvB51WzMWXXXCQ6IAQw8zEz0kfoyzNC2fV7gN4QGYb4zal1kIxHOjfVJkhD7fF6CnMuG0xOcy6wVPfcIU87L%2FfL4afHIbp9a15%2B%2FJT%2Fxf90v378%2BnGWLXe0yZXkEQWL55qVfnsZXNw%2FNH%2F9P7q6%2Bza3rzujzmZ5izTCban91O4NLfV65yJ2YzGnEcAy97pjHcqBHwAVdzGgQQ9uDZyMCgBkRkoL%2FO3pA8gmgXkiZf4sXfKpOkEjsPeW9bsgFfYFlMYMhBAAMC6mlZLcqFgM1E2ALUEESsLnL3YKW0C1OpLbxOGN4ktBR%2BsDKJMIioHGXS8mjfCE%2BjX3i696S57QjBX9aKkfN35IMTZryBnkuSVGTc014RKRYgIkeXepMBxrK%2B%2FNCtqilsbAkWdvRINahEizXXm53D6GF4wCcUOznrOzX3Ha%2FVnU7zID4GEvSVW5MyiKERumoBZRKcweZIkOmGLppC2QqGuqRHGQt2SlJF7wvSzJlZCzXijSZYI%2FGwW1q028WyL0%2BvYI4zB2zVCAh9X0SpwKSWOJMY%2BopJpzGMnWP24U%2FcGLP%2Bug2XHigHvRR0Yc%2FZS5kj8dwEkxTUREQ8JwoEdfIbWMgvy63RZXFXdkui6tC866c2ganoyqnfxmRGy6ZUEZMNw9Ft2sfmW7HoNs70X0wus%2FbR6a7adBtMMxomlBob6Dal%2B0r9EdApFou5%2Fu7kkP%2FDBmacExNODX8Mzwi7I4nVFKu1heZ7YoujnVlI6u5Havt%2FUkd2n2G6Kz%2Fde483owXP1%2FkKKh5DcObF0cqBONRon6GQxpTORx%2B%2BAdGmHKGT2fQDDK%2FVI1zE3iWqtVrEzvF8tvMTaGRWEV23rZ7nG1767etvzNLEbVt%2FKR589qLUAkeTyVPspS8CNUeZxxy%2Fn7Ms9qAMrYCHSwW0JYvNIQ2ZMd7XXHo3AiH%2FuX9p4dOv7NtAWWdCqj3K6BctEUB5bZrJNJ%2BUwHlun9OAWWbhf5KBXVKv7aI9L2qqzrpHa66MsurU759QMLr6qvfS7hZYJ0y7r1prauj6mh9h4y7nlWzjiqn2H9ZDB%2BMxvbRr2PX4DErYor%2FWy6bUGawE7V7FQJ13LYOVRWbqZXBHon9jvqWpdJ8hpOEetVruPry2i1BJn7lA5jpqJJj3JpsNMcEYVjSWfWz2YaM%2BE6Jo8iGm1Y1G7ZX666ET4VH9KzC5eZCF68sBLVNQKSx0BtS5Vo6zcQpJIL4eF1I1lTba0u5Y9Tb71NcNVGzwgqqeTPW1Tqbvk2tiTroFh9VM1aLT9PO5S8%3D#%7B%22pageId%22%3A%22gkj9TwusEVfMtpoAH-sx%22%7D)


- **C- Diamante y argumentos de constructor**

La ***clase A*** tiene un atributo a y un constructor que lo inicializa.

Las ***clases B y C*** heredan de A y tienen atributos adicionales b y c respectivamente. Cada una inicializa sus atributos y llama al constructor de A.

La ***clase D*** hereda de B y C, por lo que tiene acceso a los atributos y métodos de ambas. Su constructor inicializa los atributos a, b y c llamando a los constructores de B y C.

En resumen, el código define una jerarquía de clases donde D hereda de B y C, resolviendo el problema del diamante utilizando la función super() para inicializar los atributos compartidos.

**UML Diamante y argumentos de constructor:** [Haz click aquí](https://viewer.diagrams.net/?tags=%7B%7D&highlight=0000ff&edit=_blank&layers=1&nav=1&title=UMLapartadoc.drawio#R7VrbctpIEP0aVe0%2BkNKVyyNgm2yWZJ0Qx8mTaywN0gShIdJgwF%2BfHmmEruCBgKG8uCiXuufefbr7MEgx%2BtPlIEQz7yN1sK%2FoqrNUjCtF11sdE%2F5zxSpRmJqeKNyQOIlKyxQj8oyFUhXaOXFwVOjIKPUZmRWVNg0CbLOCDoUhXRS7jalfXHWGXFxRjGzkV7X3xGFeom3rrUz%2FHhPXS1fWmp2kZYrSzuIkkYccusipjGvF6IeUsuRpuuxjn9sutcv9P6t7fzhpDj58jn6hu96%2FXz99ayST3ewyZH2EEAds76mfJ%2BOb99%2FMn99ntzefF%2Bqg%2B%2FihIYaoT8ifC3t1xWHZKrVgtCBTHwUg9cY0YCPRAufvIZ%2B4ATzbsDEcguIJh4yA8buigdEZaG2P%2BM4Qreicbz9iyJ6kUs%2BjIXmGaZEPTRoooDlkAkd6s9BjxEeCWgVtiCPoc5vaRFurhihioo9NfR%2FNIvIYb5h3maLQJUGPMkan6UR0HjjYEdLaybHAQjpZw4aPl%2FSE8Bi3Bl7mcCg8M8B0ilm4gi6idQ0yEWVaKi8yzGpNofNyeO0IHRJh4q6nXq%2F2BcIKBS7YIFvOKC1nSi4HDiksh3zwe4AY7nErRnkAwkPupJkqhuUOENUrEAWpwfegGF0%2BGDzBraVWgAu2ZzmQ%2BnjMNkI0miGbBO4w7nNlZpov4vBcRWHs2I%2Fh4RHHwUEMH4YYShDGMTOjsKHYOlYPPrCrvvrOUizYUB9kLZPhw7uHrE8DQBoiMaQwwHeBOYS3IdNjU188ViG5NdJfhuSq6OpdIZFHYAELWxzf7gwmIDy3R0t9cUf%2Fu%2FvYmjWMGseXPIwDp8trBEgBjTOUMIxWMR9YJ1x958K7TqeZKn7kW6%2BWBWmVl25xSOBYPMntYXVIaS7e1k%2BcFTuFYlb1Tc4ZVo0vUl2IfcTIU7EEbkkRtzSJIuF6Sy%2BOiOg8tLHolC8x6bhlcfkUQcVZEiNUZjlUnqiDC%2BwHPKU%2BPJCAsIeHv7KU8fclYRw6YaSoOVnCqPEoD6iUsIDhPOrSAPnXmbZks6zPkHI3x4nkJ2ZsJRgJmjNaTDO5xGLl04r2QlrZjUokIbjFXU3JTKNKZhrpFCLrsm27zgVtT5Z%2Fqhf%2BeTj%2BqZUIod6WJITt9j78s7ycIbvcCfhnaxP%2FfKzwz7dXUSRrRVMab%2BdCLs2DksvdzHQuLK80QpblrR21YZ4j87x2jec2kDyO93ycXkjfwQNZmvRtqRN%2FRvpqAvf4pO%2FA5E2T%2Ff63b8gv0zrbgW%2B%2F2V%2B7vgofPpLrXWecwnVnwtdTl79I2GWLxusQdq36Nfuq4sULY3%2BFG2O1WIVNq0qhdbMmE7f2YuyGKcHYW%2BfB2LUacndtKG1L6ZpvrvxLFvZ13P4JRa%2FF09EoevVuoFouDk7RpSvxK3H0UkWW5eh6KVzL8xy5smtV1%2FV1pbv5OrbM1BPZzjP3S9zuzchfN25TlP8%2FaV1Lktad1z2sVr3l6l9o3QlonaEVE7f0Rex%2BLwJYpZ%2FszuRFgNq8Yp2ED7TOiw%2Fo%2B%2FGByp1daZ4j39lp1Uu7RqG%2Bv8WLuR0Rdp6X5%2FVb7tSE4lZmZ5fuYN%2FkjyUHvYndHRZH%2FP0dxOw9xyQpZC%2BLGte%2FAQ%3D%3D#%7B%22pageId%22%3A%22qpGSB0OY20lgnZFA_qDh%22%7D)


- **D- Herencia múltiple - Caso "real":**

***Clase Pared:***

- Representa una pared en una casa, con una orientación específica.

***Clase Ventana:***

- Representa una ventana en una pared, con atributos para la pared asociada, su superficie y el tipo de protección (persiana, estor, etc.).

***Clase ParedCortina:***

- Es una subclase de Pared, que también tiene una superficie acristalada, que simboliza la superficie total de las ventanas en la pared.

***Clase Casa:***

- Representa una casa que contiene una lista de paredes.
- Tiene un método para calcular la superficie acristalada total de la casa sumando las superficies de todas las ventanas en todas las paredes.


En el código de ejemplo:

- Se crean instancias de estas clases con diferentes configuraciones.
- Se calcula e imprime la superficie acristalada total de la casa.

**UML Herencia múltiple - Caso "real":** [Haz click aquí](https://viewer.diagrams.net/?tags=%7B%7D&highlight=0000ff&edit=_blank&layers=1&nav=1&title=UML_Caso_Real.drawio#R3Zhbb5swFMc%2FDdLyMAkwIeljQ9t1k3bRInXSXpALDlgzmBmnSfrpZ8DcYkio1AS0J8yf49vvHB8ba8CJ9p8YTMKv1EdEM3V%2Fr4E7zTQNe2GJR6YcCmVp6oUQMOxLo1pY41ckxdJsi32Utgw5pYTjpC16NI6Rx1saZIzu2mYbStq9JjBAirD2IFHVX9jnoZzFXK%2F1R4SDsOzZ0OWXCJbGUkhD6NNdQwL3GnAYpbwoRXsHkQxeyaWo99DztRoYQzEfUsH89mcR%2FH38%2FfOJbuZfHuDrZ3D7UbbyAslWTviHaNCXI%2BaHEgOj29hHWUu6Bla7EHO0TqCXfd0Jxwst5BERb4YoyjYR42jfO1ijQiBiB9EIcXYQJrLCQkIro0a%2B7moXmJbUwgb%2BUoPS60HVcA1GFCSbN3AyFU6ui2PMXfcDZVhMCnpYc4C2ArEGblPOZlNDaNhjMwQKw%2B8qupwZmxw8c2x4lgLvKUMXw9FRWXqbVVec2ddENVdQJXlOy4NLpjebiFGsfPwiigHPQRTSMztWGkbpNkFsgz2MisY2hEJe2omxdrQ3qIuzVRNGOfI8TJtL5FTdY3ViMVLtkueCxDAuFSV2f0ZXw0V0YcMo4xI%2Fp0mve49M9ElIPUHbO6UhcTz%2BrC4platN2ZXAXUxjNHvfte26omkRdbP%2FY2lXJ%2FezS%2FtiG8Ci%2B1DrUMbxBDZMuw0MgLHPFkuFV50zXOgxnHJIoA9b%2BWNiEBdjQ7zp30%2BqP4TW9j1kTznrh9nQLD4td1ldSaLLXfal3FUOoOEvB6bjJwdwc0TK6iBlXjOwDfWOID8gZbcyWRwSEZbTw9Z1Y3BdbCeuDBR%2B73yk6E4b5Qnj5F%2FLxPw47%2Frx7vLj8u1%2BFK%2F17Vv%2BrXGHCe7%2FAQ%3D%3D)