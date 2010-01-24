import math
import heatmap

class HeatTile(heatmap.HeatMap):
    """ Reverse engineered from Google Maps... """
    TILE_SIZE = 256
    CBK = [128, 256, 512, 1024, 2048, 4096, 8192, 16384, 32768, 65536, 131072, 262144, 524288, 1048576, 2097152, 4194304, 8388608, 16777216, 33554432, 67108864, 134217728, 268435456, 536870912, 1073741824, 2147483648, 4294967296, 8589934592, 17179869184, 34359738368, 68719476736, 137438953472]
    CEK = [0.7111111111111111, 1.4222222222222223, 2.8444444444444446, 5.688888888888889, 11.377777777777778, 22.755555555555556, 45.51111111111111, 91.02222222222223, 182.04444444444445, 364.0888888888889, 728.1777777777778, 1456.3555555555556, 2912.711111111111, 5825.422222222222, 11650.844444444445, 23301.68888888889, 46603.37777777778, 93206.75555555556, 186413.51111111112, 372827.02222222224, 745654.0444444445, 1491308.088888889, 2982616.177777778, 5965232.355555556, 11930464.711111112, 23860929.422222223, 47721858.844444446, 95443717.68888889, 190887435.37777779, 381774870.75555557, 763549741.5111111]
    CFK = [40.74366543152521, 81.48733086305042, 162.97466172610083, 325.94932345220167, 651.8986469044033, 1303.7972938088067, 2607.5945876176133, 5215.189175235227, 10430.378350470453, 20860.756700940907, 41721.51340188181, 83443.02680376363, 166886.05360752725, 333772.1072150545, 667544.214430109, 1335088.428860218, 2670176.857720436, 5340353.715440872, 10680707.430881744, 21361414.86176349, 42722829.72352698, 85445659.44705395, 170891318.8941079, 341782637.7882158, 683565275.5764316, 1367130551.1528633, 2734261102.3057265, 5468522204.611453, 10937044409.222906, 21874088818.445812, 43748177636.891624]

    def __init__(self, zoom, tx, ty, radius=None):
        self.zoom = zoom
        self.tx = tx
        self.ty = ty

        super(HeatTile, self).__init__(*self.get_px_bounds())

    def add_points(self, points, radius):
        super(HeatTile, self).add_points([self.ll2px(*point) for point in points], radius=radius)
        
    def get_px_bounds(self):
        return (self.tx * self.TILE_SIZE, (self.tx + 1) * self.TILE_SIZE,
                (self.ty + 1) * self.TILE_SIZE, self.ty * self.TILE_SIZE)

    def get_ll_bounds(self, padding=0.0):
        (n, w) = self.px2ll(self.left - padding, self.top - padding)
        (s, e) = self.px2ll(self.right + padding, self.bottom + padding)
        return (s, n, w, e)

    def ll2px(self, lat, lon=None):
        x = self.CBK[self.zoom] + (lon * self.CEK[self.zoom])

        inner = math.sin(lat * math.pi / 180)
        inner = min(max(inner, -0.9999), 0.9999)

        y = self.CBK[self.zoom] + (0.5 * math.log((1 + inner) / (1 - inner)) * (-self.CFK[self.zoom]))

        return (x, y)

    def px2ll(self, x, y):
        offset = self.CBK[self.zoom]
        lon = (x - offset) / self.CEK[self.zoom]
        lat = (y - offset) / -self.CFK[self.zoom]
        lat = (2 * math.atan(math.exp(lat)) - math.pi / 2) / (math.pi / 180)

        return (lat, lon)