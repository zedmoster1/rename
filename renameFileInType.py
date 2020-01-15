import os
import json

class renameFile():
    '''
    ----将文件放到需要修改文件名的目录下
    ----rename>重命名
    ----rmFileTitle>删除特殊字符
    ----backName>回退到重命名之前
    '''
    def __init__(self, fileType, fileDirs, startName, specialStr=None):
        self.fileTypeList = fileType.split()
        self.fileDirsList = fileDirs
        self.startName = startName
        self.specialStr = specialStr

    def reName(self):
        '''重命名指定类型文件名'''
        for oldName in self.fileDirsList:
            if os.path.splitext(oldName)[1].strip('.') in self.fileTypeList:
                try:
                    newName = self.startName +  oldName
                    os.rename(oldName, newName)
                    tips = '--{0}>>>>{1}'.format(oldName,newName)
                    print(tips)
                except:
                    pass
        print('>>>>指定类型文件名已重命名')

    def rmFileTitle(self):
        '''删除名称中的特殊字符'''
        for oldName in self.fileDirsList:
            if os.path.splitext(oldName)[1].strip('.') in self.fileTypeList:
                try:
                    #替换名称中包含的特殊字符及空格
                    reName = oldName.replace(self.specialStr,'').strip()
                    os.rename(oldName, reName)
                except:
                    pass
        print('>>>>删除文件名中包含的特殊字符')

    def backName(self):
        '''回到重命名文件名称之前'''
        with open('logging.log', 'r', encoding='UTF-8') as f:
            log = json.loads(f.read())
            oldFileType = log[0]
            oldStartName = log[1]
            oleFileDirs = log[3]

        for oldName in oleFileDirs:
            if os.path.splitext(oldName)[1].strip('.') in oldFileType:
                try:
                    #删除名称编号规则
                    backName = oldName.strip(oldStartName)
                    os.rename(oldName, backName)
                except:
                    pass
        print('>>>>编号规则已删除，回退到重命名文件名之前')

    def log(self):
        log_dir = []
        for oldName in self.fileDirsList:
            if os.path.splitext(oldName)[1].strip('.') in self.fileTypeList:
                log_dir.append(oldName)
        log = list((self.fileTypeList, self.startName, self.specialStr, log_dir))
        with open('logging.log', 'w+', encoding='UTF-8') as f:
            json.dump(log, f)

if __name__ == '__main__':
    tips_info = '''=================\n1--重命名\n2--恢复重命名\n3--删除特殊字符\n================='''
    print(tips_info)
    # fileType = input('----输入重命名的文件类型以空格分隔（可恢复）：')
    # startName = input('----输入重命名的文件开头编号规则：')
    # specialStr = input('----输入名称中需要删除的特殊字符（无法恢复）：')
    fileType = 'png'
    startName = '图片_'
    specialStr = '1'

    #如果使用path != os.getcwd()工作路径需设置当前工作目录为
    #os.chdir(path)
    fileDirs = os.listdir(os.getcwd())

    re_name_file = renameFile(fileType, fileDirs, startName, specialStr)
    re_name_file.log()
    num = int(input('输入功能对应编号：'))-1
    if num == 0:
        re_name_file.reName()
    elif num == 1:
        re_name_file.backName()
    elif num ==2:
        re_name_file.rmFileTitle()
    else:
        print("----不支持选项！")