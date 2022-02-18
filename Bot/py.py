from PIL import Image

im1 = Image.open('kake.jpg')
im2 = Image.open('choy.jpg')


def get_concat_h_resize(im1, im2, resample=Image.BICUBIC, resize_big_image=True):
    if im1.height == im2.height:
        _im1 = im1
        _im2 = im2
    elif (((im1.height > im2.height) and resize_big_image) or
          ((im1.height < im2.height) and not resize_big_image)):
        _im1 = im1.resize((int(im1.width * im2.height / im1.height), im2.height), resample=resample)
        _im2 = im2
    else:
        _im1 = im1
        _im2 = im2.resize((int(im2.width * im1.height / im2.height), im1.height), resample=resample)
    dst = Image.new('RGB', (_im1.width + _im2.width, _im1.height))
    dst.paste(_im1, (0, 0))
    dst.paste(_im2, (_im1.width, 0))
    return dst




def get_concat_v_resize(im1, im2, resample=Image.BICUBIC, resize_big_image=True):
    if im1.width == im2.width:
        _im1 = im1
        _im2 = im2
    elif (((im1.width > im2.width) and resize_big_image) or
          ((im1.width < im2.width) and not resize_big_image)):
        _im1 = im1.resize((im2.width, int(im1.height * im2.width / im1.width)), resample=resample)
        _im2 = im2
    else:
        _im1 = im1
        _im2 = im2.resize((im1.width, int(im2.height * im1.width / im2.width)), resample=resample)
    dst = Image.new('RGB', (_im1.width, _im1.height + _im2.height))
    dst.paste(_im1, (0, 0))
    dst.paste(_im2, (0, _im1.height))
    return dst


get_concat_h_resize(im1, im2).save('h_resize.jpg')
get_concat_v_resize(im1, im2, resize_big_image=False).save('v_resize.jpg')

# def get_concat_h_multi_resize(im_list, resample=Image.BICUBIC):
#     min_height = min(im.height for im in im_list)
#     im_list_resize = [im.resize((int(im.width * min_height / im.height), min_height), resample=resample)
#                       for im in im_list]
#     total_width = sum(im.width for im in im_list_resize)
#     dst = Image.new('RGB', (total_width, min_height))
#     pos_x = 0
#     for im in im_list_resize:
#         dst.paste(im, (pos_x, 0))
#         pos_x += im.width
#     return dst
#
#
# def get_concat_v_multi_resize(im_list, resample=Image.BICUBIC):
#     min_width = min(im.width for im in im_list)
#     im_list_resize = [im.resize((min_width, int(im.height * min_width / im.width)), resample=resample)
#                       for im in im_list]
#     total_height = sum(im.height for im in im_list_resize)
#     dst = Image.new('RGB', (min_width, total_height))
#     pos_y = 0
#     for im in im_list_resize:
#         dst.paste(im, (0, pos_y))
#         pos_y += im.height
#     return dst
#
#
# def get_concat_tile_resize(im_list_2d, resample=Image.BICUBIC):
#     im_list_v = [get_concat_h_multi_resize(im_list_h, resample=resample) for im_list_h in im_list_2d]
#     return get_concat_v_multi_resize(im_list_v, resample=resample)
#
#
# get_concat_tile_resize([[im1],
#                         [im1, im2],
#                         [im1, im2, im1]]).save('new.jpg')
