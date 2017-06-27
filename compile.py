import os
basedir = '/Users/kguay/www'
rootdir = basedir + "/www"
l = list()

for subdir, dirs, files in os.walk(rootdir):
    for file in files:
    	file = os.path.join(subdir, file)
    	filename, file_extension = os.path.splitext(file)
    	ext = file_extension[1:].lower()
        subdir
        if ext == 'html' and subdir != rootdir:
            l.append("/".join(file.split("/")[5:]))

str1 = "var tipuesearch_pages = [\"/\", \"/" + "\", \"/".join(l) + "\"];"

text_file = open(basedir + "/public/tipuesearch/tipuesearch_set_list.js", "w")
text_file.write(str1)
text_file.close()
