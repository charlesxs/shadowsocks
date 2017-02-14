# Shadowsocks 客户端软件


**功能：**
    修改 python版shadowsocks-2.8.2软件添加白名单功能时期能自动区分国内外流量

    白名单: whitelist.txt,  此白名单是从ip纯真库下载并处理成白名单, 包含了大部分国内IP地址.

    whitelist.txt 格式: 每个IP或者域名或者IP段为一行添加进去即可.

**用法：**

    linux上使用:  python3 sslocal.py [start|stop|restart]
    
    windows上使用: python3 sslocal.py

**依赖:**

    python >= 3.4

**python版shadowsocks安装:**

    pip install shadowsocks
