import mapnik


stylesheet = 'style.xml'
image = 'output.png'

m = mapnik.Map(3000, 3000)
m.background = mapnik.Color('ghostwhite')
mapnik.load_map(m, stylesheet)
bbox = mapnik.Box2d(1619242.0, 6461069.0, 1993478.0, 6758260.0)
m.zoom_to_box(bbox)
# m.zoom_all()
print(m.envelope())
mapnik.render_to_file(m, image)

print('rendered image')