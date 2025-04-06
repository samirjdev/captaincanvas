import { NgModule } from '@angular/core';
import { RouterModule, Routes } from '@angular/router';
import { LandingComponent } from './components/landing/landing.component';
import { ResultsComponent } from './components/results/results.component';

export const routes: Routes = [
  { path: '', component: LandingComponent },         // <--- Default route
  { path: 'results', component: ResultsComponent },
  // any other routes ...
];

@NgModule({
  imports: [RouterModule.forRoot(routes)],
  exports: [RouterModule]
})
export class AppRoutingModule { }