import { Component } from '@angular/core';
import { FormsModule } from '@angular/forms';
import { MatFormFieldModule } from '@angular/material/form-field';
import { MatInputModule } from '@angular/material/input';
import { MatButtonModule } from '@angular/material/button';
import { CommonModule } from '@angular/common';
import { Router } from '@angular/router';
import { MatProgressSpinnerModule } from '@angular/material/progress-spinner';
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
    MatProgressSpinnerModule,
  ],
  templateUrl: './landing.component.html',
  styleUrl: './landing.component.scss'
})
export class LandingComponent {
  apiToken: string = ''; // Holds the user's token
  isLoading: boolean = false;
  errorMessage: string = '';

  constructor(private apiService: ApiService,  private router: Router) {}

  makeApiRequest(): void {
    this.isLoading = true;
    this.errorMessage = ''; // Clear any previous error message

    this.apiService.getWeeklySchedule(this.apiToken).subscribe(
      (response) => {
        this.isLoading = false;
        this.router.navigate(['/result'], { state: { data: response } });
      },
      (error) => {
        this.isLoading = false;
        console.error('API Error:', error);
        this.errorMessage = 'Canvas API token may be invalid or expired. Please regenerate token.';
      }
    );
  }
}
