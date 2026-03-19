### 1. Preparación del Entorno
Primero, crea una carpeta para tu proyecto de CV e instala las dependencias necesarias:

```bash
# Creamos un entorno virtual para mantener limpio tu sistema
python3 -m venv venv
source venv/bin/activate
# Instalamos las herramientas de procesamiento
pip install PyYAML jinja2 weasyprint
```

### 2. Estructura de Archivos
Necesitarás tres archivos básicos en tu carpeta:
1.  `cv_data.yaml`: El archivo con tu información (el que definimos antes).
2.  `template.html`: Una plantilla con etiquetas Jinja2 y CSS (puedes usar clases de **Tailwind** o CSS puro).
3.  `generator.py`: El script de Python que une todo.

### 3. Comandos útiles en Bash para tu flujo diario
Una vez configurado, estos son los comandos que más usarás en tu terminal de Ubuntu:

* **Para actualizar y generar:** Cada vez que hagas un cambio en tu YAML, solo corre:
    ```bash
    python3 generator.py
    python3 generator.py --profile technical
    ```
