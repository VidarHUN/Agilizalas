
import unittest

from logparser.parser import Parser


class TestParser(unittest.TestCase):
    def setUp(self) -> None:
        self.parser: Parser = Parser()

    def test_sent_portevent_not_none(self) -> None:
        line = "2014/Oct/24 18:34:28.927072 mtc PORTEVENT " \
               "SipClientLayerComponent.ttcn:202(function:sendInternalMessage) Sent on sipInternalPort[0] to 849 " \
               "@variables.internalPortMessageWithAspsSip : {"
        actual = self.parser.check_portevent(line)
        self.assertIsNotNone(actual)
        self.assertTupleEqual(actual.groups(), ("2014/Oct/24 18:34:28.927072", "mtc", "PORTEVENT", "Sent", "849",
                                                "@variables.internalPortMessageWithAspsSip"))

    def test_receive_portevent_not_none(self) -> None:
        line = "2014/Oct/24 18:34:28.912747 mtc PORTEVENT " \
               "SipClientLayerComponent.ttcn:254(function:receiveInternalMessage) Receive operation on port " \
               "sipInternalPort[0] succeeded, message from 849: @variables.internalPortMessageWithAspsSip : { "
        actual = self.parser.check_portevent(line)
        self.assertIsNotNone(actual)
        self.assertTupleEqual(actual.groups(), ("2014/Oct/24 18:34:28.912747", "mtc", "PORTEVENT", "Receive", "849",
                                                "@variables.internalPortMessageWithAspsSip"))

    def test_portevent_none(self) -> None:
        line = ""
        actual = self.parser.check_portevent(line)
        self.assertIsNone(actual)

    def test_timerop(self) -> None:
        line = "2014/Oct/24 18:34:28.927258 mtc TIMEROP " \
               "SipClientLayerComponent.ttcn:245(function:receiveInternalMessage) Start timer " \
               "TimerTestCaseInternalCommunicationGuard: 185 s"
        actual = self.parser.check_timerop(line)
        self.assertIsNotNone(actual)
        self.assertTupleEqual(actual.groups(), ("2014/Oct/24 18:34:28.927258", "mtc", "TIMEROP", "Start timer",
                                                "TimerTestCaseInternalCommunicationGuard", "185"))

    def test_timerop_none(self) -> None:
        line = ""
        actual = self.parser.check_timerop(line)
        self.assertIsNone(actual)

    def test_get_param_keys_not_none(self) -> None:
        line = 'method := "INVITE"'
        actual = self.parser.get_sip_param_keys(line)
        self.assertIsNotNone(actual)
        self.assertTupleEqual(actual, ('method', 'INVITE', 0))
        line = '    method := "INVITE"'
        actual = self.parser.get_sip_param_keys(line)
        self.assertIsNotNone(actual)
        self.assertTupleEqual(actual, ('method', 'INVITE', 1))
        line = "statusCode := 100,"
        actual = self.parser.get_sip_param_keys(line)
        self.assertIsNotNone(actual)
        self.assertTupleEqual(actual, ('statusCode', '100', 0))
        line = 'reasonPhrase := "Trying"'
        actual = self.parser.get_sip_param_keys(line)
        self.assertIsNotNone(actual)
        self.assertTupleEqual(actual, ('reasonPhrase', 'Trying', 0))

    def test_get_param_keys_none(self) -> None:
        line = ['method := "INVITE_E 100"', 'valami := "INVITE"']
        for li in line:
            actual = self.parser.get_sip_param_keys(li)
            self.assertIsNone(actual)
