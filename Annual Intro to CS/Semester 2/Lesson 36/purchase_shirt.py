#!usr/bin/python3
import cgi

def readForm():
    information = []
    formData = cgi.FieldStorage()

    information.append(formData.getvalue("first_name"))
    information.append(formData.getvalue("last_name"))
    information.append(formData.getvalue("clothe"))
    information.append(formData.getvalue("size"))

    colors = []
    colors.append(formData.getvalue("color_black"))
    colors.append(formData.getvalue("color_white"))
    colors.append(formData.getvalue("color_blue"))
    colors.append(formData.getvalue("color_red"))
    colors.append(formData.getvalue("color_green"))
    colors.append(formData.getvalue("color_yellow"))

    information.append(colors)
    information.append(formData.getvalue("comments"))

    return information

def htmlTop():
    print ('''Content-type:text/html\n\n
    <!DOCTYPE html>
    <html>
        <head>
            <title>Classwork 36</title>

            <style>
                body {
                    background-color: rgb(174, 232, 255);
                    text-align: center;
                }

                .form_item {
                    padding: .25%;
                }
            </style>
        </head>
        <body>''')
    
def htmlTail():
    print ('''
        </body>
    </html>''')

def main():
    htmlTop()
    print("Hello! Your inputs are {}".format(readForm()))
    htmlTail()

if __name__ == '__main__':
    try:
        main()
    except:
        cgi.print_exception()