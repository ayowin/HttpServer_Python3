
from io import BytesIO;
import random;
from PIL import Image,ImageDraw,ImageFont;
import base64;

class Util:
    '''
        generate verify code
        @id: verify code id that you want to specify, default is None
        @count: how many characters you want, default is 6
        @jpegPath: save file(*.jpg) by jpegPath, default is None
        @return:
            return the following json, 
                1. id for your specified.
                2. result for verify code string.
                3. base64 for verify code image's base64 encode string.
            {
                "id": xxx,
                "result": "xxx",
                "base64": "xxx"
            }
    '''
    @staticmethod
    def verifyCode(id=None,count=6,jpegPath=None):
        code = {};
        code["id"] = "";
        code["base64"] = "";
        code["result"] = "";

        # generate id
        if id != None :
            code["id"] = id;
        # generate result
        for i in range(count) :
            number = random.randint(0, 9)
            upperCase = chr(random.randint(65, 90))
            lowerCase  = chr(random.randint(97, 122))
            code["result"] += str(random.choice([number, upperCase, lowerCase]))
        # generate base64
        # construct image for drawing
        imageSize = (600,200);
        image = Image.new(mode="RGB",size=imageSize,color=(random.randint(0,255),random.randint(0,255),random.randint(0,255)));
        draw = ImageDraw.Draw(image);
        # draw disrupt background rectangle
        horizontal = random.randint(15,25);
        vertical = random.randint(5,10);
        for i in range(horizontal):
            for j in range(vertical):
                x0 = i*(imageSize[0]/horizontal);
                y0 = j*(imageSize[1]/vertical);
                x1 = (i+1)*(imageSize[0]/horizontal);
                y1 = (j+1)*(imageSize[1]/vertical);
                backgroundColor = (random.randint(0,255),random.randint(0,255),random.randint(0,255));
                draw.rectangle(xy=(x0,y0,x1,y1),fill=backgroundColor);
        # draw characters
        for i in range(count) :
            char = code["result"][i];
            blockSize = 1*imageSize[0]/count;
            fontSize = int(blockSize);
            fontSize = random.randint(fontSize+20,fontSize+30);
            x = (i+0.15)*blockSize;
            y = (imageSize[1]-fontSize)/2;
            draw.text(xy=(x,y),
                      align="center",
                      text=char,
                      font=ImageFont.truetype("./micross.ttf",fontSize),
                      fill=(random.randint(0,255),random.randint(0,255),random.randint(0,255)));
        # save for base64
        bytesIO = BytesIO();
        image.save(bytesIO,"jpeg");
        data = bytesIO.getvalue();
        base64Bytes = base64.b64encode(data);
        base64String = str(base64Bytes,"UTF-8");
        code["base64"] = base64String;
        # save for file
        if jpegPath != None :
            image.save(jpegPath,"jpeg");
        return code;
