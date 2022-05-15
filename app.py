import os
import argparse
from logparser.parser import Parser
import time


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
            params_length = len(om.parameter_keys)
            sip_msg = ""
            phrase = ""
            code = ""
            for p in om.parameter_keys:
                if params_length == 1 and p[0] == 'method':
                    sip_msg = p[1]
                elif p[1].strip().isnumeric() and p[0] == 'statusCode':
                    code = p[1]
                elif p[0] == 'reasonPhrase':
                    phrase = p[1]

            if params_length > 1:
                sip_msg = phrase.strip() + "_" + code.strip()

            if om.receiving_component == "":
                py.write(f"\twith obj{om.obj_num}:\n")
                py.write(f"\t\tobj{om.obj_num}.{om.event_type}('{om.operation_type}', {om.duration})\n")
            elif len(sip_msg) > 0:
                py.write(f"\twith obj{om.obj_num}:\n")
                py.write(f"\t\tobj{obj_dict[om.receiving_component]}.{sip_msg}()\n")
            # else:
            #     py.write(f"\t\tobj{obj_dict[om.receiving_component]}.{om.event_type}()\n")

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
    # parser.print()

    filename = f"Communication{time.time()}"
    run_message(filename, parser.get_messages())
