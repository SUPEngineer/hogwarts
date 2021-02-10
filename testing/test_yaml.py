import yaml


def test_yaml():
    with open("./datas/calc.yml")as f:
        ya = yaml.safe_load(f)
        print(ya['add']['datas'])
        return ya['add']['datas']
