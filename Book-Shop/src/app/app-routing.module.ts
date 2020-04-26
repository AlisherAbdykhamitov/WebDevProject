import { NgModule } from '@angular/core';
import { Routes, RouterModule } from '@angular/router';
import {MainComponent} from './main/main.component';
import {ProductListComponent} from './product-list/product-list.component';
import {ProductDetailComponent} from './product-detail/product-detail.component';


const routes: Routes = [
  /*{path: '' , component: MainComponent},
  {path: 'categories/:id/products' , component: ProductListComponent},
  {path: 'categories/:id/produсts/:id/product-detail', component: ProductDetailComponent}*/
  {path: '', component: MainComponent},
];

@NgModule({
  imports: [RouterModule.forRoot(routes)],
  exports: [RouterModule]
})
export class AppRoutingModule { }
