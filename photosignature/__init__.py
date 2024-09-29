from pathlib import Path
import base64
from jinja2 import Environment, PackageLoader


def sign_svg(out_svg: Path, input_image: Path, title: str = '', signature: str = '', color='808080') -> None:
    environment = Environment(loader=PackageLoader('photosignature'))
    template = environment.get_template(r'svg_template.svg')

    with open(input_image, 'rb') as png_file:
        encoded_string = base64.b64encode(png_file.read()).decode('utf-8')

    with open(out_svg, 'w', encoding='utf-8') as svg_file:
        content = template.render(image_data=encoded_string, color=color, title=title, signature=signature)
        svg_file.write(content)
