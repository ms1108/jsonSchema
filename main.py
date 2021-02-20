# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.

from genson import SchemaBuilder


def genson():
    builder = SchemaBuilder()
    builder.add_schema({"type": "object", "properties": {}})
    # 例子
    # builder.add_object({"hi": "there"})
    # builder.add_object({"hi": None})
    builder.add_object({
        "code": 0,
        "res": "test success",
        "jsonSchema": ""
    })
    builder.add_object({
        "code": 0,
        "res": "test success",
        "jsonSchema": None
    })
    print(builder.to_json(indent=2))


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    genson()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
