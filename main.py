#importing all neccecary libraries
import easyocr
import g4f
from gradio_client import Client
from g4f.Provider import (
    Bing
    )


##################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################

#EasyOCR part



#define the ocr language

print("Please provide the language you want to use:")
print()
print("input - language")
print("en - english")
print("ar - arabic")
print()
readerask = input("> ")
reader = easyocr.Reader([readerask]) # this needs to run only once to load the model into memory



#find and read the question


result_question = reader.readtext('question.png', detail = 0)


#ask for the mode the user wants to use
print()
print("What kind of question is your question that you are trying to solve?")
print()
print("1 - Multiple Choice (4 Choices)")
print("2 - Multiple Choice (5 Choices)")
print("3 - Multiple Choice (6 Choices)")
print("4 - Multiple Answers (4 Choices) (2 Answers)")
print("5 - Multiple Answers (4 Choices) (3 Answers)")
print("6 - Multiple Answers (5 Choices) (2 Answers)")
print("7 - Multiple Answers (5 Choices) (3 Answers)")
print("8 - Multiple Answers (6 Choices) (2 Answers)")
print("9 - Multiple Answers (6 Choices) (3 Answers)")
print("10 - Input Question")
print("11 - Multiple Choice (3 Choices)")
print()

question_type = input("> ")
question_type = int(question_type)


#1 - Four Choice Questions  DONE   CONFIRMED TO WORK
if question_type == 1:

    #find and read the answers
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
    prequestion_list = ["IF YOU SEE ANY SPELLING MISTAKES, PLEASE FIX THEM IN YOUR MIND, the question might be seperated into short phrases, so if you notice that, please fix them in your mind, please answer as accurately as possible. When you answer, ONLY ANSWER WITH THE ACTUAL ANSWER PICKED AND NOTHING ELSE, you arent allowed to add any explanation or any additional words to the answer chosen by you, so you would only type the number of the answer and the answer next to it seperated by a colon. Answer in the language of the question and answers. Answer in the language of the question and answers. This is an example of how you should answer:", """ "Answer #: example answer """]
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
    print()
    print()
    print("Final output:")
    print(final_sendoff)

#2 - Five Choice Question   DONE
elif question_type == 2:

    #find and read the answers
    result_answer1 = reader.readtext('ans1.png', detail = 0)
    result_answer2 = reader.readtext('ans2.png', detail = 0)
    result_answer3 = reader.readtext('ans3.png', detail = 0)
    result_answer4 = reader.readtext('ans4.png', detail = 0)
    result_answer5 = reader.readtext('ans5.png', detail = 0)


    #join the stuff outputted together in a useable format
    variable_question = "\n".join(result_question)
    variable_ans1 = "\n".join(result_answer1)
    variable_ans2 = "\n".join(result_answer2)
    variable_ans3 = "\n".join(result_answer3)
    variable_ans4 = "\n".join(result_answer4)
    variable_ans5 = "\n".join(result_answer5)

    #make a prompt to be used for before the actual questions + answers so GPT-4 can know how to answer
    prequestion_list = ["IF YOU SEE ANY SPELLING MISTAKES, PLEASE FIX THEM IN YOUR MIND, the question might be seperated into short phrases, so if you notice that, please fix them in your mind, please answer as accurately as possible. When you answer, ONLY ANSWER WITH THE ACTUAL ANSWER PICKED AND NOTHING ELSE, you arent allowed to add any explanation or any additional words to the answer chosen by you, so you would only type the number of the answer and the answer next to it seperated by a colon. Answer in the language of the question and answers. This is an example of how you should answer:", """ "Answer #: example answer """]
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
    final_ans5_list = ["Answer 5: ", variable_ans5]
    final_ans5 = "\n".join(final_ans5_list)


    #debug step
    #print(final_question)
    #print(final_ans1)
    #print(final_ans2)
    #print(final_ans3)
    #print(final_ans4)
    #print(final_ans5)


    #this grabs all the final variables into one list, then into a variable. this is now the constructed prompt that goes to GPT-4
    final_sendoff_list = [final_question, final_ans1, final_ans2, final_ans3, final_ans4, final_ans5]
    final_sendoff = "\n".join(final_sendoff_list)
    print()
    print()
    print("Final output:")
    print(final_sendoff)

#3 - Six Choice Question  DONE

elif question_type == 3:

    #find and read the answers
    result_answer1 = reader.readtext('ans1.png', detail = 0)
    result_answer2 = reader.readtext('ans2.png', detail = 0)
    result_answer3 = reader.readtext('ans3.png', detail = 0)
    result_answer4 = reader.readtext('ans4.png', detail = 0)
    result_answer5 = reader.readtext('ans5.png', detail = 0)
    result_answer6 = reader.readtext('ans6.png', detail = 0)


    #join the stuff outputted together in a useable format
    variable_question = "\n".join(result_question)
    variable_ans1 = "\n".join(result_answer1)
    variable_ans2 = "\n".join(result_answer2)
    variable_ans3 = "\n".join(result_answer3)
    variable_ans4 = "\n".join(result_answer4)
    variable_ans5 = "\n".join(result_answer5)
    variable_ans6 = "\n".join(result_answer6)

    #make a prompt to be used for before the actual questions + answers so GPT-4 can know how to answer
    prequestion_list = ["IF YOU SEE ANY SPELLING MISTAKES, PLEASE FIX THEM IN YOUR MIND, the question might be seperated into short phrases, so if you notice that, please fix them in your mind, please answer as accurately as possible. When you answer, ONLY ANSWER WITH THE ACTUAL ANSWER PICKED AND NOTHING ELSE, you arent allowed to add any explanation or any additional words to the answer chosen by you, so you would only type the number of the answer and the answer next to it seperated by a colon. Answer in the language of the question and answers. This is an example of how you should answer:", """ "Answer #: example answer """]
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
    final_ans5_list = ["Answer 5: ", variable_ans5]
    final_ans5 = "\n".join(final_ans5_list)
    final_ans6_list = ["Answer 6: ", variable_ans6]
    final_ans6 = "\n".join(final_ans6_list)


    #debug step
    #print(final_question)
    #print(final_ans1)
    #print(final_ans2)
    #print(final_ans3)
    #print(final_ans4)
    #print(final_ans5)
    #print(final_ans6)


    #this grabs all the final variables into one list, then into a variable. this is now the constructed prompt that goes to GPT-4
    final_sendoff_list = [final_question, final_ans1, final_ans2, final_ans3, final_ans4, final_ans5,final_ans6]
    final_sendoff = "\n".join(final_sendoff_list)
    print()
    print()
    print("Final output:")
    print(final_sendoff)

#4 - Multiple Answers (4 Choices) (2 Answers)   DONE   CONFIRMED TO WORK

elif question_type == 4:

    #find and read the answers
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
    prequestion_list = ["IF YOU SEE ANY SPELLING MISTAKES, PLEASE FIX THEM IN YOUR MIND, the question might be seperated into short phrases, so if you notice that, please fix them in your mind, please answer as accurately as possible. When you answer, ONLY ANSWER WITH THE ACTUAL 2 ANSWERS PICKED AND NOTHING ELSE, you arent allowed to add any explanation or any additional words to the answer chosen by you, so you would only type the number of the answers and the answers next to it seperated by a colon. Answer in the language of the question and answers. This is an example of how you should answer:", """ "Answer #: example answer  and Answer #: example answer """]
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
    print()
    print()
    print("Final output:")
    print(final_sendoff)

#5 - Multiple Answers (4 Choices) (3 Answers)   DONE

elif question_type == 5:

    #find and read the answers
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
    prequestion_list = ["IF YOU SEE ANY SPELLING MISTAKES, PLEASE FIX THEM IN YOUR MIND, the question might be seperated into short phrases, so if you notice that, please fix them in your mind, please answer as accurately as possible. When you answer, ONLY ANSWER WITH THE ACTUAL 3 ANSWERS PICKED AND NOTHING ELSE, you arent allowed to add any explanation or any additional words to the answer chosen by you, so you would only type the number of the answers and the answers next to it seperated by a colon. Answer in the language of the question and answers. This is an example of how you should answer:", """ "Answer #: example answer  ,  Answer #: example answer   and Answer #: example answer"""]
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
    print()
    print()
    print("Final output:")
    print(final_sendoff)


#6 - Multiple Answers (5 Choices) (2 Answers)   DONE

elif question_type == 6:

    result_answer1 = reader.readtext('ans1.png', detail = 0)
    result_answer2 = reader.readtext('ans2.png', detail = 0)
    result_answer3 = reader.readtext('ans3.png', detail = 0)
    result_answer4 = reader.readtext('ans4.png', detail = 0)
    result_answer5 = reader.readtext('ans5.png', detail = 0)


    #join the stuff outputted together in a useable format
    variable_question = "\n".join(result_question)
    variable_ans1 = "\n".join(result_answer1)
    variable_ans2 = "\n".join(result_answer2)
    variable_ans3 = "\n".join(result_answer3)
    variable_ans4 = "\n".join(result_answer4)
    variable_ans5 = "\n".join(result_answer5)

    #make a prompt to be used for before the actual questions + answers so GPT-4 can know how to answer
    prequestion_list = ["IF YOU SEE ANY SPELLING MISTAKES, PLEASE FIX THEM IN YOUR MIND, the question might be seperated into short phrases, so if you notice that, please fix them in your mind, please answer as accurately as possible. When you answer, ONLY ANSWER WITH THE ACTUAL 2 ANSWERS PICKED AND NOTHING ELSE, you arent allowed to add any explanation or any additional words to the answer chosen by you, so you would only type the number of the answers and the answers next to it seperated by a colon. Answer in the language of the question and answers. This is an example of how you should answer:", """ "Answer #: example answer  and Answer #: example answer """]
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
    final_ans5_list = ["Answer 5: ", variable_ans5]
    final_ans5 = "\n".join(final_ans5_list)


    #debug step
    #print(final_question)
    #print(final_ans1)
    #print(final_ans2)
    #print(final_ans3)
    #print(final_ans4)


    #this grabs all the final variables into one list, then into a variable. this is now the constructed prompt that goes to GPT-4
    final_sendoff_list = [final_question, final_ans1, final_ans2, final_ans3, final_ans4, final_ans5]
    final_sendoff = "\n".join(final_sendoff_list)
    print()
    print()
    print("Final output:")
    print(final_sendoff)

#7 - Multiple Answers (5 Choices) (3 Answers)  DONE

elif question_type == 7:

    #find and read the answers
    result_answer1 = reader.readtext('ans1.png', detail = 0)
    result_answer2 = reader.readtext('ans2.png', detail = 0)
    result_answer3 = reader.readtext('ans3.png', detail = 0)
    result_answer4 = reader.readtext('ans4.png', detail = 0)
    result_answer5 = reader.readtext('ans5.png', detail = 0)


    #join the stuff outputted together in a useable format
    variable_question = "\n".join(result_question)
    variable_ans1 = "\n".join(result_answer1)
    variable_ans2 = "\n".join(result_answer2)
    variable_ans3 = "\n".join(result_answer3)
    variable_ans4 = "\n".join(result_answer4)
    variable_ans5 =  "\n".join(result_answer5)


    #make a prompt to be used for before the actual questions + answers so GPT-4 can know how to answer
    prequestion_list = ["IF YOU SEE ANY SPELLING MISTAKES, PLEASE FIX THEM IN YOUR MIND, the question might be seperated into short phrases, so if you notice that, please fix them in your mind, please answer as accurately as possible. When you answer, ONLY ANSWER WITH THE ACTUAL 3 ANSWERS PICKED AND NOTHING ELSE, you arent allowed to add any explanation or any additional words to the answer chosen by you, so you would only type the number of the answers and the answers next to it seperated by a colon. Answer in the language of the question and answers. This is an example of how you should answer:", """ "Answer #: example answer  ,  Answer #: example answer   and Answer #: example answer"""]
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
    final_ans5_list =  ["Answer 5: ", variable_ans5]
    final_ans5 = "\n".join(final_ans5_list)




    #debug step
    #print(final_question)
    #print(final_ans1)
    #print(final_ans2)
    #print(final_ans3)
    #print(final_ans4)


    #this grabs all the final variables into one list, then into a variable. this is now the constructed prompt that goes to GPT-4
    final_sendoff_list = [final_question, final_ans1, final_ans2, final_ans3, final_ans4, final_ans5]
    final_sendoff = "\n".join(final_sendoff_list)
    print()
    print()
    print("Final output:")
    print(final_sendoff)

#8 - Multiple Answers (6 Choices) (2 Answers)  DONE

elif question_type == 8:

    #find and read the answers
    result_answer1 = reader.readtext('ans1.png', detail = 0)
    result_answer2 = reader.readtext('ans2.png', detail = 0)
    result_answer3 = reader.readtext('ans3.png', detail = 0)
    result_answer4 = reader.readtext('ans4.png', detail = 0)
    result_answer5 = reader.readtext('ans5.png', detail = 0)
    result_answer6 = reader.readtext('ans6.png', detail = 0)


    #join the stuff outputted together in a useable format
    variable_question = "\n".join(result_question)
    variable_ans1 = "\n".join(result_answer1)
    variable_ans2 = "\n".join(result_answer2)
    variable_ans3 = "\n".join(result_answer3)
    variable_ans4 = "\n".join(result_answer4)
    variable_ans5 = "\n".join(result_answer5)
    variable_ans6 = "\n".join(result_answer6)

    #make a prompt to be used for before the actual questions + answers so GPT-4 can know how to answer
    prequestion_list = ["IF YOU SEE ANY SPELLING MISTAKES, PLEASE FIX THEM IN YOUR MIND, the question might be seperated into short phrases, so if you notice that, please fix them in your mind, please answer as accurately as possible. When you answer, ONLY ANSWER WITH THE ACTUAL 2 ANSWERS PICKED AND NOTHING ELSE, you arent allowed to add any explanation or any additional words to the answer chosen by you, so you would only type the number of the answers and the answers next to it seperated by a colon. Answer in the language of the question and answers. This is an example of how you should answer:", """ "Answer #: example answer  and Answer #: example answer """]
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
    final_ans5_list = ["Answer 5: ", variable_ans5]
    final_ans5 = "\n".join(final_ans5_list)
    final_ans6_list = ["Answer 6: ", variable_ans6]
    final_ans6 = "\n".join(final_ans6_list)


    #debug step
    #print(final_question)
    #print(final_ans1)
    #print(final_ans2)
    #print(final_ans3)
    #print(final_ans4)


    #this grabs all the final variables into one list, then into a variable. this is now the constructed prompt that goes to GPT-4
    final_sendoff_list = [final_question, final_ans1, final_ans2, final_ans3, final_ans4, final_ans5, final_ans6]
    final_sendoff = "\n".join(final_sendoff_list)
    print()
    print()
    print("Final output:")
    print(final_sendoff)

#9 - Multiple Answers (6 Choices) (3 Answers) DONE

elif question_type == 9:

    #find and read the answers
    result_answer1 = reader.readtext('ans1.png', detail = 0)
    result_answer2 = reader.readtext('ans2.png', detail = 0)
    result_answer3 = reader.readtext('ans3.png', detail = 0)
    result_answer4 = reader.readtext('ans4.png', detail = 0)
    result_answer5 = reader.readtext('ans5.png', detail = 0)
    result_answer6 = reader.readtext('ans6.png', detail = 0)


    #join the stuff outputted together in a useable format
    variable_question = "\n".join(result_question)
    variable_ans1 = "\n".join(result_answer1)
    variable_ans2 = "\n".join(result_answer2)
    variable_ans3 = "\n".join(result_answer3)
    variable_ans4 = "\n".join(result_answer4)
    variable_ans5 =  "\n".join(result_answer5)
    variable_ans6 =  "\n".join(result_answer6)

    #make a prompt to be used for before the actual questions + answers so GPT-4 can know how to answer
    prequestion_list = ["IF YOU SEE ANY SPELLING MISTAKES, PLEASE FIX THEM IN YOUR MIND, the question might be seperated into short phrases, so if you notice that, please fix them in your mind, please answer as accurately as possible. When you answer, ONLY ANSWER WITH THE ACTUAL 3 ANSWERS PICKED AND NOTHING ELSE, you arent allowed to add any explanation or any additional words to the answer chosen by you, so you would only type the number of the answers and the answers next to it seperated by a colon. Answer in the language of the question and answers. This is an example of how you should answer:", """ "Answer #: example answer  ,  Answer #: example answer   and Answer #: example answer"""]
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
    final_ans5_list =  ["Answer 5: ", variable_ans5]
    final_ans5 = "\n".join(final_ans5_list)
    final_ans6_list =  ["Answer 6: ", variable_ans6]
    final_ans6 = "\n".join(final_ans6_list)




    #debug step
    #print(final_question)
    #print(final_ans1)
    #print(final_ans2)
    #print(final_ans3)
    #print(final_ans4)


    #this grabs all the final variables into one list, then into a variable. this is now the constructed prompt that goes to GPT-4
    final_sendoff_list = [final_question, final_ans1, final_ans2, final_ans3, final_ans4, final_ans5, final_ans6]
    final_sendoff = "\n".join(final_sendoff_list)
    print()
    print()
    print("Final output:")
    print(final_sendoff)

#10 - Input Question  DONE

elif question_type == 10:

    #no answers needed to be read, it's an input answer anyways 


    #join the stuff outputted together in a useable format
    variable_question = "\n".join(result_question)

    #make a prompt to be used for before the actual questions + answers so GPT-4 can know how to answer
    prequestion_list = ["IF YOU SEE ANY SPELLING MISTAKES, PLEASE FIX THEM IN YOUR MIND, the question might be seperated into short phrases, so if you notice that, please fix them in your mind, please answer as accurately as possible. When you answer, you arent allowed to add any explanation or any additional words to the answer that would fit."]
    prequestion = "\n".join(prequestion_list)

    #add prequestion, a simple "ask the following question" thing, and put the actual question and join them as a list
    final_question_list = [prequestion, "Answer the following question: ", variable_question]
    final_question = "\n".join(final_question_list)





    #debug step
    #print(final_question)



    #this grabs all the final variables into one list, then into a variable. this is now the constructed prompt that goes to GPT-4
    final_sendoff_list = [final_question]
    final_sendoff = "\n".join(final_sendoff_list)
    print()
    print()
    print("Final output:")
    print(final_sendoff)


#11 - Three Choice Question   DONE
elif question_type == 11:

    #find and read the answers
    result_answer1 = reader.readtext('ans1.png', detail = 0)
    result_answer2 = reader.readtext('ans2.png', detail = 0)
    result_answer3 = reader.readtext('ans3.png', detail = 0)


    #join the stuff outputted together in a useable format
    variable_question = "\n".join(result_question)
    variable_ans1 = "\n".join(result_answer1)
    variable_ans2 = "\n".join(result_answer2)
    variable_ans3 = "\n".join(result_answer3)

    #make a prompt to be used for before the actual questions + answers so GPT-4 can know how to answer
    prequestion_list = ["IF YOU SEE ANY SPELLING MISTAKES, PLEASE FIX THEM IN YOUR MIND, the question might be seperated into short phrases, so if you notice that, please fix them in your mind, please answer as accurately as possible. When you answer, ONLY ANSWER WITH THE ACTUAL ANSWER PICKED AND NOTHING ELSE, you arent allowed to add any explanation or any additional words to the answer chosen by you, so you would only type the number of the answer and the answer next to it seperated by a colon. Answer in the language of the question and answers. This is an example of how you should answer:", """ "Answer #: example answer """]
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


    #debug step
    #print(final_question)
    #print(final_ans1)
    #print(final_ans2)
    #print(final_ans3)
    #print(final_ans4)
    #print(final_ans5)


    #this grabs all the final variables into one list, then into a variable. this is now the constructed prompt that goes to GPT-4
    final_sendoff_list = [final_question, final_ans1, final_ans2, final_ans3]
    final_sendoff = "\n".join(final_sendoff_list)
    print()
    print()
    print("Final output:")
    print(final_sendoff)

##################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################

#GPT4Free Part
print()
print("Which model would you like to use for response?")
print()
print("MORE MODELS COMING SOON")
print()
print("1 - GPT-4  (SMARTEST MODEL)")
print("2 - GPT 3.5 (FASTEST MODEL) (ChatGPT)")
print("3 - Phixtral (Open Source)")
print("4 - Beyonder (Open Source)")


print()
model_to_use = input("> ")
model_to_use = int(model_to_use)

#printing some stuff, including verifying that answering the question has started
print("Generating answer...")
g4f.debug.logging = False  # enable logging
g4f.check_version = False  # disable automatic version checking
print(g4f.version)  # check version
print(g4f.Provider.Ails.params)  # supported args

if model_to_use == 1:
    # the response of GPT-4 gets created here
    response = g4f.ChatCompletion.create(
        model=g4f.models.gpt_4,
        provider=g4f.Provider.Bing,
        messages=[{"role": "user", "content": final_sendoff}]
    )  


    #prints out the answer
    print()
    print(response)

elif model_to_use == 2:
    # the response of GPT 3.5 gets created here
    response = g4f.ChatCompletion.create(
        model=g4f.models.gpt_35_turbo,
        provider=g4f.Provider.You,
        messages=[{"role": "user", "content": final_sendoff}]
    )  


    #prints out the answer
    print()
    print(response)

elif model_to_use == 3:
    # the response of Phixtral gets created here
    client = Client("https://mlabonne-phixtral-chat.hf.space/--replicas/xblu7/")
    result = client.predict(
    final_sendoff,	# str  in 'Message' Textbox component
    api_name="/chat"
)
    print()
    print(result)


elif model_to_use == 4:
    # the response of Beyonder gets created here
    client = Client("https://mlabonne-beyonder-4x7b-v2-gguf-chat.hf.space/--replicas/f33hu/")
    result = client.predict(
		    final_sendoff,	# str  in 'Message' Textbox component
		    final_sendoff,	# str  in 'parameter_0' Textbox component
		    api_name="/chat"
    )
    print()
    print(result)


#ggs, you got your answer :)
