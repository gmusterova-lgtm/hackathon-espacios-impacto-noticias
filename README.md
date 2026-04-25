# Prototipo semiautomático para identificar impactos públicos de equipamientos culturales a partir de noticias digitales

Este repositorio acompaña la propuesta seleccionada en la Hackathon Datos & Cultura, Cátedra ESPACIOS.

La idea central es convertir noticias, notas institucionales y agendas culturales en una capa de información estructurada que permita describir qué tipo de impacto público generan los equipamientos culturales. El foco no está en contar apariciones en prensa sin más, sino en relacionar cada pieza informativa con un equipamiento concreto y clasificarla según dimensiones de impacto comparables.

## Conexión directa con la propuesta

El repositorio está organizado para reflejar exactamente la lógica planteada en la propuesta:

• problema: la información sobre impacto público está dispersa y no suele quedar estructurada
• objetivo: recoger, vincular y clasificar noticias relacionadas con equipamientos culturales
• casos piloto: IVAM y Centre del Carme
• metodología: normalización, vinculación, limpieza, clasificación multietiqueta y revisión manual parcial
• resultado esperado: ficha por equipamiento, dimensiones activadas y evolución temporal

## Uso inicial de PITEC

En esta fase inicial, PITEC actúa como base estructural del prototipo. Los casos piloto se han localizado y contrastado en la plataforma antes de construir la muestra de noticias.

Casos verificados en PITEC:
- INSTITUT VALENCIÀ D'ART MODERN (IVAM)
- Centre del Carme de Cultura Contemporània (CCCC)

Esta consulta inicial permite:
- seleccionar y normalizar equipamientos piloto
- utilizar sus registros como referencia de identificación
- detectar posibles inconsistencias en los datos
- combinar la base estructural de PITEC con validación externa mediante noticias y revisión manual

## Qué incluye esta primera versión

Esta es una base de trabajo pensada para mostrar trazabilidad metodológica, viabilidad técnica inicial y capacidad de desarrollo. Incluye:

• una estructura clara de carpetas
• un conjunto de datos demo para pruebas
• reglas iniciales de clasificación interpretables
• un pipeline sencillo para generar fichas por equipamiento
• una carpeta `.github` preparada para dar imagen de proyecto bien organizado

## Casos piloto

En la fase inicial del prototipo se plantean dos casos de prueba:

• IVAM
• Centre del Carme

La idea es empezar con equipamientos valencianos con presencia mediática suficiente y perfiles institucionales diferenciados. Esto permite probar la lógica del sistema con una muestra acotada antes de escalarla.

## Flujo del prototipo

1. Seleccionar equipamientos piloto.
2. Normalizar variantes nominales.
3. Recoger noticias, notas institucionales y agendas culturales.
4. Vincular cada pieza informativa con su equipamiento.
5. Limpiar duplicados y ruido documental.
6. Clasificar cada texto con lógica multietiqueta.
7. Agregar resultados por equipamiento y periodo.
8. Generar fichas y visualizaciones simples.

## Dimensiones iniciales de impacto

• notoriedad pública
• cohesión social
• transformación territorial
• fortalecimiento del sector cultural
• derechos culturales
• influencia pública

## Estructura del repositorio

```text
hackathon-espacios-impacto-noticias/
├── .github/
│   └── workflows/
│       └── python-check.yml
├── data/
│   └── demo/
│       ├── news_demo.csv
│       └── news_schema.md
├── docs/
│   ├── arquitectura.md
│   ├── guion_video.md
│   ├── propuesta_resumen.md
│   └── github_setup.md
├── notebooks/
│   └── README.md
├── outputs/
│   └── demo_profiles.json
├── src/
│   ├── entity_linking.py
│   ├── impact_rules.py
│   └── pipeline_demo.py
├── .gitignore
├── requirements.txt
└── README.md
```

## Cómo ejecutar la demo

```bash
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
python src/pipeline_demo.py
```

Esto genera un archivo de salida en `outputs/demo_profiles.json` con una ficha básica por equipamiento.

## Qué mostrar en el vídeo

Para el vídeo de presentación de 5 minutos, este repositorio permite enseñar:

• que la propuesta ya tiene traducción operativa
• que las dimensiones del PDF ya están convertidas en reglas y estructura de datos
• que existe un pipeline reproducible, aunque todavía sea una prueba de concepto
• que el desarrollo puede seguir creciendo sobre una base ordenada

## Siguiente desarrollo previsto

La siguiente fase natural sería sustituir parte de las reglas iniciales por un enfoque híbrido con revisión manual y, si la muestra lo permite, un clasificador supervisado sencillo entrenado con noticias etiquetadas.
