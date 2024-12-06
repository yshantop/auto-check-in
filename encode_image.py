from PIL import Image
import base64
import io

def compress_image(image_path, max_size=(400, 400), quality=30):
    # 打开图片
    img = Image.open(image_path)
    
    # 调整图片大小
    img.thumbnail(max_size, Image.Resampling.LANCZOS)
    
    # 压缩
    output = io.BytesIO()
    img.save(output, format='JPEG', quality=quality)
    
    # 保存压缩后的图片以供预览
    img.save('compressed_img.jpg', quality=quality)
    
    return output.getvalue()

try:
    # 压缩图片
    compressed_image = compress_image("img.jpg")
    encoded_string = base64.b64encode(compressed_image).decode()
    
    # 打印信息
    print(f"原始图片大小: {len(open('img.jpg', 'rb').read())/1024:.2f}KB")
    print(f"压缩后大小: {len(compressed_image)/1024:.2f}KB")
    print(f"Base64 大小: {len(encoded_string)/1024:.2f}KB")
    
    # 保存
    with open("image_base64.txt", "w") as text_file:
        text_file.write(encoded_string)
    print("成功保存到 image_base64.txt")
        
except Exception as e:
    print(f"发生错误: {str(e)}") 