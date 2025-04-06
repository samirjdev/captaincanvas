import { Routes } from '@angular/router';
import { LandingComponent } from './components/landing/landing.component';
import { ResultComponent } from './components/result/result.component';

export const routes: Routes = [
  { path: '', component: LandingComponent }, // Default route
  { path: 'result', component: ResultComponent },
];
