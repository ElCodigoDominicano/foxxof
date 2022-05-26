"""
A simple vulnerable service

- Every minute a .vbs(visual basic script) file is written to the TEMP directory.
- Tested on a Windows 11 Pro VM
[!] to create exe -> pyinstaller -F --hiddenimport win32timezone vuln.py
[!] to install service -> vuln.exe install
[!] to start service -> vuln.exe start
[!] to remove service -> vuln.exe stop
"""
import os
import servicemanager
import shutil
import subprocess
import sys

import win32event
import win32service
import win32serviceutil

SRCDIR = 'C:\\Users\\Hal_Emmerich\\Projects\\'
TGTDIR = 'C:\\Windows\\Temp'


class VulnServer(win32serviceutil.ServiceFramework):
    _svc_name_ = "VulnerableService"
    _svc_display_name_ = "Vulnerable Service"
    _svc_description_ = ("Executes VBScripts at regular intervals....")

    def __init__(self, args):
        self.vbs = os.path.join(TGTDIR, 'vulnservice_task.vbs')
        self.timeout = 1000 * 60
        win32serviceutil.ServiceFramework.__init__(self, args)
        self.hWaitStop = win32event.CreateEvent(None, 0, 0, None)

    def SvcStop(self):
        self.ReportServiceStatus(win32service.SERVICE_STOP_PENDING)
        win32event.SetEvent(self.hWaitStop)

    def SvcDoRun(self):
        self.ReportServiceStatus(win32service.SERVICE_RUNNING)
        self.main()

    def main(self):
        while True:
            ret_code = win32event.WaitForSingleObject(self.hWaitStop, self.timeout)
            if ret_code == win32event.WAIT_OBJECT_0:
                servicemanager.LogInfoMsg("Service is stopping")
                break
            src = os.path.join(SRCDIR, 'vulnservice_task.vbs')
            shutil.copy(src, self.vbs)
            subprocess.call("cscript.exe %s" % self.vbs, shell=False)
            os.unlink(self.vbs)

if __name__ == '__main__':
    if len(sys.argv) == 1:
        servicemanager.Initialize()
        servicemanager.PrepareToHostSingle(VulnServer)
        servicemanager.StartServiceCtrlDispatcher()
    else:
        win32serviceutil.HandleCommandLine(VulnServer)
