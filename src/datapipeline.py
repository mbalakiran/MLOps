import os
import argparse
import yaml
import logging

def read_config(config_path):
    with open(config_path) as yaml_f:
        config = yaml.safe_load(yaml_f)
    return config


def main(config_path, datasource):
    config= read_config(config_path)
    print(config)

if __name__ == "__main__":
    args = argparse.ArgumentParser()
    defa = os.path.join("config","params.yaml")
    args.add_argument("--config", default= defa)
    args.add_argument("--datasource",default=None)

    parsed_args = args.parse_args()
    main(config_path=parsed_args.config, datasource=parsed_args.datasource)
    # print(parsed_args.config, parsed_args.datasource)
