import angr
import time
t = time.clock()
p = angr.Project('./vm')
st = p.factory.entry_state()
sm = p.factory.simulation_manager(st)
sm.explore(find = 0x400A5C,avoid = [0x4009F3,0x400A68])
flag = sm.found[0].posix.dumps(0)
print(flag)
print('time:',round(time.clock()-t,2),'s')