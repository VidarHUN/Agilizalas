import os
import argparse
from logparser.parser import Parser

'''
class Message:
    def __init__(self, id, timestamp, sending_component, event_type, operation_type, receiving_component, message_type,
                 parameter_keys, duration):
        self.id = id
        self.timestamp = timestamp
        self.sending_component = sending_component
        self.event_type = event_type
        self.operation_type = operation_type
        self.receiving_component = receiving_component
        self.message_type = message_type
        self.parameter_keys = parameter_keys
        self.duration = duration
        self.obj_num = 0
'''

def generate_python(messages, filename):

    obj_dict = {}

    with open('generated.py', 'w') as py:
        py.write("import napkin\n\n")
        py.write("import os\n\n")
        py.write(f"@napkin.seq_diagram('{filename}')\n")
        py.write("def diag(c):\n")
        py.write("\tobj1 = c.object('system')\n")
        obj_dict['system'] = 1
        i = 3
        for ob in messages:
            py.write(f"\tobj{i} = c.object('{ob.sending_component}')\n")
            ob.obj_num = i
            obj_dict[ob.sending_component] = i
            i += 1
        py.write("\n")

        for om in messages:
            py.write(f"\twith obj{om.obj_num}:\n")
            if om.receiving_component == "":
                py.write(f"\t\tobj{om.obj_num}.{om.event_type}()\n")
            else:
                py.write(f"\t\tobj{obj_dict[om.receiving_component]}.{om.event_type}()\n")

        py.write("\n\n\n")
        py.write("def generate():\n")
        py.write("\tnapkin.generate(output_format='plantuml_png', output_dir='./output')\n")
        py.write(f"\tos.remove('./output/{filename}.puml')\n")
        py.write("\tnapkin.generate(output_format='plantuml_txt', output_dir='./output')\n")

        py.write("\n\nif __name__ == '__main__':\n")
        py.write('\tgenerate()')
        py.close()


def read_messages():
    messages = []
    with open("gui/messages.txt", "r") as m:
        lines = m.readlines()
        for line in lines:
            messages.append(line)
    message_objects = []
    for mess in messages:
        exec(f"message_objects.append({mess})")
    return message_objects


def run_txt(filename):
    message = read_messages()
    generate_python(message, filename)
    os.system("python generated.py")


def run_message(filename, message):
    generate_python(message, filename)
    os.system("python generated.py")


# See https://pypi.org/project/napkin/ for more about this library
if __name__ == '__main__':
    arg_parser = argparse.ArgumentParser(description='Process some integers.')
    arg_parser.add_argument('--file', dest='file',
                        help='path of the log files')

    args = arg_parser.parse_args()

    parser = Parser()
    parser.parse(args.file)
    parser.print()

    filename = "Communication"
    run_message(filename, parser.get_messages())

