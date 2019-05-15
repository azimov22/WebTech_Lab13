import { Component, OnInit } from '@angular/core';
import { TaskListService } from '../task-list.service';
import { ActivatedRoute } from '@angular/router';
import {Location} from '@angular/common'
import { ITaskDetail } from '../itask-list';

@Component({
  selector: 'app-task-list-detail',
  templateUrl: './task-list-detail.component.html',
  styleUrls: ['./task-list-detail.component.css']
})
export class TaskListDetailComponent implements OnInit {

  public tasks: ITaskDetail[] = [];
  public taskList: any = {};

  public id: number;

  constructor(
    private provider: TaskListService,
    private route: ActivatedRoute,
    private location: Location
    ) { }

  ngOnInit() {
    this.id = parseInt(this.route.snapshot.paramMap.get('id'));
    if (this.id) {
      this.provider.getTaskListTasks(this.id).then(res => {
        this.tasks = res;
      });
      this.provider.getTaskListDetail(this.id).then(res => {
        this.taskList = res;
      });
    }
  }

  navigateBack() {
    this.location.back();
  }
}
