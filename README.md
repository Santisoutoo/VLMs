# VLMs - Image Captioning con BLIP, ViT-GPT2 y Gemini

Proyecto de generación automática de descripciones de imágenes usando tres modelos Vision-Language diferentes: BLIP (Salesforce), ViT-GPT2 (nlpconnect) y Gemini 2.5 Pro (Google).

## Resumen

Este proyecto compara tres modelos para describir imágenes automáticamente:

- **BLIP**: Modelo open source con buen balance entre calidad y velocidad
- **ViT-GPT2**: Modelo más ligero y rápido para recursos limitados  
- **Gemini 2.5 Pro**: API de Google con máxima calidad y capacidad de leer texto en imágenes

Cada modelo procesa imágenes de la carpeta `img/` y guarda las descripciones en archivos de texto en `outputs/`.

## Estructura del Proyecto

```
.
├── dockerfile                 # Contenedor Docker con dependencias
├── makefile                   # Comandos para construir y ejecutar
├── requirements.txt           # Dependencias de Python
├── pyproject.toml            # Configuración del proyecto
├── main.py                   # Punto de entrada principal
├── README.md                 # Este archivo
│
├── img/                      # Imágenes de entrada
│   ├── clouds/              # Fotos de nubes
│   ├── drinks/              # Fotos de bebidas
│   ├── food/                # Fotos de comida
│   ├── planes/              # Fotos de aviones
│   └── racing_cars/         # Fotos de coches de carreras
│
├── outputs/                  # Descripciones generadas
│   ├── model_1/             # Resultados de BLIP
│   ├── model_2/             # Resultados de ViT-GPT2
│   └── gemini/              # Resultados de Gemini
│
└── scr/                      # Código fuente
    ├── gemini/
    │   └── gemini.py        # Integración con Gemini API
    └── models/
        ├── model_1/
        │   └── blip_captioner.py      # Implementación BLIP
        └── model_2/
            └── vitgpt2_captioner.py   # Implementación ViT-GPT2
```

## Requisitos

- Docker
- Make
- Para Gemini: clave de API de Google (variable `GEMINI_API` en archivo `.env`)

## Instalación y Uso

### 1. Construir el contenedor Docker

```bash
make build
```

Este comando construye la imagen Docker con todas las dependencias necesarias.

### 2. Ejecutar modelos

#### Modelo 1 (BLIP)

```bash
make run-model1
```

Genera descripciones usando BLIP. Los resultados se guardan en `outputs/model_1/`.

#### Modelo 2 (ViT-GPT2)

```bash
make run-model2
```

Genera descripciones usando ViT-GPT2. Los resultados se guardan en `outputs/model_2/`.

#### Gemini 2.5 Pro

Primero, crea un archivo `.env` en la raíz del proyecto:

```bash
echo "GEMINI_API=tu_clave_api_aqui" > .env
```

Luego ejecuta:

```bash
make run-gemini
```

Genera descripciones usando Gemini. Los resultados se guardan en `outputs/gemini/`.

### 3. Abrir shell interactivo (opcional)

Si quieres explorar el contenedor o ejecutar comandos personalizados:

```bash
make shell
```

## Añadir tus propias imágenes

1. Crea una carpeta dentro de `img/` con el nombre de tu categoría
2. Añade tus imágenes (formatos soportados: `.jpg`, `.jpeg`, `.png`)
3. Ejecuta cualquiera de los modelos

Ejemplo:

```bash
mkdir img/mi_categoria
cp mis_fotos/* img/mi_categoria/
make run-model1
```

## Comparar resultados

Después de ejecutar los modelos, puedes comparar las descripciones:

```bash
# Ver descripción de BLIP
cat outputs/model_1/mi_imagen.jpg.txt

# Ver descripción de ViT-GPT2
cat outputs/model_2/mi_imagen.jpg.txt

# Ver descripción de Gemini
cat outputs/gemini/mi_imagen.jpg.txt
```