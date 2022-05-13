#!/usr/bin/python3
# Description:
#   lib/algebra/complex.py を元に、
#   dist/_notes/index.md
#   dist/_notes/algebra/complex.md を生成。
# Usage:
#   $ python3 generate_notes.py
import glob
import os
import sys

lib_folder = "lib/"
docs_folder = "docs/"
notes_folder = "dist/_notes/"
pages_folder = "dist/_pages/"
github_base_url = "https://github.com/moyomogi/python_2022_lib"

# YAML front matter
yaml_front_matter = """---
layout: page
title: Home
id: home
permalink: /
---"""

lib_paths = glob.glob(f"{lib_folder}*/*.py")
notes = []


if not os.path.exists(f"{pages_folder}"):
    os.mkdir(f"{pages_folder}")
if not os.path.exists(f"{notes_folder}"):
    os.mkdir(f"{notes_folder}")

for lib_path in lib_paths:
    with open(lib_path, "r") as f_lib:
        lib_lines = f_lib.readlines()
        split = lib_path.split("/")
        # print("split:", split, file=sys.stderr)

        par_folder = split[-2]  # algebra
        file_name = split[-1]  # complex.py
        file_base_name = file_name[:-3]  # complex
        link_name = f"{par_folder}/{file_base_name}"

        docs_lines = ""
        docs_path = f"{docs_folder}{link_name}.md"
        if os.path.isfile(docs_path):
            with open(docs_path, "r") as f_docs:
                docs_lines = f_docs.readlines()
                # RegEx

        note = {
            "lib_lines": lib_lines,
            "docs_lines": docs_lines,
            "par_folder": par_folder,
            "file_name": file_name,
            "file_base_name": file_base_name,
            "link_name": link_name,
        }
        notes.append(note)

        # Create dist/_notes/algebra
        if not os.path.exists(f"{notes_folder}{par_folder}"):
            os.mkdir(f"{notes_folder}{par_folder}")
notes.sort(key=lambda x: x["link_name"])

# Write dist/_pages/index.md
with open(f"{pages_folder}index.md", "w") as f:
    print(yaml_front_matter, file=f)
    print(file=f)

    print("## リンク", file=f)
    for note in notes:
        link_name = note["link_name"]
        # - [algebra/complex](https://moyomogi.github.io/python_2022_lib/algebra/complex)
        # print(f"- [{link_name}]({par_folder}/{file_name})", file=f)
        print(f"- [[{link_name}]]", file=f)
    print(file=f)

    print("## 使用したテンプレート", file=f)
    print(
        "[maximevaillancourt/digital-garden-jekyll-template](https://github.com/maximevaillancourt/digital-garden-jekyll-template)",
        file=f,
    )

# Write dist/_notes/*/*.md
for note in notes:
    lib_lines = note["lib_lines"]
    docs_lines = note["docs_lines"]
    par_folder = note["par_folder"]
    file_name = note["file_name"]
    file_base_name = note["file_base_name"]
    link_name = note["link_name"]
    print("link_name:", link_name, file=sys.stderr)

    # Write dist/_notes/algebra/complex.md
    with open(f"{notes_folder}{link_name}.md", "w") as f_notes:
        # YAML front matter
        print("---", file=f_notes)
        print("layout: page", file=f_notes)
        print(f"title: {link_name}", file=f_notes)
        print("---", file=f_notes)
        print(file=f_notes)

        print(f"# {link_name}", file=f_notes)
        print(file=f_notes)
        print("".join(docs_lines).strip(), file=f_notes)
        print(file=f_notes)
        # https://github.com/moyomogi/python_2022_lib/blob/master/lib/algebra/complex.py
        print(f"[View on GitHub]({github_base_url}/blob/master/{lib_folder}{par_folder}/{file_name})", file=f_notes)
        print(file=f_notes)
        print("```py", file=f_notes)
        print("".join(lib_lines).strip(), file=f_notes)
        # for line in lib_lines:
        #     print(line, file=f_notes, end="")
        print("```", file=f_notes)
        print(file=f_notes)

        print("## リンク", file=f_notes)
        for note in notes:
            link_name = note["link_name"]
            # - [[algebra/complex]]
            print(f"- [[{link_name}]]", file=f_notes)
