import { Component } from '@angular/core';
import { FormsModule } from '@angular/forms';
import { MatFormFieldModule } from '@angular/material/form-field';
import { MatInputModule } from '@angular/material/input';
import { MatButtonModule } from '@angular/material/button';
import { CommonModule } from '@angular/common';
import { Router } from '@angular/router';
import { ApiService } from '../../services/api.service'; // Adjusted the path to the correct location

@Component({
  selector: 'app-landing',
  standalone: true,
  imports: [
    CommonModule,
    FormsModule,
    MatFormFieldModule,
    MatInputModule,
    MatButtonModule,
  ],
  templateUrl: './landing.component.html',
  styleUrl: './landing.component.scss'
})
export class LandingComponent {
  apiToken: string = ''; // Holds the user's token

  constructor(private apiService: ApiService,  private router: Router) {}

  makeApiRequest() {
    if (!this.apiToken) {
      alert('Please enter your API token.');
      return;
    }

    this.apiService.getWeeklySchedule(this.apiToken).subscribe(
      (response) => {
        this.router.navigate(['/result'], { state: { data: response } });
      },
      (error) => {
        console.error('API Error:', error);
        alert('Failed to make the API request. Check the console for details.');
      }
    );
  }
}
