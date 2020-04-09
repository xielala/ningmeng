

#配置文件
#propert  config  ini log4j

#configparser类里的ConfigParser模块
#configparser可以读取配置信息
import  configparser
#sectiom action value

cf=configparser.ConfigParser()

cf.read('case.config',encoding='utf-8')

#读取配置文件的数据两种方式：
# res=cf.get('MODE','mode')
# print(res)
#
# res_1=cf['MODE']['mode']
# print(res_1)

# print(cf.sections())
# print(cf.items('PYTHON11'))

#数据类型讨论的问题
print(type(cf.get('PYTHON11','num')))
print(type(cf.get('PYTHON11','name')))