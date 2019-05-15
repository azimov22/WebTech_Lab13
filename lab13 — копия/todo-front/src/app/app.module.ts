import { BrowserModule } from '@angular/platform-browser';
import {ClassProvider, NgModule} from '@angular/core';
import { AppRoutingModule } from './app-routing.module';
import { AppComponent } from './app.component';
import { MainComponent } from './main/main.component';
import { TaskListService } from './task-list.service';
import { TaskListDetailComponent } from './task-list-detail/task-list-detail.component';
import { TaskDetailComponent } from './task-detail/task-detail.component';
import {HTTP_INTERCEPTORS, HttpClientModule} from '@angular/common/http';
import {FormsModule} from '@angular/forms';
import {AuthInterceptor} from './AuthInterceptor';


@NgModule({
  declarations: [
    AppComponent,
    MainComponent,
    TaskListDetailComponent,
    TaskDetailComponent
  ],
  imports: [
    BrowserModule,
    AppRoutingModule,
    HttpClientModule,
    FormsModule
  ],
  providers: [ TaskListService,
    {
    provide: HTTP_INTERCEPTORS,
    useClass: AuthInterceptor,
    multi: true
  } as ClassProvider ],
  bootstrap: [AppComponent]
})
export class AppModule { }
