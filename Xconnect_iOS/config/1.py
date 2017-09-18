import yaml
# aa = open("config.yml","r")
# x = yaml.load_all(aa)
# print x["msg_1"]
# import yaml
#
# yaml_str = """
# name: 灰蓝
# age: 0
# job: Tester
# """
# f= open("test.yml")
# y = yaml.dump(yaml_str)
# print (y)
import yaml
fs = open("test.yml","rb")
y = yaml.load_all(fs)
for y1 in y:
    print(y1)
