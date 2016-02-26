# 未来道具计划
>El psy congroo

## 未来道具0号机
Image - Classify Vertical Horizontal

图片文件夹横版竖版分离脚本，适用于 OS X 系统。
将脚本挂载到文件夹后，丢入该文件夹的图片将会自动按照横版竖版自动归类。

使用方法

- 将脚本考入系统内置脚本文件夹

```shell
sudo cp "Image - Classify Vertical Horizontal.scpt" "/Library/Scripts/Folder Action Scripts/" 
```

- 将脚本挂载到文件夹
在要挂载脚本的文件夹的右键弹出式菜单中选择“文件夹操作”(Folder Action setup),选择本脚本即可生效。

不足

没有处理目标文件夹中已存在同名文件的情况。
没有处理丢进来的不是图片的情况。

## 未来道具1号机
music163_get_lyric_json

给出歌曲在网易云音乐的 ID ，下载对应的歌词 json 内容。

使用方法

```shell
python music163_get_lyric_json.py 401249250
```

或者重定向输出到文件

```shell
python music163_get_lyric_json.py 401249250 > output.json
```

不足

没有处理错误情况


## 未来道具2号机
lrcutility

对 LRC 做词法分析，构成时间与歌词匹配的词典。
以及再将该词典打包成LRC歌词

是 未来道具3号机 的重要组成部件

不足

无法解析叠在一起的时间标签，如

    [xx:xx.xxx][xx:xx.xxx] xxxxx


## 未来道具3号机
music163_json2LRC

将从网易抓来的json歌词恢复成 LRC 文件

使用方法

```shell
python music163_json2LRC.py input.json> output.lrc
```

可以结合 未来道具1号机(music163_get_lyric_json)一起使用，直接将下载下来的数据转成 LRC 保存

```shell
python music163_get_lyric_json.py 34478647 | python music163_json2LRC.py > output.lrc
```

## 未来道具4号机
music163_lrc

未来道具1到3号使用太麻烦，所以用 javascript 写了个脚本，可以一键显示歌词

使用方法

将下面这段代码保存为书签。

```js
javascript:void(function(u,s){s=document.body.appendChild(document.createElement('script'));s.src=u+'?ts='+Date.now();s.charset='UTF-8'}('//cdn.rawgit.com/hufan-Akari/Future-Gadgets-Project/master/music163_lrc.js'))
```


不足

页面会跳转，IE ,Edge , Safari 无法作为文件下载。

