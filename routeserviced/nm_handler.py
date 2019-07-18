import logger
import NetworkManger
import dbus.mainloop.glib

class nm_handler():
    def __init__(self):
        self.log = logging.getLogger(__name__)
        dbus.mainloop.glib.DBusGMainLoop(set_as_default=True)
        
        try:
            self.nm = NetworkManager.NetworkManager
        except DbusError:
            self.log("problem, is NetworkManager running?")
            # this should hande a variety of tested error conditions!
    def perm_check(self):
        p = self.nm.GetPermissions()
        if (p['org.freedesktop.NetworkManager.network-control'] != 'yes'):
            self.log("running unprivileged, cannot configure interfaces")
        self.permstate = p
    def checkpoint_init(self, devices='all', timeout=15, flags=0):
        if ( self.permstate['org.freedesktop.NetworkManager.checkpoint-rollback'] != yes ):
            self.log('unable to create snapshots, that\'s not best')
            return False
        chks = self.nm.Checkpoints
        if devices = 'all':
            devs = []
        if not chks:
            self.log('No checkpoints found, making one')
            # there should be a config check here
            try:
                chk0 = self.nm.CheckpointCreate(devs, timeout, flags)
            except DbusException:
                self.log('checkpoint creation failed)



