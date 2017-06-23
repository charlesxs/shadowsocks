# Shadowsocks 客户端软件


**功能：**
    修改 python版shadowsocks-2.8.2软件添加白名单功能使其能自动区分国内外流量

    白名单: whitelist.txt,  此白名单是从ip纯真库下载并处理成白名单, 包含了大部分国内IP地址.

    whitelist.txt 格式: 每个IP或者域名或者IP段为一行添加进去即可.

**用法：**

    Mac上使用:  ./bin/shadowsocks [start | stop | restart | list | change <num>]
    
    windows上使用: python3 sslocal.py
    
    例子:
        
        <img width="483" alt="restart-001" src="https://user-images.githubusercontent.com/7393682/27466207-825dda4e-580b-11e7-87dc-ee11012b59e9.png">
        
        <img width="484" alt="list-001" src="https://user-images.githubusercontent.com/7393682/27466219-93587188-580b-11e7-9d78-a672f5e96705.png">
                
        <img width="496" alt="change-001" src="https://user-images.githubusercontent.com/7393682/27466188-673523e4-580b-11e7-9988-b6e501cf0f15.png">
        
        <img width="472" alt="list-002" src="https://user-images.githubusercontent.com/7393682/27466222-9cbded5c-580b-11e7-9a93-c0f5c0289f1f.png">


**依赖:**

    python >= 3.4

**python版shadowsocks安装:**

    pip install shadowsocks

