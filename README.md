# covid-segmentation-IA

Proyecto de segmentación semántica de tomografías (CT) de tórax en pacientes con COVID-19, usando el dataset de la competencia [COVID-19 CT Images Segmentation](https://www.kaggle.com/competitions/covid-segmentation) de Kaggle.

El objetivo es segmentar, pixel por pixel, las zonas del pulmón afectadas por ground-glass opacity y consolidación.


## Cómo correrlo

Solo se necesita correr `main.ipynb` de inicio a fin (Kernel → Restart & Run All). Este notebook llama internamente a `etl.ipynb`, `eda.ipynb` y `dataset.ipynb` con `%run`, así que no hace falta correrlos por separado.

1. Coloca los archivos `.npy` del dataset dentro de `data/`.
1. Abre `main.ipynb`.
1. Corre todas las celdas de arriba a abajo.

## Librerías necesarias
- `numpy` 
- `matplotlib` 
- `torch` / `torchvision` 
- `scipy`
- `albumentations` 