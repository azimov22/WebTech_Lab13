import { Component, OnInit } from '@angular/core';
import { ITaskList } from '../itask-list';
import { TaskListService } from '../task-list.service';
import {Location} from '@angular/common';

@Component({
  selector: 'app-task-list',
  templateUrl: './main.component.html',
  styleUrls: ['./main.component.css']
})
export class MainComponent implements OnInit {

  public taskLists: ITaskList[] = [];
  public name: any = '';
  public user = '';
  public isLogged = false;
  public login = '';
  public password = '';

  constructor(
    private provider: TaskListService) { }

  ngOnInit() {

    const token = localStorage.getItem('token');
    if (token) {
      this.isLogged = true;
    }

    if (this.isLogged) {
      this.getTaskLists();
    }

  }

  getTaskLists() {
    this.provider.getTaskList().then(res => {
      this.taskLists = res;
    });
  }

  updateTaskList(taskList: ITaskList) {
    this.provider.updateTaskList(taskList).then(res => {
      console.log(taskList.name + ' updated');
    });
  }

  deleteTaskList(taskList: ITaskList) {
    this.provider.deleteTaskList(taskList.id).then(res => {
      console.log(taskList.name + ' deleted');
      this.provider.getTaskList().then(r => {
        this.taskLists = r;
      });
    });
  }

  createTaskList() {
    if (this.name !== '') {
      this.provider.createTaskList(this.name, this.user).then(res => {
        this.name = '';
        this.user = 'azimov';
        this.taskLists.push(res);
      });
    }
  }

  auth() {
    if (this.login !== '' && this.password !== '') {
      this.provider.auth(this.login, this.password).then(res => {
        localStorage.setItem('token', res.Token);
        this.isLogged = true;
        this.getTaskLists();
      });
    }
  }

  logout() {
    this.provider.logout().then(res => {
      this.isLogged = false;
      localStorage.clear();
    });
  }
}
