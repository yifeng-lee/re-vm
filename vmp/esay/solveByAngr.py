import angr

p = angr.Project('./EasyVM',auto_load_libs=False)
state = p.factory.blank_state(addr=0x400B2A)
sm = p.factory.simulation_manager(state)
sm.explore(find=0x400B73)
print(sm.found[0].posix.dumps(0))