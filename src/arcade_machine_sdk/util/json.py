import json
from pathlib import Path
from typing import Dict, Any

def load(file_path: str) -> Dict[str, Any]:
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

def save(file_path: str, data: Dict[str, Any]) -> None:
    """
    Guarda un diccionario como un archivo JSON.

    args:
        **file_path**: Ruta completa al archivo JSON.
        **json**: Diccionario a escribir como JSON.
    """
    path = Path(file_path)
    with path.open("w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=4)
