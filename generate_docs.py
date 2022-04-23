#!/usr/bin/python3
# Description:
#   lib/algebra/complex.py を用いて、docs/algebra/complex.md を生成。
# Usage:
#   $ python3 generate_docs.py
import glob
import os
import sys

lib_folder = "lib/"
docs_folder = "docs/"

file_paths = glob.glob(f"{lib_folder}*/*.py")

for file_path in file_paths:
    with open(file_path, "r") as f_lib:
        lines = f_lib.readlines()
        print("file:", file_path, file=sys.stderr)
        split = file_path.split("/")
        print("split:", split, file=sys.stderr)
        par_dir = split[-2]  # algebra
        file_name = split[-1]  # complex.py

        # Create docs/algebra
        if not os.path.exists(f"{docs_folder}{par_dir}"):
            os.mkdir(f"{docs_folder}{par_dir}")

        # Write docs/algebra/complex.md
        with open(f"{docs_folder}{par_dir}/{file_name[:-3]}.md", "w") as f_docs:
            print(f"# {file_name}", file=f_docs)
            print("```py", file=f_docs)
            for line in lines:
                print(line, file=f_docs, end="")
            print("```", file=f_docs)
