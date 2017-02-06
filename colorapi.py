import hug
import colorsys
import webcolors


@hug.get(versions=1, examples='name=red')
def color(name: hug.types.text):
    rgb = webcolors.name_to_rgb(name)
    return {
        name: {
            'hex': webcolors.name_to_hex(name),
            'rgb': rgb,
            'rgb%': webcolors.name_to_rgb_percent(name),
            'hls': colorsys.rgb_to_hls(*rgb),
            'hsv': colorsys.rgb_to_hsv(*rgb),
            'yiq': colorsys.rgb_to_yiq(*rgb)
        }
    }


@hug.get(versions=2, examples='name=red')
def color(name: hug.types.text):
    rgb = webcolors.name_to_rgb(name)
    return {
        name: {
            'hex': webcolors.name_to_hex(name),
            'rgb': rgb,
            'rgb%': webcolors.name_to_rgb_percent(name)
        }
    }

