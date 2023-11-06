import yaml
import json
import time
def doptask1():
    sttime = time.time()
    with open("../input_yaml.yml", "r", encoding="UTF-8") as yaml_in, open("../out_json.json", "w") as json_out:
        yaml_object = yaml.safe_load(yaml_in)
        json.dump(yaml_object,json_out)
    endtime = time.time()
    restime = endtime - sttime
    print("Время выполнения используя готовые библиотеки - ", restime)
doptask1()
