"""My Individual Flask App specifically for the page for drug sale arrests"""


from flask import Flask
from ProductionCode.data_procesor import drug_sale_arrests

app = Flask(__name__)


data = []


@app.route('/')
def homepage():
    """Determines the route to the homepage"""

    return "Hello! Welcome to our website with the amazingly" \
    "curated title: Analyzing Criminal Drug Abuse Treatment in Females" \
    "\nAlso known as drug_abuse_treatment.py" \
    "\n" \
    "\n" \
    "Here are the main usages of our program for your research/interests: " \
    '\npython3 app.py --meeting ["frequency", "count"]' \
    '\npython3 app.py --sellArrests lowerBoundCount upperBoundCount' \
    '\n' \
    '\nTo reach the drug sale arrests page, take the path /arrests/lower/upper'



@app.route('/arrests/<lower>/<upper>', strict_slashes=False)
def drug_sale(lower, upper):
    """Determines the route to the drug sale arrests page"""
    return str(drug_sale_arrests(int(lower), int(upper))) + " people"


if __name__ == '__main__':
    app.run()
