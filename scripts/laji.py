import os
del_extension = {
    '.tmp': '临时文件',
    '._mp': '临时文件_mp',
    '.log': '日志文件',
    '.gid': '临时帮助文件',
    '.chk': '磁盘检查文件',
    '.old': '临时备份文件',
    '.xlk': 'Excel备份文件',
    '.bak': '临时备份文件bak'
}
del_windir = ['prefetch', 'temp']
USER_PROFILE = os.environ['userprofile']

def del_dir_or_file(item):
    try:
        if os.path.isfile(item):
            os.remove(item)
            print ("file",item,"removed")
        elif os.path.isdir(item):
            os.rmdir(item)
            print("dir",item,"removed")

    except WindowsError:
        print("failure",item,"can't remove")

def formatSize(b):
    try:
        kb = b // 1024
    except:
        print("传入字节格式不对")
        return "Error"
    if kb > 1024:
        M = kb // 1024
        if M > 1024:
            G = M // 1024
            return "%dG" % G
        else:
            return "%dM" % M
    else:
        return "%dkb" % kb

class DiskClean(object):
    def __init__(self):
        self.del_info = {}
        self.del_file_paths = []
        self.total_size = 0
        for i,j in del_extension.items():
            self.del_info[i] = dict(name = j,count = 0 )

    def scanf(self):
        for roots,dirs,files in os.walk(USER_PROFILE):
            for files_item in files:
                file_extension = os.path.splitext(files_item)[1]
                if file_extension in self.del_info:
                    file_full_path = os.path.join(roots,files_item)
                    self.del_file_paths.append(file_full_path)
                    self.del_info[file_extension]['count'] += 1
                    self.total_size += os.path.getsize(file_full_path)

    def show(self):
        re = formatSize(self.total_size)
        for i in self.del_info:
            print(self.del_info[i]["name"],"共计",self.del_info[i]["count"],"个")
        return re

    def delete_files(self):
        for i in self.del_file_paths:
            print(i)
            del_dir_or_file(i)
