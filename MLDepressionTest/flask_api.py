import pickle
import pandas as pd
from sklearn.preprocessing import MinMaxScaler


class Depress:
    def Inputs(self,result):
        #result = req.get("queryResult")
        #print(result)
        parameters = result.get("parameters")
        person_age = parameters.get('person_age')
        df = pd.read_csv('scaled.csv')
        Scaler = MinMaxScaler()
        df['Age'] = Scaler.fit_transform(df[['Age']])
        person_age = Scaler.transform([[person_age]])[0][0]
        print("Person Age = ",person_age)

        Gender = parameters.get('Gender')

        if Gender == 'female':
            Gender = 0
        elif Gender == 'male':
            Gender = 1
        else:
            Gender = 2

        print("Gender : ",Gender)

        family_history = parameters.get('family_history')

        if family_history == 'No':
            family_history = 0
        else:
            family_history = 1

        print("Family History : ", family_history)

        benefits = parameters.get('benefits')

        if benefits == 'No idea':
            benefits = 0
        elif benefits == 'No':
            benefits = 1
        else:
            benefits = 2

        print("Benefits",benefits)

        care_options = parameters.get('care_options')

        if care_options == 'No':
            care_options = 0
        elif care_options == 'Not Sure':
            care_options = 1
        else:
            care_options = 2

        print("Care Options",care_options)

        anonymity = parameters.get('anonymity')

        if anonymity == 'No idea':
            anonymity = 0
        elif anonymity == 'No':
            anonymity = 1
        else:
            anonymity = 2
        print("Anonymity :",anonymity)

        Leave = parameters.get('leave')

        if Leave == 'No idea':
            Leave = 0
        elif Leave == 'Somewhat difficult':
            Leave = 1
        elif Leave == 'Somewhat easy':
            Leave = 2
        elif Leave == 'Very Difficult':
            Leave = 3
        else:
            Leave = 4
        print("Leave : ",Leave)

        Work_interfere = parameters.get('work_interfere')

        if Work_interfere == 'No idea':
            Work_interfere = 0
        elif Work_interfere == 'Never':
            Work_interfere = 1
        elif Work_interfere == 'Often':
            Work_interfere = 2
        elif Work_interfere == 'Rarely':
            Work_interfere = 3
        else:
            Work_interfere = 4

        print("Work Interfere",Work_interfere)

        physhealthinterview = parameters.get('physhealthinterview')

        if physhealthinterview == 'maybe':
            physhealthinterview = 0
        elif physhealthinterview == 'no':
            physhealthinterview = 1
        else:
            physhealthinterview = 2

        print("Physical Interview",physhealthinterview)

        remote_work = parameters.get('remote_work')

        if remote_work == 'no':
            remote_work = 0
        else:
            remote_work = 1

        print("Remote Work",remote_work)

        coworkers = parameters.get('coworkers')

        if coworkers == 'no':
            coworkers = 0
        elif coworkers == 'Sometimes':
            coworkers = 1
        else:
            coworkers = 2

        print("Co-workers",coworkers)

        mentalhealthinterview = parameters.get('mentalhealthinterview')

        if mentalhealthinterview == 'Maybe':
            mentalhealthinterview = 0
        elif mentalhealthinterview == 'no':
            mentalhealthinterview = 1
        else:
            mentalhealthinterview = 2

        print("Mental Health Interview",mentalhealthinterview)

        no_employees = parameters.get('no_employees')

        if 0 < no_employees and no_employees < 5:
            no_employees = 0
        elif 100 <= no_employees <= 500:
            no_employees = 1
        elif  26 <= no_employees <=100:
            no_employees = 2
        elif 500 <= no_employees <=1000:
            no_employees = 3
        elif 6 <= no_employees <=25:
            no_employees = 4
        else:
            no_employees = 5

        print("No of Employees",no_employees)

        wellness_program = parameters.get('wellness_program')

        if wellness_program == 'No idea':
            wellness_program = 0
        elif wellness_program == 'no':
            wellness_program = 1
        else:
            wellness_program = 2

        print("Wellness Programs",wellness_program)

        tech_company = parameters.get('tech_company')

        if tech_company == 'no':
            tech_company = 0
        else:
            tech_company= 1

        print("Tech Company",tech_company)

        seek_help = parameters.get('seek_help')

        if seek_help == 'No idea':
            seek_help = 0
        elif seek_help == 'no':
            seek_help = 1
        else:
            seek_help = 2

        print("Seek Help",seek_help)

        supervisor = parameters.get('supervisor')

        if supervisor == 'no':
            supervisor = 0
        elif supervisor == 'Some':
            supervisor = 1
        else:
            supervisor = 2

        print("Supervisor : ",supervisor)


        mentalhealthconsequence = parameters.get('mentalhealthconsequence')

        if mentalhealthconsequence == 'maybe':
            mentalhealthconsequence = 0
        elif mentalhealthconsequence == 'no':
            mentalhealthconsequence = 1
        else:
            mentalhealthconsequence = 2

        print("Metal Health Consequence",mentalhealthconsequence)

        physhealthconsequence = parameters.get('physhealthconsequence')

        if physhealthconsequence == 'maybe':
            physhealthconsequence = 0
        elif physhealthconsequence == 'no':
            physhealthconsequence = 1
        else:
            physhealthconsequence = 2

        print("Physical Health Consequence",physhealthconsequence)

        mentalvsphysical = parameters.get('mentalvsphysical')

        if mentalvsphysical == 'no idea':
            mentalvsphysical = 0
        elif mentalvsphysical == 'No':
            mentalvsphysical = 1
        else:
            mentalvsphysical = 2

        print("Mental vs Physical",mentalvsphysical)


        Input = [person_age, Gender, family_history, benefits, care_options, anonymity, Leave, Work_interfere, physhealthinterview, remote_work, coworkers, mentalhealthinterview, no_employees, wellness_program, tech_company, seek_help, supervisor, mentalhealthconsequence, physhealthconsequence, mentalvsphysical]

        print(Input)

        pickle_in = open('final.pkl', "rb")
        classifier = pickle.load(pickle_in)
        print(classifier.predict([Input]))

        return Result(classifier.predict([Input])[0])

def Result(val):

    if val == 1:
        return {

            "fulfillmentMessages": [
                {
                    "text": {
                        "text": [
                            "It is advisable to visit a psychiatrist"
                        ]

                    }
                },

            ]
        }
    else:
        return {

            "fulfillmentMessages": [
                {
                    "text": {
                        "text": [
                            "You are alright! Take care !!"
                        ]

                    }
                },

            ]
        }


