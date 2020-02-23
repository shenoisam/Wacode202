import random
import time

import speech_recognition as sr

class SpeechRecognizer:
    def run_program(self):
        # set the list of words, maxnumber of guesses, and prompt limit
        WORDS = ["Innovative", "Specificity", 'Cinnamon', 'Rural', 'Transubstantiate', 'squirrel']
        NUM_GUESSES = 3
        PROMPT_LIMIT = 5

        # create recognizer and mic instances
        recognizer = sr.Recognizer()
        microphone = sr.Microphone()

        # get a random word from the list

        # format the instructions string
        instructions = (
            "Let's see how drunk you are:\n"
            "Try to pronounce the follwing words\n"
            "Innovative, Specificity, Cinnamon, Rural, Transubstantiate, and squirrel"
        ).format(words=', '.join(WORDS), n=NUM_GUESSES)

        # show instructions and wait 3 seconds before starting the game
        print(instructions)
        time.sleep(3)

        for i in range(NUM_GUESSES):
            word = random.choice(WORDS)
            # get the guess from the user
            # if a transcription is returned, break out of the loop and
            #     continue
            # if no transcription returned and API request failed, break
            #     loop and continue
            # if API request succeeded but no transcription was returned,
            #     re-prompt the user to say their guess again. Do this up
            #     to PROMPT_LIMIT times
            for j in range(PROMPT_LIMIT):
                print(f"This is the word {word}")
                print('Speak!'.format(i + 1))

                guess = self.recognize_speech_from_mic(recognizer, microphone)
                if guess["transcription"]:
                    break
                if not guess["success"]:
                    break
                # print("You are pretty drunk\n")

            # if there was an error, stop the game
            if guess["error"]:
                print("ERROR: {}".format(guess["Error"]))
                break

            # show the user the transcription
            print("You said: {}".format(guess["transcription"]))

            # determine if guess is correct and if any attempts remain
            guess_is_correct = guess["transcription"].lower() == word.lower()
            user_has_more_attempts = i < 2

            # determine if the user has won the game
            # if not, repeat the loop if user has more attempts
            # if no attempts left, the user loses the game
            if guess_is_correct:
                print("Good to go".format(word))
                break
            elif i < 2:
                print("You might have had too many")
            else:
                print("You should not be driving.".format(word))
                break

    def recognize_speech_from_mic(self, r, m):
        """Transcribe speech from recorded from `microphone`.

        Returns a dictionary with three keys:
        "success": a boolean indicating whether or not the API request was
                   successful
        "error":   `None` if no error occured, otherwise a string containing
                   an error message if the API could not be reached or
                   speech was unrecognizable
        "transcription": `None` if speech could not be transcribed,
                   otherwise a string containing the transcribed text
        """
        # check that recognizer and microphone arguments are appropriate type
        if not isinstance(r, sr.Recognizer):
            raise TypeError("`recognizer` must be `Recognizer` instance")

        if not isinstance(m, sr.Microphone):
            raise TypeError("`microphone` must be `Microphone` instance")

        # adjust the recognizer sensitivity to ambient noise and record audio
        # from the microphone
        with m as source:
            r.adjust_for_ambient_noise(source)
            audio = r.listen(source)

        # set up the response object
        response = {
            "success": True,
            "error": None,
            "transcription": None
        }

        # try recognizing the speech in the recording
        # if a RequestError or UnknownValueError exception is caught,
        #     update the response object accordingly
        try:
            response["transcription"] = recognizer.recognize_google(audio)
        except sr.RequestError:
            # API was unreachable or unresponsive
            response["success"] = False
            response["error"] = "API unavailable"
        except sr.UnknownValueError:
            # speech was unintelligible
            response["error"] = "Unable to recognize speech"

        return response


s = SpeechRecognizer()
s.run_program()