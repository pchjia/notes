常用命令 - 键值相关命令，服务器相关命令

redis-cli

1.键值相关命令
    keys pattern            # 返回满足给定pattern的所有键
    exists key_name         # 确认给定键是否存在
    del key_name            # 删除给定键

    expire key_name n       # 设置过期时间，n秒
    ttl key_name            # 返回键距离过期的时间，-1表示已经过期
    persist key_name        # 取消给定键的过期时间

    select n                # 选择下标为n的数据库
    move key_name n         # 将本数据库下的key移动到给定标号的数据库中

    randomkey               # 随机返回key空间的一个key

    rename key_name new_name # 重命名key的名称

    type key_name           # 返回键的数据类型


2.服务器相关命令
    ping                    # 测试连接是否存活
    echo                    # 在命令行打印一段内容
    select n                # 选择数据库编号(0 - 15)，默认为16个
    quit/exit               # 退出
    dbsize                  # 返回当前数据库中key的个数
    info                    # 获取服务器的信息和统计
    config get *            # 获取配置参数的值
        config get dir
    flushdb                 # 删除当前数据库中所有的keys
    flushall                # 删除所有数据库中的所有keys

