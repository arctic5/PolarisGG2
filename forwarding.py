from ctypes import *

# Faucet Forwarding Stuff

global forwarding
forwarding = cdll.LoadLibrary("faucetforwarding.dll")

def upnp_set_description(description):
    return c_int(forwarding.upnp_set_description(description))
def upnp_discover(delay):
    return c_int(forwarding.upnp_discover(delay))
def upnp_forward_port(iport, eport, proto, leaseDuration):
    return c_int(forwarding.upnp_forward_port(iport, eport, proto, leaseDuration))
def upnp_release_port(eport, proto):
    return c_int(forwarding.upnp_release_port(eport, proto))
def upnp_error_string(error_code):
    forwarding.upnp_error_string.restype = c_char_p
    return forwarding.upnp_error_string(error_code)