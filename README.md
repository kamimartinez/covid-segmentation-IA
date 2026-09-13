# COVID Segmentation

Proyecto de segmentación semántica de tomografías de tórax para pacientes con COVID-19. El repositorio se centra en un único notebook de investigación y entrenamiento para detectar regiones pulmonares afectadas por vidrio esmerilado y consolidación.

## Estructura del repositorio

- `covid-segmentation.ipynb`: notebook principal con carga de datos, exploración, preprocessamiento, entrenamiento y evaluación.
- `data/`: archivos `.npy` del dataset.
- `README.md`: documentación del proyecto.
- `requirements.txt`: dependencias necesarias para ejecutar el notebook.

## Requisitos

- Python 3.10+
- Jupyter / VS Code con soporte para notebooks

## Instalación

### Linux/macOS

```bash
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

### Windows (PowerShell)

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
pip install -r requirements.txt
```

### Windows (Command Prompt)

```cmd
python -m venv .venv
.\.venv\Scripts\activate.bat
pip install -r requirements.txt
```

## Cómo ejecutar

1. Asegúrate de tener los archivos del dataset dentro de `data/`.
2. Abre `covid-segmentation.ipynb` en Jupyter o VS Code.
3. Ejecuta todas las celdas de arriba a abajo.

## Dependencias principales

- `numpy`
- `pandas`
- `matplotlib`
- `scipy`
- `torch`
- `albumentations`
- `segmentation-models-pytorch`
- `tqdm`