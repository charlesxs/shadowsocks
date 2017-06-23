# Shadowsocks 客户端软件


**功能：**
    修改 python版shadowsocks-2.8.2软件添加白名单功能使其能自动区分国内外流量

    白名单: whitelist.txt,  此白名单是从ip纯真库下载并处理成白名单, 包含了大部分国内IP地址.

    whitelist.txt 格式: 每个IP或者域名或者IP段为一行添加进去即可.

**用法：**

    Mac上使用:  ./bin/shadowsocks [start | stop | restart | list | change <num>]
    
    windows上使用: python3 sslocal.py

    例子:

        ![restart](/../screenshots/screenshots/restart-001.png?raw=true)

        ![list](/../screenshots/screenshots/list-001.png?raw=true)

        ![change](/../screenshots/screenshots/change-001.png?raw=true)

        ![list](/../screenshots/screenshots/list-002.png?raw=true)


**依赖:**

    python >= 3.4

**python版shadowsocks安装:**

    pip install shadowsocks

