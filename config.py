class Permission():
    NONE = 0x0000               # 无权限
    HUMAN_REGISTER = 0x0001     # 人事登记
    HUMAN_UPDATE = 0x0002       # 人事变更
    HUMAN_COMFIRM = 0x0004      # 人事复核
    HUMAN_DELETE = 0x0008       # 人事删除
    
    INSTITUTE_REGISTER = 0x0010 # 机构登记
    INSTITUTE_UPDATE = 0x0020   # 机构变更
    INSTITUTE_CONFIRM = 0x0040  # 机构复核
    INSTITUTE_DELETE = 0x0080   # 机构删除
    
