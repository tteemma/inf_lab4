import time


def spece_count(str):
    return len(str) - len(str.lstrip())


def ymljson(file,out_f):
    # file = r"input_yaml.yml"

    bufer = ""
    root = {}
    with open(file, 'r', encoding="UTF-8") as f:
        bufer = f.readlines()
        # print(bufer)

    hier = []
    for i in bufer:
        key, value = i.split(":", 1)
        layer, key = spece_count(key) // 2, key.lstrip()
        # print(layer,key)
        hier.insert(layer, key)  # Добавить эл по индексу layer
        # print(hier[-1])
        # print(key)
        while hier[-1] != key:
            hier.pop()
        if value == '\n':
            current_tree = root
            for node in hier:
                if node in current_tree:
                    current_tree = current_tree[node]
                else:
                    current_tree[node] = {}
        else:
            current_tree = root
            for node in hier:
                if node in current_tree:
                    current_tree = current_tree[node]
                else:
                    current_tree[node] = value.strip()
    # print(str(root).replace('\'', '\"'))

    a = str(root).replace('\'','\"')
    with open(out_f, 'w', encoding="UTF-8") as file_out:
        file_out.write(a)

sttime = time.time()
for i in range(100):
    ymljson(r"input_yaml.yml",r"outJson.json")
endtime = time.time()
restime = endtime - sttime
print("Время выполнения, моей программы -", str(restime))

# ymljson(r"input_yaml_forTask3(1).yml")
# ymljson(r"input_yaml_forTask3(2).yml")
