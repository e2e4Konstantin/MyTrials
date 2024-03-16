class Workers:
    instances = []

    def __init__(self, task, working_power):
        self.task = task
        self.working_power = working_power
        Workers.instances.append(self)

    def remaining_time(self, task):
        working_power = sum([x.working_power for x in Workers.instances if x.task = self.task])
        time = self.task.time/working_power