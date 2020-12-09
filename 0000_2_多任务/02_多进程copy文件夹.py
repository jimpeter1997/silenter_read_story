"""
存在的问题：
1。 无法拷贝大文件（需要在读写那边添加while True）
2。 只能从当前文件夹copy
"""

import os
import multiprocessing


def copy_file(file_name, old_folder_name, new_folder_name):
    """完成文件的复制"""
    # 产生异常，不会显示
    print("----->模拟copy文件： %s" % file_name)
    print("把 %s 从%s copy到 %s" % (file_name, old_folder_name, new_folder_name))
    old_f = open(old_folder_name+"/"+file_name, "rb")
    content = old_f.read()
    old_f.close()

    new_f = open(new_folder_nam+"/"+file_name, "wb")
    new_f.write(content)
    new_f.close()

    # 如果拷贝完了文件，那么想队列中写入一个消息，表示已经完成
    q.put(file_name)


def main():
    # 1. 获取用户要copy的文件夹的名字
    old_folder_name = input("请输入要copy的文件夹的名字：")

    # 2. 创建一个新的文件夹
    try:
        new_folder_name = old_folder_name + "_backup"
        os.mkdir(new_folder_name)
    except:
        pass
    # 3. 获取文件夹内所有待copy的文件名字 listdir()
    file_names = os.listdir(old_folder_name)

    # 4. 创建进程池
    po = multiprocessing.Pool(5)

    # 5. 创建一个队列
    multiprocessing.Manager().Queue()

    # 6. 向进程池中添加copy文件的任务
    for file_name in file_names:
        # 复制原文件夹中的文件，到新的文件夹中去
        po.apply_async(copy_file, args=(file_name, old_folder_name, new_folder_name))
    po.close()
    # po.join()
    all_file_num = len(file_names)  # 保存文件总个数
    copy_ok_num = 0
    while True:
        file_name = q.get()
        print("已经完成copy： %s" % file_name)
        print("拷贝进度： %f" % (copy_ok_num/all_file_num))
        print("拷贝进度： %.2f %%" % (copy_ok_num*100/all_file_num))
        print("\r拷贝进度： %.2f %%" % (copy_ok_num*100/all_file_num), end="")
        # \r :回到开头重新输出
        # %.2f : 表示小数，且有两位
        # end="" : 不换行
        # %% : 两个百分号，显示一个%
        copy_ok_num  += 1
        if copy_ok_num >= all_file_num:
            break

    print()  # 为了程序执行完毕之后换行


if __name__ == '__main__':
    main()
