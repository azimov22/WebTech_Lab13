import { EventEmitter, Injectable } from '@angular/core';
import {MainService} from './main.service';
import {HttpClient} from '@angular/common/http';
import { ITaskList, ITask, IAuthResponse, ITaskDetail } from '../app/itask-list';

@Injectable({
  providedIn: 'root'
})
export class TaskListService extends MainService {

  constructor(http: HttpClient) {
    super(http);
   }

  getTaskList(): Promise<ITaskList[]> {
    return this.get('http://127.0.0.1:8000/task_lists', {});
  }

  getTaskListDetail(id: number): Promise<ITaskList> {
    return this.get(`http://127.0.0.1:8000/task_lists/${id}/`, {});
  }

  getTaskListTasks(id: number): Promise<ITaskDetail[]> {
    return this.get(`http://127.0.0.1:8000/task_lists/${id}/tasks/`, {});
  }

  getTaskDetail(id: number): Promise<ITask> {
    return this.get(`http://127.0.0.1:8000/tasks/${id}`, {});
  }

  createTaskList(name: any, user: any): Promise<ITaskList> {
    return this.post('http://127.0.0.1:8000/task_lists/', {
      name: name, created_by: user
    });
  }
  updateTaskList(taskList: ITaskList) {
    return this.put(`http://127.0.0.1:8000/task_lists/${taskList.id}/`, {
      name: taskList.name
    });
  }

  deleteTaskList(id: number): Promise<any> {
    return this.delet(`http://127.0.0.1:8000/task_lists/${id}/`, {
    });
  }

  auth(login: string, hey: string): Promise<IAuthResponse> {
    return this.post('http://127.0.0.1:8000/login/', {
      username: login,
      password: hey,
    });
  }

  logout(): Promise<any> {
    return this.post('http://127.0.0.1:8000/logout/', {});
  }

}
