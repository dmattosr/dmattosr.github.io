import yaml
import argparse
from pathlib import Path
from jinja2 import Environment, FileSystemLoader
from weasyprint import HTML

# -----------------------------
# 1. CLI ARGUMENTS
# -----------------------------
parser = argparse.ArgumentParser(description="CV Builder")

parser.add_argument(
    "--profile",
    choices=["short", "technical"],
    default="short",
    help="Tipo de CV a generar",
)

parser.add_argument(
    "--lang",
    default="es",
    help="Idioma (por ahora solo es)",
)

args = parser.parse_args()

# 1. Cargar datos desde el YAML
with open('cv_data.yaml', 'r', encoding='utf-8') as f:
    data = yaml.safe_load(f)

# 2. Configurar Jinja2 para cargar la plantilla HTML
env = Environment(loader=FileSystemLoader('.'))
template = env.get_template('template.html')

# 3. Renderizar el HTML con tus datos
html_out = template.render(c=data, mode=args.profile)

# 4. Generar el PDF
HTML(string=html_out).write_pdf("CV_Daniel_Mattos.pdf")
HTML(string=html_out).write_pdf("cv-DanielMattos-SoftwareEngineer.pdf")
HTML(string=html_out).write_pdf("../assets/cv-DanielMattos-SoftwareEngineer.pdf")
print("¡CV generado con éxito: CV_Daniel_Mattos.pdf!")
