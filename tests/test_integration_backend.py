import pathlib
import unittest

from logparser.message import Message
from logparser.parser import Parser


class TestParserIntegration(unittest.TestCase):
    def setUp(self) -> None:
        self.parser: Parser = Parser()
        self.dir: pathlib.Path = pathlib.Path(__file__).parent.resolve()

    def test_parse(self) -> None:
        self.parser.parse(str(self.dir / 'testinput.txt'))
        messages = self.parser.get_messages()
        self.assertIsNotNone(messages)
        self.assertListEqual([Message(id=0, timestamp='2014/Oct/24 18:34:29.390320', sending_component='mtc',
                                      event_type='PORTEVENT',
                                      operation_type='Sent', receiving_component='849',
                                      message_type='@variables.internalPortMessageWithAspsSip',
                                      parameter_keys=[('statusCode', '100', 6), ('reasonPhrase', 'Trying', 6),
                                                      ('method', 'INVITE', 7)],
                                      duration=0, obj_num=0), Message(id=1, timestamp='2014/Oct/24 18:34:29.904175',
                                                                      sending_component='856', event_type='TIMEROP',
                                                                      operation_type='Stop timer',
                                                                      receiving_component='',
                                                                      message_type='', parameter_keys=[],
                                                                      duration='60',
                                                                      obj_num=0)], messages)
