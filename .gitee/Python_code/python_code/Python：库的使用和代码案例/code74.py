# 程序员鼓励师
# 播放一个音频

from pynput import keyboard
# 引入播放音频的模块
from playsound import playsound

# 创建一个计数器，记录当前用户按了多少次键盘
count = 0

def onRelease(key):
    """
    这个函数，就是在用户释放键盘按键的时候，就会被调用到
    这个函数不是咱们自己调用的，而是咱们把这个函数交给了 Listener 自己，
    由这个 Listener 在用户释放按键的时候自动调用
    像这样的不是我们自己主动调用，而是交给别人，在合适的时机进行调用，这样的函数，叫做“回调函数(callback function)”
    :param key:用户按下了哪个键
    :return:
    """
    print(key)
    global count
    count += 1
    if count % 10 == 0: # 只有按的次数是10的倍数的时候才会播放音频
        # 播放一个音频！
        # playsound('python_code/sound/1.mp3')   # 传入的参数就是要播放的文件名
        playsound('D:/Python_code/python_code/sound/1.mp3')  # 替换为实际完整路径

# 当我们创建好 listener 之后，用户的键盘按键动作就会被捕获到
# 我们还希望捕获到之后能够执行一段代码
listener = keyboard.Listener(on_release=onRelease)
# 这个操作不是在进行调用，而是把函数名当成了一个变量传到了 Listener 里面，具体什么时候调用，由 Listener 自己决定
# 所谓的“自己决定”就是会说它会检测键盘什么时候释放，释放，就执行，不释放就不执行
listener.start()
listener.join()