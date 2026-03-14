# 程序员鼓励师
# 多个音频循环播放
import random
from threading import Thread

from pynput import keyboard
# 引入播放音频的模块
from playsound import  playsound

soundList = ['D:/Python_code/python_code/sound/1.mp3','D:/Python_code/python_code/sound/2.mp3','D:/Python_code/python_code/sound/3.mp3']

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
        # 如果感觉播放得太频繁了，吵到耳朵了，也可以适当降低一下频率，把除余的数字改大一点
        # 播放音频！
        # 先生成随机数
        i = random.randint(0,len(soundList) - 1)
        # 此处的播放音频，消耗时间比较多，可能会引起输入的卡顿(不流畅)
        # 可以创建一个线程，在线程里面播放音频！
        # playsound(soundList[i])   # 传入的参数就是要播放的文件名
        t = Thread(target=playsound,args=(soundList[i],))   # 在一个新的线程里面完成播放音频
        # (新的线程可以想象成一个新的执行流)
        # 上面这里只是给线程安排任务，下面才是创建了一个线程出来
        t.start()

# 当我们创建好 listener 之后，用户的键盘按键动作就会被捕获到
# 我们还希望捕获到之后能够执行一段代码
listener = keyboard.Listener(on_release=onRelease)
# 这个操作不是在进行调用，而是把函数名当成了一个变量传到了 Listener 里面，具体什么时候调用，由 Listener 自己决定
# 所谓的“自己决定”就是会说它会检测键盘什么时候释放，释放，就执行，不释放就不执行
listener.start()
listener.join()

# 编写一段代码，感受一下这个程序的效果
# 播放音频可能出现卡顿
# 再次感受下代码的效果，此时感觉就流畅了！
# 现在是把频率降低到 xx 下播放一次，感觉好不少啦！