from __future__ import annotations

from typing import List, Optional, Sequence

from pygls.lsp.types.basic_structures import (WorkDoneProgressBegin,
                                              WorkDoneProgressEnd,
                                              WorkDoneProgressReport)
from rope.base.taskhandle import BaseJobSet, BaseTaskHandle

from pylsp.workspace import Workspace


class PylspJobSet(BaseJobSet):
    name: str
    count: int
    done: int = 0
    job_name: str = ""
    handle: PylspTaskHandle

    def __init__(self, handle: PylspTaskHandle):
        self.handle = handle

    def started_job(self, name: Optional[str]) -> None:
        if name:
            self.job_name = name

    def finished_job(self) -> None:
        pass

    def check_status(self) -> None:
        pass

    def get_active_job_name(self) -> str:
        pass

    def get_percent_done(self) -> Optional[float]:
        pass

    def get_name(self) -> str:
        pass

    def increment(self) -> None:
        """
        Increment the number of tasks to complete.

        This is used if the number is not known ahead of time.
        """
        self.count += 1

    @property
    def _workspace(self) -> Workspace:
        return self.handle.workspace


class PylspTaskHandle(BaseTaskHandle):
    name: str
    observers: List
    job_sets: List[PylspJobSet]
    stopped: bool
    workspace: Workspace

    def __init__(self, workspace: Workspace):
        self.workspace = workspace

    def create_jobset(self, name="JobSet", count=None):
        result = PylspJobSet(self, name=name, count=count)
        self.job_sets.append(result)
        self._inform_observers()
        return result

    def stop(self) -> None:
        pass

    def current_jobset(self) -> Optional[BaseJobSet]:
        pass

    def add_observer(self) -> None:
        pass

    def is_stopped(self) -> bool:
        pass

    def get_jobsets(self) -> Sequence[BaseJobSet]:
        pass

    def _inform_observers(self) -> None:
        for observer in self.observers:
            observer()
