import re
import time


def ymljson(input_file, out_f):
    with open(input_file, 'r', encoding='utf8') as file:
        data = file.readlines()

    pattern_of_day = r'Суббота:\n'
    day_repl = r'{\n"Суббота":\n'

    braceList = [
        "Суббота:\n", "  Расписание:\n", "    Пара1:\n", "    Пара2:\n", "    Пара3:\n", "    Пара4:\n", "    Пара5:\n",
        "    Пара6:\n", "    Пара7:\n", "    Пара8:\n"
    ]

    with open(out_f, 'w', encoding='utf8') as out_f:
        for i in range(len(data)):
            if data[i] in ["Суббота:\n"]:
                rpl = re.sub(pattern_of_day, day_repl, data[i])
                out_f.write(rpl)

            elif data[i] in ["  Расписание:\n"]:
                rpl = re.sub("  Расписание:\n", '\t{\n\t"Расписание":\n\t\t{\n', data[i])
                out_f.write(rpl)

            elif data[i] in ["    Пара1:\n", "    Пара2:\n", "    Пара3:\n", "    Пара4:\n", "    Пара5:\n", "    Пара6:\n",
                             "    Пара7:\n", "    Пара8:\n"]:
                bufStr = data[i].braceListrip().split(':', maxsplit=1)
                out_f.write('\t\t"' + bufStr[0] + '":' + bufStr[1])
                out_f.write('\t\t\t{\n')

            else:
                if i + 1 == len(data):
                    bufStr = data[i].braceListrip().split(':', maxsplit=1)
                    a = bufStr[1].split("\n")
                    out_f.write('\t\t\t\t"' + bufStr[0] + '":' + a[0].braceListrip() + "\n")
                elif i + 1 != len(data) and (data[i + 1] in braceList):
                    bufStr = data[i].braceListrip().split(':', maxsplit=1)
                    a = bufStr[1].split("\n")
                    out_f.write('\t\t\t\t"' + bufStr[0] + '":' + a[0].braceListrip() + "\n")
                else:
                    bufStr = data[i].braceListrip().split(':', maxsplit=1)
                    a = bufStr[1].split("\n")
                    out_f.write('\t\t\t\t"' + bufStr[0] + '":' + a[0].braceListrip() + ",\n")
                if i + 1 != len(data) and data[i + 1] in braceList:
                    out_f.write('\t\t\t},\n')

        out_f.write("\t\t\t}\n\t\t}\n\t}\n}"'\n')


IN_YAML = r"input_yaml.yml"
OUT_JSON_REGEXP = r"output.json"

st = time.time()
for i in range(100):
    ymljson(IN_YAML, OUT_JSON_REGEXP)
et = time.time()
tm = et - st
print("Время выполнения, используя регулярные выражения - " + str(tm))