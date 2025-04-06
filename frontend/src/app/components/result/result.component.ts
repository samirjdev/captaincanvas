import { Component } from '@angular/core';
import { CommonModule } from '@angular/common';
import { ActivatedRoute, Router } from '@angular/router';
import { MatCardModule } from '@angular/material/card';
import { MatDividerModule } from '@angular/material/divider';
import { MatListModule } from '@angular/material/list';

@Component({
  selector: 'app-result',
  standalone: true,
  imports: [CommonModule, MatCardModule, MatDividerModule, MatListModule],
  templateUrl: './result.component.html',
  styleUrl: './result.component.scss'
})
export class ResultComponent {
  scheduleData: {
    course_name: string;
    course_link: string;
    assignment: {
      name: string;
      due_date: string;
      difficulty_score: number;
      assignment_link: string;
    };
  }[][] = [];
  

  constructor(private route: ActivatedRoute, private router: Router) {
    // Access the data passed via the router's state
    const navigation = this.router.getCurrentNavigation();
    this.scheduleData = navigation?.extras.state?.['data'];
  }
}
