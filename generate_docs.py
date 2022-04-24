#!/usr/bin/python3
# Description:
#   lib/algebra/complex.py を元に、
#   dist/_notes/index.md
#   dist/_notes/algebra/complex.md を生成。
# Usage:
#   $ python3 generate_docs.py
import glob
import os
import sys

lib_folder = "lib/"
notes_folder = "dist/_notes/"
pages_folder = "dist/_pages/"
github_base_url = "https://moyomogi.github.io/python_2022_lib/"

# YAML front matter
yaml_front_matter = """---
layout: page
title: Home
id: home
permalink: /
---"""

file_paths = glob.glob(f"{lib_folder}*/*.py")
notes = []


if not os.path.exists(f"{pages_folder}"):
    os.mkdir(f"{pages_folder}")
if not os.path.exists(f"{notes_folder}"):
    os.mkdir(f"{notes_folder}")

for file_path in file_paths:
    with open(file_path, "r") as f_lib:
        lines = f_lib.readlines()
        print("file_path:", file_path, file=sys.stderr)
        split = file_path.split("/")
        print("split:", split, file=sys.stderr)

        par_folder = split[-2]  # algebra
        file_name = split[-1]  # complex.py
        file_base_name = file_name[:-3]  # complex
        link_name = f"{par_folder}/{file_base_name}"

        note = {
            "lines": lines,
            "par_folder": par_folder,
            "file_name": file_name,
            "file_base_name": file_base_name,
            "link_name": link_name,
        }
        notes.append(note)

        # Create dist/_notes/algebra
        if not os.path.exists(f"{notes_folder}{par_folder}"):
            os.mkdir(f"{notes_folder}{par_folder}")


# Write dist/_pages/index.md
with open(f"{pages_folder}index.md", "w") as f:
    print(yaml_front_matter, file=f)
    print(file=f)

    print("## リンク", file=f)
    for note in notes:
        link_name = note["link_name"]
        # - [algebra/complex](https://moyomogi.github.io/python_2022_lib/algebra/complex)
        # print(f"- [{link_name}]({github_base_url}{link_name})", file=f)
        print(f"- [[{link_name}]]", file=f)
    print(file=f)

    print("## 使用したテンプレート", file=f)
    print(
        "[maximevaillancourt/digital-garden-jekyll-template](https://github.com/maximevaillancourt/digital-garden-jekyll-template)",
        file=f,
    )

# Write dist/_notes/*/*.md
for note in notes:
    lines = note["lines"]
    par_folder = note["par_folder"]
    file_name = note["file_name"]
    file_base_name = note["file_base_name"]
    link_name = note["link_name"]

    # Write dist/_notes/algebra/complex.md
    with open(f"{notes_folder}{link_name}.md", "w") as f_docs:
        # YAML front matter
        print("---", file=f_docs)
        print("layout: note", file=f_docs)
        print(f"title: {link_name}", file=f_docs)
        print("---", file=f_docs)
        print(file=f_docs)

        print(f"# {link_name}", file=f_docs)
        # https://github.com/moyomogi/python_2022_lib/blob/master/lib/algebra/complex.py
        print(f"[View on GitHub]({github_base_url}blob/master/{lib_folder}{par_folder}/{file_name})", file=f_docs)
        print("```py", file=f_docs)
        for line in lines:
            print(line, file=f_docs, end="")
        print("```", file=f_docs)
        print(file=f_docs)

        # print("## リンク", file=f_docs)
        # for note in notes:
        #     link_name = note["link_name"]
        #     # - [algebra/complex](https://moyomogi.github.io/python_2022_lib/algebra/complex)
        #     # print(f"- [{link_name}]({github_base_url}{link_name})", file=f_docs)
        #     print(f"- [[{link_name}]]", file=f_docs)
