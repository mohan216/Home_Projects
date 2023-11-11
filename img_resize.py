from PIL import Image
import os

source_folder = r"C:\Users\mohan\PycharmProjects\Home_projects\Static\Cat"
output_folder = r"C:\Users\mohan\PycharmProjects\Home_projects\Static\Cat2"
new_size = (480, 360)

for filename in os.listdir(source_folder):
    with Image.open(os.path.join(source_folder, filename)) as img:
        img = img.resize(new_size)
        img.save(os.path.join(output_folder, filename))

source_folder = r"C:\Users\mohan\PycharmProjects\Home_projects\Static\Mom"
output_folder = r"C:\Users\mohan\PycharmProjects\Home_projects\Static\Mom2"

for filename in os.listdir(source_folder):
    with Image.open(os.path.join(source_folder, filename)) as img:
        img = img.resize(new_size)
        img.save(os.path.join(output_folder, filename))



# from PIL import Image
# img = Image.open(r"C:\Users\mohan\PycharmProjects\Home_projects\Static\Mom\img2.jpg")
# rotated_img = img.rotate(180, expand=True)
# rotated_img.save(r"C:\Users\mohan\PycharmProjects\Home_projects\Static\Mom\img2.jpg")
# img.close()
# rotated_img.close()


