import json
import os.path

from util import get_base_dir


class FileTool:
    config_file = os.path.join(get_base_dir(), 'data', 'config.json')

    class Keys:
        REQUEST_DURATION = 'request_duration'  # 查询间隔
        OPACITY = 'opacity'  # 不透明度

    @classmethod
    def get_config_value(cls, key):
        """
        根据键获取配置文件的值
        :param key: str, 配置文件中的键
        :return: 配置文件的值
        """
        config = FileTool.load_configs()
        return config.get(key)

    @classmethod
    def load_configs(cls):
        with open(cls.config_file, mode='r') as f:
            config = json.load(f)
        return config

    @classmethod
    def set_config_value(cls, key, value):
        config = cls.load_configs()
        config[key] = value
        with open(cls.config_file, 'w') as f:
            json.dump(config, f)


if __name__ == '__main__':
    print(FileTool.get_config_value(FileTool.Keys.REQUEST_DURATION))
    FileTool.set_config_value('opacity', 0.7)
