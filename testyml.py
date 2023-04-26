import yaml

with open('List_object.yaml','r') as file:
    try:
        print(yaml.safe_load(file))
    except yaml.YAMLError as exc:
        print(exc)