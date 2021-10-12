from flask import Flask,request
class Quiz:
    def __init__(self,question,question_subparts,images,explanation,img_explanation,multi_select_true,multi_select_false,no_questions,choices1,choices2,choices3,choices4,Explanation_true,Explanation_false):
        self.question = question
        self.question_subparts = question_subparts
        self.images = images
        self.explanation = explanation
        self.img_explanation = img_explanation
        self.multi_select_true = multi_select_true
        self.multi_select_false = multi_select_false
        self.Explanation_true = Explanation_true
        self.Explanation_false = Explanation_false

        self.no_questions = no_questions
        self.choices1 = choices1
        self.choices2 = choices2
        self.choices3 = choices3
        self.choices4 = choices4
        self.text_opt = list()
        self.img_opt = list()
        self.choices = list()
        self.multi_selects = False



    def question(self):
        return self.question
    
    def sub_question(self):
        return self.question_subparts
    
    def img_question(self):
        return self.images
    
    def explanation(self):
        return self.explanation

    def img_explanation(self):
        return self.img_explanation
    
    def options(self):
        if request.form['option_1'] or request.form['img_option_1']:
            self.text_opt.append({"is_correct":True if request.form.get('checkbox_1') or request.form.get("checkbox_img_1") else False,"value":{"text":[x for x in request.form.get("option_1").split("$$") if x != ""],"img":[x for x in request.form.get("img_option_1").split("$$") if x != ""]}})
        if request.form['option_2'] or request.form['img_option_2']:
            self.text_opt.append({"is_correct":True if request.form.get('checkbox_2') or request.form.get("checkbox_img_2") else False,"value":{"text":[y for y in request.form.get("option_2").split("$$") if y != ""],"img":[y for y in request.form.get("img_option_2").split("$$") if y != ""]}})
        if request.form['option_3'] or request.form['img_option_3']:
            self.text_opt.append({"is_correct":True if request.form.get('checkbox_3') or request.form.get("checkbox_img_3") else False,"value":{"text":[z for z in request.form.get("option_3").split("$$") if z != ""],"img":[z for z in request.form.get("img_option_3").split("$$") if z != ""]}})
        if request.form['option_4'] or request.form['img_option_4']:
            self.text_opt.append({"is_correct":True if request.form.get('checkbox_4') or request.form.get("checkbox_img_4") else False,"value":{"text":[a for a in request.form.get("option_4").split("$$") if a != ""],"img":[a for a in request.form.get("img_option_4").split("$$") if a != ""]}})
        return self.text_opt

    def multi_select(self):
        if self.multi_select_true:
            return True
        if self.multi_select_false:
            return False
        else:
            return False


    def meta_explanation(self):
        if self.Explanation_true:
            return True
        if self.Explanation_false:
            return False
        
    
    def choice(self):
        if self.choices1:
            self.choices.append(1)
        if self.choices2:
            self.choices.append(2)
        if self.choices3:
            self.choices.append(3)
        if self.choices4:
            self.choices.append(4)
        return self.choices

    def no_question(self):
        return self.no_questions

    



           
    
        #return {"options":opts}
    #return {"is_correct":op1_checked,"value" : opt_1,"is_correct":op2_checked,"value":opt_2,"is_correct":op3_checked,"value" : opt_3,"is_correct":op4_checked,"value":opt_4}


