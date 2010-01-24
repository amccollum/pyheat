import threading, Queue
import pyheat.heattile

from points import points

# Simple batch job processor
class Batcher(threading.Thread):
    def __init__(self, init_fn=None, task_fn=None):
        super(Batcher, self).__init__()
        self.inputs = Queue.Queue()
        self.outputs = Queue.Queue()
        
        if init_fn is not None:
            self.do_init = init_fn
            
        if task_fn is not None:
            self.do_task = task_fn
            
        self.start()
    
    def run(self):
        self.do_init()
        while True:
            (args, kwargs) = self.inputs.get(True, None)
            self.outputs.put(self.do_task(*args, **kwargs))

    def do_init(self, *args, **kwargs):
        pass

    def do_task(self, *args, **kwargs):
        raise NotImplemented

    def process(self, *args, **kwargs):
        self.inputs.put((args, kwargs))
        return self.outputs.get(True, None)
        

class TileMaster(Batcher):
    def do_task(self, zoom, tx, ty):
        radius = 1.5**zoom
        alpha = 1.0 - (zoom / 20.0)
        
        tile = pyheat.heattile.HeatTile(zoom, tx, ty)
        (lat_min, lat_max, lon_min, lon_max) = tile.get_ll_bounds(padding=2*radius)
        tile.add_points(points, radius=radius)
        tile.transform_color(alpha=alpha)
        return tile.get_image()


