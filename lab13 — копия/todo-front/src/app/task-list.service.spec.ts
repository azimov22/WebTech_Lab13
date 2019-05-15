import { TestBed } from '@angular/core/testing';

// @ts-ignore
import { TaskListService } from './task-list.service';

class TaskListService {
}

describe('TaskListService', () => {
  beforeEach(() => TestBed.configureTestingModule({}));

  it('should be created', () => {
    const service: TaskListService = TestBed.get(TaskListService);
    expect(service).toBeTruthy();
  });
});
