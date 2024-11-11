import zipfile

# name of the new Zip file
zip_file_name = 'new_zip_file.zip'

# name of the source file
file_name = 'file_to_compress.txt'

# Create a ZipFile Object
zip_object = zipfile.ZipFile(zip_file_name, 'w')

# Add the source file to the zip file
zip_object.write(file_name, compress_type=zipfile.ZIP_DEFLATED)

# Close the Zip File
zip_object.close()