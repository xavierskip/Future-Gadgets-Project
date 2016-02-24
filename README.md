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
python music163_get_lyric_json.py 401249250 > example.json
```

不足

没有处理错误情况
