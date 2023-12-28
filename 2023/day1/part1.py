import re

collection_name = "b1_asd"
pattern = re.compile(r"b(\d)_(\w)*")
if pattern.match(collection_name) is None:
    print(0)
else:
    print(pattern.match(collection_name).group(1))
