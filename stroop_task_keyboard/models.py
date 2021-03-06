from otree.api import (
    models, widgets, BaseConstants, BaseSubsession, BaseGroup, BasePlayer,
    Currency as c, currency_range
)

import random

author = 'Maggie'

doc = """Player is given words to read.  In the first round, the words will be in black font.  In the second round, 
the words will be a color word, and the font color will match the color of the word.  In the third round, 
the words will be a color word, but the font color will not match the color of the word. No matter what the word 
reads as, the player needs to respond with the font color, not how the text reads.  The player will be rewarded for 
each color they get correct. """


class Constants(BaseConstants):
    name_in_url = 'stroop_task_keyboard'
    players_per_group = None
    num_rounds = 6


class Subsession(BaseSubsession):
    def creating_session(self):
        # randomize player to treatments (one treatment group for rounds 1-3, a second, different treatment group for rounds 4-6)
        if self.round_number == 1:
            for p in self.get_players():
                p.participant.vars['treatment_group'] = random.choice(['A', 'B', 'C'])   #first treatment group for rounds 1-3

                    #now setting second, different treatment group for rounds 4-6
                if p.participant.vars['treatment_group'] == "A":
                    p.participant.vars['treatment_group2'] = random.choice(['B', 'C'])
                if p.participant.vars['treatment_group'] == "B":
                    p.participant.vars['treatment_group2'] = random.choice(['A', 'C'])
                if p.participant.vars['treatment_group'] == "C":
                    p.participant.vars['treatment_group2'] = random.choice(['A', 'B'])

                print("set p.participant.vars['treatment_group]' to", p.participant.vars['treatment_group'], "for rounds 1-3")
                print("set p.participant.vars['treatment_group2]' to", p.participant.vars['treatment_group2'], "for rounds 4-6")

        self.session.vars["color_goals_key_A1"] = ['r', 'r', 'g', 'r', 'b', 'p', 'b', 'g', 'b', 'p',
                                                   'g', 'b', 'g', 'r', 'p', 'g', 'b', 'r', 'p', 'b']  # words key (round 1 or 4)
        self.session.vars["color_goals_key_A2"] = ['b', 'g', 'r', 'p', 'p', 'p', 'g', 'r', 'b', 'r',
                                                   'r', 'g', 'g', 'p', 'b', 'p', 'g', 'g', 'r','p']  # match words key (round 2 or 5)
        self.session.vars["color_goals_key_A3"] = ['r', 'g', 'r', 'b', 'b', 'b', 'p', 'g', 'b', 'g',
                                                   'p', 'b', 'g', 'g', 'r', 'p', 'p', 'g', 'r','b']  # conflict words key (round 3 or 6)

        self.session.vars["color_goals_key_B1"] = ['p', 'p', 'g', 'r', 'b', 'g', 'p', 'g', 'b', 'r',
                                                   'b', 'g', 'g', 'b', 'p', 'r', 'b', 'r', 'b', 'b']  # words key (round 1 or 4)
        self.session.vars["color_goals_key_B2"] = ['g', 'r', 'b', 'g', 'p', 'r', 'g', 'b', 'g', 'g',
                                                   'r', 'b', 'r', 'b', 'p', 'p', 'g', 'r', 'b', 'p']  # match words key (round 2 or 5)
        self.session.vars["color_goals_key_B3"] = ['g', 'p', 'p', 'g', 'r', 'b', 'g', 'b', 'p', 'r',
                                                   'g', 'r', 'b', 'p', 'b', 'g', 'r', 'r', 'b', 'p']  # conflict words key (round 3 or 6)

        self.session.vars["color_goals_key_C1"] = ['r', 'p', 'b', 'r', 'g', 'p', 'p', 'r', 'g', 'b',
                                                   'p', 'r', 'r', 'b', 'b', 'g', 'p', 'r', 'b', 'g']  # words key (round 1 or 4)
        self.session.vars["color_goals_key_C2"] = ['g', 'r', 'p', 'r', 'g', 'p', 'b', 'p', 'g', 'r',
                                                   'p', 'r', 'g', 'b', 'g', 'g', 'r', 'p', 'b', 'b']  # match words key (round 2 or 5)
        self.session.vars["color_goals_key_C3"] = ['b', 'b', 'g', 'b', 'r', 'p', 'g', 'p', 'b', 'r',
                                                   'b', 'r', 'p', 'b', 'g', 'r', 'r', 'g', 'p', 'g']  # conflict words key (round 3 or 6)

        self.session.vars["word_correct_round1"] = []
        self.session.vars["word_correct_round2"] = []
        self.session.vars["word_correct_round3"] = []
        self.session.vars["word_correct_round4"] = []
        self.session.vars["word_correct_round5"] = []
        self.session.vars["word_correct_round6"] = []

class Group(BaseGroup):
    def set_color_goals(self):
        for i in range(6):
            n = i + 1
            self.session.vars['text_displayed' + str(n)] = []
        # makes 6 arrays to hold the goals and text displayed for the 6 rounds

        for p in self.get_players():
            for j in range(2):  ## sets text displayed for words and match words rounds (rounds 1, 2, 4, and 5)
                n = j + 1  # for rounds 1 and 2
                k = j + 4  # for rounds 4 and 5
                for i in range(20):
                    if p.participant.vars['treatment_group'] == "A":
                        if self.session.vars['color_goals_key_A' + str(n)][i] == "r":
                            self.session.vars['text_displayed' + str(n)].append("red")
                        if self.session.vars['color_goals_key_A' + str(n)][i] == "g":
                            self.session.vars['text_displayed' + str(n)].append("green")
                        if self.session.vars['color_goals_key_A' + str(n)][i] == "b":
                            self.session.vars['text_displayed' + str(n)].append("blue")
                        if self.session.vars['color_goals_key_A' + str(n)][i] == "p":
                            self.session.vars['text_displayed' + str(n)].append("purple")

                    if p.participant.vars['treatment_group'] == "B":
                        if self.session.vars['color_goals_key_B' + str(n)][i] == "r":
                            self.session.vars['text_displayed' + str(n)].append("red")
                        if self.session.vars['color_goals_key_B' + str(n)][i] == "g":
                            self.session.vars['text_displayed' + str(n)].append("green")
                        if self.session.vars['color_goals_key_B' + str(n)][i] == "b":
                            self.session.vars['text_displayed' + str(n)].append("blue")
                        if self.session.vars['color_goals_key_B' + str(n)][i] == "p":
                            self.session.vars['text_displayed' + str(n)].append("purple")

                    if p.participant.vars['treatment_group'] == "C":
                        if self.session.vars['color_goals_key_C' + str(n)][i] == "r":
                            self.session.vars['text_displayed' + str(n)].append("red")
                        if self.session.vars['color_goals_key_C' + str(n)][i] == "g":
                            self.session.vars['text_displayed' + str(n)].append("green")
                        if self.session.vars['color_goals_key_C' + str(n)][i] == "b":
                            self.session.vars['text_displayed' + str(n)].append("blue")
                        if self.session.vars['color_goals_key_C' + str(n)][i] == "p":
                            self.session.vars['text_displayed' + str(n)].append("purple")

                    if p.participant.vars['treatment_group2'] == "A":
                        if self.session.vars['color_goals_key_A' + str(n)][i] == "r":
                            self.session.vars['text_displayed' + str(k)].append("red")
                        if self.session.vars['color_goals_key_A' + str(n)][i] == "g":
                            self.session.vars['text_displayed' + str(k)].append("green")
                        if self.session.vars['color_goals_key_A' + str(n)][i] == "b":
                            self.session.vars['text_displayed' + str(k)].append("blue")
                        if self.session.vars['color_goals_key_A' + str(n)][i] == "p":
                            self.session.vars['text_displayed' + str(k)].append("purple")

                    if p.participant.vars['treatment_group2'] == "B":
                        if self.session.vars['color_goals_key_B' + str(n)][i] == "r":
                            self.session.vars['text_displayed' + str(k)].append("red")
                        if self.session.vars['color_goals_key_B' + str(n)][i] == "g":
                            self.session.vars['text_displayed' + str(k)].append("green")
                        if self.session.vars['color_goals_key_B' + str(n)][i] == "b":
                            self.session.vars['text_displayed' + str(k)].append("blue")
                        if self.session.vars['color_goals_key_B' + str(n)][i] == "p":
                            self.session.vars['text_displayed' + str(k)].append("purple")

                    if p.participant.vars['treatment_group2'] == "C":
                        if self.session.vars['color_goals_key_C' + str(n)][i] == "r":
                            self.session.vars['text_displayed' + str(k)].append("red")
                        if self.session.vars['color_goals_key_C' + str(n)][i] == "g":
                            self.session.vars['text_displayed' + str(k)].append("green")
                        if self.session.vars['color_goals_key_C' + str(n)][i] == "b":
                            self.session.vars['text_displayed' + str(k)].append("blue")
                        if self.session.vars['color_goals_key_C' + str(n)][i] == "p":
                            self.session.vars['text_displayed' + str(k)].append("purple")



            # now setting text displayed for conflict words rounds (rounds 3 and 6) to be incongruent with font color
                # conflict words text displayed for round 3
            if p.participant.vars['treatment_group'] == "A":
                self.session.vars['text_displayed' + str(3)] = ['green', 'blue', 'purple', 'green', 'purple', 'red', 'green', 'red', 'red', 'blue',
                                                                'blue', 'green', 'purple', 'red', 'purple', 'green', 'blue', 'red', 'blue', 'purple']
            if p.participant.vars['treatment_group'] == "B":
                self.session.vars['text_displayed' + str(3)] = ['purple', 'blue', 'green', 'red', 'blue', 'purple', 'red', 'green', 'red', 'purple',
                                                                'blue', 'purple', 'purple', 'blue', 'red', 'red', 'blue', 'green', 'purple', 'red']
            if p.participant.vars['treatment_group'] == "C":
                self.session.vars['text_displayed' + str(3)] = ['red', 'green', 'blue', 'red', 'purple', 'blue', 'red', 'blue', 'green', 'green',
                                                                'green', 'blue', 'green', 'red', 'blue', 'purple', 'blue', 'red', 'green', 'purple']

                # now conflict words text displayed for round 6
            if p.participant.vars['treatment_group2'] == "A":
                self.session.vars['text_displayed' + str(6)] = ['green', 'blue', 'purple', 'green', 'purple', 'red', 'green', 'red', 'red', 'blue',
                                                                'blue', 'green', 'purple', 'red', 'purple', 'green', 'blue', 'red', 'blue', 'purple']
            if p.participant.vars['treatment_group2'] == "B":
                self.session.vars['text_displayed' + str(6)] = ['purple', 'blue', 'green', 'red', 'blue', 'purple', 'red', 'green', 'red', 'purple',
                                                                'blue', 'purple', 'purple', 'blue', 'red', 'red', 'blue', 'green', 'purple', 'red']
            if p.participant.vars['treatment_group2'] == "C":
                self.session.vars['text_displayed' + str(6)] = ['red', 'green', 'blue', 'red', 'purple', 'blue', 'red', 'blue', 'green', 'green',
                                                                'green', 'blue', 'green', 'red', 'blue', 'purple', 'blue', 'red', 'green', 'purple']

            # printing color goals key and text displayed
            for i in range(3):  # printing for rounds 1-3
                n = i + 1
                print("For round ", str(n), 'the color goals are set to: ',
                      self.session.vars['color_goals_key_' + p.participant.vars['treatment_group'] + str(n)], '\n')
                print("For round ", str(n), 'the text displayed will show: ', self.session.vars['text_displayed' + str(n)], '\n')

            for i in range(3):  # printing for rounds 4-6
                y = i + 1
                k = i + 4
                print("For round ", str(k), 'the color goals are set to: ',
                      self.session.vars['color_goals_key_' + p.participant.vars['treatment_group2'] + str(y)], '\n')
                print("For round ", str(k), 'the text displayed will show: ',
                      self.session.vars['text_displayed' + str(k)], '\n')

    def check_color_answers(self):
        print('\n\nFOR ROUND', self.round_number)

        controller = self.get_player_by_role('Controller')
        controller_color_answers = [controller.word1, controller.word2, controller.word3, controller.word4,
                                    controller.word5, controller.word6, controller.word7, controller.word8,
                                    controller.word9, controller.word10, controller.word11, controller.word12,
                                    controller.word13, controller.word14, controller.word15, controller.word16,
                                    controller.word17, controller.word18, controller.word19, controller.word20]
        for p in self.get_players():
            if self.round_number < 4:
                if p.participant.vars['treatment_group'] == "A":
                    for i in range(20):
                        if controller_color_answers[i] == self.session.vars['color_goals_key_A' + str(self.round_number)][i]:
                            controller.total_words_correct += 1
                            controller.payoff += c(0.10)
                            self.session.vars["word_correct_round" + str(self.round_number)].append(True)
                            print('For word', i + 1, 'color was correct. Controller.total_words_correct is',
                                  controller.total_words_correct, 'and controller.payoff is', controller.payoff)
                            print('color_goals_key_A[', i, '] was',
                                  self.session.vars['color_goals_key_A' + str(self.round_number)][i],
                                  'and controller_color_answers[', i, '] was', controller_color_answers[i])
                            print('For A self.session.vars[word_correct_round', self.round_number, '][', i, '] is ', self.session.vars["word_correct_round" + str(self.round_number)], '\n')
                            if i == 0:
                                controller.word1correct = True
                            if i == 1:
                                controller.word2correct = True
                            if i == 2:
                                controller.word3correct = True
                            if i == 3:
                                controller.word4correct = True
                            if i == 4:
                                controller.word5correct = True
                            if i == 5:
                                controller.word6correct = True
                            if i == 6:
                                controller.word7correct = True
                            if i == 7:
                                controller.word8correct = True
                            if i == 8:
                                controller.word9correct = True
                            if i == 9:
                                controller.word10correct = True
                            if i == 10:
                                controller.word11correct = True
                            if i == 11:
                                controller.word12correct = True
                            if i == 12:
                                controller.word13correct = True
                            if i == 13:
                                controller.word14correct = True
                            if i == 14:
                                controller.word15correct = True
                            if i == 15:
                                controller.word16correct = True
                            if i == 16:
                                controller.word17correct = True
                            if i == 17:
                                controller.word18correct = True
                            if i == 18:
                                controller.word19correct = True
                            if i == 19:
                                controller.word20correct = True

                        else:
                            self.session.vars["word_correct_round" + str(self.round_number)].append(False)
                            print('For word', i + 1, 'color was incorrect. Controller.total_words_correct is still',
                                  controller.total_words_correct, 'and controller.payoff is still', controller.payoff)
                            print('color_goals_key_A[', i, '] was',
                                  self.session.vars['color_goals_key_A' + str(self.round_number)][i],
                                  'and controller_color_answers[', i, '] was', controller_color_answers[i])
                            print('For A self.session.vars[word_correct_round', self.round_number, '][', i, '] is ',
                                  self.session.vars["word_correct_round" + str(self.round_number)], '\n')

                if p.participant.vars['treatment_group'] == "B":
                    for i in range(20):
                        if controller_color_answers[i] == self.session.vars['color_goals_key_B' + str(self.round_number)][i]:
                            controller.total_words_correct += 1
                            controller.payoff += c(0.10)
                            self.session.vars["word_correct_round" + str(self.round_number)].append(True)
                            print('For word', i + 1, 'color was correct. Controller.total_words_correct is',
                                  controller.total_words_correct, 'and controller.payoff is', controller.payoff)
                            print('color_goals_key_B[', i, '] was',
                                  self.session.vars['color_goals_key_B' + str(self.round_number)][i],
                                  'and controller_color_answers[', i, '] was', controller_color_answers[i])
                            print('For B self.session.vars[word_correct_round', self.round_number, '][', i, '] is ',
                                  self.session.vars["word_correct_round" + str(self.round_number)], '\n')
                            if i == 0:
                                controller.word1correct = True
                            if i == 1:
                                controller.word2correct = True
                            if i == 2:
                                controller.word3correct = True
                            if i == 3:
                                controller.word4correct = True
                            if i == 4:
                                controller.word5correct = True
                            if i == 5:
                                controller.word6correct = True
                            if i == 6:
                                controller.word7correct = True
                            if i == 7:
                                controller.word8correct = True
                            if i == 8:
                                controller.word9correct = True
                            if i == 9:
                                controller.word10correct = True
                            if i == 10:
                                controller.word11correct = True
                            if i == 11:
                                controller.word12correct = True
                            if i == 12:
                                controller.word13correct = True
                            if i == 13:
                                controller.word14correct = True
                            if i == 14:
                                controller.word15correct = True
                            if i == 15:
                                controller.word16correct = True
                            if i == 16:
                                controller.word17correct = True
                            if i == 17:
                                controller.word18correct = True
                            if i == 18:
                                controller.word19correct = True
                            if i == 19:
                                controller.word20correct = True

                        else:
                            self.session.vars["word_correct_round" + str(self.round_number)].append(False)
                            print('For word', i + 1, 'color was incorrect. Controller.total_words_correct is still',
                                  controller.total_words_correct, 'and controller.payoff is still', controller.payoff)
                            print('color_goals_key_B[', i, '] was',
                                  self.session.vars['color_goals_key_B' + str(self.round_number)][i],
                                  'and controller_color_answers[', i, '] was', controller_color_answers[i])
                            print('For B self.session.vars[word_correct_round', self.round_number, '][', i, '] is ', self.session.vars["word_correct_round" + str(self.round_number)], '\n')

                if p.participant.vars['treatment_group'] == "C":
                    for i in range(20):
                        if controller_color_answers[i] == self.session.vars['color_goals_key_C' + str(self.round_number)][i]:
                            controller.total_words_correct += 1
                            controller.payoff += c(0.10)
                            self.session.vars["word_correct_round" + str(self.round_number)].append(True)
                            print('For word', i + 1, 'color was correct. Controller.total_words_correct is',
                                  controller.total_words_correct, 'and controller.payoff is', controller.payoff)
                            print('color_goals_key_C[', i, '] was',
                                  self.session.vars['color_goals_key_C' + str(self.round_number)][i],
                                  'and controller_color_answers[', i, '] was', controller_color_answers[i])
                            print('For C self.session.vars[word_correct_round', self.round_number, '][', i, '] is ',
                                  self.session.vars["word_correct_round" + str(self.round_number)], '\n')
                            if i == 0:
                                controller.word1correct = True
                            if i == 1:
                                controller.word2correct = True
                            if i == 2:
                                controller.word3correct = True
                            if i == 3:
                                controller.word4correct = True
                            if i == 4:
                                controller.word5correct = True
                            if i == 5:
                                controller.word6correct = True
                            if i == 6:
                                controller.word7correct = True
                            if i == 7:
                                controller.word8correct = True
                            if i == 8:
                                controller.word9correct = True
                            if i == 9:
                                controller.word10correct = True
                            if i == 10:
                                controller.word11correct = True
                            if i == 11:
                                controller.word12correct = True
                            if i == 12:
                                controller.word13correct = True
                            if i == 13:
                                controller.word14correct = True
                            if i == 14:
                                controller.word15correct = True
                            if i == 15:
                                controller.word16correct = True
                            if i == 16:
                                controller.word17correct = True
                            if i == 17:
                                controller.word18correct = True
                            if i == 18:
                                controller.word19correct = True
                            if i == 19:
                                controller.word20correct = True

                        else:
                            self.session.vars["word_correct_round" + str(self.round_number)].append(False)
                            print('For word', i + 1, 'color was incorrect. Controller.total_words_correct is still',
                                  controller.total_words_correct, 'and controller.payoff is still', controller.payoff)
                            print('color_goals_key_C[', i, '] was',
                                  self.session.vars['color_goals_key_C' + str(self.round_number)][i],
                                  'and controller_color_answers[', i, '] was', controller_color_answers[i])
                            print('For C self.session.vars[word_correct_round', self.round_number, '][', i, '] is ',
                                  self.session.vars["word_correct_round" + str(self.round_number)], '\n')

            if self.round_number >= 4:
                if p.participant.vars['treatment_group2'] == "A":
                    for i in range(20):
                        if controller_color_answers[i] == self.session.vars['color_goals_key_A' + str(self.round_number-3)][i]:
                            controller.total_words_correct += 1
                            controller.payoff += c(0.10)
                            self.session.vars["word_correct_round" + str(self.round_number)].append(True)
                            print('For word', i + 1, 'color was correct. Controller.total_words_correct is',
                                  controller.total_words_correct, 'and controller.payoff is', controller.payoff)
                            print('color_goals_key_A[', i, '] was',
                                  self.session.vars['color_goals_key_A' + str(self.round_number-3)][i],
                                  'and controller_color_answers[', i, '] was', controller_color_answers[i])
                            print('For A self.session.vars[word_correct_round', self.round_number, '][', i, '] is ',
                                  self.session.vars["word_correct_round" + str(self.round_number)], '\n')
                            if i == 0:
                                controller.word1correct = True
                            if i == 1:
                                controller.word2correct = True
                            if i == 2:
                                controller.word3correct = True
                            if i == 3:
                                controller.word4correct = True
                            if i == 4:
                                controller.word5correct = True
                            if i == 5:
                                controller.word6correct = True
                            if i == 6:
                                controller.word7correct = True
                            if i == 7:
                                controller.word8correct = True
                            if i == 8:
                                controller.word9correct = True
                            if i == 9:
                                controller.word10correct = True
                            if i == 10:
                                controller.word11correct = True
                            if i == 11:
                                controller.word12correct = True
                            if i == 12:
                                controller.word13correct = True
                            if i == 13:
                                controller.word14correct = True
                            if i == 14:
                                controller.word15correct = True
                            if i == 15:
                                controller.word16correct = True
                            if i == 16:
                                controller.word17correct = True
                            if i == 17:
                                controller.word18correct = True
                            if i == 18:
                                controller.word19correct = True
                            if i == 19:
                                controller.word20correct = True

                        else:
                            self.session.vars["word_correct_round" + str(self.round_number)].append(False)
                            print('For word', i + 1, 'color was incorrect. Controller.total_words_correct is still',
                                  controller.total_words_correct, 'and controller.payoff is still', controller.payoff)
                            print('color_goals_key_A[', i, '] was',
                                  self.session.vars['color_goals_key_A' + str(self.round_number-3)][i],
                                  'and controller_color_answers[', i, '] was', controller_color_answers[i])
                            print('For A self.session.vars[word_correct_round', self.round_number, '][', i, '] is ',
                                  self.session.vars["word_correct_round" + str(self.round_number)], '\n')

                if p.participant.vars['treatment_group2'] == "B":
                    for i in range(20):
                        if controller_color_answers[i] == self.session.vars['color_goals_key_B' + str(self.round_number-3)][i]:
                            controller.total_words_correct += 1
                            controller.payoff += c(0.10)
                            self.session.vars["word_correct_round" + str(self.round_number)].append(True)
                            print('For word', i + 1, 'color was correct. Controller.total_words_correct is',
                                  controller.total_words_correct, 'and controller.payoff is', controller.payoff)
                            print('color_goals_key_B[', i, '] was',
                                  self.session.vars['color_goals_key_B' + str(self.round_number-3)][i],
                                  'and controller_color_answers[', i, '] was', controller_color_answers[i])
                            print('For B self.session.vars[word_correct_round', self.round_number, '][', i, '] is ',
                                  self.session.vars["word_correct_round" + str(self.round_number)], '\n')
                            if i == 0:
                                controller.word1correct = True
                            if i == 1:
                                controller.word2correct = True
                            if i == 2:
                                controller.word3correct = True
                            if i == 3:
                                controller.word4correct = True
                            if i == 4:
                                controller.word5correct = True
                            if i == 5:
                                controller.word6correct = True
                            if i == 6:
                                controller.word7correct = True
                            if i == 7:
                                controller.word8correct = True
                            if i == 8:
                                controller.word9correct = True
                            if i == 9:
                                controller.word10correct = True
                            if i == 10:
                                controller.word11correct = True
                            if i == 11:
                                controller.word12correct = True
                            if i == 12:
                                controller.word13correct = True
                            if i == 13:
                                controller.word14correct = True
                            if i == 14:
                                controller.word15correct = True
                            if i == 15:
                                controller.word16correct = True
                            if i == 16:
                                controller.word17correct = True
                            if i == 17:
                                controller.word18correct = True
                            if i == 18:
                                controller.word19correct = True
                            if i == 19:
                                controller.word20correct = True

                        else:
                            self.session.vars["word_correct_round" + str(self.round_number)].append(False)
                            print('For word', i + 1, 'color was incorrect. Controller.total_words_correct is still',
                                  controller.total_words_correct, 'and controller.payoff is still', controller.payoff)
                            print('color_goals_key_B[', i, '] was',
                                  self.session.vars['color_goals_key_B' + str(self.round_number-3)][i],
                                  'and controller_color_answers[', i, '] was', controller_color_answers[i])
                            print('For B self.session.vars[word_correct_round', self.round_number, '][', i, '] is ',
                                  self.session.vars["word_correct_round" + str(self.round_number)], '\n')


                if p.participant.vars['treatment_group2'] == "C":
                    for i in range(20):
                        if controller_color_answers[i] == self.session.vars['color_goals_key_C' + str(self.round_number-3)][i]:
                            controller.total_words_correct += 1
                            controller.payoff += c(0.10)
                            self.session.vars["word_correct_round" + str(self.round_number)].append(True)
                            print('For word', i + 1, 'color was correct. Controller.total_words_correct is',
                                  controller.total_words_correct, 'and controller.payoff is', controller.payoff)
                            print('color_goals_key_C[', i, '] was',
                                  self.session.vars['color_goals_key_C' + str(self.round_number-3)][i],
                                  'and controller_color_answers[', i, '] was', controller_color_answers[i])
                            print('For C self.session.vars[word_correct_round', self.round_number, '][', i, '] is ',
                                  self.session.vars["word_correct_round" + str(self.round_number)], '\n')
                            if i == 0:
                                controller.word1correct = True
                            if i == 1:
                                controller.word2correct = True
                            if i == 2:
                                controller.word3correct = True
                            if i == 3:
                                controller.word4correct = True
                            if i == 4:
                                controller.word5correct = True
                            if i == 5:
                                controller.word6correct = True
                            if i == 6:
                                controller.word7correct = True
                            if i == 7:
                                controller.word8correct = True
                            if i == 8:
                                controller.word9correct = True
                            if i == 9:
                                controller.word10correct = True
                            if i == 10:
                                controller.word11correct = True
                            if i == 11:
                                controller.word12correct = True
                            if i == 12:
                                controller.word13correct = True
                            if i == 13:
                                controller.word14correct = True
                            if i == 14:
                                controller.word15correct = True
                            if i == 15:
                                controller.word16correct = True
                            if i == 16:
                                controller.word17correct = True
                            if i == 17:
                                controller.word18correct = True
                            if i == 18:
                                controller.word19correct = True
                            if i == 19:
                                controller.word20correct = True

                        else:
                            self.session.vars["word_correct_round" + str(self.round_number)].append(False)
                            print('For word', i + 1, 'color was incorrect. Controller.total_words_correct is still',
                                  controller.total_words_correct, 'and controller.payoff is still', controller.payoff)
                            print('color_goals_key_C[', i, '] was',
                                  self.session.vars['color_goals_key_C' + str(self.round_number-3)][i],
                                  'and controller_color_answers[', i, '] was', controller_color_answers[i])
                            print('For C self.session.vars[word_correct_round', self.round_number, '][', i, '] is ',
                                  self.session.vars["word_correct_round" + str(self.round_number)], '\n')


class Player(BasePlayer):
    word1 = models.StringField(widget=widgets.RadioSelectHorizontal, label='', choices=[['r', 'red'], ['g', 'green'], ['b', 'blue'], ['p', 'purple']])
    word2 = models.StringField(widget=widgets.RadioSelectHorizontal, label='', choices=[['r', 'red'], ['g', 'green'], ['b', 'blue'], ['p', 'purple']])
    word3 = models.StringField(widget=widgets.RadioSelectHorizontal, label='', choices=[['r', 'red'], ['g', 'green'], ['b', 'blue'], ['p', 'purple']])
    word4 = models.StringField(widget=widgets.RadioSelectHorizontal, label='', choices=[['r', 'red'], ['g', 'green'], ['b', 'blue'], ['p', 'purple']])
    word5 = models.StringField(widget=widgets.RadioSelectHorizontal, label='', choices=[['r', 'red'], ['g', 'green'], ['b', 'blue'], ['p', 'purple']])
    word6 = models.StringField(widget=widgets.RadioSelectHorizontal, label='', choices=[['r', 'red'], ['g', 'green'], ['b', 'blue'], ['p', 'purple']])
    word7 = models.StringField(widget=widgets.RadioSelectHorizontal, label='', choices=[['r', 'red'], ['g', 'green'], ['b', 'blue'], ['p', 'purple']])
    word8 = models.StringField(widget=widgets.RadioSelectHorizontal, label='', choices=[['r', 'red'], ['g', 'green'], ['b', 'blue'], ['p', 'purple']])
    word9 = models.StringField(widget=widgets.RadioSelectHorizontal, label='', choices=[['r', 'red'], ['g', 'green'], ['b', 'blue'], ['p', 'purple']])
    word10 = models.StringField(widget=widgets.RadioSelectHorizontal, label='', choices=[['r', 'red'], ['g', 'green'], ['b', 'blue'], ['p', 'purple']])
    word11 = models.StringField(widget=widgets.RadioSelectHorizontal, label='', choices=[['r', 'red'], ['g', 'green'], ['b', 'blue'], ['p', 'purple']])
    word12 = models.StringField(widget=widgets.RadioSelectHorizontal, label='', choices=[['r', 'red'], ['g', 'green'], ['b', 'blue'], ['p', 'purple']])
    word13 = models.StringField(widget=widgets.RadioSelectHorizontal, label='', choices=[['r', 'red'], ['g', 'green'], ['b', 'blue'], ['p', 'purple']])
    word14 = models.StringField(widget=widgets.RadioSelectHorizontal, label='', choices=[['r', 'red'], ['g', 'green'], ['b', 'blue'], ['p', 'purple']])
    word15 = models.StringField(widget=widgets.RadioSelectHorizontal, label='', choices=[['r', 'red'], ['g', 'green'], ['b', 'blue'], ['p', 'purple']])
    word16 = models.StringField(widget=widgets.RadioSelectHorizontal, label='', choices=[['r', 'red'], ['g', 'green'], ['b', 'blue'], ['p', 'purple']])
    word17 = models.StringField(widget=widgets.RadioSelectHorizontal, label='', choices=[['r', 'red'], ['g', 'green'], ['b', 'blue'], ['p', 'purple']])
    word18 = models.StringField(widget=widgets.RadioSelectHorizontal, label='', choices=[['r', 'red'], ['g', 'green'], ['b', 'blue'], ['p', 'purple']])
    word19 = models.StringField(widget=widgets.RadioSelectHorizontal, label='', choices=[['r', 'red'], ['g', 'green'], ['b', 'blue'], ['p', 'purple']])
    word20 = models.StringField(widget=widgets.RadioSelectHorizontal, label='', choices=[['r', 'red'], ['g', 'green'], ['b', 'blue'], ['p', 'purple']])

    treatment_group = models.StringField()
    # payoff = models.CurrencyField()
    total_words_correct = models.IntegerField(initial=0)

    word1correct = models.BooleanField(initial=False)
    word2correct = models.BooleanField(initial=False)
    word3correct = models.BooleanField(initial=False)
    word4correct = models.BooleanField(initial=False)
    word5correct = models.BooleanField(initial=False)
    word6correct = models.BooleanField(initial=False)
    word7correct = models.BooleanField(initial=False)
    word8correct = models.BooleanField(initial=False)
    word9correct = models.BooleanField(initial=False)
    word10correct = models.BooleanField(initial=False)
    word11correct = models.BooleanField(initial=False)
    word12correct = models.BooleanField(initial=False)
    word13correct = models.BooleanField(initial=False)
    word14correct = models.BooleanField(initial=False)
    word15correct = models.BooleanField(initial=False)
    word16correct = models.BooleanField(initial=False)
    word17correct = models.BooleanField(initial=False)
    word18correct = models.BooleanField(initial=False)
    word19correct = models.BooleanField(initial=False)
    word20correct = models.BooleanField(initial=False)


    def role(self):
        if self.id_in_group == 1:
            return 'Controller'
