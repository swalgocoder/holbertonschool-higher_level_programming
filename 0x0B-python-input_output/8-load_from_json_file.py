#!/usr/bin/python3

def load_from_json_file(filename):
    with open(filename, 'r') as f:
        import os
        import json
        return json.loads(f.read())
