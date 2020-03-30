from PIL import Image
import uuid

def createSubImages(picture):
  im = Image.open(picture)
  
  leftSide = im.crop((0, 180, im.width / 2, (im.height - (.1 * im.height))))
  leftTop = leftSide.crop((0, 0, leftSide.width, leftSide.height / 4))
  leftUpper = leftSide.crop((0, leftSide.height / 4, leftSide.width, (2 * leftSide.height / 4)))
  leftLower = leftSide.crop((0, (leftSide.height / 2), leftSide.width, (3 * leftSide.height / 4)))
  leftBottom = leftSide.crop((0, (leftSide.height - (.97 * (leftSide.height / 4))), leftSide.width, (leftSide.height)))

  rightSide = im.crop((im.width / 2, 180, im.width, im.height - (.1 * im.height)))
  rightTop = rightSide.crop((0, 0, rightSide.width, rightSide.height / 4))
  rightUpper = rightSide.crop((0, rightSide.height / 4, rightSide.width, (2 * rightSide.height / 4)))
  rightLower = rightSide.crop((0, (rightSide.height / 2), rightSide.width, (3 * rightSide.height / 4)))
  rightBottom = rightSide.crop((0, (rightSide.height - (.97 * (rightSide.height / 4))), rightSide.width, (rightSide.height)))

  leftTop.save(f"/Users/Tanner/code/products/Instagram/croppedImages/{uuid.uuid1()}.jpg")
  leftUpper.save(f"/Users/Tanner/code/products/Instagram/croppedImages/{uuid.uuid1()}.jpg")
  leftLower.save(f"/Users/Tanner/code/products/Instagram/croppedImages/{uuid.uuid1()}.jpg")
  leftBottom.save(f"/Users/Tanner/code/products/Instagram/croppedImages/{uuid.uuid1()}.jpg")

  rightTop.save(f"/Users/Tanner/code/products/Instagram/croppedImages/{uuid.uuid1()}.jpg")
  rightUpper.save(f"/Users/Tanner/code/products/Instagram/croppedImages/{uuid.uuid1()}.jpg")
  rightLower.save(f"/Users/Tanner/code/products/Instagram/croppedImages/{uuid.uuid1()}.jpg")
  rightBottom.save(f"/Users/Tanner/code/products/Instagram/croppedImages/{uuid.uuid1()}.jpg")

if __name__ == "__main__":
  createSubImages()
