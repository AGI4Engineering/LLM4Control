from tex2py import tex2py
from typing import Union
from pathlib import Path

def generate_bench_tree(tex_file : Union[str,Path] = None):
    if tex_file is None:
        raise ValueError("tex_file is not provided")

    with open(tex_file,'r') as file:
        data = file.read()
    
    bench = tex2py(data)

    return bench
