import { Component, OnInit } from '@angular/core';
import { TaskListService } from '../task-list.service';
import { Location } from '@angular/common';
import { ActivatedRoute } from '@angular/router';

@Component({
  selector: 'app-task-detail',
  templateUrl: './task-detail.component.html',
  styleUrls: ['./task-detail.component.css']
})
export class TaskDetailComponent implements OnInit {

  public id: number = 0;

  public task: any = {}

  constructor(
    private provider: TaskListService,
    private route: ActivatedRoute,
    private location: Location
  ) { }

  ngOnInit() {
    this.id = parseInt(this.route.snapshot.paramMap.get('id'));

    if (this.id) {
      this.provider.getTaskDetail(this.id).then(res => {
        this.task = res;
      });
    }
  }

  navigateBack(){
    this.location.back();
  }
}
