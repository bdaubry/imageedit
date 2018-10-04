# import imageio
import PIL
from PIL import Image
import images2gif

def resizegif(filename):
#     base_gif = imageio.mimread(filename)
#     reader = imageio.get_reader(filename)
#     new_gif = []
#     new_name = filename[0:len(filename)-4]+'_new.gif'
#     print(new_name)
#     print(reader.get_data(index))
#     dur = reader.get_meta_data()['duration']
#     for frame in base_gif:
#         frame = Image.resize((frame.size[1]/2,frame.size[2]/2))
#         new_gif.append(frame)
#     imageio.mimsave(new_name, new_gif, fps=dur)
    
    frames = images2gif.readGif("Abra.gif",False)
    for frame in frames:
        frame.thumbnail((100,100), Image.ANTIALIAS)

    images2gif.writeGif('abranew.gif', frames)

