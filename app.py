#Dillon Tall CSC 330 Midterm Project
#Flask Import
from flask import Flask, render_template

app = Flask(__name__)

# Main dictionary used for animal name and corresponding facts
# The facts are passed in as a list, this is because I found it easier
# using a list to space them out in the html file and so I can also edit
# each seperate fact
animal_facts = {
    
     'dog': [
        "1. It's estimated that roughly 21% of all dogs snore in their sleep.",
        "2. When dogs poop, they align themselves with the earth’s magnetic field. Specifically, with the north-south axis.",
        "3. The United States has the most dogs – home to nearly 76 million dogs. Brazil comes in second, followed by China.",
        "4. The average dog can run at the speed of 19 MPH (miles per hour).",
        "5. A dog is able to locate the source of a sound in 6/100th of a second.",
        "Source: https://thesmartcanine.com/fun-dog-facts/",
    ],

     'cat': [
        "1. A group of cats is called a “clowder.",
        "2. Cats make about 100 different sounds. Dogs make only about 10.",
        "3. Approximately 400,000 people are bitten by cats in the U.S. annually.",
        "4. A cat's hearing is better than a dog's. And a cat can hear high-frequency sounds up to two octaves higher than a human.",
        "5. A cat can travel at a top speed of approximately 31 mph (49 km) over a short distance.",
        "Source: https://www.factretriever.com/cat-facts",
    ],

     'elephant': [
        "1. It takes a female 22 months from conception to have a baby. This is longer than any other animal in the world.",
        "2. The average life span for an elephant in the wild is from 50 to 70 years. They oldest known elephant in the world lived to be 82 years of age.",
        "3. The heaviest elephant in the world weighed 26,000 pounds.",
        "4. The trunk of an elephant has more than 150,000 muscles and tendons in it.",
        "5. The tusks of an elephant can weigh up to 200 pounds and can grow up to 10 feet in length.",
        "Source: https://www.elephant-world.com/facts-about-elephants/",
    ],
    
}
#Dynamic route using "animal" variable used to pass onto html template
@app.route('/fact/<animal>')
def fact(animal):
    #Get corresponding animal fact
    fact = animal_facts.get(animal.lower())
    #Returns the html template (fact.html) passing the animal and fact variables
    return render_template('fact.html', animal=animal.capitalize(), fact=fact)

if __name__ == '__main__':
    app.run(debug=True)