"""
这是做路径处理的公共方法
"""
from pathlib import Path


log_path = Path(__file__).absolute().parent.parent/"logs"/"test.log"


if __name__ == '__main__':
    print(log_path)