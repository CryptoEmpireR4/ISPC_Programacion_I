libros = [
('Papelucho programador', 'Marcela Paz', 1983),
('Don Python de la Mancha', 'Miguel de Cervantes', 1615),
('Raw_input y Julieta', 'William Shakespeare', 1597),
('La tuplamorfosis', 'Franz Kafka', 1915),
# ...
]
autores = {
# autor: nacimiento, defunción, idioma
'William Shakespeare': ((1564, 4, 26), (1616, 5, 3), 'inglés'),
'Franz Kafka': ((1883, 7, 3), (1924, 6, 3), 'alemán'),
'Marcela Paz': ((1902, 2, 28), (1985, 6, 12), 'español'),
'Miguel de Cervantes': ((1547, 9, 29), (1616, 4, 22), 'español'),
# ...
}

titulo = input('Ingrese titulo del libro: ')
fila_libros=0
autor_busqueda=0

while libros[fila_libros][0]!=titulo:
    fila_libros+=1

autor_busqueda=libros[fila_libros][1]

print('El libro fue escrito en '+str(autores[autor_busqueda][2]))
print('por '+str(libros[fila_libros][1]))
print('El autor fallecio '+str(int(autores[autor_busqueda][1][0])-int(libros[fila_libros][2]))+" años")
print('después de haber escrito el libro')
