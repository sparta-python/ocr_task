from PIL import Image
import pyocr


def make(image):
    tools = pyocr.get_available_tools()
    tool = tools[0]
    img = Image.open(image)

    txt = tool.image_to_string(
        img, lang="eng+jpn", builder=pyocr.builders.TextBuilder()
    )
    return txt
