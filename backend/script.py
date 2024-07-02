import asyncio
from dbutils import getanswer

def read_questions(file_path):
    with open(file_path, 'r') as file:
        questions = file.readlines()
    return [question.strip() for question in questions]

async def generate_answers(questions):
    tasks = [getanswer(question) for question in questions]
    answers = await asyncio.gather(*tasks)
    return answers

def write_answers(answers, file_path):
    with open(file_path, 'w') as file:
        for answer in answers:
            file.write(str(answer) + "\n")

async def main():
    questions = read_questions('questions.txt')
    answers = await generate_answers(questions)
    write_answers(answers, 'answers.txt')

if __name__ == "__main__":
    asyncio.run(main())
