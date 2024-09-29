from pathlib import Path
import base64
import subprocess


def sign_svg(svg_image: Path, png_image: Path, title: str = '', signature: str = '', color='808080') -> None:
    with open(r'photosignature/templates/svg_template.svg', 'r') as svg_template:
        template_content = svg_template.read()

    with open(png_image, 'rb') as png_file:
        encoded_string = base64.b64encode(png_file.read()).decode('utf-8')

    with open(svg_image, 'w', encoding='utf-8') as svg_file:
        svg_file.write(template_content.replace('{{image_data}}', encoded_string)
                       .replace('{{title}}', title)
                       .replace('{{signature}}', signature)
                       .replace('{{color}}', color))


colors = {'DSC_2672': '808080', 'DSC_2674': '808080', 'DSC_2676': 'E0E0E0', 'DSC_2687': 'E0E0E0',
          'DSC_2693': 'E0E0E0', 'DSC_2698': 'E0E0E0', 'DSC_2704': 'E0E0E0', 'DSC_2708': 'E0E0E0',
          'DSC_2891': '404040', 'DSC_2892': '404040', 'DSC_2896': '404040', 'DSC_2900': '404040',
          'DSC_2905': '404040', 'DSC_2910': '404040', 'DSC_2911': '404040', 'DSC_2912': '404040',
          'DSC_2913': '404040', 'DSC_2920': '404040', 'DSC_2922': '404040', 'DSC_2924': '404040',
          'DSC_2925': '404040', 'DSC_2930': '404040', 'DSC_2931': '404040', 'DSC_2932': 'E0E0E0',
          'DSC_2940': '404040', 'DSC_2942': '404040', 'DSC_2952': '404040', 'DSC_2954': '404040',
          'DSC_2960': '404040', 'DSC_2962': '404040', 'DSC_2968': '404040', 'DSC_2972': '404040',
          'DSC_2976': '404040', 'DSC_2982': '404040', 'DSC_2983': '404040', 'DSC_2984': '404040',
          'DSC_2988': '404040', 'DSC_2997': '404040', 'DSC_3010': '404040', 'DSC_3019': '404040',
          'DSC_3027': 'E0E0E0', 'DSC_3032': 'E0E0E0', 'DSC_3033': 'E0E0E0', 'DSC_3054': '404040',
          'DSC_3080': 'E0E0E0', 'DSC_3083': '404040', 'DSC_3087': 'E0E0E0', 'DSC_3088': 'E0E0E0',
          'DSC_3091': 'E0E0E0', 'DSC_3094': 'E0E0E0', 'DSC_3118': 'FFFFFF', 'DSC_3122': '404040',
          'DSC_3127': 'E0E0E0', 'DSC_3131': 'E0E0E0', 'DSC_3133': '404040', 'DSC_3136': '404040',
          'DSC_3138': '404040', 'DSC_3165': 'E0E0E0', 'DSC_3177': '404040', 'DSC_3178': '404040'}


if __name__ == '__main__':
    pic_folder = Path(r'C:\Users\luisp\Pictures\Nueva carpeta\Berrea 2024\out\png')
    for pic in list(pic_folder.rglob('*.png')):
        svg_name = pic.stem + '_signed'
        out_svg = (pic_folder.parent / 'svg' / (svg_name + '.svg'))
        out_jpg = (pic_folder.parent / 'jpg' / (svg_name + '.jpg'))
        sign_svg(out_svg, pic, signature=r'Luis Pedro Vicente Matilla, 22/09/2024', color=colors[pic.stem])
        subprocess.run('magick "{svg_file}" -resize {width}x{height} "{jpg_file}"'.format(
            svg_file=out_svg, width=6000, height=4000, jpg_file=out_jpg))
