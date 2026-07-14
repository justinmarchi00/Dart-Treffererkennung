from vision.geometry import Geometry

geo = Geometry()

print(
    geo.get_hit(500, 500)
)

print(
    geo.get_hit(500, 230)
)

print(
    geo.get_hit(800, 500)
)