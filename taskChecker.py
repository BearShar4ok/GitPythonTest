from utils import db_action, DBAction, run_code


class Task:
    id: int
    name: str
    output: str
    description: str


def _init_(self, task_id: int, name: str, discription: str, output: str):
    self.id = task_id
    self.name = name
    self.discription = discription
    self.output = output

def get_task(task_id: int) -> Task:
    db_task = db_action(
        '''
            select * from tasks where id = ?
        ''',
        (task_id), DBAction.fetchone
    )
