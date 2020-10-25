from PIL import Image

def merge_two_images(file1, file2):
    """Merge two images into one, displayed side by side
    :param file1: path to first image file
    :param file2: path to second image file
    :return: the merged Image object
    """
    image1 = Image.open(file1)
    image2 = Image.open(file2)

    (width1, height1) = image1.size
    (width2, height2) = image2.size

    result_width = width1 + width2
    result_height = max(height1, height2)

    result = Image.new('RGB', (result_width, result_height))
    result.paste(im=image1, box=(0, 0))
    result.paste(im=image2, box=(width1, 0))
    return result

def merge_images(files):
    """Merge two images into one, displayed side by side
    :param file1: path to first image file
    :param file2: path to second image file
    :return: the merged Image object
    """
    result_height = 0
    widths = []
    images = []
    for file in files: 
      image = Image.open(file)
      images.append(image)
      (width, height) = image.size
      result_height = result_height + height
      widths.append(width)

    result_width = max(widths)

    result = Image.new('RGB', (result_width, result_height))
    
    image_position = (0, 0)
    for image in images:
      result.paste(im=image, box=image_position)
      image_position = (0, image_position[1] + height)

    return result

def create_merged(show_title, num_seasons):
  query_search = show_title + "S"
  title = query_search[:-1]
  range_to_use = num_seasons + 1
  images_to_merge = [query_search + str(x) + ".png" for x in range(1, range_to_use)]
  merged = merge_images(images_to_merge)
  file_name_merged = f'{title}Merged.png'
  print("Created " + file_name_merged)
  merged.save(file_name_merged, 'PNG')

shows = [["Fleabag", 2], ["Barry", 2], ["Black Mirror", 5], ["High Maintenance", 4], ["The Boys", 2], ["Der Tatortreiniger", 7],
        ["Stranger Things", 3], ["True Detective", 3], ["Babylon Berlin", 3]]

for show in shows:
  create_merged(show[0], show[1])