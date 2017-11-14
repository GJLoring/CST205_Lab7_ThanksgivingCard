#!/usr/bin/python
'''
Team 5 Hopper
    Jose Garcia Ledesma
    Grace Alvarez
    Christian Guerrero
    Gabriel Loring
CST205-40_FA17 Lab #6
November 13th 2017
'''

# Does not support Unicode so we are limited in our languages
cardText = ["Happy Thanksgiving",
            "Feliz dia de accion de gracias",
            "Joyeux Action de Graces",
            "Vrolijke Thanksgiving",
            "Furaha ya Shukrani",
            "Maligayang Pasasalamat"]
      

colors = [makeColor(128,  0,  0),
          makeColor(128,128,  0),
          makeColor(  0,128,  0),
          makeColor(  0,128,128),
          makeColor(  0,  0,128),
          makeColor(128,  0,128)]

# Since we have covered lists, but not random I used excel to generate a list of random numbers
# for turkey scale and rotation
randomData = [
[12,5.14477177292013],[11,4.94787095439254],[12,0.864285039856611],[9,4.81890505844699],[6,2.1446830619198],
[4,0.426620907735677],[19,2.44472179300302],[17,1.95196869389524],[1,5.61767740253519],[8,3.67672869567304],
[19,2.44891278917641],[5,0.0356702730716165],[16,1.01436242599693],[16,4.27168084712282],[9,5.23531553628476],
[3,4.01021334990998],[18,5.84945134735731],[2,3.59301099599679],[7,3.76403396123789],[15,2.82907090307243],
[15,4.63118764414353],[6,4.44174409503567],[17,3.30390784902386],[8,5.65065844596611],[10,2.49599706800443],
[9,2.02029622485163],[17,4.31110010861508],[1,0.831892582208965],[3,1.15176487744642],[13,6.04916714193268],
[18,3.7457208724091],[17,6.16320135940603],[4,1.93547215754429],[3,3.40873867788461],[2,1.25899873993894],
[1,4.32920194828425],[15,4.40516779374186],[0,5.17682856256787],[14,0.519967413670087],[3,0.119969597293543],
[15,0.531055041256374],[16,0.660213389938572],[16,5.31363750604388],[2,2.47316421440954],[16,2.86402545869173],
[7,5.79620925110019],[8,5.59735042069794],[14,5.24005458687475],[18,6.19424132600526],[0,4.10329441978992],
[15,3.62793777632839],[9,2.45591375478005],[6,2.8135677150912],[5,4.06098385870963],[5,5.00406903283542],
[14,1.33276265681992],[1,4.2829462030596],[8,2.20971652109855],[7,1.76938515055151],[10,6.13282889492302],
[16,5.35562637475977],[6,1.69552014627098],[12,6.19747815620476],[8,0.404104516066864],[1,0.966776067139277],
[6,2.64882713327941],[10,3.5110908791036],[18,0.0995452632482771],[3,5.50648081509503],[1,1.61561366423939],
[13,4.51897496716418],[3,2.51761321367527],[12,3.64742635148047],[1,3.87613695290603],[6,3.51838946718823],
[12,5.92645162003616],[10,5.26436072430903],[14,5.63343648308749],[14,1.56047179167759],[7,3.20413483353299],
[16,0.0643002408138972],[12,0.58136874472728],[14,5.50436910517179],[7,0.901689903690566],[14,3.08584657000432],
[3,0.773080896900731],[7,2.04498415691037],[1,0.860978657029353],[11,6.27479585488944],[12,0.179074844731708],
[4,2.44920733338623],[12,4.41680310847902],[11,3.43919277370613],[1,5.54733611666061],[5,0.740425766618672],
[15,2.68251507976418],[4,4.51456248446365],[6,2.16319578037582],[13,2.56476233339003],[14,5.90290060424401]]


'''
Turkey is a list of shapes, each shape is a list of points, each point is a coordinate pair
The coordinates were borrowed from my sons homework exercise on plotting points
'''
turkey=[
# Shape1
[[-3,-11],[-3.5,-12.5],[-4,-12],[-4.5,-12.5],[-4,-13],[-3,-14],[-2,-15.5],[-1.5,-16],[-1.5,-15.5],[-2,-14],[-1,-15],[0,-15.5],[-0.5,-14.5],[-1,-14],[0,-14.5],[0,-14],[-0.5,-13.5],[-2,-13],[-2.5,-12.5],[-1.5,-11.5],[-3,-11]],
# Shape2
[[-1.5,-11.5],[0,-11.5],[0.5,-12],[0.5,-13],[-0.5,-12.5],[-0.5,-13.5],[0,-14],[1.5,-15],[2,-16],[2.5,-15.5],[2,-15],[3,-15.5],[3.5,-15.5],[3.5,-15],[2,-14.5],[3,-14.5],[3.5,-14.5],[3.5,-14],[2,-13.5],[1,-13.5],[1.5,-12.5],[0.5,-12]],
# Shape3
[[1.5,-12.5],[2.5,-11.5],[4.5,-11.5],[6.5,-10],[7.5,-8.5],[9,-7],[9.5,-5.5],[10.5,-4],[10.5,-3],[10,-2.5],[8.5,-2],[9.5,-3.5],[9.5,-5.5]],
# Shape4
[[-3,-11],[-4,-10],[-4,-8.5],[-5.5,-7],[-4,-8],[-3,-8],[-1,-7.5],[2,-6],[4.5,-4],[5.5,-1.5],[7,-2.5],[8.5,-2]],
# Shape5
[[-5.5,-7],[-6.5,-6.5],[-7,-5.5],[-8,-5],[-8,-3.5],[-9,-3.5],[-9.5,-3],[-10.5,-3],[-10.5,-4],[-10,-5.5],[-9,-6.5],[-8,-6.5],[-7,-5.5]],
# Shape6
[[-10.5,-3],[-11.5,-2.5],[-12,-1],[-11,1],[-9,1],[-10.5,0],[-11,-1],[-10.5,-2],[-9.5,-2],[-9.5,-3]],
# Shape7
[[-9,1],[-8,1.5],[-8,0],[-7,-0.5],[-7,-1.5],[-6,-2.5],[-5,-2.5],[-5,-3.5],[-4,-4.5],[-3,-4.5],[-3.5,-5.5],[-2,-6],[-1.5,-7],[-1,-7.5]],
# Shape8
[[-8,1.5],[-7,2],[-6,2.5],[-3.5,2.5],[-4,2],[-4,1],[-3,0.5],[-3.5,0],[-3,-1],[-2,-1],[-2.5,-2],[-2,-3],[-0.5,-3],[-1,-4],[0,-5],[0.5,-4.5],[1,-5.5],[2,-6]],
# Shape9
[[-3.5,2.5],[-1.5,2.5],[-1.5,2.5],[0.5,2],[1.5,1.5],[2.5,1],[3.5,0.5],[5,-1],[5.5,-1.5]],
# Shape10
[[-11,1],[-12,2],[-11.5,4],[-10.5,5],[-8.5,4],[-6,2.5]],
# Shape11
[[-10.5,5],[-10.5,6],[-10,7.5],[-9,8.5],[-8,8.5],[-6,6],[-3.5,2.5]],
# Shape12
[[-8,8.5],[-7.5,10],[-6.5,10.5],[-5.5,11],[-4.5,10.5],[-3.5,7.5],[-2.5,5],[-1.5,2.5]],
# Shape13
[[-4.5,10.5],[-4,11.5],[-3,12],[-2,12.5],[-1,12],[-0.5,11.5],[-0.5,7],[-0.5,2.5]],
# Shape14
[[-0.5,11.5],[0,12.5],[1,12.5],[2.5,12],[3.5,11],[2.5,8],[0.5,2]],
# Shape15
[[3.5,11],[5,11],[6,10.5],[7,9],[4,5],[1.5,1.5]],
# Shape16
[[7,9],[8.5,8.5],[9.5,7],[8,7.5],[6.5,6.5],[6,5],[6,3.5],[2.5,1]],
# Shape17
[[6,3.5],[6,1],[3.5,0.5]],
# Shape18
[[6,1],[5.5,0],[5,-1]],
# Shape19
[[9.5,7],[10.5,6.5],[11,5],[9.5,5],[8,3],[7.5,2],[8,1.5],[8.5,1.5],[9,2.5],[9.5,3.5],[9.5,4.5],[10.5,4.5],[11,4],[11,5]],
# Shape20
[[8.5,-2],[8,0.5],[8,1.5]],
# Shape21
[[9.5,3.5],[10,3],[11.5,2.5],[11,4]],
# Shape22
[[9.5,1.5],[10.5,1.5],[11.5,2.5],[10,3],[9.5,2.5],[9.5,1.5],[9,1],[8,0.5]],
# Shape23
[[10.5,1.5],[11.5,1],[11.5,0],[11,-2],[10,-2.5]],
# Shape24
[[8.5,6],[8,5.5],[8.5,5],[9,5.5],[8.5,6]],
# Shape25
[[9,5.5],[8.5,5.5],[8.5,5]]]

def copyToCenter(source):
  copyOfSource = makeEmptyPicture( getWidth(source)*2,  getHeight(source)*2)
  for x in range (0, getWidth(source)):
    for y in range (0, getHeight(source)):
      setColor( getPixel(copyOfSource, x+getWidth(source)/2, y+getHeight(source)/2), getColor(getPixel(source, x, y)))

  return copyOfSource
  

def pyCopy(source, target, targetX, targetY):

  # Problem 2, Bullet point three instructs us to positvily address over-running image edges
  # So we will return with inserting if the source image is larger then the destination
  # and if the edge of the inserted image would over run the edge of the collage we will
  # slide our insertion point until it fits 
  #Make sure our destination is large enough 
  if source.getWidth() > target.getWidth() or source.getHeight() >target.getHeight():
    return #Image is to large to insert
   
  #Shift the image to fit inside destination if necessary 
  if source.getWidth()+ targetX > target.getWidth():
    targetX = target.getWidth()-source.getWidth()     
  if source.getHeight()+ targetY > target.getHeight():
    targetY = target.getHeight()-source.getHeight()
  
  #Actual insert    
  for x in range (0, getWidth(source)):
    for y in range (0, getHeight(source)):
      setColor( getPixel(target, x+targetX, y+targetY), getColor(getPixel(source, x, y)))

  return target


def mirrorLeftToRight(pic):
    for x in range (pic.getWidth()/2):
      for y in range (pic.getHeight()):
        destinationX = pic.getWidth() -x -1
        pxOut = getPixel(pic,destinationX,y)
        pxIn = getPixel(pic,x,y)
        setColor(pxOut, getColor(pxIn))  
  
def mirrorRightToLeft(pic):
    for x in range (pic.getWidth()/2,pic.getWidth() ):
      for y in range (pic.getHeight()):
        destinationX = pic.getWidth()-x
        pxOut = getPixel(pic,destinationX,y)
        pxIn = getPixel(pic,x,y)
        setColor(pxOut, getColor(pxIn))  
           
def mirrorTopToBottom(pic):
    for x in range (pic.getWidth()):
      for y in range (pic.getHeight()/2):
        destinationy = pic.getHeight() -y -1
        pxOut = getPixel(pic,x,destinationy)
        pxIn = getPixel(pic,x,y)
        setColor(pxOut, getColor(pxIn))                          
  
def mirrorBottomToTop(pic):
  for x in range (pic.getWidth()):
    for y in range (pic.getHeight()/2,pic.getHeight()):
      destinationy = pic.getHeight() -y
      pxOut = getPixel(pic,x,destinationy)
      pxIn = getPixel(pic,x,y)
      setColor(pxOut, getColor(pxIn))   
 
def quadruple_mirror(pic):
  mirrorLeftToRight(pic)
  mirrorTopToBottom(pic)
  
def lightenUp(pic, percent=0.5):
  percent = percent + 1
  pixels = getPixels(pic)
  for p in pixels:
    setRed(p, getRed(p) * percent)
    setGreen(p, getGreen(p) * percent)
    setBlue(p, getBlue(p) * percent)

def makeNegative(pic):
  pixels = getPixels(pic)
  for p in pixels:
    setRed(p, 255-getRed(p))
    setGreen(p, 255-getGreen(p))
    setBlue(p, 255-getBlue(p))  

def betterBnW(pic):
  pixels = getPixels(pic)
  for p in pixels:
    r = getRed(p)
    g = getGreen(p)
    b = getBlue(p)
    l =  r*0.299 + g*0.587 + b*0.114
    setRed(p, l)
    setGreen(p, l)
    setBlue(p, l) 


def drawTurkey(pic,color,xOffset,yOffset,scale=10,rotation=0):
  yScale = scale * -1 # Data set has is flipped top to bottom, so we will just use a negative scale to correct
  for shape in turkey:
    x1 = int((shape[0][0] * cos(rotation) - shape[0][1] * sin(rotation)) * scale + xOffset)
    y1 = int((shape[0][1] * cos(rotation) + shape[0][0] * sin(rotation)) * yScale + yOffset)
    for point in shape:
      x2 = int((point[0] * cos(rotation) - point[1] * sin(rotation))* scale + xOffset)
      y2 = int((point[1] * cos(rotation) + point[0] * sin(rotation))* yScale + yOffset)
      addLine(pic,x1,y1,x2,y2,color)
      x1 = x2
      y1 = y2

  
def randomTurkey(pic):
  i = 0
  for x in range(pic.getWidth()*.2, pic.getWidth()*.8, 75):
    for y in range(pic.getHeight()*.2, pic.getHeight()*.8, 100):
      i = i + 1
      if i > 99:
        i = 0
      scale = randomData[i][0]/3
      rotation = randomData[i][1]
      drawTurkey(pic,colors[int(rotation%6)],x,y,scale, rotation)


def message(pic):
  fontsize = 60
  y = pic.getHeight()/4 + fontsize
  x = pic.getWidth()/4
  count = 0
  formating = makeStyle(mono, bold, fontsize)
  for line in cardText:
    addTextWithStyle(pic, x, y, line,formating,colors[count])
    y = y +fontsize
    count = count + 1        
                                  		
#creates a sepia-tone picture, it requires a black and white picture
def Sepia():
  print("calling Sepia")
  bw_pic = betterBnW(pic)
  pixels = getPixels(bw_pic)
  for p in pixels:
    r = getRed(p)
    b = getBlue(p)
  
    #value multiplier for red
    if r < 63:
      newR = 1.1 * r
    elif r > 62 and r < 192:
      newR = 1.15 * r
    else:
      newR = 1.08 * r 
      if newR > 255:
        newR = 255

    #value multiplier for blue
    if b < 63:
      newB = 0.9 * b
    elif b > 62 and b < 192:
      newB = 0.85 * b
    else:
      newB = 0.93 * b

    setRed(p, newR)
    setBlue(p, newB)

#creates a black and white picture
def betterBnW(pic):
  print("calling betterBnW")
  pixels = getPixels(pic)
  for p in pixels:
    r = getRed(p)
    g = getGreen(p)
    b = getBlue(p)
    l =  r*0.299 + g*0.587 + b*0.114
    setRed(p, l)
    setGreen(p, l)
    setBlue(p, l)
  return pic
    


canvasWidth = 1980
canvasHeigth = 1020
canvas = makeEmptyPicture( canvasWidth,  canvasHeigth)
filename= ["//Users//gabriel//Desktop//11.jpeg",
           "//Users//gabriel//Desktop//12.jpeg",
           "//Users//gabriel//Desktop//13.jpeg",
           "//Users//gabriel//Desktop//14.jpeg", 
           "//Users//gabriel//Desktop//15.png",   
           "//Users//gabriel//Desktop//16.jpeg",
           "//Users//gabriel//Desktop//17.jpeg"] 
numberOfPhotos = len(filename)
pic= [None] * numberOfPhotos
for imgcount in range(numberOfPhotos):
  pic[imgcount] = makePicture(filename[imgcount])


#Transform 5 of the images as requested in assignment
mirrorLeftToRight(pic[1])
makeNegative(pic[2])
lightenUp(pic[4])
quadruple_mirror(pic[3])  
betterBnW(pic[0])

# Insert the 8 images into 2 col x 4 rows
cols = 9
rows = 5
imgcount = 0
for row in range(rows):
  for col in range(cols):

    if imgcount == 5:
      imgcount = 0
    targetX = (canvasWidth/cols)*col
    targetY = (canvasHeigth/rows)*row
    pyCopy(pic[imgcount], canvas, targetX, targetY)  
    imgcount = imgcount + 1

addRectFilled(canvas, canvas.getWidth()/5, canvas.getHeight()/4, int(canvas.getWidth()*.6), canvas.getHeight()/2, makeColor(192,128,128))
randomTurkey(canvas)
message(canvas)

repaint(canvas)

writePictureTo(canvas,"//Users//gabriel//Desktop//CST205_card.jpg")