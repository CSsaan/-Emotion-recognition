# -Emotion-recognition
Facial expression detection and classification. And use PyQt5 for GUI creation. And packaged into an exe executable file.


### haarcascade_files：
  * 使用Haar Cascadse进行人脸识别

### icon：
  *存放图标文件

### images：
  *存放待检测表情图片

### models：
  *放置模型文件
  
### train：
  *存放训练数据集文件

### 使用pyinstaller打包exe ([pyinstaller](http://baidsssu.com))
  1.spec文件生成:pyi-makespec -w xxx.py
  *打开生成的spec文件，修改其默认脚本，完成自定义打包需要的配置。
  
  2.完成自定义打包：pyinstaller -d xxx.spec


