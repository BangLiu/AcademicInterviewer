import sys
from random import sample, randrange
import math
import pygame as pg
import pyttsx3
engine = pyttsx3.init()
engine.setProperty('voice', "com.apple.speech.synthesis.voice.daniel")


# NOTE: change variables to put your own question sets, as well as other settings.
Qs = {
    "research": [
        "Can you introduce yourself?"
        "Tell me about your PhD research.",
        "What is your most proud project?",
        "Which 3 works are you most proud of?",
        "How is your work different than other's in your field?",
        "What is your role in the research projects?",
        "What is the theory contribution in your works?",
        "What is your most significant research accomplishments",
        "Tell me about your most significant publications",
        "What is your publishing experience",
        "What is the most exciting thing you have discovered in your research?",
        "What is the most significant piece of research that you have read recently",
        "What have you read outside your field that interested you?",
        "Type of research program you envisage",
        "many papers of yours are in industry not research track, why? do you have any theory contribution?",
        "you have many different research topics, are they correlated?"],
    "teaching": [
        "What is your teaching philosophy?",
        "What is your teaching style?",
        "Tell me about your teaching experience?",
        "How do you explain a hard concept to a student?",
        "How to teach undergrad or grad courses? What is the difference?",
        "How to teach in a big or small class?",
        "What courses you want to teach or develop?",
        "Which courses in our department you can teach?",
        "How to teach less-motivated students?",
        "How to teach diverse students?",
        "How to involve students in your research?",
        "How do you balance teaching and research"],
    "department": [
        "How do you think your research program would fit into the department?",
        "What research would you anticipate doing here at our campus?",
        "How would your background and experiences strengthen the department?",
        "What is your attitude towards service? In what ways, other than research and teaching could you contribute to this department?",
        "Why are you interested in this department",
        "Why are you interested in this university",
        "Why do you want this job?",
        "What are your expectations of the University and this position?",
        "Could you tell us about your long-range plans and commitment to this department?",
        "What can you bring to the department that is uniquely yours?",
        "What do you think most uniquely qualifies you for this position?",
        "Who will you collaborate with externally?",
        "Who would you collaborate with within the department? What other departments could you work with?"
        "We are keen to develop collaborations between departments. What opportunities for multi-disciplinary work does your research offer?"],
    "career": [
        "What is your long-term goal",
        "What is your future research plan",
        "Why do you want this job?",
        "Where do you see yourself in five years?",
        "Where do you see yourself in ten years?",
        "What goals do you have for your research or funding or teaching?",
        "What are your funding plans?",
        "Do you have any grant writing experience?",
        "As you are from Canada, how can you get gran in U.S.?",
        "Why you want to come to United States?",
        "Why academic instead of industry?",
        "What do you want your research group or lab to be like? Number of students?",
        "What will be your major focus as an independent researcher?",
        "How would you convince a funding body that they should fund your research rather than one of the other hundreds of proposals they receive?",
        "In one sentence, what is the most important question you want to address?"],
    "behavior": [
        "How did you handle a difficult situation with a project?",
        "How have you handled a difficult situation with people?",
        "Tell me about a mistake you made during your PhD",
        "How do you solve conflicts with people?",
        "How do you get support from the industry?",
        "What is your weakness?",
        "What is your strength?",
        "Describe a time when you were faced with a stressful situation that demonstrated your coping skills.",
        "Tell me about a time when you had too many things to do and you were required to prioritize your tasks.",
        "Give me an example of a time when something you tried to accomplish and failed."]}
Q_TYPES = list(Qs.keys())
NUM_Q_TYPES = len(Q_TYPES)
NUM_Q_LIMIT = 4  # maximum 3 questions from each group
TIME_LIMIT = 2.5 * 60  # maximum 3 minutes for each question
#TIME_LIMIT = 5
N_MAX_SAMPLE_TIMES = 20


def random_questions(q_type, n_q):
    return sample(Qs[q_type], n_q)


def main():
    asked_qs = []
    info = pg.display.Info()
    screen = pg.display.set_mode(
        (info.current_w, info.current_h), pg.FULLSCREEN)
    screen_rect = screen.get_rect()
    font = pg.font.Font(None, 45)
    clock = pg.time.Clock()
    color = (randrange(256), randrange(256), randrange(256))
    q = random_questions(Q_TYPES[0], 1)[0]
    asked_qs.append(q)
    engine.say(q)
    engine.runAndWait()
    txt = font.render(q, True, color)
    timer = TIME_LIMIT
    done = False
    n_q = 0

    while not done:
        # done with keyboard
        for event in pg.event.get():
            if event.type == pg.KEYDOWN:
                if event.key == pg.K_ESCAPE:
                    done = True

        timer -= 1
        # Update the text surface and color every 10 frames.
        if timer <= 0:
            timer = TIME_LIMIT
            color = (randrange(256), randrange(256), randrange(256))
            n_q += 1
            n_q_type = math.floor(n_q / NUM_Q_LIMIT)
            asked = True
            n_try = 0
            while asked:
                q = random_questions(Q_TYPES[n_q_type], 1)[0]
                if q not in asked_qs:
                    asked = False
                    asked_qs.append(q)
                n_try += 1
                if n_try > N_MAX_SAMPLE_TIMES:
                    break
            engine.say(q)
            engine.runAndWait()
            txt = font.render(q, True, color)

        screen.fill((30, 30, 30))
        screen.blit(txt, txt.get_rect(center=screen_rect.center))
        pg.display.flip()
        clock.tick(1)  # I "issue" 1 frames per second

        if n_q == NUM_Q_TYPES * NUM_Q_LIMIT - 1 and timer <= 1:
            done = True


if __name__ == '__main__':
    pg.init()
    main()
    pg.quit()
    sys.exit()
