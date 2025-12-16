from abc import ABC, abstractmethod
from .game_meta import GameMeta
from ..constants import BASE_RESOLUTION, DEFAULT_FPS
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
        metadata.validate()
        self._running = False
        self.metadata = metadata
        self.__surface = None

    def start(self, surface: pygame.Surface) -> None:
        """
        Marca el juego como activo.
        - Su uso en clases concretas debe llamar a **super()**.
        - Se llama cada vez que el usuario inicia el juego desde el menú del Core.
        - A este método se le debe pasar una superficie en la que el juego se dibujará.

        args:
            **screen**: Pantalla o superficie en la que el juego se dibujará.
        """
        self._running = True
        self.__surface = surface

    def stop(self) -> None:
        """
        Detiene el juego, libera recursos dinámicos si es necesario.
        - Su uso en clases concretas debe llamar a **super()**.
        - Se llama cuando el usuario vuelve al menú o cierra el juego.
        """
        self._running = False

    @abstractmethod
    def handle_events(self, events: list[pygame.event.Event]) -> None:
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
    def running(self) -> bool:
        """
        Devuelve el estado actual del juego (activo o no).
        Útil para el Core para saber si debe llamar a update() y render().
        """
        return self._running
    
    @property
    def surface(self) -> pygame.Surface:
        """
        Devuelve la superficie actual en la que el juego se está dibujando.
        """
        if self.__surface == None:
            raise AttributeError("No hay ninguna superficie disponible")
        return self.__surface

    def run_independently(self) -> None:
        """
        Ejecuta el juego de forma independiente sin necesidad del Core.
        Útil para desarrollo y testing.
        """
        if not pygame.get_init():
            pygame.init()

        screen = pygame.display.set_mode(BASE_RESOLUTION)
        pygame.display.set_caption(self.metadata.title)
        clock = pygame.time.Clock()
        self.start(screen)

        try:
            while self._running:
                events = pygame.event.get()

                for event in events:
                    if event.type == pygame.QUIT:
                        self.stop()
                        break

                if self._running:
                    self.handle_events(events)

                if self._running:
                    dt = clock.get_time() / 1000.0
                    self.update(dt)

                if self._running:
                    self.render()
                    pygame.display.flip()

                clock.tick(DEFAULT_FPS)

        except KeyboardInterrupt:
            pass
        
        finally:
            self.stop()
            pygame.quit()