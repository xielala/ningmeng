#配置文件
#propert  config  ini log4j

#configparser类里的ConfigParser模块
#configparser可以读取配置信息
import  configparser
#sectiom action value

class ReadConfig:
    def read_config(self,file_name,section,option):
        cf=configparser.ConfigParser()
        cf.read(file_name,encoding='utf-8')
        return cf.get(section,option)

if __name__ == '__main__':
    print(ReadConfig().read_config('case.config','PYTHON11','num'))