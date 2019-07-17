import NetworkManger

class nm_handler():
    def __init__(self):
        try:
            self.permstate = NetworkManager.NetworkManager.GetPermissions()
        except:
            print("problem, is NetworkManager running?")
        if self.permstate['org.freedesktop.NetworkManager.network-control'] != 'yes':
            print("running unprivileged, cannot configure interfaces")



