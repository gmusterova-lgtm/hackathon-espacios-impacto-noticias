# Arquitectura inicial del prototipo

## Entrada

La entrada combina:

• nombre oficial del equipamiento
• variantes nominales
• referencias territoriales
• piezas informativas en formato texto

## Procesamiento

1. normalización del nombre del equipamiento
2. vinculación noticia-equipamiento con coincidencia nominal y contexto
3. limpieza del corpus
4. clasificación multietiqueta con reglas interpretables
5. revisión manual parcial de una muestra
6. agregación por equipamiento

## Salida

• tabla de noticias clasificadas
• ficha por equipamiento
• archivo JSON de salida para visualización posterior

## Decisión de diseño

La primera versión se apoya en reglas simples porque permiten trazabilidad, revisión rápida y ajuste fino en una muestra pequeña. Esta decisión está alineada con el objetivo de demostrar viabilidad técnica y metodológica, no de cerrar todavía un sistema de producción.
