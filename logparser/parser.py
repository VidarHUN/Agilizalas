import re
from typing import Dict, Optional
from logparser.message import *


class Parser:
    """ Parser class
    Parses a file with parse method, and stores specific messages.
    """

    def __init__(self) -> None:
        self.messages: List[Message] = []

    def print(self) -> NoReturn:
        """ Prints messages to std_out """
        for i in self.messages:
            print(i.__repr__())

    def check_portevent(self, line: str) -> Optional[re.Match]:
        """ Checks if line is a valid PORTEVENT log
        We only parse SENT and RECEIVE log lines, the method checks if a given line matches their regex.

        Parameters:
        line: str - log line to be checked
        Return:
        Optional[re.Match] - returns the match object if valid, None otherwise
        """
        regex = {"Sent": r"(\d{4}.[a-zA-Z]{3}.\d{2} \d{2}:\d{2}:\d{2}.\d{6}) "
                                         r"(\w*) ([A-Z]+) .* (Sent) on .* to (\w+) ([@\w.]+)",
                                 "Receive": r"(\d{4}.[a-zA-Z]{3}.\d{2} \d{2}:\d{2}:\d{2}.\d{6}) "
                                            r"(\w*) ([A-Z]+) .* (Receive) .* from (\w+).*: ([@\w.]+)"
                                 }
        for k in regex:
            match_obj: re.Match = re.search(regex[k], line)
            if match_obj is not None:
                return match_obj
        return None

    def check_timerop(self, line: str) -> Optional[re.Match]:
        """ Checks if line is a valid TIMEROP log
        TIMEROP logs may only be START TIMER, TIMEOUT or STOP TIMER

        Parameters:
        line: str - log line to be checked
        Return:
        Optional[re.Match] - returns the match object if valid, None otherwise
        """
        regex = r"(\d{4}.[a-zA-Z]{3}.\d{2} \d{2}:\d{2}:\d{2}.\d{6}) (\w*) ([A-Z]+) .* " \
                     r"(Start timer|Timeout|Stop timer) (\w+): ([\d\.]+)"
        match_obj = re.search(regex, line)
        return match_obj

    def get_sip_param_keys(self, line) -> Optional[Tuple[str, str, int]]:
        """ Parses parameter keys from given log line

        Parameters:
        line: str - log line to be parsed
        Returns:
        Optional[Tuple[str, str, int]] - returns the parameter key and depth if valid log line, None otherwise
        """
        stripped = line.lstrip()
        param_depth = int((len(line) - len(line.lstrip())) / 4)
        key = stripped.split(" ")[0]
        value = ""
        if '"' in stripped:
            value = stripped.split('"')[1].strip(' ').strip(',')
        elif '{' not in stripped and '}' not in stripped:
            value = stripped.split(':=')[1].strip(",").strip("\n")

        # Ha az első szó betű vagy szám, (vagy tartalmaz "_"karaktert)
        if key.isalnum() or "_" in key:
            #print(f"{key} {value}")
            if key in ['method', 'statusCode', 'reasonPhrase'] and '_' not in value:
                if value[0] == " ":
                    value = value[1:]
                if value[-1] == ",":
                    value = value[:-1]
                return (key, value, param_depth)
        return None

    def get_messages(self) -> List[Message]:
        """ Returns the messages
        Getter method for internal messages

        Returns:
        List[Message] - internal messages
        """
        return self.messages

    def parse(self, file: str) -> NoReturn:
        """ Parses the given file
        Iterates through the given file and for each line it check if it contains an interesting (PORTEVENT, TIMEROP)
        message or not.

        Parameters:
        file: str - file path
        """
        message_scope = False
        id = 0
        with open(file, "r") as f:
            for line in f:
                if re.search(r"^\d{4}.[a-zA-Z]{3}.\d{2} \d{2}:\d{2}:\d{2}.\d{6}", line) is not None:
                    if "PORTEVENT" in line:
                        if 'sip' in line or "Sip" in line:
                            if line[-2] == '{':
                                match_obj = self.check_portevent(line)
                                if match_obj:
                                    self.messages.append(Message(id, timestamp=match_obj.group(1),
                                                                 sending_component=match_obj.group(2),
                                                                 event_type=match_obj.group(3),
                                                                 operation_type=match_obj.group(4),
                                                                 receiving_component=match_obj.group(5),
                                                                 message_type=match_obj.group(6)))
                                    message_scope = True
                                    id += 1
                            # nem tudom hogy kell-e
                            else:
                                message_scope = False
                    elif "TIMEROP" in line:
                        message_scope = False
                        match_obj = self.check_timerop(line)
                        self.messages.append(Message(id, timestamp=match_obj.group(1),
                                                     sending_component=match_obj.group(2),
                                                     event_type=match_obj.group(3),
                                                     operation_type=match_obj.group(4),
                                                     duration=match_obj.group(6)))
                        id += 1
                    else:
                        message_scope = False
                else:
                    if message_scope:
                        param_tuple = self.get_sip_param_keys(line)
                        if param_tuple is not None:
                            self.messages[-1].add_parameter_key(param_tuple)
