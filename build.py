"""Unnecessary built script written in the amount of time a sane person
would have throw the page together using one of those online img => base64
converters, but that's cheating."""

import base64

with open('horse.jpg', 'rb') as img:
    img_data = img.read()
    encoded = 'data:image/jpeg;base64,{}'.format(base64.b64encode(img_data))

with open('index.html', 'w+') as output:
    output.write("""
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>The horse says "DOCTORATE DENIED".</title>
    <style>
        html, body {{ 
            background: #f4dbbf;
            margin: 0; 
            padding: 0; 
        }}
        #container {{
            border: 1px solid #51320e;
            border-radius: 3px;
            display: block;
            left: 50%;
            line-height: 0;
            position: absolute;
            top: 50%;
            transform: translate(-50%, -50%);
        }}
    </style>
</head>
<body>
    <div id="container">
        <a href="https://www.youtube.com/watch?v=CcnMDM5wA7k">
            <img src="{}" />
        </a>
    </div>
</body>
</html>
    """.format(encoded)
)

print 'I have a horsey. Ney, ney...'
