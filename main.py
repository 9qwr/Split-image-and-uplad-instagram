from PIL import Image
import os
import time
import getpass
from instagrapi import Client
from bidi.algorithm import get_display
class Instagram:
    def upload_Image(self, image_path, rows, cols, captions, username, password, tag):
        try:
            image = Image.open(image_path)
            width, height = image.size
            cell_width = width // cols
            cell_height = height // rows
            cl = Client()
            cl.login(username, password)
            temp_filenames = []
            for row in range(rows):
                for col in range(cols):
                    left = col * cell_width
                    upper = row * cell_height
                    right = left + cell_width
                    lower = upper + cell_height
                    part = image.crop((left, upper, right, lower))

                    temp_filename = f'temp_part_{row * cols + col + 1}.jpg'
                    part.save(temp_filename, 'JPEG', quality=95)
                    temp_filenames.append(temp_filename)

            for idx in range(len(temp_filenames) - 1, -1, -1):
                caption = f"{captions[idx]} {tag}"
                cl.photo_upload(temp_filenames[idx], caption=caption)
                time.sleep(6)
                message = f"تم نشر الصورة رقم {len(temp_filenames) - idx} رجاء لا تغلق الأداة حتى الاكتمال"
                print(get_display(message))
                os.remove(temp_filenames[idx])

            print(get_display('.. تم نشر جميع الصور بنجاح شكراً للانتظار'))
        except Exception as e:
            print(get_display(f'حدث خطا ما : {e}')) 

if __name__ == "__main__":
    print('''

                 ,  ,
              #▄▓██████▀
            "▀███████████▄Z
           ▄Z████████████▄▄
            ▄▀█████████▓▀▀Z
             ' ▀█▀███▀█ ▀
                ' ▀█▌"
                   ▐█
                   ██
                   ██
    ""▀▀▀██▄▄   ▄▄▄██▄a▄▄   ,▄▄██▀▀""
           "▀██▄⌠▀▀▀▀▀'¡▄██▀"
               ▀██▄  ▄██▀`
                  ████"
               ▄▄█▌▀╙██▄▄
          ██▄▄██▀█    █▀███▀█▌

       Made By https://t.me/ik48x 💘
          
          
       ''')
    
    image_path = input("Enter Path Image : ")
    rows = 3  
    cols = 3  
    captions = [f"{i}" for i in range(1, 10)]
    tag = "@j4s_8"
    username = input('Enter Username :')
    password = getpass.getpass('Enter Password :')
    
    insta = Instagram()
    insta.upload_Image(image_path, rows, cols, captions, username, password, tag)
