from flask import Flask,render_template,request,url_for
import json
from utilize import Quiz
app = Flask(__name__)


@app.route('/')
def home():
    return render_template('home.html')
full_body = list()
quizz = dict()

@app.route('/data', methods = ['POST', 'GET'])


def data():  
    global title
    global total_questions
    global choices
    global select
    global explain
    if request.method == 'POST':
        quizzes = Quiz(request.form.get('question'),request.form.get('question_sub_topic'),request.form.get('question_img'),request.form.get("Explanation"),request.form.get("Explanation_img"),request.form.get("multi_select_true"),request.form.get("multi_select_false"),request.form.get('no_questions'),request.form.get("choices1"),request.form.get("choices2"),request.form.get("choices3"),request.form.get("choices4"),request.form.get("Explanation_true"),request.form.get("Explanation_false"))
    
        if request.form.get('Start'):
            ti = request.form.get('title')
            qu = request.form.get('no_questions')
            choice = quizzes.choice()
            multi = quizzes.multi_select()
            exp = quizzes.meta_explanation()
            title = ti
            total_questions = qu
            choices = choice
            select = multi
            explain = exp
            return render_template("quiz_entry.html")

        if request.form.get("submit_button") == "submit_button":
            full_body.append({"question_body":{"question" :quizzes.question,"question_subparts" : [x for x in quizzes.question_subparts.split("$$") if x != ""],"images":[x for x in quizzes.images.split("$$") if x != ""],"Explanation":{"text":[x for x in quizzes.explanation.split("$$") if x != ""],"img":[x for x in quizzes.img_explanation.split("$$") if x != ""]},"options":quizzes.options()}})
            quizz["quizzes"] = full_body
            return render_template("quiz_entry.html")

        if request.form.get("finish_button") == "finish_button":         
            quizz["metadata"] = {"source":{"url":"https://nptel.ac.in/","type":"pdf"},"explanation":explain,"total_questions":total_questions,"choices":choices,"multi_select":select,"title":title}            
                
            json_object = json.dumps(quizz)
            with open(str(title)+".json", "w") as outfile:
                outfile.write(json_object)
                return f"Json File Created Successfully! \U0001f600"

    return f"Cought Problem, Delete this json file and repeat the process."




if __name__ == "__main__":
    app.run(debug=True,port=8000)
