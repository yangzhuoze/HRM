class Permission():
    NONE = 0x0000               # 无权限
    HUMAN_QUERY = 0x0001        # 人事查询
    HUMAN_CREATE = 0x0002       # 人事登记
    HUMAN_UPDATE = 0x0004       # 人事变更
    HUMAN_COMFIRM = 0x0008      # 人事复核
    HUMAN_DELETE = 0x000F       # 人事删除
    
    INSTITUTE_QUERY = 0x0010    # 机构查询
    INSTITUTE_CREATE = 0x0020   # 机构登记
    INSTITUTE_UPDATE = 0x0040   # 机构变更
    INSTITUTE_CONFIRM = 0x0080  # 机构复核
    INSTITUTE_DELETE = 0x00F0   # 机构删除
    
    SALARY_QUERY = 0x0100       # 薪酬查询
    SALARY_CREATE = 0x0200      # 薪酬登记
    SALARY_UPDATE = 0x0400      # 薪酬变更
    SALARY_CONFIRM = 0x0800     # 薪酬复核
    SALARY_DELETE = 0x0F00      # 薪酬删除
    
    POSITION_QUERY = 0x1000     # 职位查询
    POSITION_CREATE = 0x2000    # 职位登记
    POSITION_UPDATE = 0x4000    # 职位变更
    POSITION_CONFIRM = 0x8000   # 职位复核
    POSITION_DELETE = 0xF0000   # 职位删除
