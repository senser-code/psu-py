import psuwrapper
import json
import os
import utils

config = json.loads(utils.read_file("./config.json"))
obfuscator = psuwrapper.obfuscator(config.get("key"))
obfuscateddir = os.path.join(os.getcwd(), "obfuscatedscripts")
for file in os.listdir("./scripts"):
    file_path = os.path.join(os.getcwd(), "scripts", file)
    print(f'obfuscating {file}')
    if (os.path.isfile(file_path)):
        try:
            script = obfuscator.obfuscate(utils.read_file(file_path), config.get("options"))
            utils.write_file(os.path.join(obfuscateddir, file), script)
            print(f'obfuscated {file}')
        except:
            print(f'failed to obfuscate {file}')