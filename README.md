# parkinson_uv_backend

Este es el repositorio del backend del proyecto ParkinsonUV. 

## Tecnlogías utilizadas
<div style="display: flex; justify-content: center;">
  <div style="display: flex;">
    <img src="https://cdn.hashnode.com/res/hashnode/image/upload/v1636780048014/niLN2J80j.png" alt="React" height="50" style="margin: 10px;">
    <img src="https://upload.wikimedia.org/wikipedia/commons/thumb/0/0a/Python.svg/1200px-Python.svg.png" alt="React" height="50" style="margin: 10px;">
  </div>
</div>

## Instalación y ejecución en Local
Para ejecutar local tener en cuenta: 

### Ambiente virtual de Python
Crear o tener ambiente virtual de Python y activarlo: 

```bash
  python -m venv myenv
  cd myenv/scripts/activate
```
### Clonamos el repo en myenv
Clonamos el repo en el ambient evirtual de Python y luego entramos en él: 

```bash
  git clone https://github.com/Joules17/parkinson_uv_backend.git
  cd parkinson_uv_backend
```

### Instalar dependencias

```bash
  pip install -r requirements.txt
```

### Correr en local

Estando en el ambiente, y en la carpeta del repositorio y este con el .env: 
```bash
  python manage.py runserver 6060
```
