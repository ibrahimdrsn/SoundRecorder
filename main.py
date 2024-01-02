
from recorder import Recorder
r = Recorder()
print(r.get_device_info())

from recorder import Recorder
r = Recorder()
r.record(5, output='out.wav')

from recorder import Recorder
Recorder.play('out.wav')