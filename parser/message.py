class Message:
  def __init__(self, id, timestamp, sending_component, event_type, sending_file, operation_type, receiving_component, message_type, parameter_keys):
    self._id = id
    self._timestamp = timestamp
    self._sending_component = sending_component
    self._event_type = event_type
    self._sending_file = sending_file
    self._operation_type = operation_type
    self._receiving_component = receiving_component
    self._message_type = message_type
    self._parameter_keys = parameter_keys
    
  def get_sending_component(self):
    return self._sending_component

  def get_receiving_component(self):
    return self._receiving_component

  def get_operation_type(self):
    return self._operation_type

  def get_sending_file(self):
    return self._sending_file

  def get_message_type(self):
    return self._message_type

  def get_parameter_keys(self):
    return self._parameter_keys
