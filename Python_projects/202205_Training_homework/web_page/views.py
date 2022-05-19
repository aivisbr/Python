from flask import Blueprint, render_template, request
import requests
import misc_fun as mf 


# Get word list
url = "https://raw.githubusercontent.com/just4spike/diff_files/main/all_words.json"
response = requests.get(url)
words = response.json()["tezaurs"] # tezaurs, valid_guesses or words


views = Blueprint(__name__, "viewsBp")

# Index page
@views.route("/")
def home():
    return render_template("index.html")

@views.route("/guess", methods=["POST","GET"])
def guess():
    if request.method == "POST":
        known = [request.form[f"lt{num}"] for num in range(1,6)] # letter position from lt1..lt5
        combined = known + list(request.form["good_l"].upper()) # combine letters from lt1..lt5 and good_l

        # Get unique values
        goodletters = mf.get_uniq_val(lst = combined)

        # Get unique values
        badletters = mf.get_uniq_val(lst = list(request.form["bad_l"].upper()))

        # Reduce 'words' list with known information (goodletters and badletters)
        intres = mf.find_words(wrds=words, letters=goodletters, include=True)
        finres = sorted(mf.find_words(wrds=intres, letters=badletters, include=False))

        # Reduce 'finres' list with known information (letter position)
        finres_by_pos = mf.find_words_by_pos(wrds=finres, letters=known)

        #print(goodletters, badletters, finres, finres_by_pos)

        return render_template("guess.html", wlist = finres_by_pos,
        gl="".join(goodletters), bl="".join(badletters),
        l1=known[0], l2=known[1], l3=known[2], l4=known[3], l5=known[4])
    else:
        finres_by_pos = ""
        return render_template("guess.html", wlist = finres_by_pos)

# Information about recources used in this work
@views.route("/info")
def info_addit():
    return render_template("additinfo.html")
