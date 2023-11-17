<div align="right">
    language : 中文 /
    <a title="English" href="https://github.com/liziyy/HFUT-WLAN-Autocheckin/main/README_en.md">English</a>
</div>
<h1 align="center"> HFUT-WLAN-AUTOCHECKIN</h1>


> 本项目是合肥工业大学力学系本科20级的开源项目, 学有余力（~~学不动了~~)的情况下为便利校内广大师生, 传播友爱与互助, 将校园网的登录和认证过程写成了一个简单的程序, 实现了全自动连接与认证, 开箱即用. 
>
> 源代码开放出来供开发者和使用者改进及监督. 为保护母校信息, 所有涉及网络安全的信息(如ip地址等)已做保护处理.  
>
> 如果需要借鉴本项目思路, 请符合`Mozilla Public License Version 2.0`相关规定, 最基本请附上原作出处和合肥工业大学力学系版权所有, 感谢配合!

 [![](https://img.shields.io/badge/%E5%90%88%E8%82%A5%E5%B7%A5%E4%B8%9A%E5%A4%A7%E5%AD%A6-%40hfut-blue?style=flat-square)](http://www.hfut.edu.cn/) [![](https://img.shields.io/badge/%E5%B7%A5%E7%A8%8B%E5%8A%9B%E5%AD%A6%E7%B3%BB-%40hfut-orange/style=plastic)](http://em.hfut.edu.cn/) [![](https://img.shields.io/badge/license-Mozilla%20Public%20License%202-red)](https://www.mozilla.org/en-US/MPL/2.0/)

![1](https://github.com/liziyy/HFUT-WLAN-Autocheckin/assets/132997940/9ef93280-ba6d-436a-ba51-f13ea573cea0)
- 程序第一运行需要输入校园网账号和密码(账号密码会加密储存在本地)，如果只是临时登录(非本人PC)选择不保存就行。
- 如果需要全自动化登录可以使用附加功能`1.开启开机自动连接WiFi`（全自动化登录：开机后自动运行程序连接校园网，如果保存了账号密码就能全自动化连接了）
- 如果想要连接其它WiFi怎么办，自行切换即可，程序只会在**开机后**或你**主动运行程序后**帮你连上校园网后就会结束运行
- 如果开机的时候不想连接校园网怎么办，程序会自动监测，如果你连了别的网络会提示你是否切换，不想用校园网了就按提示输入就行了
- 如何彻底卸载程序
  - 删除`C:\Users\用户名\AppData\Local\HFUT-wlan-autocheckin`这个文件夹及其所有文件，用户名因人而异
    - 找不到APPData这个文件夹怎么办？这个文件夹是系统默认隐藏了，在资源管理器选择`显示隐藏文件`就可以看见了
  - 按下键盘的`win`键和`r`键，输入`regedit`回车，根据目录层级找到`HKEY_CURRENT_USER\\SOFTWARE\\Microsoft\\Windows\\CurrentVersion\\Run`，点击Run目录（不要展开），在Run对应的键值里找到`HFUT-wlan-autocheckin`将这一条删除即可
  - 至此程序已彻底从你的电脑里消失了
<h2 align="center"> <span style='font-size:40px;'>&#127801;</span>安全性声明</h2> 

> - 使用之前校验一下MD5
>   - 怎么校验MD5？[在线工具](https://www.md5ma.com/md5-calculator)
>   - [腾讯哈勃](https://habo.qq.com/)有安全性检验报告，`MD5:  79e30332af1a5da8011f94927c8ac35e`，检索已有报告即可
>   - ![image](https://github.com/liziyy/HFUT-WLAN-Autocheckin/assets/132997940/8fdbf55f-b0c5-459f-955c-db90faa4618c)
> - 懂代码的朋友动手截取一下网络数据，把源代码关键参数换了自行编译一下也能用
> - 这是本地程序，不经过任何第三方服务器
> - 你输入的账号密码只存储在`C:\Users\用户名\AppData\Local\HFUT-wlan-autocheckin`这个文件夹当中，保存内容已使用RSA算法加密，每次登录都会进行解密，所以这个文件夹的内容最好别动
# 项目规划

- [ ] 英文`Read.me`
- [ ] Github action
- [ ] Linux: `curl`=>`HWA.sh`
- [ ] Windows: `HWA.bat`
- [x] 使用python完成基础功能编写(liziyy)
- [x] 实现全自动连接校园网（liziyy)
- [x] 简单测速?(liziyy)
- [ ] Management接口（查看设备与使用情况）
- [x] 测试WiFi信号强度(Liziyy)
- [ ] Golang: 兼容Win,MAC,Linux
- [ ] Android: `HWA.APK`
- [ ] HarmonyOs: `HWA.hap`


<h2 align="center"> <span style='font-size:40px;'>&#128071;</span>写在前面 </h2> 

> 本人力学系普普通通本科生, 爱党爱国爱校, 此项目为课余所学知识编写, 为便利广大师生使用校园网做出贡献, 也为志同道合的朋友提供思路, 借开源平台之力, 实现程序不断优化. 
>
> 这次我和我的小伙伴一起开发@nommihang 
> 开源的代码已处理过(考虑母校信息安全，望谅解).
> 原始代码在群内，仅供校内开发者参考.

<h2 align="center"> <span style='font-size:40px;'>&#9889;</span>浅谈设计思路 </h2> 

> 程序的技术含量不是很高, 分析一下网络请求就写出来了。
>
>  移动端后期会跟进，鸿蒙端也一样。
>
> - 程序权限上要求会高一些，因为涉及到修改注册表（实现开机自启）、查询并修改网络状态以及在`C:\Users\用户名\AppData\Local\HFUT-wlan-autocheckin`建立目录等操作
>
> - 限于时间~~和精力~~原因，欢迎志同道合的朋友加入开发，放个群号: 439410997


<h2 align="center"> <span style='font-size:40px;'>&#127915;</span>License </h2> 

[![](https://img.shields.io/badge/license-Mozilla%20Public%20License%202-red)](https://www.mozilla.org/en-US/MPL/2.0/)
