from rich.progress import BarColumn, Progress, TimeRemainingColumn


class ProgressParser(Progress):
    """Renders progress bars that can be updated using a callback method."""

    def __init__(self):
        super().__init__(
            "[progress.description]{task.description}",
            BarColumn(bar_width=None,),
            "[progress.percentage]{task.percentage:>3.0f}%",
            TimeRemainingColumn(),
            transient=True,
            expand=True
        )
        self.task_description = None
        self.task_id = None
        self.started = False

    def parse_progress(self, task_description, progress, max):
        """Updates the progress bar display.

        Args:
            task_description (str): Describes what is happening. If it differs
                from the current task description, a new progress bar will be
                shown.
            progress (int): Current progress value.
            max (int): Maximum possible value.
        """

        if self.task_description == task_description:
            if not self.started:
                self.start_task(self.task_id)
                self.started = True
            self.update(self.task_id, completed=progress)
        else:
            if self.task_id is not None:
                self.update(self.task_id, completed=max)
                self.remove_task(self.task_id)
            self.started = False
            self.task_description = task_description
            self.task_id = self.add_task(
                task_description, completed=progress, total=max, start=False)