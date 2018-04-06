from PIL import Image

def main(argv):
    # このコードは引数と標準出力を用いたサンプルコードです。
    # このコードは好きなように編集・削除してもらって構いません。
    # ---
    # This is a sample code to use arguments and outputs.
    # Edit and remove this code as you like.

    command = argv[0]
    output_path = argv[1]
    
    if command == "concat": 
        output_img = handle_concat(argv)
    elif command == "resize": 
        output_img = handle_resize(argv)
    elif command == "rotate": 
        output_img = handle_rotate(argv)
        
    output_img.save(output_path)
    
def handle_concat(input_list): 
    input_path = input_list[2:]
    img_width = 0
    for input_path_part in input_path: 
        input_img_part = Image.open(input_path_part)
        img_height = input_img_part.size[1]
        img_width += input_img_part.size[0]
    con_img = Image.new("RGB", (img_width, img_height))
    pos_width = 0
    for input_path_part in input_path: 
        input_img_part = Image.open(input_path_part)
        con_img.paste(input_img_part, (pos_width, 0))
        pos_width += input_img_part.size[0]
    return con_img

def handle_resize(input_list): 
    rate = input_list[2]
    input_path = input_list[3]
    input_img = Image.open(input_path)
    output_img_width, output_img_height = input_img.size[0] * rate, input_img.size[1] * rate
    output_img = input_img.resize((int(output_img_width), int(output_img_height)))
    return output_img

def handle_rotate(input_list): 
    angle = input_list[2]
    input_path = input_list[3]
    input_img = Image.open(input_path)
    output_img = input_img.rotate(angle, expand = True)
    return output_img


