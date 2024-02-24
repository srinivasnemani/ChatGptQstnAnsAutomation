import time


def execute_with_retry_and_save_answers(client, question_to_chatgpt, model_name=None,
                                        context_instruction_to_gpt=None,
                                        frequency_penalty=0.25,
                                        presence_penalty=0.22):
    retry_count = 0
    max_retries = 5
    wait_time = 3
    if model_name is None:
        model_name = "gpt-3.5-turbo"

    if context_instruction_to_gpt is None:
        context_instruction_to_gpt = (""" I am Preparing for an Job Interview. Act as Tutor to help me answer this question. 
                            Give it with sub headings. Give answers between 400 to 500 words.
                            After giving subheading, start the content in next line. """)

    while retry_count < max_retries:
        try:
            # Your code block
            completion = client.chat.completions.create(
                model=model_name,
                messages=[
                    {"role": "user", "content": question_to_chatgpt},
                    {"role": "system",
                     "content": context_instruction_to_gpt},
                ],
                top_p=1,
                frequency_penalty=frequency_penalty,
                presence_penalty=presence_penalty
            )
            # If the code block succeeds, return the result
            return completion
        except Exception as e:
            # Increment the retry count
            retry_count += 1
            # Print the error message
            print(f"An error occurred: {e}")
            # Wait for a moment before retrying
            time.sleep(wait_time)

            if retry_count > 4:
                # Save the question to a text file
                file_name = f"{question_to_chatgpt[:10]}_{time.strftime('%Y%m%d %H%M%S')}.txt"
                with open(file_name, 'w') as file:
                    file.write(question_to_chatgpt)

    # If all retries fail, print a message
    print("Max retries reached. Unable to complete the operation.")
    return None  # or raise an exception if preferred
