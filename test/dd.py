from loguru import logger

from tools.日志目录处理方法 import log_path

# 持久化日志文件
logger.add(sink=log_path,
           encoding="utf8",
           level="INFO",
           rotation='100kB',
           retention=2)

# 场景1： 断言记录日志
logger.info("-------------------执行登录的操作--------------")
actural_result = "登录成功"
expected_result = "登录成功"
logger.info(f"执行结果是{actural_result}")
logger.info(f"预期结果是{expected_result}")
try:
    assert actural_result == expected_result,"断言失败，预期结果和实际结果不一样！"
    logger.info("断言成功！")
except AssertionError as e:
    logger.error("记录日志：断言失败！{e}")
    # 如果直接这样捕获记录日志，这个用例不会被识别为失败的用例。所以不统计到错误率；想要被统计：需要手动抛出异常
    raise e