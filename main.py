#importing all neccecary libraries
import easyocr
import g4f
from g4f.Provider import (
    Bing
)


##################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################

#EasyOCR part

#define the ocr language
reader = easyocr.Reader(['ar']) # this needs to run only once to load the model into memory

#find and read the images
result_question = reader.readtext('question.png', detail = 0)
result_answer1 = reader.readtext('ans1.png', detail = 0)
result_answer2 = reader.readtext('ans2.png', detail = 0)
result_answer3 = reader.readtext('ans3.png', detail = 0)
result_answer4 = reader.readtext('ans4.png', detail = 0)


#join the stuff outputted together in a useable format
variable_question = "\n".join(result_question)
variable_ans1 = "\n".join(result_answer1)
variable_ans2 = "\n".join(result_answer2)
variable_ans3 = "\n".join(result_answer3)
variable_ans4 = "\n".join(result_answer4)

#make a prompt to be used for before the actual questions + answers so GPT-4 can know how to answer
prequestion_list = ["IF YOU SEE ANY SPELLING MISTAKES, PLEASE FIX THEM IN YOUR MIND, the question might be seperated into short phrases, so if you notice that, please fix them in your mind, please answer as accurately as possible, act like this is a test for you. When you answer, ONLY ANSWER WITH THE ACTUAL ANSWER PICKED AND NOTHING ELSE, you arent allowed to add any explanation or any additional words to the answer chosen by you, so you would only type the number of the answer and the answer next to it seperated by a colon. This is an example of how you should answer:", """ "Answer #: example answer """]
prequestion = "\n".join(prequestion_list)

#add prequestion, a simple "ask the following question" thing, and put the actual question and join them as a list
final_question_list = [prequestion, "Answer the following question: ", variable_question]
final_question = "\n".join(final_question_list)

#do the same thing for the answers, but without the prequestion
final_ans1_list = ["Answer 1: ", variable_ans1]
final_ans1 = "\n".join(final_ans1_list)
final_ans2_list = ["Answer 2: ", variable_ans2]
final_ans2 = "\n".join(final_ans2_list)
final_ans3_list = ["Answer 3: ", variable_ans3]
final_ans3 = "\n".join(final_ans3_list)
final_ans4_list = ["Answer 4: ", variable_ans4]
final_ans4 = "\n".join(final_ans4_list)


#debug step
#print(final_question)
#print(final_ans1)
#print(final_ans2)
#print(final_ans3)
#print(final_ans4)


#this grabs all the final variables into one list, then into a variable. this is now the constructed prompt that goes to GPT-4
final_sendoff_list = [final_question, final_ans1, final_ans2, final_ans3, final_ans4]
final_sendoff = "\n".join(final_sendoff_list)
print(final_sendoff)

##################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################

#GPT4Free Part

#printing some stuff, including verifying that answering the question has started
print("Generating answer...")
g4f.debug.logging = False  # Enable logging
g4f.check_version = False  # Disable automatic version checking
#print(g4f.version)  # Check version
#print(g4f.Provider.Ails.params)  # Supported args


# the response of GPT-4 gets created here
response = g4f.ChatCompletion.create(
    model=g4f.models.gpt_4,
    provider=g4f.Provider.Bing,
    messages=[{"role": "user", "content": final_sendoff}]
)  


#prints out the answer
print(response)

#ggs, you got your answer
