class GameMeta:
    """Clase que sigue el patrón Builder para construir metadatos de un juego."""
    
    def __init__(self) -> None:
        self._title = ""
        self._description = ""
        self._release_date = ""
        self._tags: list[str] = []
        self._group_number = -1
        self._authors: list[str] = []
    
    def with_title(self, title: str) -> 'GameMeta':
        self._title = title
        return self
    
    def with_description(self, description: str) -> 'GameMeta':
        self._description = description
        return self
    
    # TODO: esto debería representarse con un UNIX timestamp o una fecha de Python, pero por ahora se puede dejar así. Además, es siquiera esto necesario?
    def with_release_date(self, release_date: str) -> 'GameMeta':
        self._release_date = release_date
        return self
    
    def with_tags(self, tags: list[str]) -> 'GameMeta':
        self._tags.extend(tags)
        return self
    
    def add_tag(self, tag: str) -> 'GameMeta':
        self._tags.append(tag)
        return self
    
    def with_group_number(self, group_number: int) -> 'GameMeta':
        self._group_number = group_number
        return self
    
    def with_authors(self, authors: list[str]) -> 'GameMeta':
        self._authors.extend(authors)
        return self
    
    def add_author(self, author: str) -> 'GameMeta':
        self._authors.append(author)
        return self
    
    @property
    def title(self) -> str:
        return self._title
    
    @property
    def description(self) -> str:
        return self._description
    
    @property
    def release_date(self) -> str:
        return self._release_date
    
    @property
    def tags(self) -> list[str]:
        return self._tags.copy()
    
    @property
    def group_number(self) -> int:
        return self._group_number
    
    @property
    def authors(self) -> list[str]:
        return self._authors.copy()
    
    def validate(self) -> None:
        if not self._title:
            raise ValueError(f"No se especificó un título (\"title\") para el juego en sus metadatos")
        if not self._description:
            raise ValueError(f"No se especificó una descripción (\"description\") para el juego en sus metadatos")
        if not self._release_date:
            raise ValueError(f"No se especificó una fecha de lanzamiento (\"release_date\") para el juego en sus metadatos")
        if not self._tags:
            raise ValueError(f"No se especificó al menos una etiqueta (\"tags\") para el juego en sus metadatos")
        if self._group_number == -1:
            raise ValueError(f"No se especificó el número del grupo (\"group_number\") que hizo el juego en sus metadatos")
        if not self._authors:
            raise ValueError(f"No se especificó al menos un autor (\"authors\") que haya hecho el juego en sus metadatos")