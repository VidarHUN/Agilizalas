from dataclasses import dataclass, field
from typing import List, Tuple, NoReturn


# Goldschmidt falra mászna az OOP-tlanságtól, kijavíthatjuk majd
@dataclass
class Message:
    id: int
    timestamp: str
    sending_component: str
    event_type: str
    operation_type: str = ""
    receiving_component: str = ""
    message_type: str = ""
    parameter_keys: List[Tuple[str, str, int]] = field(default_factory=list)
    duration: int = 0
    obj_num: int = 0

    def add_parameter_key(self, key: Tuple[str, int]) -> NoReturn:
        """ Appends a parameter key to the parameter key list in a message
        Parameter:
        key: Tuple[str, int] - parameter key to be appended
        """
        self.parameter_keys.append(key)
