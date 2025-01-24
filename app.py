from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/about")
def about():
    return render_template("about.html")

@app.route("/contact")
def contact():
    return render_template("contact.html")

@app.route("/news")
def news():
    return render_template("new.html")

@app.route("/product")
def product():
    product = {
        "img_url": "https://assets.adidas.com/images/w_600,f_auto,q_auto/6e90a0002f92427e8d51aebe013f074f_9366/Gazelle_Indoor_Shoes_Red_H06261_01_standard.jpg",
        "name": "Gazelle Indoor Shoes Red",
        "price": 119.99,
        "description": 
        "The adidas Gazelle Indoor Shoes in Red offer a stylish take on a classic silhouette. Featuring a vibrant red suede upper, these shoes are designed for both comfort and durability. The iconic 3-Stripes and gold Gazelle lettering add a touch of heritage, while the gum rubber outsole provides excellent grip and traction. Perfect for everyday wear, these shoes blend vintage charm with modern performance."
    }
    return render_template("product.html", product=product)

@app.route("/product2")
def product2():
    product = {
        "img_url": "https://assets.adidas.com/images/w_600,f_auto,q_auto/844c66f5aa784114b481b174386c627b_9366/Gazelle_Indoor_Shoes_Blue_IG4998_01_standard.jpg",
        "name": "Gazelle Indoor Shoes Blue",
        "price": 89.99,
        "description": 
        "The adidas Gazelle Indoor Shoes in Blue bring a fresh update to a timeless design. With a rich blue suede upper, these shoes offer both style and durability. Signature 3-Stripes and gold Gazelle branding enhance their classic look, while the gum rubber outsole ensures superior grip and traction. Ideal for everyday wear, these shoes combine vintage appeal with modern comfort and performance."
 
    }
    return render_template("product.html", product=product)

@app.route("/product3")
def product3():
    product = {
        "img_url": "https://assets.adidas.com/images/w_600,f_auto,q_auto/af597595e6bb491b9854ae9601832d61_9366/Gazelle_Indoor_Shoes_Blue_H06260_01_standard.jpg",
        "name": "Gazelle Indoor Shoe Oceon Wave",
        "price": 99.99,
        "description": "The adidas Gazelle Indoor Shoe in Ocean Wave offers a fresh twist on a classic design. Featuring a striking Ocean Wave blue suede upper, these shoes are both stylish and durable. The iconic 3-Stripes and gold Gazelle lettering add a touch of heritage, while the gum rubber outsole ensures excellent grip and traction. Perfect for everyday wear, these shoes blend vintage charm with modern comfort and performance.."
    }
    return render_template("product.html", product=product)

@app.route("/product4")
def product4():
    product = {
        "img_url": "https://assets.adidas.com/images/w_600,f_auto,q_auto/cbb49237159140b98e90ed4ff79509d4_9366/Gazelle_Indoor_Shoes_White_IH7502_01_standard.jpg",
        "name": "Gazelle Indoor Shoes White",
        "price": 135.99,
        "description": "The adidas Gazelle Indoor Shoes in White deliver a sleek and timeless look. With a clean white suede upper, these shoes offer both style and durability. The iconic 3-Stripes and gold Gazelle branding enhance their classic appeal, while the gum rubber outsole provides superior grip and traction. Ideal for everyday wear, these shoes seamlessly blend vintage charm with modern comfort and performance."
    }
    return render_template("product.html", product=product)

@app.route("/product5")
def product5():
    product = {
        "img_url": "https://assets.adidas.com/images/w_600,f_auto,q_auto/ed067dbb02344f39b71a92803a0c9a1a_9366/Gazelle_Argentina_Shoes_White_ID3718_01_standard.jpg",
        "name": "Gazelle Shoe Argentina Edition" ,
        "price": 169.99,
        "description": "The adidas Gazelle Shoe Argentina Edition celebrates Argentine pride with a unique and stylish design. Featuring a vibrant sky blue and white suede upper, reminiscent of the national flag, these shoes showcase iconic 3-Stripes and gold Gazelle branding. The gum rubber outsole ensures excellent grip and traction, while the soft lining offers enhanced comfort. Perfect for fans and collectors, these shoes blend national heritage with the timeless appeal of the Gazelle silhouette."
    }
    return render_template("product.html", product=product)

@app.route("/productbotm")
def productbotm():
    product={
        "img_url": "https://assets.adidas.com/images/w_600,f_auto,q_auto/617921e1d5be4abe910417b155b5d3f5_9366/Arsenal_24-25_Home_Authentic_Jersey_Red_IT6140_HM1.jpg",
        "name": "Arsenal 24/25 Home Authenitic Jersey",
        "price": 69.99,
        "description": "The Arsenal home kit showcases the club's iconic red color, complemented by white sleeves and accents. With a design that often incorporates subtle patterns or textures, the kit proudly displays the Arsenal crest on the chest. It symbolizes the team's tradition, passion, and rich history, instilling a sense of pride and loyalty among fans globally."
    }
    return render_template("product.html", product=product)
@app.route("/productbotm2")
def productbotm2():
    product={
        "img_url": "https://assets.adidas.com/images/w_600,f_auto,q_auto/bfcea7fce3d549d9a7dabc557474ec0f_9366/Iconic_Wrapping_3-Stripes_Snap_Trackpant_Black_IN1833_21_model.jpg",
        "name": "Iconic Wrapping 3-Stripes Snap Ttrackpant",
        "price": 29.99,
        "description": "The Iconic Wrapping 3-Stripes Snap Track Pant by adidas features a classic athletic design with a modern twist. These track pants showcase the signature adidas 3-Stripes running down the sides, wrapping around the legs for a dynamic look. "
    }
    return render_template("product.html", product=product)
@app.route("/productbotm3")
def productbotm3():
    product={
        "img_url": "https://assets.adidas.com/images/w_600,f_auto,q_auto/9ea6fa4647874f21a81a7776868c536f_9366/Inter_Miami_CF_24-25_Messi_Home_Jersey_Kids_Pink_JE9743_02_laydown.jpg",
        "name": "Adidas Messi Inter Miami Jersey",
        "price": 49.99,
        "description": "The Inter Miami Jersey featuring Lionel Messi combines sleek design with premium performance. Highlighting Messi's iconic number 10, this jersey is crafted with breathable, moisture-wicking fabric to keep fans comfortable. The vibrant pink and black color scheme, emblematic of Inter Miami, is accentuated by the club's crest and adidas branding. This jersey is a must-have for Messi fans and soccer enthusiasts, celebrating the legendary player's move to Major League Soccer. Ronaldo is still better LOL"    
    }
    return render_template("product.html", product=product)

@app.route("/productbotm4")
def productbotm4():
    product={
        "img_url": "https://assets.adidas.com/images/w_600,f_auto,q_auto/2c817b23becc40c49edce727fe0c21c0_9366/Argentina_1994_Away_Jersey_Blue_IS0266_HM1.jpg",
        "name": "Argentina 1994 Away Jersey",
        "price": 89.99,
        "description": 
        "The Argentina 1994 Away Jersey is a classic piece of soccer history. Featuring iconic sky blue and navy blue stripes, this retro kit from the 1994 FIFA World Cup showcases the Argentine Football Association (AFA) crest on the chest"
    }
    return render_template("product.html", product=product)
@app.route("/productbotm5")
def productbotm5():
    product={
        "img_url": "https://assets.adidas.com/images/h_840,f_auto,q_auto,fl_lossy,c_fill,g_auto/cbcbb34496cf42e29e6aac9f006713ab_9366/Prime_Backpack_Black_EX6948_01_standard.jpg",
        "name": "Adidas Black Prime Backpack",
        "price": 129.99,
        "description":  "The adidas Black Prime Backpack combines style and functionality. Featuring a sleek black design, it offers multiple compartments for organized storage, including a padded laptop sleeve. The durable fabric ensures long-lasting use, while the adjustable, padded shoulder straps provide comfort. Perfect for daily use, school, or travel, this backpack is both practical and stylish."
    }
    return render_template("product.html", product=product)

@app.route("/signupadiclub")
def signupadiclub():
    return render_template("signupadiclub.html" )

@app.route("/loginadiclub")
def loginadiclub():
    return render_template("loginadiclub.html")

app.run(debug=True)
