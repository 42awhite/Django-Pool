import sys
import os
import settings # Importamos nuestras variables

def render_template(template_path):
    # 1. Validar extensión 
    if not template_path.endswith('.template'):
        print("Error: El archivo debe tener extensión .template")
        return

    # 2. Validar existencia 
    if not os.path.exists(template_path):
        print(f"Error: El archivo {template_path} no existe.")
        return

    try:
        # Leer el contenido de la plantilla
        with open(template_path, 'r') as f:
            content = f.read()

        # 3. Reemplazar patrones usando las variables de settings.py 
        # Usamos vars(settings) para obtener un diccionario de las variables definidas
        # y .format(**dict) para inyectarlas en los tags {variable}
        result = content.format(**vars(settings))

        # 4. Definir nombre de salida (.html) 
        output_path = template_path.replace('.template', '.html')
        
        with open(output_path, 'w') as f:
            f.write(result)
            
    except Exception as e:
        print(f"Error inesperado: {e}")

if __name__ == '__main__':
    if len(sys.argv) != 2:
        print("Uso: python3 render.py <archivo.template>")
    else:
        render_template(sys.argv[1])