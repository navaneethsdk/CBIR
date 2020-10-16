import os
from flask import Flask, render_template, request, jsonify
from HSVhistDescriptor import ColorDescriptor
from searcher import Searcher

data ={
    "BS" : {
        "name":"Bacterial spot",
        "description":"Bacterial spot is caused by four species of Xanthomonas and occurs worldwide wherever tomatoes are grown. Bacterial spot causes leaf and fruit spots, which leads to defoliation, sun-scalded fruit, and yield loss.",
        "remedies":"Transplant treatment with streptomycin, Copper sprays and other topical treatments, Plant activator sprays"
    },
    "BM" : {
        "name":"Black Measles",
        "description":"Grapevine measles, also called esca, black measles or Spanish measles, has long plagued grape growers with its cryptic expression of symptoms and, for a long time, a lack of identifiable causal organism(s). The name 'measles' refers to the superficial spots found on the fruit ",
        "remedies":"Presently, there are no effective management strategies for measles. Wine grape growers with small vineyards will often have field crews remove infected fruit prior to harvest. Raisins affected by measles will be discarded during harvest or at the packing house, while table grape growers will leave affected fruit on the vine. Current research is focused on protecting pruning wounds from fungal infections to minimize suspect fungi from colonizing fresh wounds."
    },
    "AS": {
        "name":"Apple scab",
        "description":"Apple scab is a common disease of plants in the rose family (Rosaceae) that is caused by the ascomycete fungus Venturia inaequalis.[1] While this disease affects several plant genera, including Sorbus, Cotoneaster, and Pyrus, it is most commonly associated with the infection of Malus trees, including species of flowering crabapple, as well as cultivated apple.",
        "remedies":"Choose resistant varieties when possible. Rake under trees and destroy infected leaves to reduce the number of fungal spores available to start the disease cycle over again next spring. Water in the evening or early morning hours (avoid overhead irrigation) to give the leaves time to dry out before infection can occur. Spread a 3- to 6-inch layer of compost under trees, keeping it away from the trunk, to cover soil and prevent splash dispersal of the fungal spores."
    }
}

INDEX = os.path.join(os.path.dirname(__file__), 'index.csv')

app = Flask(__name__)
app.config["DEBUG"] = True

# search route
@app.route('/search', methods=['POST'])
def search():
    if request.method == "POST":
        RESULTS_ARRAY = []
        # get url
        # image_url = request.form.get('img')
        image = request.files["images"]
        image_name = image.filename
        image.save(os.path.join(os.getcwd(), image_name))
        try:
            # initialize the image descriptor
            cd = ColorDescriptor((8, 12, 3))
            # load the query image and describe it
            # from skimage import io
            import cv2
            # query = io.imread(image_url)
            # query = (query * 255).astype("uint8")
            # (r, g, b) = cv2.split(query)
            # query = cv2.merge([b, g, r])
            query = cv2.imread(os.path.join(os.getcwd(), image_name))    
            features = cd.describe(query)
            # perform the search
            searcher = Searcher(INDEX)
            results = searcher.search(features)
            results = sorted(results)
            print(results)
            # loop over the results, displaying the score and image name
            for (score, resultID) in results:
                RESULTS_ARRAY.append({
                    "image": str(resultID), 
                    "score": str(score),
                    "info" : data[str(resultID)[0:2]]
                    })
                break
            # return success
            return jsonify(results=(RESULTS_ARRAY[:3]))
        except:
            # return error
            return jsonify({"sorry": "Sorry, no results! Please try again."})


app.run()