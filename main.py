import easyocr
import g4f
reader = easyocr.Reader(['en']) # this needs to run only once to load the model into memory
result_question = reader.readtext('question.png', detail = 0)
result_answer1 = reader.readtext('ans1.png', detail = 0)
result_answer2 = reader.readtext('ans2.png', detail = 0)
result_answer3 = reader.readtext('ans3.png', detail = 0)
result_answer4 = reader.readtext('ans4.png', detail = 0)


variable_question = "\n".join(result_question)
variable_ans1 = "\n".join(result_answer1)
variable_ans2 = "\n".join(result_answer2)
variable_ans3 = "\n".join(result_answer3)
variable_ans4 = "\n".join(result_answer4)

prequestion_list = ["IF YOU SEE ANY SPELLING MISTAKES, PLEASE FIX THEM IN YOUR MIND, the question might be seperated into short phrases, so if you notice that, please fix them in your mind, please answer as accurately as possible, act like this is a test for you. When you answer, ONLY ANSWER WITH THE ACTUAL ANSWER PICKED AND NOTHING ELSE, you arent allowed to add any explanation or any additional words to the answer chosen by you, so you would only type the number of the answer and the answer next to it seperated by a colon. This is an example of how you should answer:", """ "Answer #: example answer """]
prequestion = "\n".join(prequestion_list)
final_question_list = [prequestion, "Answer the following question: ", variable_question]
final_question = "\n".join(final_question_list)
final_ans1_list = ["Answer 1: ", variable_ans1]
final_ans1 = "\n".join(final_ans1_list)
final_ans2_list = ["Answer 2: ", variable_ans2]
final_ans2 = "\n".join(final_ans2_list)
final_ans3_list = ["Answer 3: ", variable_ans3]
final_ans3 = "\n".join(final_ans3_list)
final_ans4_list = ["Answer 4: ", variable_ans4]
final_ans4 = "\n".join(final_ans4_list)

#print(final_question)
#print(final_ans1)
#print(final_ans2)
#print(final_ans3)
#print(final_ans4)

final_sendoff_list = [final_question, final_ans1, final_ans2, final_ans3, final_ans4]
final_sendoff = "\n".join(final_sendoff_list)
print(final_sendoff)

g4f.debug.logging = True  # Enable logging
g4f.check_version = False  # Disable automatic version checking
print(g4f.version)  # Check version
print(g4f.Provider.Ails.params)  # Supported args

# Automatic selection of provider


# Normal response
response = g4f.ChatCompletion.create(
    model=g4f.models.gpt_4,
    messages=[{"role": "user", "content": final_sendoff}]
)  # Alternative model setting

print(response)
