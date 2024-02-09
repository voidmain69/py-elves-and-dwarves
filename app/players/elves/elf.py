from abc import ABC, abstractmethod
from app.players.player import Player


class Elf(Player, ABC):
    @abstractmethod
    def __init__(self, nickname: str, musical_instrument: str) -> None:
        super().__init__(nickname)
        self.__musical_instrument = musical_instrument

    def play_elf_song(self) -> None:
        print(f"{self.nickname} is playing a song on the "
              f"{self.__musical_instrument}")