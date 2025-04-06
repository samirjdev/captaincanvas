import { Injectable } from '@angular/core';
import { HttpClient } from '@angular/common/http';
import { Observable } from 'rxjs';


@Injectable({
  providedIn: 'root'
})
export class ApiService {
  private baseUrl = 'http://127.0.0.1:5000/api';

  constructor(private http: HttpClient) {}

  getWeeklySchedule(apiToken: string): Observable<any> {
    const headers = { Authorization: apiToken };
    return this.http.get(`${this.baseUrl}/weekly-schedule`, { headers });
  }
}
