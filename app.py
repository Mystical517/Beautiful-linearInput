# -*- coding: UTF-8 -*-

from flask import Flask, request, render_template
import json
import re

app = Flask(__name__)


@app.route('/')
def index():

    return render_template('index.html')


@app.route('/transform')
def transform():
    formula = request.args.get("input")
    matrixTemplate = """
    \\left (
    \\begin{matrix}
        %s
    \\end{matrix}
    \\right  )
        """
    matrixTemplate = re.sub('\s', '', matrixTemplate)

    if (formula):
        texFormula = ""
        rowList = formula.split("<br />")
        for i in rowList:
            elements = i.split(" ")

            for element in elements:
                print(element)
                texFormula += element + "&"

            texFormula = texFormula[0:-1]  # 去掉多余的&
            texFormula = texFormula + "\\\\"
        matrixTemplate = matrixTemplate % texFormula
    else:
        welcom = "welcome & to\\\\ beautiful & linearInput"
        matrixTemplate = matrixTemplate % welcom

    return render_template('transform.html', linearInput=matrixTemplate)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
