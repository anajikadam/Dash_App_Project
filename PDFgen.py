# Python libraries
from fpdf import FPDF
from datetime import datetime, timedelta
import os
from PIL import Image, ImageDraw, ImageFont, ImageOps
from glob import glob

class PDFgenerate():
    global HEIGHT, WIDTH
    HEIGHT, WIDTH = 297, 210
    def create_pdf_report(self,filename):
        def CreateTitle():
            filename1 = 'assets/Img/img.png'
            bg = Image.open(filename1, 'r')
            w, h = bg.size
            text = 'Covid-19 Analysis Report'
            x = datetime.now()
            date = str(x.date())
            time = str(x.strftime("%X"))
            font0 = ImageFont.truetype(r'C:\Windows\Fonts\arial.ttf', 80)
            font = ImageFont.truetype(r'C:\Windows\Fonts\arial.ttf', 40)
            ImageDraw.Draw(bg).text( (w/2-400,20),   text, (0,0,139), font = font0 )   #(255,69,0)
            ImageDraw.Draw(bg).text( (2300, 30),   date, (0,0,0), font = font )
            ImageDraw.Draw(bg).text( (2300, 90),   time, (0,0,0), font = font )
            #bg.show()
            bg.save("Images/title.png", format="png")

        def create_analytics_report(filename):
            pdf = FPDF() # A4 (210 by 297 mm)
            ''' First Page '''
            pdf.add_page()
            CreateTitle()
            pdf.image("Images/title.png", 0, 0, WIDTH)
            im = Image.open('Images/fig1.jpeg')
            # Add border and save
            bordered = ImageOps.expand(im, border=2, fill=(0,0,0))
            bordered.save("Images/fig1.jpeg")
            pdf.image("Images/fig1.jpeg",30,50,150,80)
            
            im = Image.open('Images/fig2.jpeg')
            # Add border and save
            bordered = ImageOps.expand(im, border=2, fill=(0,0,0))
            bordered.save("Images/fig2.jpeg")
            pdf.image("Images/fig2.jpeg",30,150,150,80)

            ''' Second Page '''
            pdf.add_page()
            im = Image.open('Images/fig3.jpeg')
            # Add border and save
            bordered = ImageOps.expand(im, border=2, fill=(0,0,0))
            bordered.save("Images/fig3.jpeg")
            pdf.image("Images/fig3.jpeg",30,50,150,80)
            
            im = Image.open('Images/fig4.jpeg')
            # Add border and save
            bordered = ImageOps.expand(im, border=2, fill=(0,0,0))
            bordered.save("Images/fig4.jpeg")
            pdf.image("Images/fig4.jpeg",30,150,150,80)

            ''' Third Page '''
            pdf.add_page()
            im = Image.open('Images/fig5.jpeg')
            # Add border and save
            bordered = ImageOps.expand(im, border=2, fill=(0,0,0))
            bordered.save("Images/fig5.jpeg")
            pdf.image("Images/fig5.jpeg",30,50,150,80)
            
            im = Image.open('Images/fig6.jpeg')
            # Add border and save
            bordered = ImageOps.expand(im, border=2, fill=(0,0,0))
            bordered.save("Images/fig6.jpeg")
            pdf.image("Images/fig6.jpeg",30,150,150,80)

            ''' Forth Page '''
            pdf.add_page()
            im = Image.open('Images/fig7.jpeg')
            # Add border and save
            bordered = ImageOps.expand(im, border=2, fill=(0,0,0))
            bordered.save("Images/fig7.jpeg")
            pdf.image("Images/fig7.jpeg",30,20,150,80)
            
            im = Image.open('Images/fig8.jpeg')
            # Add border and save
            bordered = ImageOps.expand(im, border=2, fill=(0,0,0))
            bordered.save("Images/fig8.jpeg")
            pdf.image("Images/fig8.jpeg",30,110,150,80)
            
            im = Image.open('Images/fig9.jpeg')
            # Add border and save
            bordered = ImageOps.expand(im, border=2, fill=(0,0,0))
            bordered.save("Images/fig9.jpeg")
            pdf.image("Images/fig9.jpeg",30,200,150,80)
            pdf.output(filename, 'F')
        
        create_analytics_report(filename)

# if __name__ == '__main__':
#     filename = "assets/pdf/report.pdf"
#     obj = PDFgenerate()
#     obj.create_pdf_report(filename)



    #     # FPDF(orientation='L', format='A4', unit="mm")
    #     pdf = FPDF(orientation='P', format='A4', unit="mm") # A4 (210 by 297 mm)
    #     pdf.add_page() 
    # #     pdf.image("Img/img2.PNG", 10, 10, WIDTH-30)
    #     pdf.image("Images/fig1.jpeg",10,10,100,80)
    #     pdf.image("Images/fig1.jpeg",110,90,100,80)

    #     ''' Second Page '''
    #     pdf.add_page()
    #     pdf.image("Images/fig2.jpeg",0,0,WIDTH-0,HEIGHT-0)

    #     pdf.output(filename, 'F')