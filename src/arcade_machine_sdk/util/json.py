import json
from pathlib import Path
from typing import Dict, Any

def load_json(file_path: str) -> Dict[str, Any]:
    """
    Carga un archivo JSON y devuelve un diccionario.

    args:
        **file_path**: Ruta completa al archivo JSON.

    returns:
        Diccionario con los datos del JSON.
    """
    path = Path(file_path)
    if not path.exists():
        raise FileNotFoundError(f"No se encontró el archivo JSON en {file_path}")

    with path.open("r", encoding="utf-8") as f:
        return json.load(f)

def set_value_json(file_path: str, key: str, value: Any) -> None:
    """
    Añade o actualiza un valor en el JSON y guarda los cambios.

    args:
        **file_path**: Ruta completa al archivo JSON.
        **key**: Clave a añadir o actualizar en el JSON.
        **value**: Valor a asignar a la clave.
    """
    data = load_json(file_path)
    data[key] = value

    path = Path(file_path)
    with path.open("w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=4)
