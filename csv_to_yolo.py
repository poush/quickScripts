# README:
# 0th column is assumed to have image path
# 3rd column is assumed to have class name
# 4,5,6,8 th columns are assumed to have x1,y1,x2,y2 of the image
# it creates a folder called "anno" and store new annotation files there
# feel free to update indexes as present in your annotation file


from PIL import Image

# assumes that the single annotation file name is data.txt
with open("data.txt", "r") as f:
    txt = f.read()
    classes = {}
    files = {}
    i = -1
    for line in txt.split("\n"):
        record = line.split(",")

        # assumes there are 8 columns in each row, update it according to yours
        if len(record) < 8:
            break
        
        #update index of the class here
        if record[3] not in classes:
            i+=1
            classes[record[3]] = i

        #full path of image
        fname = record[0]

        im = Image.open(fname)
        width, height = im.size

        # indexes for dimensions
        xmin, ymin, xmax, ymax = [int(x) for x in record[4:8]]
        
        #uncomment two lines below if the other two dimensions are width and height instead of xmax and ymax
        #xmax = xmin + xmax
        #ymax = ymin + ymax
        

        x = (xmin + xmax)/2.0
        y = (ymin + ymax)/2.0
        w = xmax - xmin
        h = ymax - ymin

        x1 = str(x/width)
        y1 = str(y/height)
        w1 = str(w/width)
        h1 = str(h/height)


        filename = "anno/" +record[0].split(".")[0].split("/")[1]+".txt"

        towrite = " ".join([str(classes[record[3]]), x1 , y1, w1, h1])

        if filename not in files:
            files[filename] = [towrite]
        else:
            files[filename].append(towrite)

    for fe in files:
        fw = open(fe, "w")
        for line in files[fe]:
            fw.write(line + "\n")
        fw.close()
