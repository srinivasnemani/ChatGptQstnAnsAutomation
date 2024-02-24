import time
import os
from openai import OpenAI
from export_answers_to_document import add_question_and_answer_to_document
from execute_with_retry import execute_with_retry_and_save_answers

openai_api_key = 'YourAPIKeyHere..'
answers_document_path = r"C:\Users\WinVM9\OneDrive\Desktop\Learning\OpenaAI_API_Test\questions_and_answers.docx"
file_path = os.path.abspath(answers_document_path)
question_file = r"C:\Users\WinVM9\OneDrive\Desktop\Learning\OpenaAI_API_Test\questions_1.txt"

if __name__ == '__main__':
    client = OpenAI(api_key=openai_api_key)
    file_path = os.path.abspath(answers_document_path)

    with open(question_file, 'r') as file:
        for line in file:
            question = line

            print(line)
            print("--------------------------------------------")

            # If required change the parameters, check Open AI documentation for presence_penalty, frequency_penalty
            completion_3 = execute_with_retry_and_save_answers(client, question)
            # completion_4 = execute_with_retry_and_save_question(client, question, model_name="gpt-4")
            completion_3_modified = execute_with_retry_and_save_answers(client, question, frequency_penalty=0.65,
                                                                        presence_penalty=1.25, )

            add_question_and_answer_to_document(file_path, question, completion_3.choices[0].message.content)
            add_question_and_answer_to_document(file_path, question, completion_3_modified.choices[0].message.content)
            time.sleep(1)
    print("done..")
