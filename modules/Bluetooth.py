import pexpect
import time
import subprocess

class Bluetooth:

    def __init__(self):
        pass

    def initSession(self):

        self.session = pexpect.spawn("bluetoothctl", encoding="utf-8")
        self.session.expect("#")

        return 

    def connectDevice(self, macAddress):
        self.initSession()

        self.session.sendline(f"pair {macAddress}")
        try:
            self.session.expect("Pairing successful", timeout=20)
        except pexpect.exceptions.TIMEOUT:
            self.session.sendline("exit")
            self.session.close()
            return 0

        time.sleep(2)
        self.session.sendline(f"connect {macAddress}")
        try:
            self.session.expect("Connection successful", timeout=20)
        except pexpect.exceptions.TIMEOUT:
            return 0
        self.close()

        return 1

    def disconnectDevice(self, macAddress):
        self.initSession()
        self.session.sendline(f"disconnect {macAddress}")
        index = self.session.expect(["Successful disconnected", "Failed to disconnect", pexpect.EOF, pexpect.TIMEOUT])
        self.close()
        if index == 0:
            return 1
        else:
            return 0

    def removeDevice(self, macAddress):
        self.initSession()
        self.session.sendline(f"remove {macAddress}")
        index = self.session.expect(["Device has been removed", "Failed to remove", pexpect.EOF, pexpect.TIMEOUT])
        self.close()
        if index == 0:
            return 1
        else:
            return 0
        print("removiendo")
#        subprocess.run(["bluetoothctl","remove", macAddress], capture_output=True, text=True)

    def close(self):
        self.session.sendline("exit")
        self.session.close()

        return


