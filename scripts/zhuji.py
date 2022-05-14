import wmi
import socket

w = wmi.WMI()
def winInfo():
    for cs in w.Win32_computerSystem():
        # print(cs)
        print(f"电脑名称: {cs.caption}")
        print("使用者: %s" % cs.UserName)
        print("制造商: %s" % cs.Manufacturer)
        print("系统信息: %s" % cs.SystemFamily)
        print("工作组: %s" % cs.Workgroup)
        print("机器型号: %s" % cs.model)
        print("")

    for OS in w.Win32_OperatingSystem():
        # print(OS)
        print("操作系统: %s" % OS.Caption)
        print("语言版本: %s" % OS.MUILanguages)
        print("系统位数: %s" % OS.OSArchitecture)
        print("注册人: %s" % OS.RegisteredUser)
        print("系统驱动: %s" % OS.SystemDevice)
        print("系统目录: %s" % OS.SystemDirectory)
        print("")

    # 获取电脑IP和MAC信息
    for address in w.Win32_NetworkAdapterConfiguration(ServiceName = "Netwtw06"):
        # print(address)
        print(f"IP地址: {address.IPAddress[0]}")
        print("MAC地址: %s" % address.MACAddress)
        print("网络描述: %s" % address.Description)
        print("")

    # 获取电脑CPU信息
    for processor in w.Win32_Processor():
        # print(processor)
        print("CPU型号: %s" % processor.Name.strip())
        print("CPU核数: %s" % processor.NumberOfCores)
        print("")

    # 获取BIOS信息
    for BIOS in w.Win32_BIOS():
        # print(BIOS)
        print("使用日期: %s" % BIOS.Description)
        print("主板型号: %s" % BIOS.SerialNumber)
        print("当前语言: %s" % BIOS.CurrentLanguage)
        print("")

    # 获取内存信息
    for memModule in w.Win32_PhysicalMemory():
        totalMemSize = int(memModule.Capacity)
        print("内存厂商: %s" % memModule.Manufacturer)
        print("内存型号: %s" % memModule.PartNumber)
        print("内存大小: %.2fGB" % (totalMemSize / 1024 ** 3))
        print("")

    # 获取磁盘信息
    for disk in w.Win32_DiskDrive():
        diskSize = int(disk.size)
        print("磁盘名称: %s" % disk.Caption)
        print("硬盘型号: %s" % disk.Model)
        print("磁盘大小: %.2fGB" % (diskSize / 1024 ** 3))

    # 获取显卡信息
    for xk in w.Win32_VideoController():
        print("显卡名称: %s" % xk.name)
        print("")

    # 获取计算机名称和IP
    hostname = socket.gethostname()
    ip = socket.gethostbyname(hostname)
    print("计算机名称: %s" % hostname)
    print("IP地址: %s" % ip)