#!/usr/bin/env python3

import os
import sys

from ruamel import yaml
from argparse import ArgumentParser
from jsonschema import validate
from jsonschema.exceptions import ValidationError

def load_yaml(filename):
    assert os.path.isfile(filename)
    with open(filename) as f:
        obj = yaml.safe_load(f)
    return obj

def validate_yaml(target=None, schema=None):
    target_yml = load_yaml(target)
    schema_yml = load_yaml(schema)
    try:
        validate(target_yml, schema_yml)
        result = 0
    except ValidationError as ve:
        print(ve)
        result = -1
    return result

def main():
    args = sys.argv[1:]
    parser = ArgumentParser()
    parser.add_argument(
        'target',
        metavar='TARGET',
        help='path to target yaml file to validate',
    )
    parser.add_argument(
        'schema',
        metavar='SCHEMA',
        help=' path to schema yaml file to validate with',
    )
    ns = parser.parse_args(args)
    print(ns)
    return validate_yaml(**ns.__dict__)

if __name__ == '__main__':
    sys.exit(main())
