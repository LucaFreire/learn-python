'''A teacher wants to choose one in four students, for erase the blackboard. Create a system
where the machine pick one student to do the job.'''

import random
alunos = ["Joãozinho" , "Pedrinho" , "Luquinhas" , "Andrézinho"]
sort = random.choice(alunos) 
print(f"{sort} foi o escolhido, se lascou!")


