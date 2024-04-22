import imageprocessor as ip
resized_image = ip.resize_image(image, width=800, height=600)
cropped_image = ip.crop_image(image, x=100, y=100, width=400, height=300)
filtered_image = ip.apply_filter(image, filter_type='blur', radius=5)
converted_image = ip.convert_image(image, format='png')
thumbnail = ip.generate_thumbnail(image, size=200)
ip.save_image(resized_image, 'path/to/resized_image.jpg')

