<div align="center">
   <img width="160" src="./matoi.png" alt="logo"></br>



matoi 是一个在Linux / Windows平台下运行的信息收集、漏洞应急工具

这个项目的名字来源于
    <p>TRIGGER公司所制作的原创动画《KILL la KILL（斩服少女）》的<a href="https://zh.moegirl.org.cn/%E7%BC%A0%E6%B5%81%E5%AD%90">缠流子(Matoi Ryuuko)</a></p>
</div>

## matoi声明

### 本工具旨在辅助安全测试，请勿用于非法用途

- matoi 是作者本人将来的毕业设计，当前还在开发的beta阶段。
- matoi 不会对使用者收取额外的费用，版权属于整个开源社区。
- matoi 核心代码将在2021.6后进行开源，届时会更新相关仓库。

## matoi功能

matoi目前beta版本仅封装了信息收集、子域名扫描的功能

- 爬虫
- 端口探测
- C段探测
- 子域名探测
- 信息收集报告
- 敏感信息探测
- 指纹识别
- 漏洞扫描
- 漏洞推送
- 漏洞报告
- 自定义POC

## 演示

![image](./matoi.gif)

由于端口扫描的局限性，引入了fofa的链接，作为单个URL探测的参考

## 鸣谢

> [Flask 页面模板](https://github.com/Donvink/Spider.BC) 应用Python爬虫、Flask框架、Echarts、WordCloud等技术将豆瓣租房信息爬取出来保存于Excel和数据库中，进行数据可视化操作、制作网页展示。

> [Dirscan目录扫描工具](https://github.com/j3ers3/Dirscan) A simple and fast directory scanning tool for pentesters。
