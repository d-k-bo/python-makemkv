# noqa: D100
from typing import Any, Optional

try:
    from rich.progress import BarColumn, Progress, TaskID, TimeRemainingColumn
except ImportError as exc:
    raise ImportError(
        "'makemkv.progress' requires 'rich' to be installed. You can "
        "install it with 'pip install rich' or 'pip install makemkv[cli]."
    ) from exc


class ProgressParser(Progress):
    """Renders progress bars that can be updated using a callback method."""

    def __init__(self, **kwargs: Any) -> None:
        if "transient" not in kwargs:
            kwargs["transient"] = True
        if "expand" not in kwargs:
            kwargs["expand"] = True
        super().__init__(
            "[progress.description]{task.description}",
            BarColumn(bar_width=None),
            "[progress.percentage]{task.percentage:>3.0f}%",
            TimeRemainingColumn(),
            **kwargs,
        )
        self.task_description: Optional[str] = None
        self.task_id: Optional[TaskID] = None
        self.started: bool = False

    def __enter__(self):  # noqa: ANN204,D105
        super().__enter__()

        return self

    def parse_progress(self, task_description: str, progress: int, max: int) -> None:
        """Update the progress bar display.

        Args:
            task_description: Describes what is happening. If it differs
                from the current task description, a new progress bar will be
                shown.
            progress: Current progress value.
            max: Maximum possible value.
        """
        if self.task_description == task_description:
            assert self.task_id is not None
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
                task_description, completed=progress, total=max, start=False
            )
