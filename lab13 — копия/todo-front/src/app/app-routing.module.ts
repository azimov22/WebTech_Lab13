import { NgModule } from '@angular/core';
import { Routes, RouterModule } from '@angular/router';
import { TaskListDetailComponent } from './task-list-detail/task-list-detail.component';
import { AppComponent } from './app.component';
import { MainComponent } from './main/main.component';
import { TaskDetailComponent } from './task-detail/task-detail.component';

const routes: Routes = [
  {path: '', component: MainComponent},
  {path: 'task_lists/:id/tasks', component: TaskListDetailComponent},
  {path: 'tasks/:id', component: TaskDetailComponent},
];

@NgModule({
  imports: [RouterModule.forRoot(routes)],
  exports: [RouterModule]
})
export class AppRoutingModule { }
