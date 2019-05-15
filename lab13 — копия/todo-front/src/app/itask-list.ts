export interface ITaskList {
    id: number;
    name: string;
    created_by: string;
}

export interface ITask {
    id: number;
    name: string;
    created_at: string;
    due_on: string;
    status: string;
}

export interface ITaskDetail {
    id: number;
    name: string;
    status: string;
}

export interface IAuthResponse {
  Token: string;
}

