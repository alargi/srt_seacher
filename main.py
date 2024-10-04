import os

def srt_listdir(path):
    '''
    输出示例：['1-阿梓录播2024-10-02T19_37_53-1080P 60帧-AVC_中文（自动生成）.srt', '2-阿梓录播2024-10-02T20_07_57-1080P 60帧-AVC_中文（自动生成）.srt', '3-阿梓录播2024-10-02T20_38_01-1080P 60帧-AVC_中文（自动生成）.srt', '4-阿梓录播2024-10-02T21_08_05-1080P 60帧-AVC_中文（自动生成）.srt', '5-阿梓录播2024-10-02T21_38_09-1080P 60帧-AVC_中文（自动生成）.srt', '6-阿梓录播2024-10-02T22_08_13-1080P 60帧-AVC_中文（自动生成）.srt']
    '''
    files = os.listdir(path)
    srt_files=[]
    for file in files:
        if file[-3:] =='srt':
            srt_files.append(file)
    #print(srt_files)
    return srt_files

def find_from_srt(keyword,srt_name,folder_file):
    '''
    输出示例：['00:02:10,094 --> 00:02:12,094\n', '00:04:26,040 --> 00:04:28,004\n', '00:07:08,041 --> 00:07:09,037\n', '00:22:09,000 --> 00:22:11,044\n', '00:25:11,039 --> 00:25:12,051\n', '00:25:53,018 --> 00:25:54,062\n', '00:26:20,089 --> 00:26:22,071\n', '00:27:51,008 --> 00:27:52,076\n', '00:29:21,062 --> 00:29:23,022\n']
    '''
    time_dots=[]
    srt_file=folder_file+'\\'+srt_name
    with open(srt_file,'r',encoding='UTF-8') as f:
        lines=f.readlines()
        for n in range(len(lines)):
            if lines[n] =='\n':
                continue
            else:
                if keyword in lines[n]:
                    time_dots.append(lines[n-1])
                elif n==len(lines)-1:
                    print("no such word")
    #print(time_dots)
    return time_dots

def find_folder(key='梓'):
    '''
    输出示例：['【无畏契约英雄揭秘】龙勃勒-角色宣传CG', '[福州搞笑哥第一视角]2024-09-28']
    '''
    keys=[]
    if key=='梓':
        keys=['梓']
    elif key=='炫':
        keys=['炫','龙','福州']
    files = os.listdir(r'D:\Download\jijidownload')
    file_to_return=[]
    for k in keys:
        for file in files:
            if k in file:
                file_to_return.append(r'D:\Download\jijidownload'+'\\'+file)
    #print(file_to_return)
    return file_to_return

def find(name_key='梓',key_word='去了'):
    folder_list=find_folder(name_key)
    for folder in folder_list:
        srt_list=srt_listdir(folder)
        for srt in srt_list:
            time_dots=find_from_srt(key_word,srt,folder)
            print(folder)
            print(srt)
            print(time_dots)
            print()


find('炫','去了')