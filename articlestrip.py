#!/usr/bin/python3.6
### HTML Article Element Stripper
#
### Written by: DeeJayh
#
### Use for archival purposes and information retention.
### Using this program to steal information and portray it as your own,
### otherwise known as Copyright Infringement, is expressly prohibited.
### Credit people for their work. Don't be a douche.
#
### Released under the MIT License

import os

for root, directories, filenames in os.walk(os.getcwd()):
    for dir in directories:
        dir = dir
    for file in filenames:
        stripped = []
        if file == "index.html":
            print(f"Found {file}. Opening.")
            with open(f'{root}/index.html', encoding="utf8") as f:
                line = f.readline()
                insidearticle = False
                while line:
                    line = f.readline()
                    if line.strip().startswith("<article"):
                        stripped.append(line)
                        insidearticle = True
                    elif line.strip().startswith("</article"):
                        stripped.append(line)
                        insidearticle = False
                    elif insidearticle == True:
                        stripped.append(line)
                    else:
                        pass
                print(f"{file} stripped. Writing to Index.md.")

            with open(f'{root}/index.md', 'w') as f:
                for line in stripped:
                    f.writelines(line)
            print("Index.md complete.")


exit(0)