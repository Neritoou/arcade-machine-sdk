from abc import ABC, abstractmethod
from typing import List
from .game_meta import GameMeta
import pygame

class GameBase(ABC):
    """
    Clase base que todo juego debe implementar para integrarse al Core.

    Arquitectura pensada para un loop único del Core:
      - El Core mantiene la ventana y el loop global.
      - Los juegos nunca crean su propio loop ni su propia ventana.
      - Cada juego expone métodos que el Core llama por frame.

    Flags importantes:
      - running: True cuando el juego está activo.
    """
    def __init__(self, metadata: GameMeta) -> None:
        # Flag para saber si el juego está activo
        self._running = False
        metadata.validate()
        self.metadata = metadata

    def start(self) -> None:
        """
        Marca el juego como activo.
        - Su uso en clases concretas debe llamar a **super()**.
        - Se llama cada vez que el usuario inicia el juego desde el menú del Core.
        """
        self._running = True

    def stop(self) -> None:
        """
        Detiene el juego, libera recursos dinámicos si es necesario.
        - Su uso en clases concretas debe llamar a **super()**.
        - Se llama cuando el usuario vuelve al menú o cierra el juego.
        """
        self._running = False

    @abstractmethod
    def handle_input(self, events: List[pygame.event.Event]) -> None:
        """
        Recibe los eventos que pasan por el Core (teclado, mouse, joystick)
        y los procesa para la lógica del juego.
        - Nunca debe llamar a `pygame.event.get()` por sí mismo.

        args:
            **events**: lista de eventos de pygame capturados en el frame actual
        """
        pass

    @abstractmethod
    def update(self, dt: float) -> None:
        """
        Actualización de la lógica del juego por frame.
        - Se llama solo si `_running=True`.

        args:
            **dt**: tiempo en segundos desde el último frame (para movimientos independientes del FPS)
        """
        pass
    
    @abstractmethod
    def render(self) -> None:
        """
        Dibuja todo el estado del juego en la superficie que pasa el Core.
        - Nunca crea su propia ventana.
        - Se llama solo si `_running=True`.
        """
        pass

    @property
    def is_running(self) -> bool:
        """
        Devuelve el estado actual del juego (activo o no).
        Útil para el Core para saber si debe llamar a update() y render().
        """
        return self._running