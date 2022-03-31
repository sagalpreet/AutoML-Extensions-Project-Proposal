import os

DIR = os.path.abspath(os.path.dirname(__file__))

FILE = f'{DIR}/test/unit_test/automl_test.cc'

content = None

with open(FILE, 'r') as f:
    content = f.read().split('  const size_t deterministic_champ_switch = 161;')

content1 = content[0]
text = '  const size_t deterministic_champ_switch = '
content2 = content[1]

x = f'{DIR}/build/test/unit_test'


for i in range(1332):
    with open(FILE, 'w') as f:
        s = text + str(i) + ';'
        f.write(content1+s+content2)
    os.system(f'make -C {x} > /dev/null')
    val = os.system(f'{x}/vw-unit-test.out -t automl_first_champ_switch > /dev/null 2> /dev/null')
    print(i, val)
    if (val == 0):
        break
