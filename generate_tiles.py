import mapnik
import sys, os
import subprocess

subprocess.call("carto style.mml > style.xml", shell=True)

merc = mapnik.Projection('+proj=merc +a=6378137 +b=6378137 +lat_ts=0.0 +lon_0=0.0 +x_0=0.0 +y_0=0 +k=1.0 +units=m +nadgrids=@null +no_defs +over')
longlat = mapnik.Projection('+proj=longlat +ellps=WGS84 +datum=WGS84 +no_defs')


style = 'style.xml'
output_image = 'output.png'

places = {
    "CH": [
        {
        "country": "CH",
        "city": "Bern",
        "coord": (7.447, 46.948)
        },
        {
        "country": "CH",
        "city": "Lucerne",
        "coord": (8.306, 47.052)
        },
        {
        "country": "CH",
        "city": "Zurich",
        "coord": (8.542, 47.372)
        },
    ],
    "PL": [
        {
            "country": "PL",
            "city": "Wroclaw",
            "coord": (17.032, 51.110)
        },
        {
        "country": "PL",
        "city": "Gdansk",
        "coord": (18.658, 54.348)
        },
    ],
    "LV": [
        {
            "country": "LV",
            "city": "Riga",
            "coord": (24.107, 56.947)
        }
    ],
}


z = 16
imgx = 256 * z
imgy = 256 * z

for place in places['LV']:
    print('rendering: ' + place['country'] + ' ' + place['city'])
    ourput_filename = 'output/' + place['country'] + '_' + place['city'] + '_0.png'
    m = mapnik.Map(imgx, imgy)
    m.background = mapnik.Color('#FFFFFF')
    mapnik.load_map(m, style)

    m.srs = merc.params()

    bounds = (
        place['coord'][0] - 0.01, 
        place['coord'][1] + 0.01, 
        place['coord'][0] + 0.01, 
        place['coord'][1] - 0.01
    )

    bbox = mapnik.Box2d(*bounds)
    transform = mapnik.ProjTransform(longlat,merc)
    merc_bbox = transform.forward(bbox)

    m.zoom_to_box(merc_bbox)

    mapnik.render_to_file(m, ourput_filename)
